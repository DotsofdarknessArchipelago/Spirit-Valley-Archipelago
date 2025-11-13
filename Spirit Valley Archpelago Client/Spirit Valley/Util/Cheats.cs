using HarmonyLib;
using UnityEngine;
using UnityEngine.Tilemaps;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Util
{
    [HarmonyPatch]
    public class Cheats
    {
        public static bool disable = false;

        public static void wallhaks()
        {
            var map = GameObject.Find("Map/Walls");
            if (map == null)
            {
                map = GameObject.Find("ParadiseIslandMap/Walls");
            }
            if (map == null)
            {
                map = GameObject.Find("ArcticMap/Walls");
            }
            if (map == null)
            {
                map = GameObject.Find("SanctuaryMap/Walls");
            }
            map.GetComponent<TilemapCollider2D>().enabled = false;
        }
    }
}
