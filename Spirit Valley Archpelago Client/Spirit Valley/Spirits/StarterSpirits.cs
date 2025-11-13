using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using UnityEngine;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class StarterSpirits
    {
        [HarmonyPatch(typeof(FirstClinicVisitSequence), "PlayCoroutine")]
        [HarmonyPrefix]
        public static void overwritestarters(FirstClinicVisitSequence __instance)
        {
            OverworldMonster s1 = GameObject.Find("ClinicMap/Sequences/ClinicFirstVisitSequence/Pusseen_Overworld").GetComponent<OverworldMonster>();
            OverworldMonster s2 = GameObject.Find("ClinicMap/Sequences/ClinicFirstVisitSequence/Boobae_Overworld").GetComponent<OverworldMonster>();
            OverworldMonster s3 = GameObject.Find("ClinicMap/Sequences/ClinicFirstVisitSequence/Octopussy_Overworld").GetComponent<OverworldMonster>();

            s1.monsterBlueprint.monster = MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.grassdata["Trail1"][0]);
            s2.monsterBlueprint.monster = MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.grassdata["Trail1"][1]);
            s3.monsterBlueprint.monster = MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.grassdata["Trail1"][2]);

        }
    }
}
