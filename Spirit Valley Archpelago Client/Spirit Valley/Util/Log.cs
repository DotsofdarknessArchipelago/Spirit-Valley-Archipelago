using HarmonyLib;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Util
{
    [HarmonyLib.HarmonyPatch]
    public static class Log
    {
        //[HarmonyPatch(typeof(D), "Log")]
        //[HarmonyPrefix]
        //public static void log(object o)
        //{
        //    ArchipelagoConsole.LogMessage("LOGGING D : ");
        //    ArchipelagoConsole.LogMessage($"{o}");
        //}
        //
        //[HarmonyPatch(typeof(D), "LogWarning")]
        //[HarmonyPrefix]
        //public static void logwarning(object o)
        //{
        //    ArchipelagoConsole.LogMessage("LOGGING D WARNING: ");
        //    ArchipelagoConsole.LogMessage($"{o}");
        //}
        //
        //[HarmonyPatch(typeof(D), "LogList")]
        //[HarmonyPrefix]
        //public static void loglist(IEnumerable o)
        //{
        //    ArchipelagoConsole.LogMessage("LOGGING D LIST:");
        //    foreach (var item in o)
        //    {
        //        ArchipelagoConsole.LogMessage($"{item}");
        //    }
        //}
    }
}
