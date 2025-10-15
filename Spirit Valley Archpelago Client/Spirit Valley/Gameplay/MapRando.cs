using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class MapRando
    {
        [HarmonyPatch(typeof(MapManager), "Start")]
        [HarmonyPrefix]
        public static void maprando1(MapManager __instance)
        {
            if (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["randomise_map"]) == 0) { return; }

            string mapid = SceneManager.GetActiveScene().name;

            string scene = null;
            string id = null;

            //ArchipelagoConsole.LogMessage($"MAPID: {mapid}");
            foreach (TransitionArea a in __instance.transitionObjects.GetComponentsInChildren<TransitionArea>())
            {
                string newdata = "";
                if (ArchipelagoClient.ServerData.mapdata.TryGetValue($"{mapid} {a.id}", out newdata))
                {
                    scene = newdata.Split(' ')[0];
                    id = newdata.Split(' ')[1];
                }
                else
                {
                    if (mapid == "EvergreenOutpost" && a.id == "Right")
                    {
                        newdata = ArchipelagoClient.ServerData.mapdata[$"EvergreenOutpost_East Right"];
                        scene = newdata.Split(' ')[0];
                        id = newdata.Split(' ')[1];
                    }
                    else if (mapid == "Trail16" && a.id == "Cave")
                    {
                        newdata = ArchipelagoClient.ServerData.mapdata[$"Trail16_Top Cave"];
                        scene = newdata.Split(' ')[0];
                        id = newdata.Split(' ')[1];
                    }
                    else if (mapid == "Trail16" && a.id == "Right2")
                    {
                        newdata = ArchipelagoClient.ServerData.mapdata[$"Trail16_Top Right2"];
                        scene = newdata.Split(' ')[0];
                        id = newdata.Split(' ')[1];
                    }
                    else if (mapid == "Trail20" && a.id == "Right")
                    {
                        newdata = ArchipelagoClient.ServerData.mapdata[$"Trail20_Right Right"];
                        scene = newdata.Split(' ')[0];
                        id = newdata.Split(' ')[1];
                    }
                    else
                    {
                        if ((mapid == "OakwoodVillage" && (a.id == "ClinicOut"|| a.id == "HqOut"))||(mapid == "OakwoodVillage_Clinic" || (mapid == "OakwoodVillage_Hq")))
                        {
                        }
                        else
                        {
                            ArchipelagoConsole.LogError($"TRANSITION ({mapid} {a.id}) NOT IN DICT PLZ SEND TO DEV FOR FIXING");
                        }
                    }
                }

                if (scene!= null && id != null)
                {
                    if (scene == "EvergreenOutpost_East") { scene = "EvergreenOutpost"; }
                    if (scene == "Trail16_Top") { scene = "Trail16"; }
                    if (scene == "Trail20_Right") { scene = "Trail20"; }

                    ArchipelagoConsole.LogDebug($"SETTING TRANSITION: {mapid} {a.id} -> {scene} {id}");

                    a.nextSceneName = scene;
                    a.nextTransitionAreaID = id;
                }
            }
        }
    }
}
