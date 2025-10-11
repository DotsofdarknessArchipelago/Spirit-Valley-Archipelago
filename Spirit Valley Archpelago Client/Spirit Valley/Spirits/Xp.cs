using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Spirits
{
    [HarmonyLib.HarmonyPatch]
    public static class Xp
    {
        [HarmonyPatch(typeof(MonsterState), "AddXp")]
        [HarmonyPrefix]
        public static void xpmod(ref int amount)
        {
            ArchipelagoConsole.LogDebug($"adding xp {amount}");
            float mod = (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Xp_Modifer"])/100);
            if (mod == 0 ) { amount = 0; }
            else
            {
                amount = (int)(amount * mod);
            }
            ArchipelagoConsole.LogDebug($"changed xp {amount}");
        }
    }
}
