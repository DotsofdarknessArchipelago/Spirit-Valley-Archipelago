using HarmonyLib;
using Mono.Cecil.Cil;
using MonoMod.Cil;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
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
            HelperItems.save.isFastTravelUnlocked = true;
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


        [HarmonyPatch(typeof(GameState), "GetWayStoneState")]
        [HarmonyPostfix]
        public static void waystonemod(string sceneName, ref WayStoneState __result)
        {
            if (Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["randomise_warps"]))
            {
                int itemstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_warp_id_start"]);
                ArchipelagoConsole.LogDebug($"RANDOMISE WARPS ON SKIPPING ORIGNAL METHOD3");
                switch (sceneName)
                {
                    case "OakwoodVillage":
                        if(ArchipelagoClient.archlist.hasitem(itemstart + 1))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                            break;
                    case "Greensvale":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 2))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "Trail4":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 3))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "DairyFarm":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 4))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "TumbleweedTown":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 5))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "CrashSite":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 6))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "CoconutVillage":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 7))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "Trail14":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 8))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "ColdHarbor":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 9))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "Frostville1":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 10))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "AbandonedMine":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 11))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "Trail18":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 12))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "Trail19":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 13))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    case "Trail22":
                        if (ArchipelagoClient.archlist.hasitem(itemstart + 14))
                        {
                            __result.isActive = true;
                        }
                        else
                        {
                            __result.isActive = false;
                        }
                        break;
                    default:
                        ArchipelagoConsole.LogMessage($"SCENE NAME NOT KNOWN: {sceneName}");
                        break;
                }
            }
        }

        [HarmonyPatch(typeof(ColdHarborSequence), "PlayCoroutine")]
        [HarmonyILManipulator]
        public static void coldharbormod(ILContext ctx, MethodBase orig)
        {
            for (int i = 20; i < ctx.Instrs.Count; i++)
            {
                if (ctx.Instrs[i-13].OpCode == OpCodes.Ldarg_0 &&
                    ctx.Instrs[i-12].OpCode == OpCodes.Ldloc_1 &&
                    ctx.Instrs[i-11].OpCode == OpCodes.Ldftn &&
                    ctx.Instrs[i-10].OpCode == OpCodes.Newobj &&
                    ctx.Instrs[i-9].OpCode == OpCodes.Newobj &&
                    ctx.Instrs[i-8].OpCode == OpCodes.Stfld &&
                    ctx.Instrs[i-7].OpCode == OpCodes.Ldarg_0 &&
                    ctx.Instrs[i-6].OpCode == OpCodes.Ldc_I4_8 &&
                    ctx.Instrs[i-5].OpCode == OpCodes.Stfld &&
                    ctx.Instrs[i-4].OpCode == OpCodes.Ldc_I4_1 &&
                    ctx.Instrs[i-3].OpCode == OpCodes.Br &&
                    ctx.Instrs[i-2].OpCode == OpCodes.Ldarg_0 &&
                    ctx.Instrs[i-1].OpCode == OpCodes.Ldc_I4_M1 &&
                    ctx.Instrs[i].OpCode == OpCodes.Stfld
                    )
                {
                    ctx.Instrs[i - 13].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 12].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 11].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 10].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 9].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 8].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 7].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 6].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 5].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 4].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 3].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 2].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 1].OpCode = OpCodes.Nop;
                    ctx.Instrs[i].OpCode = OpCodes.Nop;
                }
            }
        }

        [HarmonyPatch(typeof(CrashSiteSequence), "PlayCoroutine")]
        [HarmonyILManipulator]
        public static void crashsitemod(ILContext ctx, MethodBase orig)
        {
            for (int i = 20; i < ctx.Instrs.Count; i++)
            {
                if (ctx.Instrs[i-13].OpCode == OpCodes.Ldarg_0 &&
                    ctx.Instrs[i-12].OpCode == OpCodes.Ldloc_1 &&
                    ctx.Instrs[i-11].OpCode == OpCodes.Ldftn &&
                    ctx.Instrs[i-10].OpCode == OpCodes.Newobj &&
                    ctx.Instrs[i-9].OpCode == OpCodes.Newobj &&
                    ctx.Instrs[i-8].OpCode == OpCodes.Stfld &&
                    ctx.Instrs[i-7].OpCode == OpCodes.Ldarg_0 &&
                    ctx.Instrs[i-6].OpCode == OpCodes.Ldc_I4_7 &&
                    ctx.Instrs[i-5].OpCode == OpCodes.Stfld &&
                    ctx.Instrs[i-4].OpCode == OpCodes.Ldc_I4_1 &&
                    ctx.Instrs[i-3].OpCode == OpCodes.Br &&
                    ctx.Instrs[i-2].OpCode == OpCodes.Ldarg_0 &&
                    ctx.Instrs[i-1].OpCode == OpCodes.Ldc_I4_M1 &&
                    ctx.Instrs[i].OpCode == OpCodes.Stfld
                    )
                {
                    ctx.Instrs[i - 13].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 12].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 11].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 10].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 9].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 8].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 7].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 6].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 5].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 4].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 3].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 2].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 1].OpCode = OpCodes.Nop;
                    ctx.Instrs[i].OpCode = OpCodes.Nop;
                }
            }
        }

        [HarmonyPatch(typeof(Trail19Sequence), "PlayCoroutine")]
        [HarmonyILManipulator]
        public static void trail19mod(ILContext ctx, MethodBase orig)
        {
            for (int i = 20; i < ctx.Instrs.Count; i++)
            {
                if (ctx.Instrs[i-13].OpCode == OpCodes.Ldarg_0 &&
                    ctx.Instrs[i-12].OpCode == OpCodes.Ldloc_1 &&
                    ctx.Instrs[i-11].OpCode == OpCodes.Ldftn &&
                    ctx.Instrs[i-10].OpCode == OpCodes.Newobj &&
                    ctx.Instrs[i-9].OpCode == OpCodes.Newobj &&
                    ctx.Instrs[i-8].OpCode == OpCodes.Stfld &&
                    ctx.Instrs[i-7].OpCode == OpCodes.Ldarg_0 &&
                    ctx.Instrs[i-6].OpCode == OpCodes.Ldc_I4_4 &&
                    ctx.Instrs[i-5].OpCode == OpCodes.Stfld &&
                    ctx.Instrs[i-4].OpCode == OpCodes.Ldc_I4_1 &&
                    ctx.Instrs[i-3].OpCode == OpCodes.Br &&
                    ctx.Instrs[i-2].OpCode == OpCodes.Ldarg_0 &&
                    ctx.Instrs[i-1].OpCode == OpCodes.Ldc_I4_M1 &&
                    ctx.Instrs[i].OpCode == OpCodes.Stfld
                    )
                {
                    ctx.Instrs[i - 13].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 12].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 11].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 10].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 9].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 8].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 7].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 6].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 5].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 4].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 3].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 2].OpCode = OpCodes.Nop;
                    ctx.Instrs[i - 1].OpCode = OpCodes.Nop;
                    ctx.Instrs[i].OpCode = OpCodes.Nop;
                }
            }
        }
    }
}
