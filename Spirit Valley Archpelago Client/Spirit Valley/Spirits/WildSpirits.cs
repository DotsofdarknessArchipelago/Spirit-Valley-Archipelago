using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System.Collections.Generic;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class WildSpirits
    {

        [HarmonyPatch(typeof(MapManager), "StartFightWithRandomMonster")]
        [HarmonyPrefix]
        public static void grassoverrite(MapManager __instance)
        {
            __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn(SceneManager.GetActiveScene().name);
        }

        [HarmonyPatch(typeof(LocationDetailsPopup), "UpdateUI")]
        [HarmonyPrefix]
        public static void mapoverrwite(LocationDetailsPopup __instance, ref MapMenuLocation ___mapMenuLocation)
        {
            ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn(___mapMenuLocation.mapLocationID);
        }
    }
}
