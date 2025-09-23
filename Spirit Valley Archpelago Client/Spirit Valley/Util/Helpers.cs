using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using UnityEngine.SceneManagement;
using static System.Collections.Specialized.BitVector32;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Util
{
    public class Spirit()
    {
        public string name;
        public Dictionary<string, int> moves;
        public Dictionary<string, int> evolution;
        public string type;
        public Dictionary<string, int> stats;
    }

    public class Trainer()
    {
        public string NAME;
        public List<trainerspirit> PARTY;
        public string GUID;
    }

    public class trainerspirit()
    {
        public string spirit;
        public int lv;
        public int shiny;
    }

    public class HelperItems()
    {
        public static GameState save => GameManager.instance.gameStates[4].data;

        public static ItemBundle[] centbundle()
        {
            ItemBundle r = new ItemBundle();
            r.item = ItemManager.instance.moneyItem;
            r.count = 1;
            r.isCountInfinite = false;
            r.randomizeCount = false;
            return [r];
        }

        public static ItemBundle[] voidbundle()
        {
            return new List<ItemBundle>().ToArray();
        }

        public static ItemBundle genbundle(Item i, bool inf, int amount = 1)
        {
            ItemBundle r = new ItemBundle();
            r.item = i;
            if (inf)
            {
                r.count = -1;
                r.isCountInfinite = true;
            }
            else
            {
                r.count = amount;
                r.isCountInfinite = false;
            }
            r.randomizeCount = false;
            return r;
        }
    }

    public class HelperSpirits()
    {
        public static Dictionary<string, MonsterSkill> skilllist = new Dictionary<string, MonsterSkill>();

        public static void genskilllist()
        {
            MonsterManager man = MonsterManager.instance;
            foreach (MonsterBaseStats mon in man.monstersBaseStats)
            {
                foreach (SkillConfiguration s in mon.skills)
                {
                    if (!skilllist.ContainsKey(s.skill.name))
                    {
                        skilllist.Add(s.skill.name, s.skill);
                    }
                }
            }
        }

    }

    public class save()
    {
        public static GameState s => GameManager.instance.gameStates[4].data;


        public static QuestState getmain(string q)
        {
            QuestState questState3 = new QuestState(QuestManager.instance.GetMainQuestById(q), QuestState.Type.MainQuest);
            questState3.isClosed = true;
            return questState3;
        }

        public static bool fixsave()
        {
            int sidequeststart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Side_Quest_Start"]);
            int mainqueststart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Main_Quest_Start"]);
            bool warprando = Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["randomise_warps"]);

            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 1))
            {
                if (s.GetSideQuestStateById("side_quest_sparring_match") == null) { s.StartSideQuest("side_quest_sparring_match"); }
                s.GetSideQuestStateById("side_quest_sparring_match").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 2))
            {
                if (s.GetSideQuestStateById("side_quest_larrys_treasure") == null) { s.StartSideQuest("side_quest_larrys_treasure"); }
                s.GetSideQuestStateById("side_quest_larrys_treasure").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 3))
            {
                if (s.GetSideQuestStateById("side_quest_perky_petunia") == null) { s.StartSideQuest("side_quest_perky_petunia"); }
                s.GetSideQuestStateById("side_quest_perky_petunia").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 4))
            {
                if (s.GetSideQuestStateById("side_quest_pleasuring_pusseen") == null) { s.StartSideQuest("side_quest_pleasuring_pusseen"); }
                s.GetSideQuestStateById("side_quest_pleasuring_pusseen").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 5))
            {
                if (s.GetSideQuestStateById("side_quest_slithering_menace") == null) { s.StartSideQuest("side_quest_slithering_menace"); }
                s.GetSideQuestStateById("side_quest_slithering_menace").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 6))
            {
                if (s.GetSideQuestStateById("side_quest_cattle_thieves") == null) { s.StartSideQuest("side_quest_cattle_thieves"); }
                s.GetSideQuestStateById("side_quest_cattle_thieves").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 7))
            {
                if (s.GetSideQuestStateById("side_quest_professional_pleasurer") == null) { s.StartSideQuest("side_quest_professional_pleasurer"); }
                s.GetSideQuestStateById("side_quest_professional_pleasurer").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 8))
            {
                if (s.GetSideQuestStateById("side_quest_fishy_duel") == null) { s.StartSideQuest("side_quest_fishy_duel"); }
                s.GetSideQuestStateById("side_quest_fishy_duel").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 9))
            {
                if (s.GetSideQuestStateById("side_quest_the_art_of_fishing") == null) { s.StartSideQuest("side_quest_the_art_of_fishing"); }
                s.GetSideQuestStateById("side_quest_the_art_of_fishing").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 10))
            {
                if (s.GetSideQuestStateById("side_quest_fishmasters_challenge") == null) { s.StartSideQuest("side_quest_fishmasters_challenge"); }
                s.GetSideQuestStateById("side_quest_fishmasters_challenge").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 11))
            {
                if (s.GetSideQuestStateById("side_quest_deadly_waters") == null) { s.StartSideQuest("side_quest_deadly_waters"); }
                s.GetSideQuestStateById("side_quest_deadly_waters").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 12))
            {
                if (s.GetSideQuestStateById("side_quest_starry_eyed_surprise") == null) { s.StartSideQuest("side_quest_starry_eyed_surprise"); }
                s.GetSideQuestStateById("side_quest_starry_eyed_surprise").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 13))
            {
                if (s.GetSideQuestStateById("side_quest_arctic_menace") == null) { s.StartSideQuest("side_quest_arctic_menace"); }
                s.GetSideQuestStateById("side_quest_arctic_menace").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 14))
            {
                if (s.GetSideQuestStateById("side_quest_legend_of_valkyrie_part1") == null) { s.StartSideQuest("side_quest_legend_of_valkyrie_part1"); }
                s.GetSideQuestStateById("side_quest_legend_of_valkyrie_part1").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 15))
            {
                if (s.GetSideQuestStateById("side_quest_legend_of_valkyrie_part2") == null) { s.StartSideQuest("side_quest_legend_of_valkyrie_part2"); }
                s.GetSideQuestStateById("side_quest_legend_of_valkyrie_part2").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 16))
            {
                if (s.GetSideQuestStateById("side_quest_hunt_for_the_centiboob_part1") == null) { s.StartSideQuest("side_quest_hunt_for_the_centiboob_part1"); }
                s.GetSideQuestStateById("side_quest_hunt_for_the_centiboob_part1").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 17))
            {
                if (s.GetSideQuestStateById("side_quest_hunt_for_the_centiboob_part2") == null) { s.StartSideQuest("side_quest_hunt_for_the_centiboob_part2"); }
                s.GetSideQuestStateById("side_quest_hunt_for_the_centiboob_part2").isClosed = true;
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(sidequeststart + 18))
            {
                if (s.GetSideQuestStateById("side_quest_hunt_for_the_centiboob_part3") == null) { s.StartSideQuest("side_quest_hunt_for_the_centiboob_part3"); }
                s.GetSideQuestStateById("side_quest_hunt_for_the_centiboob_part3").isClosed = true;
            }

            s.mainQuestStates.Clear();
            int tel = 0;
            int i = 0;
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 1)) { s.mainQuestStates.Add(getmain("main_quest_1_doctors_appointment")); }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 2)) { s.mainQuestStates.Add(getmain("main_quest_2_captain_maria")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 3)) { s.mainQuestStates.Add(getmain("main_quest_3_first_orders")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 4)) { s.mainQuestStates.Add(getmain("main_quest_4_crimson_agent")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 5)) { s.mainQuestStates.Add(getmain("main_quest_5_super_secret_orders")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 6)) { s.mainQuestStates.Add(getmain("main_quest_6_first_mission_success")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 7)) { s.mainQuestStates.Add(getmain("main_quest_7_onward_to_greensvale")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 8)) { s.mainQuestStates.Add(getmain("main_quest_8_temple_investigation")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 9)) { s.mainQuestStates.Add(getmain("main_quest_9_harmonius_disturbance")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 10)) { s.mainQuestStates.Add(getmain("main_quest_10_consulting_dolly")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 11)) { s.mainQuestStates.Add(getmain("main_quest_11_becky_can_fix_it")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 12)) { s.mainQuestStates.Add(getmain("main_quest_12_hunt_for_the_chunk")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 13)) { s.mainQuestStates.Add(getmain("main_quest_13_bridge_crossing")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 14)) { s.mainQuestStates.Add(getmain("main_quest_14_dusty_vale_awaits")); tel = 1; i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 15)) { s.mainQuestStates.Add(getmain("main_quest_15_an_audience_with_the_king")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 16)) { s.mainQuestStates.Add(getmain("main_quest_16_the_grand_cuckold_challenge")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 17)) { s.mainQuestStates.Add(getmain("main_quest_17_license_to_battle")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 18)) { s.mainQuestStates.Add(getmain("main_quest_18_box_pusher")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 19)) { s.mainQuestStates.Add(getmain("main_quest_19_total_domination")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 20)) { s.mainQuestStates.Add(getmain("main_quest_20_a_challenge_awaits")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 21)) { s.mainQuestStates.Add(getmain("main_quest_21_a_new_challenger")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 22)) { s.mainQuestStates.Add(getmain("main_quest_22_stiff_competition")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 23)) { s.mainQuestStates.Add(getmain("main_quest_23_final_fight")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 24)) { s.mainQuestStates.Add(getmain("main_quest_24_return_of_the_champion")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 25)) { s.mainQuestStates.Add(getmain("main_quest_25_breeding_season")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 26)) { s.mainQuestStates.Add(getmain("main_quest_26_mission_success")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 27)) { s.mainQuestStates.Add(getmain("main_quest_27_quest_for_the_crystal")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 28)) { s.mainQuestStates.Add(getmain("main_quest_28_how_the_dominoes_fall")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 29)) { s.mainQuestStates.Add(getmain("main_quest_29_big_balloon_adventure")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 30)) { s.mainQuestStates.Add(getmain("main_quest_30_welcome_to_paradise")); tel = 2; i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 31)) { s.mainQuestStates.Add(getmain("main_quest_31_coconut_conundrum")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 32)) { s.mainQuestStates.Add(getmain("main_quest_32_lusty_cultists")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 33)) { s.mainQuestStates.Add(getmain("main_quest_33_savior_of_coconut_village")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 34)) { s.mainQuestStates.Add(getmain("main_quest_34_slippery_when_wet")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 35)) { s.mainQuestStates.Add(getmain("main_quest_35_glimmering_price")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 36)) { s.mainQuestStates.Add(getmain("main_quest_36_arctic_adventure")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 37)) { s.mainQuestStates.Add(getmain("main_quest_37_the_frigid_maiden")); tel = 3; i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 38)) { s.mainQuestStates.Add(getmain("main_quest_38_arctic_isles")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 39)) { s.mainQuestStates.Add(getmain("main_quest_39_paisley_bones")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 40)) { s.mainQuestStates.Add(getmain("main_quest_40_demand_for_dynamite")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 41)) { s.mainQuestStates.Add(getmain("main_quest_41_stealing_from_a_dead_man")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 42)) { s.mainQuestStates.Add(getmain("main_quest_42_the_lewd_exorcist")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 43)) { s.mainQuestStates.Add(getmain("main_quest_43_suit_in_hand")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 44)) { s.mainQuestStates.Add(getmain("main_quest_44_fishing_for_treasure")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 45)) { s.mainQuestStates.Add(getmain("main_quest_45_the_proposal")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 46)) { s.mainQuestStates.Add(getmain("main_quest_46_here_comes_the_boom")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 47)) { s.mainQuestStates.Add(getmain("main_quest_47_arctic_harmony")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 48)) { s.mainQuestStates.Add(getmain("main_quest_48_crimson_chase")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 49)) { s.mainQuestStates.Add(getmain("main_quest_49_through_the_portal")); tel = 4; i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 50)) { s.mainQuestStates.Add(getmain("main_quest_50_sanctuary_shakedown")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 51)) { s.mainQuestStates.Add(getmain("main_quest_51_hostage_situation")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 52)) { s.mainQuestStates.Add(getmain("main_quest_52_breezie_runs_free")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 53)) { s.mainQuestStates.Add(getmain("main_quest_53_desperate_dash")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 54)) { s.mainQuestStates.Add(getmain("main_quest_54_battle_for_spirit_valley")); i++;}
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(mainqueststart + 55)) { s.mainQuestStates.Add(getmain("main_quest_55_life_as_a_spirit_warden")); i++; }

            s.AdvanceMainQuest(QuestManager.instance.mainQuest[i].id);

            if (i > 1){ s.GetWayStoneState("OakwoodVillage").isActive = true; }
            if (i > 6){ s.GetWayStoneState("Greensvale").isActive = true; }
            if (i > 8){ s.GetWayStoneState("Trail4").isActive = true; }
            if (i > 13){ s.GetWayStoneState("DairyFarm").isActive = true; }
            if (i > 13){ s.GetWayStoneState("TumbleweedTown").isActive = true; }
            if (i > 28){ s.GetWayStoneState("CrashSite").isActive = true; }
            if (i > 29){ s.GetWayStoneState("CoconutVillage").isActive = true; }
            if (i > 32){ s.GetWayStoneState("Trail14").isActive = true; }
            if (i > 35){ s.GetWayStoneState("ColdHarbor").isActive = true; }
            if (i > 38){ s.GetWayStoneState("Frostville1").isActive = true; }
            if (i > 39){ s.GetWayStoneState("AbandonedMine").isActive = true; }
            if (i > 47){ s.GetWayStoneState("Trail18").isActive = true; }
            if (i > 48){ s.GetWayStoneState("Trail19").isActive = true; }
            if (i > 54){ s.GetWayStoneState("Trail22").isActive = true; }


            if (SceneManager.GetActiveScene().name == "TitleScreen")
            {
                switch (tel)
                {
                    case 0:
                        s.currentSceneName = "OakwoodVillage";
                        break;
                    case 1:
                        s.currentSceneName = "TumbleweedTown";
                        break;
                    case 2:
                        s.currentSceneName = "CrashSite";
                        break;
                    case 3:
                        s.currentSceneName = "ColdHarbor";
                        break;
                    case 4:
                        s.currentSceneName = "Trail18";
                        break;
                    default:
                        s.currentSceneName = "OakwoodVillage";
                        break;
                }

                var t = GameManager.instance.gameStates[4].SaveAsync(SaveType.Auto);
                t.Wait();
            }
            else
            {
                switch (tel)
                {
                    case 0:
                        HelperItems.save.transitionSceneName = "OakwoodVillage";
                        HelperItems.save.transitionAreaID = "waystone";
                        SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                        {
                            SceneManager.LoadScene("OakwoodVillage", LoadSceneMode.Single);
                        });
                        break;
                    case 1:
                        HelperItems.save.transitionSceneName = "TumbleweedTown";
                        HelperItems.save.transitionAreaID = "waystone";
                        SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                        {
                            SceneManager.LoadScene("TumbleweedTown", LoadSceneMode.Single);
                        });
                        break;
                    case 2:
                        HelperItems.save.transitionSceneName = "CrashSite";
                        HelperItems.save.transitionAreaID = "waystone";
                        SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                        {
                            SceneManager.LoadScene("CrashSite", LoadSceneMode.Single);
                        });
                        break;
                    case 3:
                        HelperItems.save.transitionSceneName = "ColdHarbor";
                        HelperItems.save.transitionAreaID = "waystone";
                        SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                        {
                            SceneManager.LoadScene("ColdHarbor", LoadSceneMode.Single);
                        });
                        break;
                    case 4:
                        HelperItems.save.transitionSceneName = "Trail18";
                        HelperItems.save.transitionAreaID = "waystone";
                        SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                        {
                            SceneManager.LoadScene("Trail18", LoadSceneMode.Single);
                        });
                        break;

                    default:
                        HelperItems.save.transitionSceneName = "OakwoodVillage";
                        HelperItems.save.transitionAreaID = "waystone";
                        SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                        {
                            SceneManager.LoadScene("OakwoodVillage", LoadSceneMode.Single);
                        });
                        break;
                }
            }

            return true;
        }
    }
}
