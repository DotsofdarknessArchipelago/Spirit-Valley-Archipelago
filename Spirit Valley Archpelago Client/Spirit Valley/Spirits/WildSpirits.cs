using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System.Collections.Generic;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class WildSpirits
    {

        [HarmonyPatch(typeof(MapManager), "StartFightWithRandomMonster")]
        [HarmonyPrefix]
        public static void grassoverrite(MapManager __instance)
        {
            switch (__instance.mapLocationID)
            {
                case MapLocationID.Trail1:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 01");
                    break;
                case MapLocationID.EvergreenOutpost:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Evergreen Outpost");
                    break;
                case MapLocationID.Trail2:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 02");
                    break;
                case MapLocationID.MillysFarm:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Milly's Farm");
                    break;
                case MapLocationID.Trail3:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 03");
                    break;
                case MapLocationID.EvergreenCaverns:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Evergreen Caverns");
                    break;
                case MapLocationID.Trail4:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 04");
                    break;
                case MapLocationID.Trail5:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 05");
                    break;
                case MapLocationID.SandyTunnels:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Sandy Tunnels");
                    break;
                case MapLocationID.Trail6:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 06");
                    break;
                case MapLocationID.DairyFarm:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Dairy Farm");
                    break;
                case MapLocationID.Trail7:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 07");
                    break;
                case MapLocationID.Trail8:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 08");
                    break;
                case MapLocationID.DustyGrotto:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Dusty Grotto");
                    break;
                case MapLocationID.OldMastersHut:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Old Masters Hut");
                    break;
                case MapLocationID.CaveOfTorment:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Cave of Torment");
                    break;
                case MapLocationID.Trail9:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 09");
                    break;
                case MapLocationID.CrashSite:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Crash Site");
                    break;
                case MapLocationID.Trail10:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 10");
                    break;
                case MapLocationID.Trail11:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 11");
                    break;
                case MapLocationID.Trail12:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 12");
                    break;
                case MapLocationID.FishingHut:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Fishing Hut");
                    break;
                case MapLocationID.Trail13:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 13");
                    break;
                case MapLocationID.Trail14:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 14");
                    break;
                case MapLocationID.ColdHarbor:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Cold Harbour");
                    break;
                case MapLocationID.Trail15:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 15");
                    break;
                case MapLocationID.Trail16:
                    if (__instance.biome == Biome.Arctic)
                    {
                        __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 16");
                    }
                    else if (__instance.biome == Biome.Cave)
                    {
                        __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 16 Cave");
                    }
                    break;
                case MapLocationID.AbandonedMine:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Abandoned Mine");
                    break;
                case MapLocationID.Trail17:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 17");
                    break;
                case MapLocationID.Trail18:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 18");
                    break;
                case MapLocationID.Trail19:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 19");
                    break;
                case MapLocationID.Trail20:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 20");
                    break;
                case MapLocationID.Trail21:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 21");
                    break;
                case MapLocationID.SpiritPassage:
                    __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Spirit Passage");
                    break;
                case MapLocationID.Trail22:
                    if (__instance.biome == Biome.Sanctuary)
                    {
                        __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 22");
                    }
                    else if (__instance.biome == Biome.Cave)
                    {
                        __instance.wildMonsterPool = ArchipelagoClient.ServerData.grassspawn("Trail 22 Cave");
                    }
                    break;
                default:
                    break;
            }
        }

        [HarmonyPatch(typeof(LocationDetailsPopup), "UpdateUI")]
        [HarmonyPrefix]
        public static void mapoverrwite(LocationDetailsPopup __instance, ref MapMenuLocation ___mapMenuLocation)
        {
            
            switch (___mapMenuLocation.mapLocationID)
            {
                case MapLocationID.Trail1:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 01");
                    break;
                case MapLocationID.EvergreenOutpost:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Evergreen Outpost");
                    break;
                case MapLocationID.Trail2:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 02");
                    break;
                case MapLocationID.MillysFarm:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Milly's Farm");
                    break;
                case MapLocationID.Trail3:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 03");
                    break;
                case MapLocationID.EvergreenCaverns:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Evergreen Caverns");
                    break;
                case MapLocationID.Trail4:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 04");
                    break;
                case MapLocationID.Trail5:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 05");
                    break;
                case MapLocationID.SandyTunnels:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Sandy Tunnels");
                    break;
                case MapLocationID.Trail6:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 06");
                    break;
                case MapLocationID.DairyFarm:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Dairy Farm");
                    break;
                case MapLocationID.Trail7:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 07");
                    break;
                case MapLocationID.Trail8:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 08");
                    break;
                case MapLocationID.DustyGrotto:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Dusty Grotto");
                    break;
                case MapLocationID.OldMastersHut:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Old Masters Hut");
                    break;
                case MapLocationID.CaveOfTorment:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Cave of Torment");
                    break;
                case MapLocationID.Trail9:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 09");
                    break;
                case MapLocationID.CrashSite:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Crash Site");
                    break;
                case MapLocationID.Trail10:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 10");
                    break;
                case MapLocationID.Trail11:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 11");
                    break;
                case MapLocationID.Trail12:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 12");
                    break;
                case MapLocationID.FishingHut:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Fishing Hut");
                    break;
                case MapLocationID.Trail13:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 13");
                    break;
                case MapLocationID.Trail14:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 14");
                    break;
                case MapLocationID.ColdHarbor:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Cold Harbour");
                    break;
                case MapLocationID.Trail15:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 15");
                    break;
                case MapLocationID.Trail16:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 16");
                    break;
                case MapLocationID.AbandonedMine:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Abandoned Mine");
                    break;
                case MapLocationID.Trail17:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 17");
                    break;
                case MapLocationID.Trail18:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 18");
                    break;
                case MapLocationID.Trail19:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 19");
                    break;
                case MapLocationID.Trail20:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 20");
                    break;
                case MapLocationID.Trail21:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 21");
                    break;
                case MapLocationID.SpiritPassage:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Spirit Passage");
                    break;
                case MapLocationID.Trail22:
                    ___mapMenuLocation.monsters = ArchipelagoClient.ServerData.mapspawn("Trail 22");
                    break;
                default:
                    break;
            }
        }
    }
}
