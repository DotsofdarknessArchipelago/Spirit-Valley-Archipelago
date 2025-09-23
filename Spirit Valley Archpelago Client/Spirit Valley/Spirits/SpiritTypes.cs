using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Spirits
{
    [HarmonyPatch]
    public class SpiritTypes
    {

        //[HarmonyPatch(typeof(ElementalStat), "GetDoesIncreasedDamageTo")]
        //[HarmonyPrefix]
        //public static void elementdamageadd(ElementalStat damageTargetStat, ElementalStat __instance)
        //{
        //    List<ElementalStat> inc = new List<ElementalStat>();
        //    List<ElementalStat> dec = new List<ElementalStat>();
        //    foreach (var t2 in ArchipelagoClient.ServerData.typedata[stattostring(__instance.type)])
        //    {
        //        if (t2.Value == 1) { inc.Add(MonsterManager.instance.GetElementalStatByType(stringtostat(t2.Key))); }
        //        if (t2.Value == -1) { dec.Add(MonsterManager.instance.GetElementalStatByType(stringtostat(t2.Key))); }
        //    }
        //    __instance.increasedDamageTo = inc.ToArray();
        //    __instance.decreasedDamageTo = dec.ToArray();
        //}
        //
        //[HarmonyPatch(typeof(ElementalStat), "GetDoesDecreasedDamageTo")]
        //[HarmonyPrefix]
        //public static void elementdamagesub(ElementalStat damageTargetStat, ElementalStat __instance)
        //{
        //    List<ElementalStat> inc = new List<ElementalStat>();
        //    List<ElementalStat> dec = new List<ElementalStat>();
        //    foreach (var t2 in ArchipelagoClient.ServerData.typedata[stattostring(__instance.type)])
        //    {
        //        if (t2.Value == 1) { inc.Add(MonsterManager.instance.GetElementalStatByType(stringtostat(t2.Key))); }
        //        if (t2.Value == -1) { dec.Add(MonsterManager.instance.GetElementalStatByType(stringtostat(t2.Key))); }
        //    }
        //    __instance.increasedDamageTo = inc.ToArray();
        //    __instance.decreasedDamageTo = dec.ToArray();
        //}
        //
        //[HarmonyPatch(typeof(ElementalStatDetailsContainer), "PopulateIconContainers")]
        //[HarmonyPrefix]
        //public static void elementmangae1(ElementalStat elementalStat)
        //{
        //    List<ElementalStat> inc = new List<ElementalStat>();
        //    List<ElementalStat> dec = new List<ElementalStat>();
        //    foreach (var t2 in ArchipelagoClient.ServerData.typedata[stattostring(elementalStat.type)])
        //    {
        //        if (t2.Value == 1) { inc.Add(MonsterManager.instance.GetElementalStatByType(stringtostat(t2.Key))); }
        //        if (t2.Value == -1) { dec.Add(MonsterManager.instance.GetElementalStatByType(stringtostat(t2.Key))); }
        //    }
        //    elementalStat.increasedDamageTo = inc.ToArray();
        //    elementalStat.decreasedDamageTo = dec.ToArray();
        //}
        //
        //[HarmonyPatch(typeof(MonsterManager), "GetReceivesIncreasedDamageFromElementalStatsList")]
        //[HarmonyPrefix]
        //public static bool elementmangae2(MonsterManager __instance, ElementalStat targetStats, ref List<ElementalStat> __result)
        //{
        //    List<ElementalStat> list = new List<ElementalStat>();
        //    foreach (ElementalStat elementalStat in __instance.elementalStats)
        //    {
        //        if (ArchipelagoClient.ServerData.typedata[stattostring(elementalStat.type)][stattostring(targetStats.type)] == 1) { list.Add(elementalStat); }
        //    }
        //    __result = list;
        //    return false;
        //}
        //
        //
        //[HarmonyPatch(typeof(MonsterManager), "GetReceivesDecreasedDamageFromElementalStatsList")]
        //[HarmonyPrefix]
        //public static bool elementmangae3(MonsterManager __instance, ElementalStat targetStat, ref List<ElementalStat> __result)
        //{
        //    List<ElementalStat> list = new List<ElementalStat>();
        //    foreach (ElementalStat elementalStat in __instance.elementalStats)
        //    {
        //        if (ArchipelagoClient.ServerData.typedata[stattostring(elementalStat.type)][stattostring(targetStat.type)] == -1) { list.Add(elementalStat); }
        //    }
        //    __result = list;
        //    return false;
        //}
        //
        //
        //
        //public static string stattostring(ElementalType type)
        //{
        //    switch (type)
        //    {
        //        case ElementalType.Slime:
        //            return "Slime";
        //        case ElementalType.Furry:
        //            return "Furry";
        //        case ElementalType.Plant:
        //            return "Plant";
        //        case ElementalType.Scalie:
        //            return "Scalie";
        //        case ElementalType.Lust:
        //            return "Lust";
        //        case ElementalType.Oppai:
        //            return "Oppai";
        //        case ElementalType.Demon:
        //            return "Demon";
        //        case ElementalType.Avian:
        //            return "Avian";
        //        case ElementalType.Aquatic:
        //            return "Aquatic";
        //        default:
        //            break;
        //    }
        //    return null;
        //}
        //
        //public static ElementalType stringtostat(string type)
        //{
        //    switch (type)
        //    {
        //        case "Slime":
        //            return ElementalType.Slime;
        //        case "Furry":
        //            return ElementalType.Furry;
        //        case "Plant":
        //            return ElementalType.Plant;
        //        case "Scalie":
        //            return ElementalType.Scalie;
        //        case "Lust":
        //            return ElementalType.Lust;
        //        case "Oppai":
        //            return ElementalType.Oppai;
        //        case "Demon":
        //            return ElementalType.Demon;
        //        case "Avian":
        //            return ElementalType.Avian;
        //        case "Aquatic":
        //            return ElementalType.Aquatic;
        //        default:
        //            break;
        //    }
        //    return ElementalType.Normal;
        //}
    }
}
