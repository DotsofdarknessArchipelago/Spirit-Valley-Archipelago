using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class Waystone
    {

        [HarmonyPatch(typeof(WayStoneMapItem), "Start")]
        [HarmonyPostfix]
        public static void test(WayStoneMapItem __instance, ref WayStoneState ___state, ref bool ___isInteractAllowed)
        {
            ___isInteractAllowed = true;
            if (__instance.GetIsActive())
            {
                int start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["warp_locations"]);
                switch (___state.sceneName)
                {
                    case "OakwoodVillage":
                        ArchipelagoClient.sendloc(start + 1);
                        break;
                    case "Greensvale":
                        ArchipelagoClient.sendloc(start + 2);
                        break;
                    case "Trail4":
                        ArchipelagoClient.sendloc(start + 3);
                        break;
                    case "DairyFarm":
                        ArchipelagoClient.sendloc(start + 4);
                        break;
                    case "TumbleweedTown":
                        ArchipelagoClient.sendloc(start + 5);
                        break;
                    case "CrashSite":
                        ArchipelagoClient.sendloc(start + 6);
                        break;
                    case "CoconutVillage":
                        ArchipelagoClient.sendloc(start + 7);
                        break;
                    case "Trail14":
                        ArchipelagoClient.sendloc(start + 8);
                        break;
                    case "ColdHarbor":
                        ArchipelagoClient.sendloc(start + 9);
                        break;
                    case "Frostville1":
                        ArchipelagoClient.sendloc(start + 10);
                        break;
                    case "AbandonedMine":
                        ArchipelagoClient.sendloc(start + 11);
                        break;
                    case "Trail18":
                        ArchipelagoClient.sendloc(start + 12);
                        break;
                    case "Trail19":
                        ArchipelagoClient.sendloc(start + 13);
                        break;
                    case "Trail22":
                        ArchipelagoClient.sendloc(start + 14);
                        break;
                    default:
                        ArchipelagoConsole.LogMessage($"SCENE NAME NOT KNOWN: {___state.sceneName}");
                        break;
                }
            }
        }

        [HarmonyPatch(typeof(WayStoneMapItem), "OnAnimationActivateCompleted")]
        [HarmonyPrefix]
        public static bool activate(WayStoneMapItem __instance, ref WayStoneState ___state)
        {
            ArchipelagoConsole.LogMessage($"WAYSTONE ANIMATION COMPLETE");
            int start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["warp_locations"]);
            switch (___state.sceneName)
            {
                case "OakwoodVillage":
                    ArchipelagoClient.sendloc(start + 1);
                    break;
                case "Greensvale":
                    ArchipelagoClient.sendloc(start + 2);
                    break;
                case "Trail4":
                    ArchipelagoClient.sendloc(start + 3);
                    break;
                case "DairyFarm":
                    ArchipelagoClient.sendloc(start + 4);
                    break;
                case "TumbleweedTown":
                    ArchipelagoClient.sendloc(start + 5);
                    break;
                case "CrashSite":
                    ArchipelagoClient.sendloc(start + 6);
                    break;
                case "CoconutVillage":
                    ArchipelagoClient.sendloc(start + 7);
                    break;
                case "Trail14":
                    ArchipelagoClient.sendloc(start + 8);
                    break;
                case "ColdHarbor":
                    ArchipelagoClient.sendloc(start + 9);
                    break;
                case "Frostville1":
                    ArchipelagoClient.sendloc(start + 10);
                    break;
                case "AbandonedMine":
                    ArchipelagoClient.sendloc(start + 11);
                    break;
                case "Trail18":
                    ArchipelagoClient.sendloc(start + 12);
                    break;
                case "Trail19":
                    ArchipelagoClient.sendloc(start + 13);
                    break;
                case "Trail22":
                    ArchipelagoClient.sendloc(start + 14);
                    break;
                default:
                    ArchipelagoConsole.LogMessage($"SCENE NAME NOT KNOWN: {___state.sceneName}");
                    break;
            }
            if (Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["randomise_warps"]))
            {
                ArchipelagoConsole.LogDebug($"RANDOMISE WARPS ON SKIPPING ORIGNAL METHOD");
                return false;
            }
            return true;
        }


        [HarmonyPatch(typeof(WayStoneMapItem), "GetIsActive")]
        [HarmonyPrefix]
        public static bool activateoverqite(WayStoneMapItem __instance, ref WayStoneState ___state,ref bool __result)
        {

            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["randomise_warps"]))
            {
                ArchipelagoConsole.LogDebug($"RANDOMISE WARPS ON SKIPPING ORIGNAL METHOD");
                return true;
            }
            int itemstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_warp_id_start"]);
            __result = false;
            switch (___state.sceneName)
            {
                case "OakwoodVillage":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 1);
                    break;
                case "Greensvale":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 2);
                    break;
                case "Trail4":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 3);
                    break;
                case "DairyFarm":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 4);
                    break;
                case "TumbleweedTown":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 5);
                    break;
                case "CrashSite":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 6);
                    break;
                case "CoconutVillage":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 7);
                    break;
                case "Trail14":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 8);
                    break;
                case "ColdHarbor":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 9);
                    break;
                case "Frostville1":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 10);
                    break;
                case "AbandonedMine":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 11);
                    break;
                case "Trail18":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 12);
                    break;
                case "Trail19":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 13);
                    break;
                case "Trail22":
                    __result = ArchipelagoClient.archlist.hasitem(itemstart + 14);
                    break;
                default:
                    ArchipelagoConsole.LogMessage($"SCENE NAME NOT KNOWN: {___state.sceneName}");
                    break;
            }
            return false;
        }
    }
}
