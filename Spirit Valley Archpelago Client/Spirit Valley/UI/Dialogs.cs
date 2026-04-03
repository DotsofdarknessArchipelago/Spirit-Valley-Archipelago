using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using System.Linq;
using System.Reflection;
using UnityEngine.Localization;
using UnityEngine.Localization.Settings;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.UI
{
    [HarmonyPatch]
    public class Dialogs
    {
        public static Dialog[] addedialog;
        public static string[] dialogids = ["SergeantCassie_Arch_Quest5", "Captain_Arch_Quest13", "Sassy_Arch_Quest20", "Captain_Arch_Quest28", "MinerJohnson_Arch_Quest43", "PaisleyBones_Arch_Quest46", "Captain_balloon_ride_unavaliable", "Captain_boat_ride_unavaliable", "Captain_ancient_warp_unavaliable"];

        /// <summary>
        /// add checks for the Captain requireing relevant items before continuing the main quest
        /// </summary>
        [HarmonyPatch(typeof(BaseNPC), "GetDialogWithID")]
        [HarmonyPostfix]
        public static void dialogadd(string id, ref Dialog __result)
        {
            if (addedialog == null)
            {
                ArchipelagoConsole.LogDebug("ADDING NEW DIALOGS");

                addedialog = [
                    createdialog("SergeantCassie_Arch_Quest5", "You need to find the Super Secret Orders to proceed"),
                    createdialog("Captain_Arch_Quest13", "You need to find a Power Crystal before we can activate the bridge"),
                    createdialog("Sassy_Arch_Quest20", "You need to obtain a Spirit Handler Licence before you can battle"),
                    createdialog("Captain_Arch_Quest28", "You need to find the Yellow Harmony Crystal before we can move on"),
                    createdialog("MinerJohnson_Arch_Quest43", "You need to find A Fancy Suit before we can continue"),
                    createdialog("PaisleyBones_Arch_Quest46", "You need to find some Dynamite to blow up this rock"),

                    createdialog("Captain_balloon_ride_unavaliable", "You need a ticket to ride on this Balloon"),
                    createdialog("Captain_boat_ride_unavaliable", "You need to a boat ticket to travel to the artic isles"),
                    createdialog("Captain_ancient_warp_unavaliable", "we need a ancient warp core to activate this portal"),
                    ];

                ArchipelagoConsole.LogDebug("FINISHED ADDING NEW DIALOGS");
            }

            if (__result == null)
            {
                foreach (Dialog d in addedialog)
                {
                    if (d.id == id) { __result = d; return; }
                }
            }
        }

        [HarmonyPatch(typeof(Captain), "ResolveLocation")]
        [HarmonyPostfix]
        public static void dialogresolve(ref string __result, Captain __instance)
        {
            if (SceneManager.GetActiveScene().name == __result) { return; }

            if (SceneManager.GetActiveScene().name == __instance.evergreenOutpostSceneName &&
                QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_14_dusty_vale_awaits") &&
                !ArchipelagoClient.archlist.hasitem(Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_key_item_start"]) + 10))
            {
                __result = SceneManager.GetActiveScene().name;
            }
            if (SceneManager.GetActiveScene().name == __instance.tumbleweedTownSceneName &&
                QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_30_welcome_to_paradise"))
            {
                __result = SceneManager.GetActiveScene().name;
            }
            if (SceneManager.GetActiveScene().name == __instance.coconutVillageTeampleSceneName &&
                QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_37_the_frigid_maiden"))
            {
                __result = SceneManager.GetActiveScene().name;
            }
            if (SceneManager.GetActiveScene().name == __instance.trail18SceneName &&
                QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_50_sanctuary_shakedown"))
            {
                __result = SceneManager.GetActiveScene().name;
            }
        }

        public static Dialog createdialog(string name, string text)
        {

            LocalizedString temp = MonsterManager.instance.GetBaseStatsByName("Pusseen").monsterName;
            GenderedLines[] blanklines = [];

            var t = LocalizationSettings.Instance.GetStringDatabase().GetTable(temp.TableReference).AddEntry(name, text);

            Dialog output = new Dialog
            {
                id = name,
                showDialogSprites = true,
                isExitAllowed = true,
                autoSetHeroInputEnabledDialogExit = true,
                playStartSound = true,
                isInputDisabled = false
            };
            DialogLine[] temp13 = [new DialogLine { line = new LocalizedString(temp.TableReference, name) }];
            output.GetType().GetField("lines", BindingFlags.NonPublic | BindingFlags.Instance).SetValue(output, temp13);
            output.GetType().GetField("genderedLines", BindingFlags.NonPublic | BindingFlags.Instance).SetValue(output, blanklines);

            return output;
        }


        [HarmonyPatch(typeof(DialogUI), "ShowLine")]
        [HarmonyPrefix]
        public static void dialogfix1(DialogLine line, DialogUI __instance, ref Dialog ___dialog)
        {
            if (dialogids.Contains(___dialog.id))
            {
                line.npcNameOverride ??= new LocalizedString();
                line.selections ??= Array.Empty<DialogLine.Selection>();
            }
        }



        [HarmonyPatch(typeof(DialogUI), "TestAndActivateSelectionBox")]
        [HarmonyPrefix]
        public static void dialogfix2(ref DialogLine ___currentLine, ref Dialog ___dialog)
        {
            if (dialogids.Contains(___dialog.id))
            {
                ___currentLine.npcNameOverride ??= new LocalizedString();
                ___currentLine.selections ??= Array.Empty<DialogLine.Selection>();
            }
        }
    }
}
