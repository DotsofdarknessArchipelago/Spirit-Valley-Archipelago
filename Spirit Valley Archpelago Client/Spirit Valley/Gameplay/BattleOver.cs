using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{

    [HarmonyPatch]
    public class BattleOver
    {

        /// <summary>
        /// set the loot pool for after defeating a monster to nothing
        /// </summary>
        [HarmonyPatch(typeof(MapManager), "RandomizeWildMonsterLoot")]
        [HarmonyPostfix]
        public static void wildlootoverride(ref ItemBundle[] __result)
        {
            ArchipelagoConsole.LogDebug($"changing wild loot pool");
            __result = HelperItems.voidbundle();
        }

        /// <summary>
        /// debug for getting result for when a fight is over
        /// </summary>
        [HarmonyPatch(typeof(FightManager), "FightOverCoroutine")]
        [HarmonyPrefix]
        public static void battleover(FightManager __instance, ref FightManager.FightResult ___fightResult)
        {
            ArchipelagoConsole.LogDebug($"FIGHT OVER result({___fightResult})");
        }

        /// <summary>
        /// send location for defeating an enemy on the map based on its GUID
        /// </summary>
        [HarmonyPatch(typeof(EnemyMapItem), "Deactivate")]
        [HarmonyPrefix]
        public static void battle(EnemyMapItem __instance, EnemyMapItemState ___state)
        {
            ArchipelagoConsole.LogDebug($"DEACTIVATING ENEMYMAPITEM:{___state.guid}");
            ArchipelagoConsole.LogDebug($"DEACTIVATING ENEMYMAPITEM:{__instance.guid}");

            //get the start value for battle locations
            int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
            switch (___state.guid)
            {
                case "19c75671-2314-414f-b500-ef28c011d8d2"://Evergreen Outpost: Defeat Elise
                    ArchipelagoConsole.LogDebug("Evergreen Outpost: Defeat Elise");
                    ArchipelagoClient.sendloc(battleidstart + 2);
                    break;
                case "0a40a301-741a-4843-8008-799f4ba37287"://Trail 02: Defeat Billy
                    ArchipelagoConsole.LogDebug("Trail 02: Defeat Billy");
                    ArchipelagoClient.sendloc(battleidstart + 3);
                    break;
                case "bf261ea7-7b93-4c0b-89a8-da7c93550808"://Trail 02: Defeat Macy
                    ArchipelagoConsole.LogDebug("Trail 02: Defeat Macy");
                    ArchipelagoClient.sendloc(battleidstart + 4);
                    break;
                case "a79a0909-43a5-47ff-b990-a1632a224e83"://Trail 02: Defeat Skyler
                    ArchipelagoConsole.LogDebug("Trail 02: Defeat Skyler");
                    ArchipelagoClient.sendloc(battleidstart + 5);
                    break;
                case "b40b0778-da74-4660-b0a1-fba6d1d16bdd"://Trail 03: Defeat Cheese
                    ArchipelagoConsole.LogDebug("Trail 03: Defeat Cheese");
                    ArchipelagoClient.sendloc(battleidstart + 7);
                    break;
                case "c029e36a-14ec-4d07-a45b-b7b57f406575"://Trail 03: Defeat Miriam
                    ArchipelagoConsole.LogDebug("Trail 03: Defeat Miriam");
                    ArchipelagoClient.sendloc(battleidstart + 8);
                    break;
                case "6778b3a1-97d4-457d-adc1-c324dbad017e"://Trail 03: Defeat Jenna
                    ArchipelagoConsole.LogDebug("Trail 03: Defeat Jenna");
                    ArchipelagoClient.sendloc(battleidstart + 9);
                    break;
                case "e6929a89-5dc3-4118-bcf9-ff20df7ed4af"://Evergreen Caverns: Defeat Stu
                    ArchipelagoConsole.LogDebug("Evergreen Caverns: Defeat Stu");
                    ArchipelagoClient.sendloc(battleidstart + 10);
                    break;
                case "364ef3fd-dfe9-41bb-aa8c-9583af54d8f8"://Evergreen Caverns: Defeat Nicole
                    ArchipelagoConsole.LogDebug("Evergreen Caverns: Defeat Nicole");
                    ArchipelagoClient.sendloc(battleidstart + 11);
                    break;
                case "72e0b641-b787-46cb-8fe8-eb17f93073fa"://Evergreen Caverns: Defeat Rawry
                    ArchipelagoConsole.LogDebug("Evergreen Caverns: Defeat Rawry");
                    ArchipelagoClient.sendloc(battleidstart + 12);
                    break;
                case "5efd2110-61ad-4bea-9551-2bffee802492"://Ancient Temple 1: Defeat 1st Crimson Cloak
                    ArchipelagoConsole.LogDebug("Ancient Temple 1: Defeat 1st Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 13);
                    break;
                case "27d2018d-9706-4b17-981d-e408d42e1041"://Ancient Temple 1: Defeat 2nd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Ancient Temple 1: Defeat 2nd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 14);
                    break;
                case "cae4d216-6d69-470b-a721-3d83290c0de6"://Ancient Temple 1: Defeat 3rd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Ancient Temple 1: Defeat 3rd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 15);
                    break;
                case "2174dd35-f25f-4d1a-86a3-c1f46f576ff9"://Ancient Temple 1: Defeat 4th Crimson Cloak
                    ArchipelagoConsole.LogDebug("Ancient Temple 1: Defeat 4th Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 16);
                    break;
                case "677f47ac-c833-42c8-a19a-4d99d5985fdd"://Ancient Temple 1: Defeat 5th Crimson Cloak
                    ArchipelagoConsole.LogDebug("Ancient Temple 1: Defeat 5th Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 17);
                    break;
                case "7c73c737-4fd5-4266-92ea-caf02f8c9320"://Ancient Temple 1: Defeat 6th Crimson Cloak
                    ArchipelagoConsole.LogDebug("Ancient Temple 1: Defeat 6th Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 18);
                    break;
                case "122ab3e7-c278-402b-a741-c83633c93626"://Ancient Temple 2: Defeat Crimson Cloak
                    ArchipelagoConsole.LogDebug("Ancient Temple 2: Defeat Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 19);
                    break;
                case "83b06037-1fe2-47d9-8887-479a7b0104d6"://Trail 05: Defeat Mila
                    ArchipelagoConsole.LogDebug("Trail 05: Defeat Mila");
                    ArchipelagoClient.sendloc(battleidstart + 21);
                    break;
                case "e6cda171-22b9-43fb-9ca0-f2411e2e4226"://Trail 05: Defeat Roy
                    ArchipelagoConsole.LogDebug("Trail 05: Defeat Roy");
                    ArchipelagoClient.sendloc(battleidstart + 22);
                    break;
                case "72a096dd-0fe8-4146-9bf0-c7d5e5234b98"://Trail 05: Defeat Lulu
                    ArchipelagoConsole.LogDebug("Trail 05: Defeat Lulu");
                    ArchipelagoClient.sendloc(battleidstart + 23);
                    break;
                case "666003ef-c69e-4279-809a-e757e8cb60b2"://Sandy Tunnels: Defeat Chad
                    ArchipelagoConsole.LogDebug("Sandy Tunnels: Defeat Chad");
                    ArchipelagoClient.sendloc(battleidstart + 24);
                    break;
                case "265abaf4-18eb-45fd-8aba-6bc4f8844f81"://Sandy Tunnels: Defeat Destiny
                    ArchipelagoConsole.LogDebug("Sandy Tunnels: Defeat Destiny");
                    ArchipelagoClient.sendloc(battleidstart + 25);
                    break;
                case "acd2e86c-2cdd-48e9-aaed-ba84a84d70a3"://Trail 06: Defeat Kelsie
                    ArchipelagoConsole.LogDebug("Trail 06: Defeat Kelsie");
                    ArchipelagoClient.sendloc(battleidstart + 26);
                    break;
                case "8cad5228-7db2-49cd-9fcc-e625029e6817"://Trail 06: Defeat Hayden
                    ArchipelagoConsole.LogDebug("Trail 06: Defeat Hayden");
                    ArchipelagoClient.sendloc(battleidstart + 27);
                    break;
                case "4cc138d0-8b3d-4ea6-8dd4-e593ae0d9aef"://Trail 06: Defeat Juliet
                    ArchipelagoConsole.LogDebug("Trail 06: Defeat Juliet");
                    ArchipelagoClient.sendloc(battleidstart + 28);
                    break;
                case "56c3e787-d36a-4e11-aead-ea47f500e261"://Trail 07: Defeat Bella
                    ArchipelagoConsole.LogDebug("Trail 07: Defeat Bella");
                    ArchipelagoClient.sendloc(battleidstart + 30);
                    break;
                case "ab480291-fa67-4ec2-a724-c048b4537914"://Trail 07: Defeat Dakota
                    ArchipelagoConsole.LogDebug("Trail 07: Defeat Dakota");
                    ArchipelagoClient.sendloc(battleidstart + 31);
                    break;
                case "0f05b20d-99cf-4cee-852e-7e5edac5a456"://Trail 07: Defeat Cassidy
                    ArchipelagoConsole.LogDebug("Trail 07: Defeat Cassidy");
                    ArchipelagoClient.sendloc(battleidstart + 32);
                    break;
                case "e07a91ad-6fd5-4d54-8b05-36c3f9d090c1"://Trail 08: Defeat Marisa
                    ArchipelagoConsole.LogDebug("Trail 08: Defeat Marisa");
                    ArchipelagoClient.sendloc(battleidstart + 36);
                    break;
                case "bd2e9de2-30db-42f2-aa44-678cf71649ea"://Trail 08: Defeat Jenni
                    ArchipelagoConsole.LogDebug("Trail 08: Defeat Jenni");
                    ArchipelagoClient.sendloc(battleidstart + 37);
                    break;
                case "163d96da-8b46-4b1e-baf6-e46708072abe"://Trail 08: Defeat Alanna
                    ArchipelagoConsole.LogDebug("Trail 08: Defeat Alanna");
                    ArchipelagoClient.sendloc(battleidstart + 38);
                    break;
                case "af5b25fb-7066-4fca-b1fa-c94fb7e5f330"://Dusty Grotto: Defeat Arnie
                    ArchipelagoConsole.LogDebug("Dusty Grotto: Defeat Arnie");
                    ArchipelagoClient.sendloc(battleidstart + 39);
                    break;
                case "cf1d4fc7-2757-41ea-8198-322dda687398"://Dusty Grotto: Defeat Crystal
                    ArchipelagoConsole.LogDebug("Dusty Grotto: Defeat Crystal");
                    ArchipelagoClient.sendloc(battleidstart + 40);
                    break;
                case "176d7645-f963-47ca-9af5-344d1c2e8dc0"://Dusty Grotto: Defeat Skye
                    ArchipelagoConsole.LogDebug("Dusty Grotto: Defeat Skye");
                    ArchipelagoClient.sendloc(battleidstart + 41);
                    break;
                case "f792e755-6771-4f50-8dca-8d3cf8b6017a"://Trail 09: Defeat Mike
                    ArchipelagoConsole.LogDebug("Trail 09: Defeat Mike");
                    ArchipelagoClient.sendloc(battleidstart + 42);
                    break;
                case "00c525ca-41d2-40ba-a68e-c40f8990652c"://Trail 09: Defeat Clementine
                    ArchipelagoConsole.LogDebug("Trail 09: Defeat Clementine");
                    ArchipelagoClient.sendloc(battleidstart + 43);
                    break;
                case "b4d3fec1-9f7f-4b2e-a3de-cf25bc3fe399"://Trail 09: Defeat Bonnie
                    ArchipelagoConsole.LogDebug("Trail 09: Defeat Bonnie");
                    ArchipelagoClient.sendloc(battleidstart + 44);
                    break;
                case "48a6856e-4dbd-4ca9-b6d5-066b5a55d783"://Stone Temple 1: Defeat 1st Crimson Cloak
                    ArchipelagoConsole.LogDebug("Stone Temple 1: Defeat 1st Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 45);
                    break;
                case "7b40e4f2-990b-4a2c-8ccc-aa283653436a"://Stone Temple 1: Defeat 2nd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Stone Temple 1: Defeat 2nd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 46);
                    break;
                case "b3ab8b9c-5260-47a6-befc-d99487a2a53f"://Stone Temple 1: Defeat 3rd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Stone Temple 1: Defeat 3rd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 47);
                    break;
                case "bf8484cc-5889-45ce-8b18-c35b96e0d0e7"://Stone Temple 1: Defeat 4th Crimson Cloak
                    ArchipelagoConsole.LogDebug("Stone Temple 1: Defeat 4th Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 48);
                    break;
                case "02067b08-1777-4713-af0d-123bb86102fe"://Stone Temple 1: Defeat 5th Crimson Cloak
                    ArchipelagoConsole.LogDebug("Stone Temple 1: Defeat 5th Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 49);
                    break;
                case "a0268c7e-1417-41cb-aa2a-109240ff2eac"://Stone Temple 1: Defeat 6th Crimson Cloak
                    ArchipelagoConsole.LogDebug("Stone Temple 1: Defeat 6th Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 50);
                    break;
                case "ae458556-c336-43a7-a7c3-be76c84f0a48"://Crash Site: Defeat Athena
                    ArchipelagoConsole.LogDebug("Crash Site: Defeat Athena");
                    ArchipelagoClient.sendloc(battleidstart + 52);
                    break;
                case "ef863488-65f8-4827-9e80-0e1c6a42b681"://Crash Site: Defeat Janet
                    ArchipelagoConsole.LogDebug("Crash Site: Defeat Janet");
                    ArchipelagoClient.sendloc(battleidstart + 53);
                    break;
                case "b15889a3-63eb-490f-8f7b-e14555ac9d97"://Trail 10: Defeat Bailee
                    ArchipelagoConsole.LogDebug("Trail 10: Defeat Bailee");
                    ArchipelagoClient.sendloc(battleidstart + 54);
                    break;
                case "6ee5a399-6614-482d-8e07-00abcf34d10e"://Trail 10: Defeat Eve
                    ArchipelagoConsole.LogDebug("Trail 10: Defeat Eve");
                    ArchipelagoClient.sendloc(battleidstart + 55);
                    break;
                case "cc69f7aa-a078-448c-ab25-00c8f774926f"://Trail 11: Defeat Emilia
                    ArchipelagoConsole.LogDebug("Trail 11: Defeat Emilia");
                    ArchipelagoClient.sendloc(battleidstart + 57);
                    break;
                case "2bf2f7ed-e375-4747-875c-3bd1b2048e46"://Trail 11: Defeat Sydney
                    ArchipelagoConsole.LogDebug("Trail 11: Defeat Sydney");
                    ArchipelagoClient.sendloc(battleidstart + 58);
                    break;
                case "ddc0cee9-5a37-431b-baf8-8653a97f13a0"://Trail 12: Defeat Sophie
                    ArchipelagoConsole.LogDebug("Trail 12: Defeat Sophie");
                    ArchipelagoClient.sendloc(battleidstart + 59);
                    break;
                case "961a23f5-023b-4d31-ab65-b8d227a52ded"://Trail 12: Defeat Ciara
                    ArchipelagoConsole.LogDebug("Trail 12: Defeat Ciara");
                    ArchipelagoClient.sendloc(battleidstart + 60);
                    break;
                case "a4a13dee-d151-407c-8ed1-8db2d45efdf2"://Trail 13: Defeat 1st Cultist
                    ArchipelagoConsole.LogDebug("Trail 13: Defeat 1st Cultist");
                    ArchipelagoClient.sendloc(battleidstart + 62);
                    break;
                case "b4a8bd50-ab01-4e3c-8aba-0469ada1c52f"://Trail 13: Defeat 2nd Cultist
                    ArchipelagoConsole.LogDebug("Trail 13: Defeat 2nd Cultist");
                    ArchipelagoClient.sendloc(battleidstart + 63);
                    break;
                case "38dd508c-5633-47c3-b142-846c3915716d"://Trail 14: Defeat 1st Cultist
                    ArchipelagoConsole.LogDebug("Trail 14: Defeat 1st Cultist");
                    ArchipelagoClient.sendloc(battleidstart + 64);
                    break;
                case "9b009cf3-5fad-4076-88d2-3e43e004efec"://Trail 14: Defeat 2nd Cultist
                    ArchipelagoConsole.LogDebug("Trail 14: Defeat 2nd Cultist");
                    ArchipelagoClient.sendloc(battleidstart + 65);
                    break;
                case "5fbd94fe-f5dc-42bb-9f57-dbaec4d8d3c3"://Island Cave 1: Defeat 1st Cultist
                    ArchipelagoConsole.LogDebug("Island Cave 1: Defeat 1st Cultist");
                    ArchipelagoClient.sendloc(battleidstart + 66);
                    break;
                case "1ad60dfe-2454-431e-8f8a-8f512003aa1d"://Island Cave 1: Defeat 2nd Cultist
                    ArchipelagoConsole.LogDebug("Island Cave 1: Defeat 2nd Cultist");
                    ArchipelagoClient.sendloc(battleidstart + 67);
                    break;
                case "46a60f99-3cb9-42cf-860f-9e471707e263"://Island Cave 1: Defeat 3rd Cultist
                    ArchipelagoConsole.LogDebug("Island Cave 1: Defeat 3rd Cultist");
                    ArchipelagoClient.sendloc(battleidstart + 68);
                    break;
                case "5f53e18a-e6b1-473a-8252-f0d68286ca57"://Island Cave 1: Defeat 4th Cultist
                    ArchipelagoConsole.LogDebug("Island Cave 1: Defeat 4th Cultist");
                    ArchipelagoClient.sendloc(battleidstart + 69);
                    break;
                case "323cbfec-0db2-43c2-a538-e3b4cf02d260"://Cold Harbor: Defeat Vanessa
                    ArchipelagoConsole.LogDebug("Cold Harbor: Defeat Vanessa");
                    ArchipelagoClient.sendloc(battleidstart + 71);
                    break;
                case "c34254a6-6f54-4643-8319-75636a798542"://Cold Harbor: Defeat Iris
                    ArchipelagoConsole.LogDebug("Cold Harbor: Defeat Iris");
                    ArchipelagoClient.sendloc(battleidstart + 72);
                    break;
                case "705f45eb-9221-4c47-b339-e8d2b2f6d862"://Trail 15: Defeat Mia
                    ArchipelagoConsole.LogDebug("Trail 15: Defeat Mia");
                    ArchipelagoClient.sendloc(battleidstart + 74);
                    break;
                case "9f573d72-be6e-48dc-9ffd-50044176a86c"://Trail 15: Defeat Olga
                    ArchipelagoConsole.LogDebug("Trail 15: Defeat Olga");
                    ArchipelagoClient.sendloc(battleidstart + 75);
                    break;
                case "911604b8-a719-4eb6-af17-42bd8dc35a9b"://Trail 16: Defeat Karin
                    ArchipelagoConsole.LogDebug("Trail 16: Defeat Karin");
                    ArchipelagoClient.sendloc(battleidstart + 76);
                    break;
                case "1e4eb581-53ee-4f87-b021-ff0ebc931798"://Trail 16: Defeat Dahlia
                    ArchipelagoConsole.LogDebug("Trail 16: Defeat Dahlia");
                    ArchipelagoClient.sendloc(battleidstart + 77);
                    break;
                case "5d964c9f-f399-4a24-98f6-def8af276d4c"://Trail 17: Defeat Clara
                    ArchipelagoConsole.LogDebug("Trail 17: Defeat Clara");
                    ArchipelagoClient.sendloc(battleidstart + 78);
                    break;
                case "38419b1d-9908-4ef4-a962-1406aa2a4352"://Trail 17: Defeat Liv
                    ArchipelagoConsole.LogDebug("Trail 17: Defeat Liv");
                    ArchipelagoClient.sendloc(battleidstart + 79);
                    break;
                case "d09da17a-d5b6-415f-986f-9dc216400385"://Trail 17: Defeat Karly
                    ArchipelagoConsole.LogDebug("Trail 17: Defeat Karly");
                    ArchipelagoClient.sendloc(battleidstart + 80);
                    break;
                case "0a2fe22c-e43e-457f-85af-29ed94e9f57d"://Trail 18: Defeat Stacy
                    ArchipelagoConsole.LogDebug("Trail 18: Defeat Stacy");
                    ArchipelagoClient.sendloc(battleidstart + 81);
                    break;
                case "4492eac4-575d-46c8-8d4f-4418e4ab1065"://Trail 18: Defeat Anabelle
                    ArchipelagoConsole.LogDebug("Trail 18: Defeat Anabelle");
                    ArchipelagoClient.sendloc(battleidstart + 82);
                    break;
                case "5676a70d-5a1c-4868-906f-a269dffc5f2f"://Trail 18: Defeat Ingrid
                    ArchipelagoConsole.LogDebug("Trail 18: Defeat Ingrid");
                    ArchipelagoClient.sendloc(battleidstart + 83);
                    break;
                case "23aa2df5-197e-45cb-af67-dfc97e83dd3b"://Artic Temple 1: Defeat 1st Crimson Cloak
                    ArchipelagoConsole.LogDebug("Artic Temple 1: Defeat 1st Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 84);
                    break;
                case "1452eb18-e64d-4fb6-93b3-84574ee29396"://Artic Temple 1: Defeat 2nd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Artic Temple 1: Defeat 2nd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 85);
                    break;
                case "4bd72a1d-cdf9-49b4-ba2b-245dabf60035"://Artic Temple 1: Defeat 3rd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Artic Temple 1: Defeat 3rd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 86);
                    break;
                case "60f3aad3-3f2d-4ce1-ab4a-f6833957b8ab"://Artic Temple 1: Defeat 4th Crimson Cloak
                    ArchipelagoConsole.LogDebug("Artic Temple 1: Defeat 4th Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 87);
                    break;
                case "5272d410-ae2d-42b5-93a8-b06b4ba20fe2"://Artic Temple 1: Defeat 5th Crimson Cloak
                    ArchipelagoConsole.LogDebug("Artic Temple 1: Defeat 5th Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 88);
                    break;
                case "97fab556-a752-489c-8de5-04d3449afeca"://Trail 19: Defeat 1st Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 19: Defeat 1st Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 90);
                    break;
                case "ce0b7e57-6bbd-4034-9f2b-2785f6b6f07d"://Trail 19: Defeat 2nd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 19: Defeat 2nd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 91);
                    break;
                case "bbb2a608-b9f8-4701-a978-549f98628a70"://Trail 19: Defeat 3rd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 19: Defeat 3rd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 92);
                    break;
                case "4d8163f6-3e75-4112-9824-7e0247d4118f"://Trail 20: Defeat 1st Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 20: Defeat 1st Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 93);
                    break;
                case "72d37c80-d416-48b0-8e1f-ab6c9f49e40c"://Trail 20: Defeat 2nd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 20: Defeat 2nd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 94);
                    break;
                case "149cf1b9-7344-4037-88b8-42fe6f471e64"://Trail 20: Defeat 3rd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 20: Defeat 3rd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 95);
                    break;
                case "ff372848-9064-45a9-9e2c-dd98e3fd1313"://Trail 21: Defeat 1st Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 21: Defeat 1st Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 96);
                    break;  
                case "24e2596a-4820-46e2-a06a-59a5333d1e4b"://Trail 21: Defeat 2nd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 21: Defeat 2nd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 97);
                    break;
                case "0ea61b92-8dcd-4adf-a070-4bc5870b2698"://Trail 21: Defeat Kinley
                    ArchipelagoConsole.LogDebug("Trail 21: Defeat Kinley");
                    ArchipelagoClient.sendloc(battleidstart + 98);
                    break;
                case "9eeac2b8-20b3-4d35-a7b9-bb01169dc72d"://Trail Spirit Passage: Defeat 1st Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail Spirit Passage: Defeat 1st Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 99);
                    break;
                case "70e65def-a84b-4df5-873c-77d2f02fc30b"://Trail Spirit Passage: Defeat 2nd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail Spirit Passage: Defeat 2nd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 100);
                    break;
                case "b8863596-1a75-481f-94ca-4178785f0554"://Trail Spirit Passage: Defeat 3rd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail Spirit Passage: Defeat 3rd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 101);
                    break;
                case "97835a52-0d7b-4d9d-9184-8eb813faf909"://Trail Spirit Passage: Defeat 4th Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail Spirit Passage: Defeat 4th Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 102);
                    break;
                case "a2557c2e-85f8-4511-8d14-da72a962943c"://Trail Spirit Passage: Defeat 5th Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail Spirit Passage: Defeat 5th Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 103);
                    break;
                case "7f45394d-44a9-466e-b9a5-7a169ae47754"://Trail 22: Defeat 1st Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 22: Defeat 1st Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 104);
                    break;
                case "95124723-8456-47a9-91fa-1576ef841d84"://Trail 22: Defeat 2nd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 22: Defeat 2nd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 105);
                    break;
                case "c618afc1-47b2-4de3-b09d-483d57333482"://Trail 22: Defeat 3rd Crimson Cloak
                    ArchipelagoConsole.LogDebug("Trail 22: Defeat 3rd Crimson Cloak");
                    ArchipelagoClient.sendloc(battleidstart + 106);
                    break;
                default:
                    ArchipelagoConsole.LogDebug($"GUID NOT KNOWN:{___state.guid}");
                    break;
            }
        }



        /// <summary>
        /// give player 100 coins for defeating a enemy
        /// </summary>
        [HarmonyPatch(typeof(EnemyMapItem), "OnAfterMapInitiAfterFight")]
        [HarmonyPostfix]
        public static void givecoinforfight(EnemyMapItem __instance, ref EnemyMapItemState ___state, SystemData<GameState> ___gameState)
        {
            ___gameState.data.ModifyMoney(100);
            ArchipelagoConsole.LogMessage("Got 100 Coin for Defeating Trainer");
        }

        /// <summary>
        /// send location for defeating an frendly fight/side quest fight based on its GUID
        /// </summary>
        [HarmonyPatch(typeof(FrienlyFightNPCGeneric), "AfterReturnFromFightCallback")]
        [HarmonyPrefix]
        public static void frendlyfightend(FrienlyFightNPCGeneric __instance)
        {
            ArchipelagoConsole.LogDebug("ENDING FRENDLY FIGHT:");
            ArchipelagoConsole.LogDebug($"SIDE QUEST ID:{__instance.sideQuestID}");
            ArchipelagoConsole.LogDebug($"GUID:{__instance.fightInitiatorID}");
            //robbie
            int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
            switch (__instance.fightInitiatorID)
            {
                case "61822611-267a-4366-b99c-fadc5a23ad01"://Oakwood Village: Defeat Robbie
                    ArchipelagoConsole.LogDebug("Oakwood Village: Defeat Robbie");
                    ArchipelagoClient.sendloc(battleidstart + 1);
                    break;
                case "Alice"://Trail 11: Defeat Alice
                    ArchipelagoConsole.LogDebug("Trail 11: Defeat Alice");
                    ArchipelagoClient.sendloc(battleidstart + 56);
                    break;
                default:
                    break;
            }
        }

        /// <summary>
        /// send location for defeating Bonnie baiter due to NPC having unique class 
        /// </summary>
        [HarmonyPatch(typeof(BonnieBaiter), "AfterReturnFromFightCallback")]
        [HarmonyPrefix]
        public static void boniefight()
        {
            ArchipelagoConsole.LogDebug("Bonnie Baiter");
            if (GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                //case "05ba33a6-2693-49ba-b570-543c25feeeb2"://Fishing Hut: Defeat Bonnie Baiter
                ArchipelagoConsole.LogDebug("Fishing Hut: Defeat Bonnie Baiter");
                ArchipelagoClient.sendloc(battleidstart + 61);
                //break;
            }
        }

        /// <summary>
        /// send location for defeating the Crimson Agient on Trail 2 due to NPC having unique class 
        /// </summary>
        [HarmonyPatch(typeof(CrimsonAgent1), "OnAfterMapInitiAfterFight")]
        [HarmonyPrefix]
        public static void crimsonagentfight()
        {
            ArchipelagoConsole.LogDebug("CrimsonAgent1");
            if (GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                //case "53af4c29-1d1b-4655-a1db-9ed89c32a981"://Trail 02: Defeat Crimson Agent
                ArchipelagoConsole.LogDebug("Trail 02: Defeat Crimson Agent");
                ArchipelagoClient.sendloc(battleidstart + 6);
                //break;
            }
        }

        /// <summary>
        /// send locations for defeating fights started by sassy in tumbleweed town due to NPC having unique class 
        /// </summary>
        [HarmonyPatch(typeof(Sassy), "AfterReturnFromFightCallback")]
        [HarmonyPrefix]
        public static void sassyfights()
        {
            ArchipelagoConsole.LogDebug("Sassy");
            if (GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                if (GameManager.instance.GetActiveGameState().data.GetActiveMainQuestState().Quest.id == "main_quest_21_a_new_challenger")
                {
                    //case "Willy Wanker"://Tumbleweed Town: Defeat Willy Wanker
                    ArchipelagoConsole.LogDebug("Tumbleweed Town: Defeat Willy Wanker");
                    ArchipelagoClient.sendloc(battleidstart + 33);
                    //break;
                    return;
                }
                if (GameManager.instance.GetActiveGameState().data.GetActiveMainQuestState().Quest.id == "main_quest_22_stiff_competition")
                {
                    // case "Dick Cummings"://Tumbleweed Town: Defeat Dick Cummings
                    ArchipelagoConsole.LogDebug("Tumbleweed Town: Defeat Dick Cummings");
                    ArchipelagoClient.sendloc(battleidstart + 34);
                    //break;
                    return;
                }
                if (GameManager.instance.GetActiveGameState().data.GetActiveMainQuestState().Quest.id == "main_quest_23_final_fight")
                {
                    //case "Dick Louie"://Tumbleweed Town: Defeat Dick Louie
                    ArchipelagoConsole.LogDebug("Tumbleweed Town: Defeat Dick Louie");
                    ArchipelagoClient.sendloc(battleidstart + 35);
                    //break;
                }
            }
        }

        /// <summary>
        /// send location for defeating Mother Evilyn due to NPC having unique class 
        /// </summary>
        [HarmonyPatch(typeof(MotherEvilyn), "OnAfterMapInitiAfterFight")]
        [HarmonyPrefix]
        public static void motherevilinfight()
        {
            ArchipelagoConsole.LogDebug("Mother Evilyn");
            if (GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                //case "aa1ce20e-a988-48c9-8a4b-e246fb163402"://Frostville: Defeat Mother Evilyn
                ArchipelagoConsole.LogDebug("Frostville: Defeat Mother Evilyn");
                ArchipelagoClient.sendloc(battleidstart + 73);
                //break;
            }
        }

        /// <summary>
        /// send location for defeating Sally Mc Tits due to NPC having unique class 
        /// </summary>
        [HarmonyPatch(typeof(SallyMcTits), "OnAfterMapInitiAfterFight")]
        [HarmonyPrefix]
        public static void sallyfight()
        {
            ArchipelagoConsole.LogDebug("Sally McTits");
            if (GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                //case "6db1fd7b-c78b-4de1-967c-ce67e656236e"://Trail 07: Defeat Sally McTits
                ArchipelagoConsole.LogDebug("Trail 07: Defeat Sally McTits");
                ArchipelagoClient.sendloc(battleidstart + 29);
                //break;
            }
        }

        /// <summary>
        /// send location for defeating Kingley due to NPC having unique class 
        /// </summary>
        [HarmonyPatch(typeof(Kinley), "OnAfterMapInitiAfterFight")]
        [HarmonyPrefix]
        public static void kinleyfight()
        {
            ArchipelagoConsole.LogDebug("Kinley");
            if (GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                ArchipelagoConsole.LogDebug("Trail 21: Defeat Kinley");
                ArchipelagoClient.sendloc(battleidstart + 98);
            }
        }

        /// <summary>
        /// send location for defeating Valkrie boss due to it being part of a sripted sequence
        /// </summary>
        [HarmonyPatch(typeof(AncientTemple3Sequence), "PlayCoroutine")]
        [HarmonyPrefix]
        public static void valkryfight(AncientTemple3Sequence __instance)
        {
            ArchipelagoConsole.LogDebug("Valkrie");
            if (__instance.mapManager.SceneStartData.isReturningFromFight && GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                //case "Valkrie"://Ancient Temple 3: Defeat Valkrie
                ArchipelagoConsole.LogDebug("Ancient Temple 3: Defeat Valkrie");
                ArchipelagoClient.sendloc(battleidstart + 20);
                //break;
            }
        }

        /// <summary>
        /// send location for defeating Domino boss due to it being part of a sripted sequence
        /// </summary>
        [HarmonyPatch(typeof(DesertTemple2Sequence), "PlayCoroutine")]
        [HarmonyPrefix]
        public static void centiboobfight(DesertTemple2Sequence __instance)
        {
            ArchipelagoConsole.LogDebug("Domino");
            if (__instance.mapManager.SceneStartData.isReturningFromFight && GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                //case "Domino"://Stone Temple 2: Defeat Domino
                ArchipelagoConsole.LogDebug("Stone Temple 2: Defeat Domino");
                ArchipelagoClient.sendloc(battleidstart + 51);
                //break;
            }
        }

        /// <summary>
        /// send location for defeating Centiboob boss due to it being part of a sripted sequence
        /// </summary>
        [HarmonyPatch(typeof(IslandCave2Sequence), "PlayCoroutine")]
        [HarmonyPrefix]
        public static void centiboobfight(IslandCave2Sequence __instance)
        {
            ArchipelagoConsole.LogDebug("Centiboob");
            if (__instance.mapManager.SceneStartData.isReturningFromFight && GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                //case "Centiboob"://Island Cave 2: Defeat Centiboob
                ArchipelagoConsole.LogDebug("Island Cave 2: Defeat Centiboob");
                ArchipelagoClient.sendloc(battleidstart + 70);
                //break;
            }
        }

        /// <summary>
        /// send location for defeating Crimson Countess boss due to it being part of a sripted sequence
        /// </summary>
        [HarmonyPatch(typeof(ArcticTemple2sequence), "PlayCoroutine")]
        [HarmonyPrefix]
        public static void countessfight(ArcticTemple2sequence __instance)
        {
            ArchipelagoConsole.LogDebug("Crimson Countess");
            if (__instance.mapManager.SceneStartData.isReturningFromFight && GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                //case "Crimson Countess"://Artic Temple 2: Defeat Crimson Countess
                ArchipelagoConsole.LogDebug("Artic Temple 2: Defeat Crimson Countess");
                ArchipelagoClient.sendloc(battleidstart + 89);
                //break;
            }
        }

        /// <summary>
        /// send location for defeating Spirit Mother boss due to it being part of a sripted sequence
        /// </summary>
        [HarmonyPatch(typeof(InnerGroveSequence), "PlayCoroutine")]
        [HarmonyPrefix]
        public static void grovefight(InnerGroveSequence __instance)
        {
            ArchipelagoConsole.LogDebug("Spirit Mother");
            if (__instance.mapManager.SceneStartData.isReturningFromFight && GameManager.instance.GetActiveGameState().data.lastFightResult == FightManager.FightResult.HeroWon)
            {
                int battleidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Battle_Start"]);
                //case "Crimson Countess"://Artic Temple 2: Defeat Crimson Countess
                ArchipelagoConsole.LogDebug("Inner Grove: Defeat Spirit Mother");
                ArchipelagoClient.sendloc(battleidstart + 107);
                //break;
            }
        }

        /// <summary>
        /// send deathlink
        /// </summary>
        [HarmonyPatch(typeof(GameOverMenu), "Start")]
        [HarmonyPrefix]
        public static void death(GameOverMenu __instance)
        {
            if (HelperItems.save.isWildEncounter)
            {
                SpiritValleyArchipelago.ArchipelagoClient.DeathLinkHandler.SendDeathLink($"Beaten up by a wild {HelperItems.save.currentlyFightingEnemyMonster.baseStatsName}");
            }
            else
            {
                SpiritValleyArchipelago.ArchipelagoClient.DeathLinkHandler.SendDeathLink($"Defeated by {HelperItems.save.enemyNPCName.GetLocalizedString()}");
            }
        }
    }
}
