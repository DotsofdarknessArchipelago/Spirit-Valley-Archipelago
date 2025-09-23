using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using System.Collections.Generic;
using System.Text;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Spirits
{
    [HarmonyPatch]
    public class Catch
    {
        [HarmonyPatch(typeof(GameEventManager), "OnMonsterCaptured")]
        [HarmonyPrefix]
        public static void moncaught(MonsterState monsterState)
        {
            int startid = 0;
            int rarestartid = 0;
            if (monsterState.isRare)
            {
                rarestartid = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Spirit_Rare_Start"]);
            }
            startid = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Spirit_Id_Start"]);
            
            for (int i = 0; i < GameDataManager.instance.databaseEntries.Length; i++)
            {
                if (GameDataManager.instance.databaseEntries[i].name == monsterState.baseStatsName)
                {
                    if (rarestartid != 0){ArchipelagoClient.sendloc(rarestartid + i + 1);}
                    ArchipelagoClient.sendloc(startid + i + 1);
                    return;
                }
            }
        }


        [HarmonyPatch(typeof(ItemManager), "GetGuaranteedCatchBelowLevelForCatchPotency")]
        [HarmonyPrefix]
        public static bool guarenteedcatch(ref int __result)
        {
            if (Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Catch_Cheat"]))
            {
                __result = 200;
                return false;
            }
            return true;
        }

    }
}
