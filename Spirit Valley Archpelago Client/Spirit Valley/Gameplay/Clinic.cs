using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class Clinic
    {
        [HarmonyPatch(typeof(MapManager), "Start")]
        [HarmonyPostfix]
        public static void clinic(MapManager __instance)
        {
            if (__instance.isClinicScene)
            {
                SpiritValleyArchipelago.ArchipelagoClient.DeathLinkHandler.processingdeath = false;
            }
        }
    }
}
