using HarmonyLib;
using System.Collections.Generic;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Spirits
{
    [HarmonyPatch]
    public class Evolution
    {
        [HarmonyPatch(typeof(MonsterManager), "GetEvolutionPathForMonster")]
        [HarmonyPrefix]
        public static bool overwriteevo(MonsterManager __instance, MonsterBaseStats monster,ref List<EvolutionPoint> __result)
        {
            List<EvolutionPoint> list = new List<EvolutionPoint>();
            MonsterBaseStats monsterBaseStats = monster;


            list.Add(new EvolutionPoint
            {
                fromMonster = monsterBaseStats,
                levelBreakPoint = 1,
                toMonster = monsterBaseStats
            });

            if (monsterBaseStats.nextEvolutionBaseStats != null)
            {
                list.Add(new EvolutionPoint
                {
                    fromMonster = monsterBaseStats,
                    levelBreakPoint = monsterBaseStats.evolutionLevelBreakpoint,
                    toMonster = monsterBaseStats.nextEvolutionBaseStats
                });
            }

            __result = list;
            return false;
        }
    }
}
