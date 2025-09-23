using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using System.Collections.Generic;
using System.Text;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Spirits
{
    [HarmonyPatch]
    public class Affection
    {
        [HarmonyPatch(typeof(MonsterState), "AddAffection")]
        [HarmonyPrefix]
        public static void affectionpre(MonsterState __instance, int amount, out int __state)
        {
            __state = __instance.AffectionLevel;
        }

        [HarmonyPatch(typeof(MonsterState), "AddAffection")]
        [HarmonyPostfix]
        public static void affectionpost(MonsterState __instance, int amount, int __state)
        {
            if (__instance.AffectionLevel != __state)
            {
                int affectionidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Spirit_Affection_Start"]);
                for (int i = 0; i < GameDataManager.instance.databaseEntries.Length; i++)
                {
                    if (GameDataManager.instance.databaseEntries[i].name == __instance.baseStatsName)
                    {
                        ArchipelagoClient.sendloc(affectionidstart +(i*5)+__instance.AffectionLevel);
                        return;
                    }
                }
            }
        }

        [HarmonyPatch(typeof(Minigame), "TestRectOverlaps")]
        [HarmonyPostfix]
        public static void guarenteedminigame(ref bool __result)
        {
            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Minigame_Cheat"])) { return; }
            __result = true;
        }
    }
}
