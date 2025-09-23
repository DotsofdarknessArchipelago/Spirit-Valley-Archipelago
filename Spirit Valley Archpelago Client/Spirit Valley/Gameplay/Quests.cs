using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public static class Quests
    {

        [HarmonyPatch(typeof(GameState), "AdvanceMainQuest")]
        [HarmonyPrefix]
        public static void questtest(GameState __instance, string nextQuestID)
        {
            ArchipelagoConsole.LogDebug($"MAIN QUEST ADVANCING TO: {nextQuestID}");
            int main_quests_id_start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Main_Quest_Start"]) - 1;
            switch (nextQuestID)
            {
                case "main_quest_1_doctors_appointment":
                    break;
                case "main_quest_2_captain_maria":
                    ArchipelagoClient.sendloc(main_quests_id_start + 2);
                    break;
                case "main_quest_3_first_orders":
                    ArchipelagoClient.sendloc(main_quests_id_start + 3);
                    break;
                case "main_quest_4_crimson_agent":
                    ArchipelagoClient.sendloc(main_quests_id_start + 4);
                    break;
                case "main_quest_5_super_secret_orders":
                    ArchipelagoClient.sendloc(main_quests_id_start + 5);
                    break;
                case "main_quest_6_first_mission_success":
                    ArchipelagoClient.sendloc(main_quests_id_start + 6);
                    break;
                case "main_quest_7_onward_to_greensvale":
                    ArchipelagoClient.sendloc(main_quests_id_start + 7);
                    break;
                case "main_quest_8_temple_investigation":
                    ArchipelagoClient.sendloc(main_quests_id_start + 8);
                    break;
                case "main_quest_9_harmonius_disturbance":
                    ArchipelagoClient.sendloc(main_quests_id_start + 9);
                    break;
                case "main_quest_10_consulting_dolly":
                    ArchipelagoClient.sendloc(main_quests_id_start + 10);
                    break;
                case "main_quest_11_becky_can_fix_it":
                    ArchipelagoClient.sendloc(main_quests_id_start + 11);
                    break;
                case "main_quest_12_hunt_for_the_chunk":
                    ArchipelagoClient.sendloc(main_quests_id_start + 12);
                    break;
                case "main_quest_13_bridge_crossing":
                    ArchipelagoClient.sendloc(main_quests_id_start + 13);
                    break;
                case "main_quest_14_dusty_vale_awaits":
                    ArchipelagoClient.sendloc(main_quests_id_start + 14);
                    break;
                case "main_quest_15_an_audience_with_the_king":
                    ArchipelagoClient.sendloc(main_quests_id_start + 15);
                    break;
                case "main_quest_16_the_grand_cuckold_challenge":
                    ArchipelagoClient.sendloc(main_quests_id_start + 16);
                    break;
                case "main_quest_17_license_to_battle":
                    ArchipelagoClient.sendloc(main_quests_id_start + 17);
                    break;
                case "main_quest_18_box_pusher":
                    ArchipelagoClient.sendloc(main_quests_id_start + 18);
                    break;
                case "main_quest_19_total_domination":
                    ArchipelagoClient.sendloc(main_quests_id_start + 19);
                    break;
                case "main_quest_20_a_challenge_awaits":
                    ArchipelagoClient.sendloc(main_quests_id_start + 20);
                    break;
                case "main_quest_21_a_new_challenger":
                    ArchipelagoClient.sendloc(main_quests_id_start + 21);
                    break;
                case "main_quest_22_stiff_competition":
                    ArchipelagoClient.sendloc(main_quests_id_start + 22);
                    break;
                case "main_quest_23_final_fight":
                    ArchipelagoClient.sendloc(main_quests_id_start + 23);
                    break;
                case "main_quest_24_return_of_the_champion":
                    ArchipelagoClient.sendloc(main_quests_id_start + 24);
                    break;
                case "main_quest_25_breeding_season":
                    ArchipelagoClient.sendloc(main_quests_id_start + 25);
                    break;
                case "main_quest_26_mission_success":
                    ArchipelagoClient.sendloc(main_quests_id_start + 26);
                    break;
                case "main_quest_27_quest_for_the_crystal":
                    ArchipelagoClient.sendloc(main_quests_id_start + 27);
                    break;
                case "main_quest_28_how_the_dominoes_fall":
                    ArchipelagoClient.sendloc(main_quests_id_start + 28);
                    break;
                case "main_quest_29_big_balloon_adventure":
                    ArchipelagoClient.sendloc(main_quests_id_start + 29);
                    break;
                case "main_quest_30_welcome_to_paradise":
                    ArchipelagoClient.sendloc(main_quests_id_start + 30);
                    break;
                case "main_quest_31_coconut_conundrum":
                    ArchipelagoClient.sendloc(main_quests_id_start + 31);
                    break;
                case "main_quest_32_lusty_cultists":
                    ArchipelagoClient.sendloc(main_quests_id_start + 32);
                    break;
                case "main_quest_33_savior_of_coconut_village":
                    ArchipelagoClient.sendloc(main_quests_id_start + 33);
                    break;
                case "main_quest_34_slippery_when_wet":
                    ArchipelagoClient.sendloc(main_quests_id_start + 34);
                    break;
                case "main_quest_35_glimmering_price":
                    ArchipelagoClient.sendloc(main_quests_id_start + 35);
                    break;
                case "main_quest_36_arctic_adventure":
                    ArchipelagoClient.sendloc(main_quests_id_start + 36);
                    break;
                case "main_quest_37_the_frigid_maiden":
                    ArchipelagoClient.sendloc(main_quests_id_start + 37);
                    break;
                case "main_quest_38_arctic_isles":
                    ArchipelagoClient.sendloc(main_quests_id_start + 38);
                    break;
                case "main_quest_39_paisley_bones":
                    ArchipelagoClient.sendloc(main_quests_id_start + 39);
                    break;
                case "main_quest_40_demand_for_dynamite":
                    ArchipelagoClient.sendloc(main_quests_id_start + 40);
                    break;
                case "main_quest_41_stealing_from_a_dead_man":
                    ArchipelagoClient.sendloc(main_quests_id_start + 41);
                    break;
                case "main_quest_42_the_lewd_exorcist":
                    ArchipelagoClient.sendloc(main_quests_id_start + 42);
                    break;
                case "main_quest_43_suit_in_hand":
                    ArchipelagoClient.sendloc(main_quests_id_start + 43);
                    break;
                case "main_quest_44_fishing_for_treasure":
                    ArchipelagoClient.sendloc(main_quests_id_start + 44);
                    break;
                case "main_quest_45_the_proposal":
                    ArchipelagoClient.sendloc(main_quests_id_start + 45);
                    break;
                case "main_quest_46_here_comes_the_boom":
                    ArchipelagoClient.sendloc(main_quests_id_start + 46);
                    break;
                case "main_quest_47_arctic_harmony":
                    ArchipelagoClient.sendloc(main_quests_id_start + 47);
                    break;
                case "main_quest_48_crimson_chase":
                    ArchipelagoClient.sendloc(main_quests_id_start + 48);
                    break;
                case "main_quest_49_through_the_portal":
                    ArchipelagoClient.sendloc(main_quests_id_start + 49);
                    break;
                case "main_quest_50_sanctuary_shakedown":
                    ArchipelagoClient.sendloc(main_quests_id_start + 50);
                    break;
                case "main_quest_51_hostage_situation":
                    ArchipelagoClient.sendloc(main_quests_id_start + 51);
                    break;
                case "main_quest_52_breezie_runs_free":
                    ArchipelagoClient.sendloc(main_quests_id_start + 52);
                    break;
                case "main_quest_53_desperate_dash":
                    ArchipelagoClient.sendloc(main_quests_id_start + 53);
                    break;
                case "main_quest_54_battle_for_spirit_valley":
                    ArchipelagoClient.sendloc(main_quests_id_start + 54);
                    break;
                case "main_quest_55_life_as_a_spirit_warden":
                    ArchipelagoClient.sendloc(main_quests_id_start + 55);
                    ArchipelagoClient.complete();
                    break;
                default:
                    ArchipelagoConsole.LogMessage($"MAIN QUEST NOT RECONISED: {nextQuestID}");
                    break;
            }
        }

        [HarmonyPatch(typeof(GameState), "AdvanceMainQuest")]
        [HarmonyPostfix]
        public static void questrewards(GameState __instance, string nextQuestID, ref ItemBundle[] __result)
        {
            __result = HelperItems.centbundle();
        }

        [HarmonyPatch(typeof(GameState), "CloseSideQuest")]
        [HarmonyPostfix]
        public static void sidequest(GameState __instance, string id, ref ItemBundle[] __result)
        {
            ArchipelagoConsole.LogDebug($"SIDE QUEST COMPLETING: {id}");

            __result = HelperItems.centbundle();

            int id_start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Side_Quest_Start"]);
            QuestState sideQuestStateById = __instance.GetSideQuestStateById(id);
            if (sideQuestStateById == null)
            {
                ArchipelagoConsole.LogDebug("SIDE QUEST ID ERROR");
                return;
            }
            if (sideQuestStateById.isClosed == true)
            {
                switch (id)
                {
                    case "side_quest_sparring_match":
                        ArchipelagoConsole.LogDebug("side_quest_sparring_match");
                        ArchipelagoClient.sendloc(id_start + 1);
                        break;
                    case "side_quest_larrys_treasure":
                        ArchipelagoConsole.LogDebug("side_quest_larrys_treasure");
                        ArchipelagoClient.sendloc(id_start + 2);
                        break;
                    case "side_quest_perky_petunia":
                        ArchipelagoConsole.LogDebug("side_quest_perky_petunia");
                        ArchipelagoClient.sendloc(id_start + 3);
                        break;
                    case "side_quest_pleasuring_pusseen":
                        ArchipelagoConsole.LogDebug("side_quest_pleasuring_pusseen");
                        ArchipelagoClient.sendloc(id_start + 4);
                        break;
                    case "side_quest_slithering_menace":
                        ArchipelagoConsole.LogDebug("side_quest_slithering_menace");
                        ArchipelagoClient.sendloc(id_start + 5);
                        break;
                    case "side_quest_cattle_thieves":
                        ArchipelagoConsole.LogDebug("side_quest_cattle_thieves");
                        ArchipelagoClient.sendloc(id_start + 6);
                        break;
                    case "side_quest_professional_pleasurer":
                        ArchipelagoConsole.LogDebug("side_quest_professional_pleasurer");
                        ArchipelagoClient.sendloc(id_start + 7);
                        break;
                    case "side_quest_fishy_duel":
                        ArchipelagoConsole.LogDebug("side_quest_fishy_duel");
                        ArchipelagoClient.sendloc(id_start + 8);
                        break;
                    case "side_quest_the_art_of_fishing":
                        ArchipelagoConsole.LogDebug("side_quest_the_art_of_fishing");
                        ArchipelagoClient.sendloc(id_start + 9);
                        break;
                    case "side_quest_fishmasters_challenge":
                        ArchipelagoConsole.LogDebug("side_quest_fishmasters_challenge");
                        ArchipelagoClient.sendloc(id_start + 10);
                        break;
                    case "side_quest_deadly_waters":
                        ArchipelagoConsole.LogDebug("side_quest_deadly_waters");
                        ArchipelagoClient.sendloc(id_start + 11);
                        break;
                    case "side_quest_starry_eyed_surprise":
                        ArchipelagoConsole.LogDebug("side_quest_starry_eyed_surprise");
                        ArchipelagoClient.sendloc(id_start + 12);
                        break;
                    case "side_quest_arctic_menace":
                        ArchipelagoConsole.LogDebug("side_quest_arctic_menace");
                        ArchipelagoClient.sendloc(id_start + 13);
                        break;
                    case "side_quest_legend_of_valkyrie_part1":
                        ArchipelagoConsole.LogDebug("side_quest_legend_of_valkyrie_part1");
                        ArchipelagoClient.sendloc(id_start + 14);
                        break;
                    case "side_quest_legend_of_valkyrie_part2":
                        ArchipelagoConsole.LogDebug("side_quest_legend_of_valkyrie_part2");
                        ArchipelagoClient.sendloc(id_start + 15);
                        break;
                    default:
                        ArchipelagoConsole.LogMessage($"SIDE QUEST NOT RECONISED: {id}");
                        break;
                }
            }
        }


        [HarmonyPatch(typeof(QuestManager), "GetSideQuestById")]
        [HarmonyPostfix]
        public static void piperquest(string id, QuestManager __instance, ref Quest __result)
        {
            switch (id)
            {
                case "side_quest_perky_petunia":
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"].ToString())];
                    break;
                case "side_quest_slithering_menace":
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"].ToString())];
                    break;
                case "side_quest_deadly_waters":
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_DEADLY_WATERS_SPIRIT"].ToString())];
                    break;
                case "side_quest_starry_eyed_surprise":
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"].ToString())];
                    break;
                case "side_quest_arctic_menace":
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"].ToString())];
                    break;
                case "side_quest_hunt_for_the_centiboob_part1":
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_1_SPIRIT"].ToString())];
                    break;
                case "side_quest_hunt_for_the_centiboob_part2":
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_2_SPIRIT"].ToString())];
                    break;
                case "side_quest_hunt_for_the_centiboob_part3":
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_3_SPIRIT"].ToString())];
                    break;
                default:
                    break;
            }
        }

        [HarmonyPatch(typeof(Captain), "Interact")]
        [HarmonyPrefix]
        public static bool captainquests(Captain __instance)
        {
            QuestState activeMainQuestState = HelperItems.save.GetActiveMainQuestState();
            if (activeMainQuestState != null)
            {
                if (activeMainQuestState.Quest.id == "main_quest_13_bridge_crossing")
                {
                    InventoryItemState i = HelperItems.save.GetInventoryItemStateForItem(ItemManager.instance.GetItemAssetByName("KeyItem_PowerCrystal"));
                    if (i == null || i.count <= 0)
                    {
                        ArchipelagoConsole.LogMessage("\"Power Crystal\" Item required to continue questline");
                        return false;
                    }
                }
                else if (activeMainQuestState.Quest.id == "main_quest_28_how_the_dominoes_fall")
                {
                    InventoryItemState i = HelperItems.save.GetInventoryItemStateForItem(ItemManager.instance.GetItemAssetByName("KeyItem_YellowHarmonyCrystal"));
                    if (i == null || i.count <= 0)
                    {
                        ArchipelagoConsole.LogMessage("\"Yellow Harmony Crystal\" Item required to continue questline");
                        return false;
                    }
                }
            }
            return true;
        }

        [HarmonyPatch(typeof(SergeantCassie), "Interact")]
        [HarmonyPrefix]
        public static bool cassiequests(SergeantCassie __instance)
        {
            QuestState activeMainQuestState = HelperItems.save.GetActiveMainQuestState();
            if (activeMainQuestState != null)
            {
                if (activeMainQuestState.Quest.id == "main_quest_5_super_secret_orders")
                {
                    InventoryItemState i = HelperItems.save.GetInventoryItemStateForItem(ItemManager.instance.GetItemAssetByName("KeyItem_SuperSecretOrders"));
                    if (i == null || i.count<=0)
                    {
                        ArchipelagoConsole.LogMessage("\"Super Secret Orders\" Item required to continue questline");
                        return false;
                    }
                }
            }
            return true;
        }

        [HarmonyPatch(typeof(Sassy), "Interact")]
        [HarmonyPrefix]
        public static bool sassyquests(SergeantCassie __instance)
        {
            QuestState activeMainQuestState = HelperItems.save.GetActiveMainQuestState();
            if (activeMainQuestState != null)
            {
                if (activeMainQuestState.Quest.id == "main_quest_20_a_challenge_awaits")
                {
                    InventoryItemState i = HelperItems.save.GetInventoryItemStateForItem(ItemManager.instance.GetItemAssetByName("KeyItem_SpiritHandlerLicense"));
                    if (i == null || i.count <= 0)
                    {
                        ArchipelagoConsole.LogMessage("\"Spirit Handler Licence\" Item required to continue questline");
                        return false;
                    }
                }
            }
            return true;
        }

        [HarmonyPatch(typeof(MinerJohnson), "Interact")]
        [HarmonyPrefix]
        public static bool minerquests(SergeantCassie __instance)
        {
            QuestState activeMainQuestState = HelperItems.save.GetActiveMainQuestState();
            if (activeMainQuestState != null)
            {
                if (activeMainQuestState.Quest.id == "main_quest_43_suit_in_hand")
                {
                    InventoryItemState i = HelperItems.save.GetInventoryItemStateForItem(ItemManager.instance.GetItemAssetByName("KeyItem_FancySuit"));
                    if (i == null || i.count <= 0)
                    {
                        ArchipelagoConsole.LogMessage("\"Fancy Suit\" Item required to continue questline");
                        return false;
                    }
                }
            }
            return true;
        }

        [HarmonyPatch(typeof(PaisleyBones_Frostville), "Interact")]
        [HarmonyPrefix]
        public static bool dynamitequests(PaisleyBones_Frostville __instance)
        {
            QuestState activeMainQuestState = HelperItems.save.GetActiveMainQuestState();
            if (activeMainQuestState != null)
            {
                if (activeMainQuestState.Quest.id == "main_quest_46_here_comes_the_boom")
                {
                    InventoryItemState i = HelperItems.save.GetInventoryItemStateForItem(ItemManager.instance.GetItemAssetByName("KeyItem_FancySuit"));
                    if (i == null || i.count <= 0)
                    {
                        ArchipelagoConsole.LogMessage("\"Dynamite\" Item required to continue questline");
                        return false;
                    }
                }
            }
            return true;
        }

        [HarmonyPatch(typeof(CollectSpiritQuestNPCGeneric), "Interact")]
        [HarmonyPostfix]
        public static void collectionsidequest1(CollectSpiritQuestNPCGeneric __instance)
        {

            QuestState sideQuestStateById = HelperItems.save.GetSideQuestStateById(__instance.sideQuestID);
            if (sideQuestStateById == null) { return; }
            if (!sideQuestStateById.isClosed)
            {
                ArchipelagoConsole.LogMessage($"SPIRIT REQUIRED FOR QUEST: {ArchipelagoData.getquestspirit(__instance.sideQuestID)}");
            }
        }

        [HarmonyPatch(typeof(DefeatOrCaptureSpiritsQuest_NPC_Generic), "Interact")]
        [HarmonyPostfix]
        public static void collectionsidequest2(DefeatOrCaptureSpiritsQuest_NPC_Generic __instance)
        {

            QuestState sideQuestStateById = HelperItems.save.GetSideQuestStateById(__instance.sideQuestID);
            if (sideQuestStateById == null) { return; }
            if (!sideQuestStateById.isClosed)
            {
                ArchipelagoConsole.LogMessage($"SPIRIT REQUIRED FOR QUEST: {ArchipelagoData.getquestspirit(__instance.sideQuestID)}");
            }
        }

        [HarmonyPatch(typeof(OldMaster), "Interact")]
        [HarmonyPrefix]
        public static void collectionmainquest(OldMaster __instance)
        {

            QuestState activeMainQuestState = HelperItems.save.GetActiveMainQuestState();
            if (activeMainQuestState == null) { return; }
            if (activeMainQuestState.Quest.id == "main_quest_19_total_domination")
            {
                HelperItems.save.mainQuestStates.Last<QuestState>().Quest.requiredMonsters = [ArchipelagoClient.ServerData.getspirit(ArchipelagoData.getquestspirit("main_quest_19_total_domination"))];
            }
        }

        [HarmonyPatch(typeof(OldMaster), "Interact")]
        [HarmonyPostfix]
        public static void collectionmainquest2(OldMaster __instance)
        {

            QuestState activeMainQuestState = HelperItems.save.GetActiveMainQuestState();
            if (activeMainQuestState == null) { return; }
            if (activeMainQuestState.Quest.id == "main_quest_19_total_domination")
            {
                ArchipelagoConsole.LogMessage($"SPIRIT REQUIRED FOR QUEST: {ArchipelagoData.getquestspirit("main_quest_19_total_domination")}");
            }
        }

        [HarmonyPatch(typeof(Skipper), "Interact")]
        [HarmonyPostfix]
        public static void collectionmainsidequest1(Skipper __instance)
        {

            QuestState activeMainQuestState = HelperItems.save.GetActiveMainQuestState();
            if (activeMainQuestState == null) { return; }
            if (activeMainQuestState.Quest.id == "main_quest_19_total_domination")
            {
                ArchipelagoConsole.LogMessage($"SPIRIT REQUIRED FOR QUEST: {ArchipelagoData.getquestspirit("side_quest_deadly_waters")}");
            }
        }

    }
}
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  