using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;

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

            if (__instance.AffectionLevel == 0) { return; }

            for (int i = 0; i < GameDataManager.instance.databaseEntries.Length; i++)
            {
                if (GameDataManager.instance.databaseEntries[i].name == __instance.baseStatsName)
                {
                    int affectionidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Spirit_Affection_Start"]) + (i * 5);
                    for (int j = 1; j <= __instance.AffectionLevel; j++)
                    {
                        ArchipelagoClient.sendloc(affectionidstart + j);
                    }
                    return;
                }
            }            
        }

        [HarmonyPatch(typeof(MonsterState), "AddAffection")]
        [HarmonyPostfix]
        public static void affectionpost(MonsterState __instance, int amount, int __state)
        {
            int affectionidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Spirit_Affection_Start"]);

            if (__instance.AffectionLevel != __state)
            {
                for (int i = 0; i < GameDataManager.instance.databaseEntries.Length; i++)
                {
                    if (GameDataManager.instance.databaseEntries[i].name == __instance.baseStatsName)
                    {
                        for (int j = 1; j <= __instance.AffectionLevel; j++)
                        {
                            ArchipelagoClient.sendloc(affectionidstart + (i * 5) + j);
                        }
                        return;
                    }
                }
            }

            if (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["goal"]) == 3)
            {
                bool goal = true;
                for (int i = 0; i < 75; i++)
                {
                    if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(affectionidstart + (i * 5) + 5)) { goal = false; break; }
                }
                if (goal)
                {
                    ArchipelagoClient.complete();
                }
            }

        }

        [HarmonyPatch(typeof(ConsumablesTab), "GainAffectionCoroutine")]
        [HarmonyPrefix]
        public static void maxaffectionpre(MonsterState monsterState)
        {
            if (monsterState.GetIsAlive() && monsterState.IsAtMaxAffectionLevel())
            {
                for (int i = 0; i < GameDataManager.instance.databaseEntries.Length; i++)
                {
                    if (GameDataManager.instance.databaseEntries[i].name == monsterState.baseStatsName)
                    {
                        int affectionidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Spirit_Affection_Start"]) + (i * 5);
                        ArchipelagoClient.sendloc(affectionidstart + 1);
                        ArchipelagoClient.sendloc(affectionidstart + 2);
                        ArchipelagoClient.sendloc(affectionidstart + 3);
                        ArchipelagoClient.sendloc(affectionidstart + 4);
                        ArchipelagoClient.sendloc(affectionidstart + 5);
                        return;
                    }
                }
            }
        }

        [HarmonyPatch(typeof(Minigame), "AffectionLevelUpCoroutine")]
        [HarmonyPrefix]
        public static void maxaffectionpre2(ref MinigameContext ___context)
        {
            MonsterState monsterState = ___context.monsterState;
            if (monsterState.IsAtMaxAffectionLevel())
            {
                for (int i = 0; i < GameDataManager.instance.databaseEntries.Length; i++)
                {
                    if (GameDataManager.instance.databaseEntries[i].name == monsterState.baseStatsName)
                    {
                        int affectionidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Spirit_Affection_Start"]) + (i * 5);
                        ArchipelagoClient.sendloc(affectionidstart + 1);
                        ArchipelagoClient.sendloc(affectionidstart + 2);
                        ArchipelagoClient.sendloc(affectionidstart + 3);
                        ArchipelagoClient.sendloc(affectionidstart + 4);
                        ArchipelagoClient.sendloc(affectionidstart + 5);
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
