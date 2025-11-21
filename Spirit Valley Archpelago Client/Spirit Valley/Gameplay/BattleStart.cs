using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{

    [HarmonyPatch]
    public class BattleStart
    {

        /// <summary>
        /// allow for trainers to be rematched
        /// </summary>
        [HarmonyPatch(typeof(EnemyMapItem), "Interact")]
        [HarmonyPostfix]
        public static void allowmutiplefights(EnemyMapItem __instance, ref EnemyMapItemState ___state, SystemData<GameState> ___gameState)
        {
            if (___state.state == EnemyMapItemState.State.Idle)
            {
                ArchipelagoConsole.LogMessage($"Rematching Trainer");

                ___state.state = EnemyMapItemState.State.Fighting;
                ___gameState.data.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam(__instance.guid)), ArchipelagoClient.ServerData.trainerteam(__instance.guid).Length == 1, false, false, false, __instance.aILevel, false, MapManager.instance.biome, __instance.dialogName, null);
                SceneTransitionManager.instance.StartRandomTransition(delegate
                {
                    SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                    SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
                });
            }
        }


        /// <summary>
        /// set an enemy team based on its GUID
        /// </summary>
        [HarmonyPatch(typeof(EnemyMapItem), "StartFight")]
        [HarmonyPrefix]
        public static bool EnemyMapItembattle(EnemyMapItem __instance, EnemyMapItemState ___state, SystemData<GameState> ___gameState)
        {
            ArchipelagoConsole.LogDebug($"STARTING FIGHT FROM ENEMYMAPITEM:{___state.guid}");

            ___state.state = EnemyMapItemState.State.Fighting;
            ___gameState.data.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam(__instance.guid)), ArchipelagoClient.ServerData.trainerteam(__instance.guid).Length == 1, false, false, false, __instance.aILevel, false, MapManager.instance.biome, __instance.dialogName, null);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }



        /// <summary>
        /// set frendly fight/side quest team based on its GUID
        /// </summary>
        [HarmonyPatch(typeof(FrienlyFightNPCGeneric), "StartFight")]
        [HarmonyPrefix]
        public static bool frendlyfightstart(FrienlyFightNPCGeneric __instance, SystemData<GameState> ___gameState)
        {
            ArchipelagoConsole.LogDebug("STARTING FRENDLY FIGHT:");
            ArchipelagoConsole.LogDebug($"SIDE QUEST ID:{__instance.sideQuestID}");
            ArchipelagoConsole.LogDebug($"GUID:{__instance.fightInitiatorID}");

            switch (__instance.fightInitiatorID)
            {
                case "61822611-267a-4366-b99c-fadc5a23ad01"://Oakwood Village: Defeat Robbie
                    ArchipelagoConsole.LogDebug("Robbie");
                    break;
                case "ceba2e6b-5cd3-40ae-8696-f9ef461c7b14"://Trail 11: Defeat Alice
                    ArchipelagoConsole.LogDebug("Alice");
                    break;
                default:
                    ArchipelagoConsole.LogMessage("ERROR BATTLESTART.cs/FRENDLYFIGHTSTART GUID NOT KNOWN");
                    break;
            }

            ___gameState.data.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam(__instance.fightInitiatorID)), ArchipelagoClient.ServerData.trainerteam(__instance.fightInitiatorID).Length == 1, false, false, false, __instance.aILevel, false, MapManager.instance.biome, __instance.dialogName, __instance.fightInitiatorID);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }


        /// <summary>
        /// set the enemy team for Bonie Baiter fight
        /// </summary>
        [HarmonyPatch(typeof(BonnieBaiter), "StartFight")]
        [HarmonyPrefix]
        public static bool boniefight(BonnieBaiter __instance, SystemData<GameState> ___gameState)
        {
            ArchipelagoConsole.LogDebug("Bonnie Baiter");

            ___gameState.data.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam(__instance.fightInitiatorID)), ArchipelagoClient.ServerData.trainerteam(__instance.fightInitiatorID).Length == 1, false, false, false, __instance.aILevel, false, MapManager.instance.biome, __instance.dialogName, __instance.fightInitiatorID);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;

        }

        /// <summary>
        /// set the enemy team for Crimson Agent fight on Trail 2
        /// </summary>
        [HarmonyPatch(typeof(CrimsonAgent1), "StartFight")]
        [HarmonyPrefix]
        public static bool crimsonagentfight(SystemData<GameState> ___gameState, CrimsonAgent1 __instance)
        {
            ArchipelagoConsole.LogDebug("CrimsonAgent1");

            if (__instance.fightInitiatorID == "0ea61b92-8dcd-4adf-a070-4bc5870b2698")
            {
                ___gameState.data.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam("0ea61b92-8dcd-4adf-a070-4bc5870b2698")), ArchipelagoClient.ServerData.trainerteam("0ea61b92-8dcd-4adf-a070-4bc5870b2698").Length == 1, false, false, false, __instance.aILevel, false, MapManager.instance.biome, __instance.dialogName, __instance.fightInitiatorID);
            }
            else
            {
                ___gameState.data.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam("Trail 02: Crimson Agent")), ArchipelagoClient.ServerData.trainerteam("Trail 02: Crimson Agent").Length == 1, false, false, false, __instance.aILevel, false, MapManager.instance.biome, __instance.dialogName, __instance.fightInitiatorID);
            }
            SceneTransitionManager.instance.StartRandomTransition(delegate
                {
                    SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                    SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
                });
            return false;
        }

        /// <summary>
        /// set the enemy team for fights started through sassy
        /// </summary>
        [HarmonyPatch(typeof(Sassy), "StartFight")]
        [HarmonyPrefix]
        public static bool sassyfights(Sassy __instance)
        {
            ArchipelagoConsole.LogDebug("Sassy");
            if (GameManager.instance.GetActiveGameState().data.GetActiveMainQuestState().Quest.id == "main_quest_21_a_new_challenger")
            {
                //case "Willy Wanker"://Tumbleweed Town: Defeat Willy Wanker
                ArchipelagoConsole.LogDebug("Tumbleweed Town: Defeat Willy Wanker");

                HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam("Tumbleweed Town: Willy Wanker")), ArchipelagoClient.ServerData.trainerteam("Tumbleweed Town: Willy Wanker").Length == 1, false, false, false, __instance.fighConfigs[0].aILevel, false, MapManager.instance.biome, __instance.fighConfigs[0].opponentName, __instance.fightInitiatorID);
                SceneTransitionManager.instance.StartRandomTransition(delegate
                {
                    SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                    SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
                });
                return false;
            }
            if (GameManager.instance.GetActiveGameState().data.GetActiveMainQuestState().Quest.id == "main_quest_22_stiff_competition")
            {
                // case "Dick Cummings"://Tumbleweed Town: Defeat Dick Cummings
                ArchipelagoConsole.LogDebug("Tumbleweed Town: Defeat Dick Cummings");

                HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam("Tumbleweed Town: Dick Cummings")), ArchipelagoClient.ServerData.trainerteam("Tumbleweed Town: Dick Cummings").Length == 1, false, false, false, __instance.fighConfigs[1].aILevel, false, MapManager.instance.biome, __instance.fighConfigs[1].opponentName, __instance.fightInitiatorID);
                SceneTransitionManager.instance.StartRandomTransition(delegate
                {
                    SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                    SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
                });
                return false;
            }
            if (GameManager.instance.GetActiveGameState().data.GetActiveMainQuestState().Quest.id == "main_quest_23_final_fight")
            {
                //case "Dick Louie"://Tumbleweed Town: Defeat Dick Louie
                ArchipelagoConsole.LogDebug("Tumbleweed Town: Defeat Dick Louie");

                HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam("Tumbleweed Town: Dick Louie")), ArchipelagoClient.ServerData.trainerteam("Tumbleweed Town: Dick Louie").Length == 1, false, false, false, __instance.fighConfigs[2].aILevel, false, MapManager.instance.biome, __instance.fighConfigs[2].opponentName, __instance.fightInitiatorID);
                SceneTransitionManager.instance.StartRandomTransition(delegate
                {
                    SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                    SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
                });
                return false;
            }
            return false;
        }

        /// <summary>
        /// set the enemy team for Mother Evilyn fight
        /// </summary>
        [HarmonyPatch(typeof(MotherEvilyn), "StartFight")]
        [HarmonyPrefix]
        public static bool motherevilinfight(MotherEvilyn __instance)
        {
            ArchipelagoConsole.LogDebug("Mother Evilyn");

            HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam(__instance.fightInitiatorID)), ArchipelagoClient.ServerData.trainerteam(__instance.fightInitiatorID).Length == 1, false, false, false, __instance.aILevel, false, MapManager.instance.biome, __instance.dialogName, __instance.fightInitiatorID);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }

        /// <summary>
        /// set the enemy team for Sally Mc Tits fight
        /// </summary>
        [HarmonyPatch(typeof(SallyMcTits), "StartFight")]
        [HarmonyPrefix]
        public static bool sallyfight(SallyMcTits __instance)
        {
            ArchipelagoConsole.LogDebug("Sally McTits");

            HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam(__instance.fightInitiatorID)), ArchipelagoClient.ServerData.trainerteam(__instance.fightInitiatorID).Length == 1, false, false, false, __instance.aILevel, false, MapManager.instance.biome, __instance.dialogName, __instance.fightInitiatorID);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }

        /// <summary>
        /// set the enemy team for Kingly fight
        /// </summary>
        [HarmonyPatch(typeof(Kinley), "StartFight")]
        [HarmonyPrefix]
        public static bool kinlyfight(Kinley __instance)
        {
            ArchipelagoConsole.LogDebug("Kinley");

            HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam(__instance.fightInitiatorID)), ArchipelagoClient.ServerData.trainerteam(__instance.fightInitiatorID).Length == 1, false, false, false, __instance.aILevel, false, MapManager.instance.biome, __instance.dialogName, __instance.fightInitiatorID);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }

        /// <summary>
        /// set the enemy team for Valkrie Boss fight
        /// </summary>
        [HarmonyPatch(typeof(AncientTemple3Sequence), "StartFight")]
        [HarmonyPrefix]
        public static bool valkryfight(AncientTemple3Sequence __instance)
        {
            ArchipelagoConsole.LogDebug("Valkrie");

            HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam("Boss_Valkrie")), ArchipelagoClient.ServerData.trainerteam("Boss_Valkrie").Length == 1, false, false, false, __instance.valkyrieAILevel, false, MapManager.instance.biome, __instance.valkyrie.dialogName, null);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }

        /// <summary>
        /// set the enemy team for Domino Boss fight
        /// </summary>
        [HarmonyPatch(typeof(DesertTemple2Sequence), "StartFight")]
        [HarmonyPrefix]
        public static bool centiboobfight(DesertTemple2Sequence __instance)
        {
            ArchipelagoConsole.LogDebug("Domino");

            HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam("Stone Temple: Domino")), ArchipelagoClient.ServerData.trainerteam("Stone Temple: Domino").Length == 1, false, false, false, __instance.dominoAILevel, false, MapManager.instance.biome, __instance.domino.dialogName, null);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }

        /// <summary>
        /// set the enemy team for Centiboob Boss fight
        /// </summary>
        [HarmonyPatch(typeof(IslandCave2Sequence), "StartFight")]
        [HarmonyPrefix]
        public static bool centiboobfight(IslandCave2Sequence __instance)
        {
            ArchipelagoConsole.LogDebug("Centiboob");

            HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam("Island Cave: Centiboob")), ArchipelagoClient.ServerData.trainerteam("Island Cave: Centiboob").Length == 1, false, false, false, __instance.centiboobAILevel, false, MapManager.instance.biome, __instance.centiboobName, null);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }

        /// <summary>
        /// set the enemy team for Crimson Countess fight
        /// </summary>
        [HarmonyPatch(typeof(ArcticTemple2sequence), "StartFight")]
        [HarmonyPrefix]
        public static bool countessfight(ArcticTemple2sequence __instance)
        {
            ArchipelagoConsole.LogDebug("Crimson Countess");

            HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam("Artic Temple: Crimson Countess")), ArchipelagoClient.ServerData.trainerteam("Artic Temple: Crimson Countess").Length == 1, false, false, false, __instance.countessAILevel, false, MapManager.instance.biome, __instance.countess.dialogName, null);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }

        /// <summary>
        /// set the enemy team for Spirit Mother Boss fight
        /// </summary>
        [HarmonyPatch(typeof(InnerGroveSequence), "StartFight")]
        [HarmonyPrefix]
        public static bool grovefight(InnerGroveSequence __instance)
        {
            ArchipelagoConsole.LogDebug("Spirit Mother");

            HelperItems.save.SetFightData(MonsterManager.instance.SpawnTeamFromBlueprints(ArchipelagoClient.ServerData.trainerteam("Inner Grove: Spirit Mother")), ArchipelagoClient.ServerData.trainerteam("Inner Grove: Spirit Mother").Length == 1, false, false, false, __instance.enemyAILevel, false, MapManager.instance.biome, __instance.enemyName, null);
            SceneTransitionManager.instance.StartRandomTransition(delegate
            {
                SceneTransitionManager.instance.npcStartFightOverlay.Hide();
                SceneManager.LoadScene("FightScene", LoadSceneMode.Single);
            });
            return false;
        }
    }
}
