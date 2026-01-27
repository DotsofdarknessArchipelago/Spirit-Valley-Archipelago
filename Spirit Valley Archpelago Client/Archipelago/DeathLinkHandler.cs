using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using BepInEx;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using System.Collections.Generic;
using System.Threading;
using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Archipelago;

public class DeathLinkHandler
{
    private static bool deathLinkEnabled;
    private string slotName;
    private readonly DeathLinkService service;
    private readonly Queue<DeathLink> deathLinks = new();
    public bool processingdeath = false;

    private Timer timer1;

    /// <summary>
    /// instantiates our death link handler, sets up the hook for receiving death links, and enables death link if needed
    /// </summary>
    /// <param name="deathLinkService">The new DeathLinkService that our handler will use to send and
    /// receive death links</param>
    /// <param name="enableDeathLink">Whether we should enable death link or not on startup</param>
    public DeathLinkHandler(DeathLinkService deathLinkService, string name, bool enableDeathLink = false)
    {
        service = deathLinkService;
        service.OnDeathLinkReceived += DeathLinkReceived;
        slotName = name;
        deathLinkEnabled = enableDeathLink;
        
        if (deathLinkEnabled)
        {
            service.EnableDeathLink();
        }
    }

    /// <summary>
    /// enables/disables death link
    /// </summary>
    public void ToggleDeathLink()
    {
        ArchipelagoConsole.LogDebug("TOGGLING DEATHLINK");
        deathLinkEnabled = !deathLinkEnabled;

        if (deathLinkEnabled)
        {
            service.EnableDeathLink();
            timer1 = new Timer(KillPlayer, null, 5000, 5000);
        }
        else
        {
            service.DisableDeathLink();
            timer1.Dispose();
        }
    }

    /// <summary>
    /// what happens when we receive a deathLink
    /// </summary>
    /// <param name="deathLink">Received Death Link object to handle</param>
    private void DeathLinkReceived(DeathLink deathLink)
    {
        deathLinks.Enqueue(deathLink);

        SpiritValleyArchipelago.BepinLogger.LogDebug(deathLink.Cause.IsNullOrWhiteSpace()
            ? $"Received Death Link from: {deathLink.Source}"
            : deathLink.Cause);
    }

    public void KillPlayer(object state) => KillPlayer();

    /// <summary>
    /// can be called when in a valid state to kill the player, dequeueing and immediately killing the player with a
    /// message if we have a death link in the queue
    /// </summary>
    public void KillPlayer()
    {
        try
        {
            if (deathLinks.Count < 1) return;

            if (SceneManager.GetActiveScene().name == "TitleScreen" || SceneManager.GetActiveScene().name == "IntroScene") { return; }
            if (!QuestManager.instance.GetIsActiveMainQuestGreaterThan("main_quest_2_captain_maria")) {  return; }

            if (processingdeath) { return; }

            if (SceneManager.GetActiveScene().name == "OakwoodVillage_Clinic" ||
                SceneManager.GetActiveScene().name == "Greensvale_Clinic" ||
                SceneManager.GetActiveScene().name == "TumbleweedTown_Clinic" ||
                SceneManager.GetActiveScene().name == "CoconutVillage_Clinic" ||
                SceneManager.GetActiveScene().name == "Frostville1_Clinic") { return; }

            var deathLink = deathLinks.Dequeue();

            processingdeath = true;

            if (deathLink.Cause.IsNullOrWhiteSpace())
            {
                ArchipelagoConsole.LogMessage($"Receved DEATH from {deathLink.Source}");
            }
            else
            {
                ArchipelagoConsole.LogMessage($"Receved {deathLink.Source} DEATH caused by:{deathLink.Cause}");
            }

            if (SceneManager.GetActiveScene().name == "FightScene")
            {
                FightManager fm = GameObject.Find("FightManager").GetComponent<FightManager>();
                fm.EndFight(FightManager.FightResult.EnemyWon);
                fm.OnRestPressed();
            }
            else
            {
                GameState s = HelperItems.save;
                s.ReviveAllTeamMembers();
                string lastClinicName = s.lastVisitedClinicSceneName;
                if (string.IsNullOrEmpty(lastClinicName))
                {
                    lastClinicName = "OakwoodVillage_Clinic";
                }

                s.ClearFightStateData();
                s.ClearActiveItems();
                AudioManager.instance.StopMusic(0.4f);
                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                {
                    SceneManager.LoadScene(lastClinicName, LoadSceneMode.Single);
                });

            }
        }
        catch (Exception e)
        {
            SpiritValleyArchipelago.BepinLogger.LogError(e);
        }
    }

    /// <summary>
    /// called to send a death link to the multiworld
    /// </summary>
    public void SendDeathLink(string cause = null)
    {
        try
        {
            if (!deathLinkEnabled) return;

            SpiritValleyArchipelago.BepinLogger.LogMessage("sharing your death...");

            DeathLink linkToSend;
            if (cause == null)
            {
                linkToSend = new DeathLink(slotName);
            }
            else
            {
                linkToSend = new DeathLink(slotName, cause);
            }

            service.SendDeathLink(linkToSend);
        }
        catch (Exception e)
        {
            SpiritValleyArchipelago.BepinLogger.LogError(e);
        }
    }
}