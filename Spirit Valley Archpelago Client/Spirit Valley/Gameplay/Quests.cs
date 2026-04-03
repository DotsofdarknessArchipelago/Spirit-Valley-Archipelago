using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using System.Collections.Generic;
using UnityEngine.Localization;
using UnityEngine.Localization.Settings;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public static class Quests
    {

        /// <summary>
        /// send relevent location for a completed main quest when it gets advanced
        /// </summary>
        [HarmonyPatch(typeof(GameState), "AdvanceMainQuest")]
        [HarmonyPrefix]
        public static bool mainquest(GameState __instance, string nextQuestID, ref ItemBundle[] __result)
        {
            ArchipelagoConsole.LogDebug($"MAIN QUEST ADVANCING TO: {nextQuestID}");
            int main_quests_id_start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Main_Quest_Start"]) - 1;
            switch (nextQuestID)
            {
                case "main_quest_1_doctors_appointment":
                    return true;
                case "main_quest_2_captain_maria":
                    if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"]))
                    {
                        ArchipelagoConsole.LogDebug("Main Missions YMAL option false completing all main missions");
                        List<QuestState> ql = [];
                        foreach (Quest q in QuestManager.instance.mainQuest)
                        {
                            if (q.id == "main_quest_55_life_as_a_spirit_warden")
                            {
                                ql.Add(new(q, QuestState.Type.MainQuest));
                                break;
                            }
                            ql.Add(new(q, QuestState.Type.MainQuest) { isClosed = true });
                        }
                        HelperItems.save.mainQuestStates = ql;
                    }
                    else
                    {
                        ArchipelagoClient.sendloc(main_quests_id_start + 2);
                    }
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
                    if (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["goal"]) == 0) ArchipelagoClient.complete();
                    break;
                default:
                    ArchipelagoConsole.LogMessage($"MAIN QUEST NOT RECONISED: {nextQuestID}");
                    break;
            }

            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"]))
            {
                __result = HelperItems.centbundle();
                return false;
            }
            return true;

        }


        /// <summary>
        /// set the quest reward to be a single coin
        /// NOTE try and fix the problem when setting the reward to be nothing
        /// </summary>
        [HarmonyPatch(typeof(GameState), "AdvanceMainQuest")]
        [HarmonyPostfix]
        public static void questrewards(GameState __instance, string nextQuestID, ref ItemBundle[] __result)
        {
            __result = HelperItems.centbundle();
        }


        /// <summary>
        /// send the relevent location for a side quest once its complete
        /// </summary>
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
                    case "side_quest_hunt_for_the_centiboob_part1":
                        ArchipelagoConsole.LogDebug("side_quest_hunt_for_the_centiboob_part1");
                        ArchipelagoClient.sendloc(id_start + 16);
                        break;
                    case "side_quest_hunt_for_the_centiboob_part2":
                        ArchipelagoConsole.LogDebug("side_quest_hunt_for_the_centiboob_part2");
                        ArchipelagoClient.sendloc(id_start + 17);
                        break;
                    case "side_quest_hunt_for_the_centiboob_part3":
                        ArchipelagoConsole.LogDebug("side_quest_hunt_for_the_centiboob_part3");
                        ArchipelagoClient.sendloc(id_start + 18);
                        break;
                    case "side_quest_simulated_scuffle":
                        ArchipelagoConsole.LogDebug("side_quest_simulated_scuffle");
                        ArchipelagoClient.sendloc(id_start + 19);
                        break;
                    case "side_quest_gold_plated":
                        ArchipelagoConsole.LogDebug("side_quest_gold_plated");
                        ArchipelagoClient.sendloc(id_start + 20);
                        break;
                    default:
                        ArchipelagoConsole.LogMessage($"SIDE QUEST NOT RECONISED: {id}");
                        break;
                }
            }
        }


        /// <summary>
        /// overrite the spirit required in the side quests
        /// </summary>
        [HarmonyPatch(typeof(QuestManager), "GetSideQuestById")]
        [HarmonyPostfix]
        public static void sidequestoverwrite(string id, QuestManager __instance, ref Quest __result)
        {

            LocalizedString newspirit = null; //= MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.getquestspirit(__instance.sideQuestID)).monsterName;
            LocalizedString oldspirit = null;

            switch (id)
            {
                case "side_quest_perky_petunia":
                    oldspirit = __result.requiredMonsters[0].monsterName;
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"].ToString())];
                    break;
                case "side_quest_slithering_menace":
                    oldspirit = __result.requiredMonsters[0].monsterName;
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"].ToString())];
                    break;
                case "side_quest_deadly_waters":
                    oldspirit = __result.requiredMonsters[0].monsterName;
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_DEADLY_WATERS_SPIRIT"].ToString())];
                    break;
                case "side_quest_starry_eyed_surprise":
                    oldspirit = __result.requiredMonsters[0].monsterName;
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"].ToString())];
                    break;
                case "side_quest_arctic_menace":
                    oldspirit = __result.requiredMonsters[0].monsterName;
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"].ToString())];
                    break;
                case "side_quest_hunt_for_the_centiboob_part1":
                    oldspirit = __result.requiredMonsters[0].monsterName;
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_1_SPIRIT"].ToString())];
                    break;
                case "side_quest_hunt_for_the_centiboob_part2":
                    oldspirit = __result.requiredMonsters[0].monsterName;
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_2_SPIRIT"].ToString())];
                    break;
                case "side_quest_hunt_for_the_centiboob_part3":
                    oldspirit = __result.requiredMonsters[0].monsterName;
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_3_SPIRIT"].ToString())];
                    break;
                default:
                    return;
            }

            newspirit = __result.requiredMonsters[0].monsterName;

            if (oldspirit.GetLocalizedString() == newspirit.GetLocalizedString()) { return; }

            LocalizedStringDatabase db = LocalizationSettings.Instance.GetStringDatabase();

            if (__result.description.GetLocalizedString().Contains(oldspirit.GetLocalizedString()))
            {
                db.GetTable(__result.description.TableReference).AddEntryFromReference(__result.description.TableEntryReference, __result.description.GetLocalizedString().Replace(oldspirit.GetLocalizedString(), newspirit.GetLocalizedString()));
            }
        }

        /// <summary>
        /// overrite the spirit required in the side quests
        /// </summary>
        [HarmonyPatch(typeof(QuestManager), "GetMainQuestById")]
        [HarmonyPostfix]
        public static void mainquestoverwrite(string id, QuestManager __instance, ref Quest __result)
        {

            LocalizedString newspirit = null;
            LocalizedString oldspirit = MonsterManager.instance.GetBaseStatsByName("Domina").monsterName; ;

            switch (id)
            {
                case "main_quest_19_total_domination":
                    __result.requiredMonsters = [MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.getquestspirit("main_quest_19_total_domination"))];
                    break;
                default:
                    return;
            }

            newspirit = __result.requiredMonsters[0].monsterName;

            if (oldspirit.GetLocalizedString() == newspirit.GetLocalizedString()) { return; }

            LocalizedStringDatabase db = LocalizationSettings.Instance.GetStringDatabase();

            if (__result.description.GetLocalizedString().Contains(oldspirit.GetLocalizedString()))
            {
                db.GetTable(__result.description.TableReference).AddEntryFromReference(__result.description.TableEntryReference, __result.description.GetLocalizedString().Replace(oldspirit.GetLocalizedString(), newspirit.GetLocalizedString()));
            }
        }


        /// <summary>
        /// add checks for the Captain requireing relevant items before continuing the main quest
        /// </summary>
        [HarmonyPatch(typeof(Captain), "Interact")]
        [HarmonyPrefix]
        public static bool captainquests(Captain __instance, ref string ___currentSceneName)
        {
            QuestState activeMainQuestState = HelperItems.save.GetActiveMainQuestState();

            if (activeMainQuestState == null)
            {
                return true;
            }
            if (___currentSceneName == __instance.evergreenOutpostSceneName)
            {
                if (activeMainQuestState.Quest.id == "main_quest_13_bridge_crossing")
                {
                    InventoryItemState i = HelperItems.save.GetInventoryItemStateForItem(ItemManager.instance.GetItemAssetByName("KeyItem_PowerCrystal"));
                    if (i == null || i.count <= 0)
                    {
                        __instance.StartDialog("Captain_Arch_Quest13");
                        return false;
                    }
                }
                else if (QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_14_dusty_vale_awaits") && !ArchipelagoClient.archlist.hasitem(Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_key_item_start"]) + 10))
                {
                    __instance.StartDialog("Captain_Arch_Quest13");
                    return false;
                }
            }
            if (activeMainQuestState.Quest.id == "main_quest_28_how_the_dominoes_fall")
            {
                InventoryItemState i = HelperItems.save.GetInventoryItemStateForItem(ItemManager.instance.GetItemAssetByName("KeyItem_YellowHarmonyCrystal"));
                if (i == null || i.count <= 0)
                {
                    __instance.StartDialog("Captain_Arch_Quest28");
                    return false;
                }
            }

            if (___currentSceneName == __instance.tumbleweedTownSceneName && QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_30_welcome_to_paradise"))
            {
                if (ArchipelagoClient.archlist.hasitem(Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_archipelago_id_start"]) + 25) || Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"])) __instance.StartDialog("confirm_balloon_ride_dialog");
                else __instance.StartDialog("Captain_balloon_ride_unavaliable");
                return false;
            }
            if (___currentSceneName == __instance.coconutVillageTeampleSceneName && QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_37_the_frigid_maiden"))
            {
                if (ArchipelagoClient.archlist.hasitem(Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_archipelago_id_start"]) + 26) || Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"])) __instance.StartDialog("confirm_boat_ride_dialog");
                else __instance.StartDialog("Captain_boat_ride_unavaliable");
                return false;
            }
            if (___currentSceneName == __instance.trail18SceneName && QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_50_sanctuary_shakedown"))
            {
                if (ArchipelagoClient.archlist.hasitem(Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_archipelago_id_start"]) + 27) || Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"])) __instance.StartDialog("ask_portal_transition_dialog");
                else __instance.StartDialog("Captain_ancient_warp_unavaliable");
                return false;
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
                    if (i == null || i.count <= 0)
                    {
                        __instance.StartDialog("SergeantCassie_Arch_Quest5");
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
                        __instance.StartDialog("Sassy_Arch_Quest20");
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
                        __instance.StartDialog("MinerJohnson_Arch_Quest43");
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
                    InventoryItemState i = HelperItems.save.GetInventoryItemStateForItem(ItemManager.instance.GetItemAssetByName("KeyItem_Dynamite"));
                    if (i == null || i.count <= 0)
                    {
                        __instance.StartDialog("PaisleyBones_Arch_Quest46");
                        return false;
                    }
                }
            }
            return true;
        }

        //TODO FIX SPIRIT QUESTS
        //LocalizedString text; // found from somewhere in the game
        //
        //LocalizedStringDatabase db = LocalizationSettings.Instance.GetStringDatabase();
        //StringTable table = db.GetTable(text.TableReference);
        //table.AddEntryFromReference(text.TableEntryReference, "Replacement text");

        public static Dictionary<string, string> questdict = new Dictionary<string, string>{
            {"side_quest_perky_petunia","Petunia" },
            {"side_quest_slithering_menace","Serpentina" },
            {"side_quest_deadly_waters","Sharky" },
            {"side_quest_starry_eyed_surprise","Chocostar" },
            {"side_quest_arctic_menace","Polaria" },
            {"side_quest_hunt_for_the_centiboob_part1","Bunni" },
            {"side_quest_hunt_for_the_centiboob_part2","Hornie" },
            {"side_quest_hunt_for_the_centiboob_part3","Marinel" },
            };

        [HarmonyPatch(typeof(CollectSpiritQuestNPCGeneric), "Interact")]
        [HarmonyPrefix]
        public static void collectionsidequest1(CollectSpiritQuestNPCGeneric __instance)
        {
            if (__instance.sideQuestID == "side_quest_hunt_for_the_centiboob_part1" || __instance.sideQuestID == "side_quest_hunt_for_the_centiboob_part2" || __instance.sideQuestID == "side_quest_hunt_for_the_centiboob_part3") { return; }
            if (!questdict.ContainsKey(__instance.sideQuestID)) { return; }
            LocalizedString oldspirit = MonsterManager.instance.GetBaseStatsByName(questdict[__instance.sideQuestID]).monsterName;
            LocalizedString newspirit = MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.getquestspirit(__instance.sideQuestID)).monsterName;

            if (oldspirit == null) { return; }
            if (oldspirit.GetLocalizedString() == newspirit.GetLocalizedString()) { return; }

            LocalizedStringDatabase db = LocalizationSettings.Instance.GetStringDatabase();

            foreach (Dialog d in __instance.dialogs)
            {
                foreach (DialogLine l in d.GetLines())
                {
                    if (l.line.GetLocalizedString().Contains(oldspirit.GetLocalizedString()))
                    {
                        db.GetTable(l.line.TableReference).AddEntryFromReference(l.line.TableEntryReference, l.line.GetLocalizedString().Replace(oldspirit.GetLocalizedString(), newspirit.GetLocalizedString()));
                        //ArchipelagoConsole.LogDebug("CHANGING LINE");
                    }
                }
            }

        }

        [HarmonyPatch(typeof(DefeatOrCaptureSpiritsQuest_NPC_Generic), "Interact")]
        [HarmonyPrefix]
        public static void collectionsidequest2(DefeatOrCaptureSpiritsQuest_NPC_Generic __instance)
        {
            if (!questdict.ContainsKey(__instance.sideQuestID)) { return; }
            LocalizedString oldspirit = MonsterManager.instance.GetBaseStatsByName(questdict[__instance.sideQuestID]).monsterName;
            LocalizedString newspirit = MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.getquestspirit(__instance.sideQuestID)).monsterName;

            if (oldspirit == null) { return; }
            if (oldspirit.GetLocalizedString() == newspirit.GetLocalizedString()) { return; }

            LocalizedStringDatabase db = LocalizationSettings.Instance.GetStringDatabase();

            foreach (Dialog d in __instance.dialogs)
            {
                foreach (DialogLine l in d.GetLines())
                {
                    if (l.line.GetLocalizedString().Contains(oldspirit.GetLocalizedString()))
                    {
                        db.GetTable(l.line.TableReference).AddEntryFromReference(l.line.TableEntryReference, l.line.GetLocalizedString().Replace(oldspirit.GetLocalizedString(), newspirit.GetLocalizedString()));
                    }
                }
            }
        }

        [HarmonyPatch(typeof(CollectSpiritQuestMultipleNPCGeneric), "Start")]
        [HarmonyPrefix]
        public static void collectionsidequest3(CollectSpiritQuestMultipleNPCGeneric __instance)
        {
            foreach (var t in __instance.npcConfs)
            {
                LocalizedString oldspirit1 = MonsterManager.instance.GetBaseStatsByName(questdict["side_quest_hunt_for_the_centiboob_part1"]).monsterName;
                LocalizedString oldspirit2 = MonsterManager.instance.GetBaseStatsByName(questdict["side_quest_hunt_for_the_centiboob_part2"]).monsterName;
                LocalizedString oldspirit3 = MonsterManager.instance.GetBaseStatsByName(questdict["side_quest_hunt_for_the_centiboob_part3"]).monsterName;

                LocalizedStringDatabase db = LocalizationSettings.Instance.GetStringDatabase();

                foreach (Dialog d in t.npc.dialogs)
                {
                    foreach (DialogLine l in d.GetLines())
                    {
                        if (l.line.GetLocalizedString().Contains(oldspirit1.GetLocalizedString()))
                        {
                            db.GetTable(l.line.TableReference).AddEntryFromReference(l.line.TableEntryReference, l.line.GetLocalizedString().Replace(oldspirit1.GetLocalizedString(), "side_quest_hunt_for_the_centiboob_part1"));
                        }
                        if (l.line.GetLocalizedString().Contains(oldspirit2.GetLocalizedString()))
                        {
                            db.GetTable(l.line.TableReference).AddEntryFromReference(l.line.TableEntryReference, l.line.GetLocalizedString().Replace(oldspirit2.GetLocalizedString(), "side_quest_hunt_for_the_centiboob_part2"));
                        }
                        if (l.line.GetLocalizedString().Contains(oldspirit3.GetLocalizedString()))
                        {
                            db.GetTable(l.line.TableReference).AddEntryFromReference(l.line.TableEntryReference, l.line.GetLocalizedString().Replace(oldspirit3.GetLocalizedString(), "side_quest_hunt_for_the_centiboob_part3"));
                        }
                    }
                }
            }

            foreach (var t in __instance.npcConfs)
            {
                LocalizedString n1spirit = MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.getquestspirit("side_quest_hunt_for_the_centiboob_part1")).monsterName;
                LocalizedString n2spirit = MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.getquestspirit("side_quest_hunt_for_the_centiboob_part2")).monsterName;
                LocalizedString n3spirit = MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.getquestspirit("side_quest_hunt_for_the_centiboob_part3")).monsterName;

                LocalizedStringDatabase db = LocalizationSettings.Instance.GetStringDatabase();

                foreach (Dialog d in t.npc.dialogs)
                {
                    foreach (DialogLine l in d.GetLines())
                    {
                        if (l.line.GetLocalizedString().Contains("side_quest_hunt_for_the_centiboob_part1"))
                        {
                            db.GetTable(l.line.TableReference).AddEntryFromReference(l.line.TableEntryReference, l.line.GetLocalizedString().Replace("side_quest_hunt_for_the_centiboob_part1", n1spirit.GetLocalizedString()));
                        }
                        if (l.line.GetLocalizedString().Contains("side_quest_hunt_for_the_centiboob_part2"))
                        {
                            db.GetTable(l.line.TableReference).AddEntryFromReference(l.line.TableEntryReference, l.line.GetLocalizedString().Replace("side_quest_hunt_for_the_centiboob_part2", n2spirit.GetLocalizedString()));
                        }
                        if (l.line.GetLocalizedString().Contains("side_quest_hunt_for_the_centiboob_part3"))
                        {
                            db.GetTable(l.line.TableReference).AddEntryFromReference(l.line.TableEntryReference, l.line.GetLocalizedString().Replace("side_quest_hunt_for_the_centiboob_part3", n3spirit.GetLocalizedString()));
                        }
                    }
                }
            }
        }


        [HarmonyPatch(typeof(Skipper), "Interact")]
        [HarmonyPrefix]
        public static void collectionmainsidequest1(Skipper __instance)
        {
            LocalizedString oldspirit = MonsterManager.instance.GetBaseStatsByName("Sharky").monsterName;
            LocalizedString newspirit = MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.getquestspirit("side_quest_deadly_waters")).monsterName;

            if (oldspirit == null) { return; }
            if (oldspirit.GetLocalizedString() == newspirit.GetLocalizedString()) { return; }

            LocalizedStringDatabase db = LocalizationSettings.Instance.GetStringDatabase();

            foreach (Dialog d in __instance.dialogs)
            {
                foreach (DialogLine l in d.GetLines())
                {
                    if (l.line.GetLocalizedString().Contains(oldspirit.GetLocalizedString()))
                    {
                        db.GetTable(l.line.TableReference).AddEntryFromReference(l.line.TableEntryReference, l.line.GetLocalizedString().Replace(oldspirit.GetLocalizedString(), newspirit.GetLocalizedString()));
                    }
                }
            }
        }


        [HarmonyPatch(typeof(OldMaster), "Interact")]
        [HarmonyPrefix]
        public static void collectionmainquest(OldMaster __instance)
        {
            LocalizedString oldspirit = MonsterManager.instance.GetBaseStatsByName("Domina").monsterName;
            LocalizedString newspirit = MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.getquestspirit("main_quest_19_total_domination")).monsterName;
            //ArchipelagoConsole.LogDebug($"old: {oldspirit.GetLocalizedString()}, NEW: {newspirit.GetLocalizedString()}");

            if (oldspirit == null) { return; }
            if (oldspirit.GetLocalizedString() == newspirit.GetLocalizedString()) { return; }

            LocalizedStringDatabase db = LocalizationSettings.Instance.GetStringDatabase();

            foreach (Dialog d in __instance.dialogs)
            {
                foreach (DialogLine l in d.GetLines())
                {
                    if (l.line.GetLocalizedString().Contains(oldspirit.GetLocalizedString()))
                    {
                        db.GetTable(l.line.TableReference).AddEntryFromReference(l.line.TableEntryReference, l.line.GetLocalizedString().Replace(oldspirit.GetLocalizedString(), newspirit.GetLocalizedString()));
                        //ArchipelagoConsole.LogDebug("CHANGING LINE");
                    }
                }
            }
        }



        [HarmonyPatch(typeof(DoctorDolly_Hq), "OnDialogExited")]
        [HarmonyPrefix]
        public static bool evquestovverwite(DoctorDolly_Hq __instance, ref Dialog ___activeDialog, SystemData<GameState> ___gameState, Hero ___hero)
        {
            if (___activeDialog.id == "give_quest_simulated_scuffle")
            {
                if (___gameState.data.StartSideQuest("side_quest_simulated_scuffle"))
                {
                    GlobalHUD.instance.EnqueueToast(Utils.GetLocalizedStringObject("New quest started: {questTitle}", new Dictionary<string, string> {
                {
                    "questTitle",
                    QuestManager.instance.GetSideQuestById("side_quest_simulated_scuffle").title.GetLocalizedString()
                } }));
                }
            }
            else if (___activeDialog.id == "close_quest_simulated_scuffle")
            {
                //base.CloseSideQuestAndAutograntQuestRewards("side_quest_simulated_scuffle", true);
                ___gameState.data.CloseSideQuest("side_quest_simulated_scuffle", true);

                //MonsterState monsterState = __instance.simulatedScuffleSpiritReward.CreateDefaultMonsterState();
                MonsterState monsterState = new MonsterTeamMemberBlueprint()
                {
                    monster = MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.namehelper2(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_SIMULATED_SCUFFLE"].ToString())),

                    level = 5,
                    isRare = false,
                    isActiveSkillCountUnlimited = false
                }.CreateDefaultMonsterState();

                __instance.captureMenu.SetMonsterState(monsterState);
                __instance.captureMenu.gameObject.SetActive(true);
                AudioManager.instance.PlaySfx(___hero.addItemsSound);
            }
            else if (___activeDialog.id == "give_side_quest_gold_plated")
            {
                if (___gameState.data.StartSideQuest("side_quest_gold_plated"))
                {
                    GlobalHUD.instance.EnqueueToast(Utils.GetLocalizedStringObject("New quest started: {questTitle}", new Dictionary<string, string> {
                {
                    "questTitle",
                    QuestManager.instance.GetSideQuestById("side_quest_gold_plated").title.GetLocalizedString()
                } }));
                }
            }
            else if (___activeDialog.id == "side_quest_gold_plated_active_completed_accepted_part2")
            {
                ___gameState.data.ModifyMoney(-3000);

                //base.CloseSideQuestAndAutograntQuestRewards("side_quest_gold_plated", true);
                ___gameState.data.CloseSideQuest("side_quest_gold_plated", true);

                //MonsterState monsterState2 = __instance.goldPlatedSpiritReward.CreateDefaultMonsterState();
                MonsterState monsterState2 = new MonsterTeamMemberBlueprint()
                {
                    monster = MonsterManager.instance.GetBaseStatsByName(ArchipelagoData.namehelper2(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_GOLD_PLATED"].ToString())),

                    level = 5,
                    isRare = true,
                    isActiveSkillCountUnlimited = false
                }.CreateDefaultMonsterState();

                __instance.captureMenu.SetMonsterState(monsterState2);
                __instance.captureMenu.gameObject.SetActive(true);
                AudioManager.instance.PlaySfx(___hero.addItemsSound);
            }
            //base.OnDialogExited();
            if (___activeDialog.autoSetHeroInputEnabledDialogExit)
            {
                ___hero.SetInputEnabled(true);
            }
            ___activeDialog = null;

            return false;
        }

        [HarmonyPatch(typeof(LightBridge), "Start")]
        [HarmonyPrefix]
        public static bool lightbridge(LightBridge __instance)
        {
            if (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["goal"]) != 0)
            {
                if (ArchipelagoClient.archlist.hasitem(Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_key_item_start"]) + 10)) return true;
                return false;
            }
            return true;
        }

        [HarmonyPatch(typeof(BoundToMainQuest), "Start")]
        [HarmonyPrefix]
        public static bool iceblock(BoundToMainQuest __instance)
        {
            if (__instance.name != "IceBlock") return true;
            if (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["goal"]) != 0)
            {
                if (ArchipelagoClient.archlist.hasitem(Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_key_item_start"]) + 6)) return true;
                return false;
            }
            return true;
        }

        [HarmonyPatch(typeof(FrienlyFightNPCGeneric), "Interact")]
        [HarmonyPrefix]
        public static bool fightquest(FrienlyFightNPCGeneric __instance, ref bool ___questWasStartedDuringThisInteraction)
        {
            //Oakwood Village: Defeat Robbie 
            //Trail 11: Defeat Alice 

            ___questWasStartedDuringThisInteraction = false;
            bool flag = true;
            if (!string.IsNullOrEmpty(__instance.activeWhenMainQuestIsGreatedThanID))
            {
                flag = QuestManager.instance.GetIsActiveMainQuestGreaterThan(__instance.activeWhenMainQuestIsGreatedThanID);
            }
            if (flag)
            {
                QuestState sideQuestStateById = HelperItems.save.GetSideQuestStateById(__instance.sideQuestID);
                if (sideQuestStateById == null)
                {
                    __instance.StartDialog("start_quest_dialog");
                    return false;
                }

                if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Side_Missions"]))
                {
                    int questidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                    switch (__instance.sideQuestID)
                    {
                        case "side_quest_sparring_match":
                            if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(questidstart + 1))
                            {
                                __instance.StartDialog("start_fight_dialog");
                                return false;
                            }
                            else
                            {
                                __instance.StartDialog("exhausted_dialog");
                                return false;
                            }
                        case "side_quest_fishmasters_challenge":
                            if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(questidstart + 56))
                            {
                                __instance.StartDialog("start_fight_dialog");
                                return false;
                            }
                            else
                            {
                                __instance.StartDialog("exhausted_dialog");
                                return false;
                            }
                        default:
                            ArchipelagoConsole.LogError($"FrienlyFightNPCGeneric ERROR SIDE QUEST NOT ACCOUNTED FOR {__instance.sideQuestID}");
                            break;
                    }
                }


                if (!sideQuestStateById.isClosed)
                {
                    __instance.StartDialog("start_fight_dialog");
                    return false;
                }
                if (sideQuestStateById.isClosed)
                {
                    __instance.StartDialog("exhausted_dialog");
                    return false;
                }
            }
            else
            {
                __instance.StartDialog("inactive_dialog");
            }
            return false;
        }


        [HarmonyPatch(typeof(BonnieBaiter), "Interact")]
        [HarmonyPrefix]
        public static bool fightquest(BonnieBaiter __instance, SystemData<GameState> ___gameState)
        {
            QuestState sideQuestStateById = ___gameState.data.GetSideQuestStateById("side_quest_fishy_duel");
            if (sideQuestStateById == null)
            {
                __instance.StartDialog("give_side_quest_fishy_duel");
                return false;
            }
            if (!sideQuestStateById.isClosed)
            {

                __instance.StartDialog("confirm_fight_dialog");
                return false;
            }
            if (sideQuestStateById.isClosed)
            {

                if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Side_Missions"]))
                {
                    int questidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);

                    if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(questidstart + 61))
                    {
                        __instance.StartDialog("confirm_fight_dialog");
                        return false;
                    }
                }


                QuestState sideQuestStateById2 = ___gameState.data.GetSideQuestStateById("side_quest_the_art_of_fishing");
                if (sideQuestStateById2 != null)
                {
                    if (sideQuestStateById2.isClosed)
                    {

                        __instance.StartDialog("idle_dialog");
                        return false;
                    }
                    if (sideQuestStateById2.GetIsCompleted())
                    {

                        __instance.StartDialog("side_quest_the_art_of_fishing_active_completed_dialog");
                        return false;
                    }

                    __instance.StartDialog("side_quest_the_art_of_fishing_active_not_completed_dialog");
                }
            }

            return false;
        }

        [HarmonyPatch(typeof(MotherEvilyn), "Interact")]
        [HarmonyPrefix]
        public static bool fightquest2(MotherEvilyn __instance, SystemData<GameState> ___gameState)
        {

            QuestState activeMainQuestState = ___gameState.data.GetActiveMainQuestState();
            if (QuestManager.instance.GetIsActiveMainQuestLessThan("main_quest_42_the_lewd_exorcist"))
            {
                __instance.StartDialog("idle_dialog");
                return false;
            }
            if (activeMainQuestState.Quest.id == "main_quest_42_the_lewd_exorcist")
            {
                __instance.StartDialog("start_minigame_dialog");
                return false;
            }

            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"]))
            {
                int questidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);

                if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(questidstart + 73))
                {
                    __instance.StartDialog("start_fight_dialog");
                    return false;
                }
            }

            __instance.StartDialog("idle_exhausted_dialog");

            return false;
        }

        [HarmonyPatch(typeof(AncientTemple3Sequence), "GetShouldPlay")]
        [HarmonyPrefix]
        public static bool fightquest2(AncientTemple3Sequence __instance, ref bool __result)
        {
            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"]))
            {
                int questidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(questidstart + 20))
                {
                    __result = true;
                    return false;
                }
            }
            return true;
        }

        [HarmonyPatch(typeof(ArcticTemple2sequence), "GetShouldPlay")]
        [HarmonyPrefix]
        public static bool fightquest2(ArcticTemple2sequence __instance, ref bool __result)
        {
            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"]))
            {
                int questidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(questidstart + 89))
                {
                    __result = true;
                    return false;
                }
            }
            return true;
        }

        [HarmonyPatch(typeof(DesertTemple2Sequence), "GetShouldPlay")]
        [HarmonyPrefix]
        public static bool fightquest2(DesertTemple2Sequence __instance, ref bool __result)
        {
            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"]))
            {
                int questidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(questidstart + 51))
                {
                    __result = true;
                    return false;
                }
            }
            return true;
        }

        [HarmonyPatch(typeof(IslandCave2Sequence), "GetShouldPlay")]
        [HarmonyPrefix]
        public static bool fightquest2(IslandCave2Sequence __instance, ref bool __result)
        {
            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"]))
            {
                int questidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(questidstart + 70))
                {
                    __result = true;
                    return false;
                }
            }
            return true;
        }

        [HarmonyPatch(typeof(InnerGroveSequence), "GetShouldPlay")]
        [HarmonyPrefix]
        public static bool fightquest2(InnerGroveSequence __instance, ref bool __result)
        {
            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Main_Missions"]))
            {
                int questidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(questidstart + 107))
                {
                    __result = true;
                    return false;
                }
            }
            return true;
        }
    }
}

















