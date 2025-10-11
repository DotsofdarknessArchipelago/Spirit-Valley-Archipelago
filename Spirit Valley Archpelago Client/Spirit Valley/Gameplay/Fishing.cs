using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class Fishing
    {


        [HarmonyPatch(typeof(FishingSpot), "StartFightWithRandomMonster")]
        [HarmonyPrefix]
        public static bool startfight(ref LootConfiguration lootConf, FishingSpot __instance)
        {
            ArchipelagoConsole.LogMessage($"STARTING FISHING FIGHT MAP:{MapManager.instance.mapLocationID}");
            MonsterBaseStats[] area = ArchipelagoClient.ServerData.waterspawn(SceneManager.GetActiveScene().name);

            int num = lootConf.monsterRareChance;
            if (HelperItems.save.GetIsItemActiveEffectActive(ItemActiveEffect.IncreaseRareEncounterChance))
            {
                int num2 = 50;
                num += num2;
            }
            num = Mathf.Clamp(num, 0, 100);

            MonsterTeamMemberBlueprint[] array = new MonsterTeamMemberBlueprint[1];
            MonsterTeamMemberBlueprint monsterTeamMemberBlueprint = new MonsterTeamMemberBlueprint
            {
                monster = area[UnityEngine.Random.Range(0, area.Length)],
                level = lootConf.ResolveMonsterLevel(),
                isRare = (UnityEngine.Random.Range(0, 100) < num)
            };
            array[0] = monsterTeamMemberBlueprint;
            HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(array), true, true, false, false, monsterTeamMemberBlueprint.isRare ? lootConf.monsterRareFightAILevel : lootConf.monsterNormalFightAILevel, false, MapManager.instance.biome, null, null);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }


        [HarmonyPatch(typeof(FishingSpot), "GetIsDisabled")]
        [HarmonyPrefix]
        public static bool fishquestoverwite(FishingSpot __instance, ref bool __result)
        {
            if (__instance.guid == "ba3bfc03-5543-4aae-8cae-32a537ff43de")//trail11 mainquest fishing spot
            {
                __result = true;
                return false;
            }
            if (__instance.guid == "93d16f58-6de7-4293-853e-56b4107d25e1")//Abandoned Mine mainquest fishing spot
            {
                __result = true;
                return false;
            }
            return true;
        }

        [HarmonyPatch(typeof(FishingSpot), "GetLootConfigurationForRewardCount")]
        [HarmonyPrefix]
        public static bool fishlootoverwite(FishingSpot __instance, ref LootConfiguration __result)
        {
            LootConfiguration loot = __instance.fishingSpots.lootConfiguration;
            LootDropTypePool pool = new LootDropTypePool();
            LootDropTypeConfiguration spirit = new LootDropTypeConfiguration();
            LootDropTypeConfiguration money = new LootDropTypeConfiguration();
            LootDropTypeConfiguration nothing = new LootDropTypeConfiguration();
            spirit.weight = 50;
            spirit.lootDropType = LootDropType.WildMonster;
            money.weight = 50;
            money.lootDropType = LootDropType.Money;

            pool.lootDropTypeConfigurations = [spirit, money];
            loot.lootDropTypePool = pool;
            
            __result = loot;
            return false;
        }
    }
}
