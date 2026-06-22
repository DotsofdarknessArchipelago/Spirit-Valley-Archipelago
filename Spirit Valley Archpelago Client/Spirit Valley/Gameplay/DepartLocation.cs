using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class DepartLocation
    {

        //starting ids for item catorgories saved so we dont need to retreve them every time
        public static int items_consumable_start = 0;
        public static int items_crystal_start = 0;
        public static int items_equipment_start = 0;
        public static int items_key_item_start = 0;
        public static int items_potion_start = 0;
        public static int items_coins_start = 0;
        public static int items_warp_id_start = 0;

        public static GameState save => GameManager.instance.gameStates[4 + SpiritValleyArchipelago.slot].data;

        /// <summary>
        /// process items recieved when moving locations
        /// </summary>
        [HarmonyPatch(typeof(SceneManager), "LoadScene", [typeof(string), typeof(LoadSceneMode)])]
        [HarmonyPrefix]
        public static void departlocation()
        {
            if (!ArchipelagoClient.Authenticated) { return; }

            //set starting ids for item catories if they are not already set
            if (items_consumable_start == 0) { items_consumable_start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_consumable_start"]); }
            if (items_crystal_start == 0) { items_crystal_start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_crystal_start"]); }
            if (items_equipment_start == 0) { items_equipment_start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_equipment_start"]); }
            if (items_key_item_start == 0) { items_key_item_start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_key_item_start"]); }
            if (items_potion_start == 0) { items_potion_start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_potion_start"]); }
            if (items_coins_start == 0) { items_coins_start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_coins_start"]); }
            if (items_warp_id_start == 0) { items_warp_id_start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_warp_id_start"]); }

            ArchipelagoConsole.LogDebug("<color=yellow>PROCESSING ITEMS</color>");
            foreach (ArchipelagoItem item in ArchipelagoClient.archlist.list)
            {
                if (item.processed) { continue; }
                if (items_consumable_start < item.Id && item.Id <= items_crystal_start)
                {
                    switch (item.Id - items_consumable_start)
                    {
                        case (1)://Antidote
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_Antidote"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Antidote</color> to Inventory");
                            item.processed = true;
                            break;
                        case (2)://Artic Cod
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_ArcticCod"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Artic Cod</color> to Inventory");
                            item.processed = true;
                            break;
                        case (3)://Candy Cane
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_CandyCane"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Candy Cane</color> to Inventory");
                            item.processed = true;
                            break;
                        case (4)://Chocolate Cake
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_ChocolateCake"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Chocolate Cake</color> to Inventory");
                            item.processed = true;
                            break;
                        case (5)://Chocolate Starfish
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_ChocolateStarfish"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Chocolate Starfish</color> to Inventory");
                            item.processed = true;
                            break;
                        case (6)://Cleansing Tonic
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_CleansingTonic"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Cleansing Tonic</color> to Inventory");
                            item.processed = true;
                            break;
                        case (7)://Cupcake
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_Cupcake"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Cupcake</color> to Inventory");
                            item.processed = true;
                            break;
                        case (8)://Donut
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_Donut"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Donut</color> to Inventory");
                            item.processed = true;
                            break;
                        case (9)://Elusive Scent
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_ElusiveScent"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Elusive Scent</color> to Inventory");
                            item.processed = true;
                            break;
                        case (10)://Evolution Charm
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_EvolutionCharm"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Evolution Charm</color> to Inventory");
                            item.processed = true;
                            break;
                        case (11)://Fallen Star
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_FallenStar"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Fallen Star</color> to Inventory");
                            item.processed = true;
                            break;
                        case (12)://Golden Seed of Life
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_GoldenSeedOfLife"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Golden Seed of Life</color> to Inventory");
                            item.processed = true;
                            break;
                        case (13)://Goldfish
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_GoldFish"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Goldfish</color> to Inventory");
                            item.processed = true;
                            break;
                        case (14)://Infinity Charm
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_InfinityCharm"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Infinity Charm</color> to Inventory");
                            item.processed = true;
                            break;
                        case (15)://Lollipop
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_Lollipop"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Lollipop</color> to Inventory");
                            item.processed = true;
                            break;
                        case (16)://Northern Blowfish
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_NorthernBlowfish"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Northern Blowfish</color> to Inventory");
                            item.processed = true;
                            break;
                        case (17)://Potent Scent
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_PotentScent"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Potent Scent</color> to Inventory");
                            item.processed = true;
                            break;
                        case (18)://Sea Cucumber
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_SeaCucumber"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Sea Cucumber</color> to Inventory");
                            item.processed = true;
                            break;
                        case (19)://Seed of Life
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_SeedOfLife"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Seed of Life</color> to Inventory");
                            item.processed = true;
                            break;
                        case (20)://Spirit Repellent
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_SpiritRepellent"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Spirit Repellent</color> to Inventory");
                            item.processed = true;
                            break;
                        case (21)://Strawberry cake
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_StrawberryCake"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Strawberry cake</color> to Inventory");
                            item.processed = true;
                            break;
                        case (22)://XP Boosters
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_XPBoosters"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>XP Boosters</color> to Inventory");
                            item.processed = true;
                            break;
                        default:
                            break;
                    }
                }
                else if (items_crystal_start < item.Id && item.Id <= items_equipment_start)
                {
                    switch (item.Id - items_crystal_start)
                    {
                        case (1)://Spirit Crystal
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Crystal_SpiritCrystal"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Spirit Crystal</color> to Inventory");
                            item.processed = true;
                            break;
                        case (2)://Spirit Crystal +1
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Crystal_SpiritCrystal+1"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Spirit Crystal +1</color> to Inventory");
                            item.processed = true;
                            break;
                        case (3)://Spirit Crystal +2
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Crystal_SpiritCrystal+2"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Spirit Crystal +2</color> to Inventory");
                            item.processed = true;
                            break;
                        default:
                            break;
                    }
                }
                else if (items_equipment_start < item.Id && item.Id <= items_key_item_start)
                {
                    switch (item.Id - items_equipment_start)
                    {
                        case (1)://Ball Gag
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_BallGag"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Ball Gag</color> to Inventory");
                            item.processed = true;
                            break;
                        case (2)://Ball Gag +1
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_BallGag+1"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Ball Gag +1</color> to Inventory");
                            item.processed = true;
                            break;
                        case (3)://Ball Gag +2
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_BallGag+2"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Ball Gag +2</color> to Inventory");
                            item.processed = true;
                            break;
                        case (4)://Butt Plug of Life
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_Butt PlugOfLife"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Butt Plug of Life</color> to Inventory");
                            item.processed = true;
                            break;
                        case (5)://Butt Plug of Life +1
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_Butt PlugOfLife+1"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Butt Plug of Life +1</color> to Inventory");
                            item.processed = true;
                            break;
                        case (6)://Butt Plug of Life +2
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_Butt PlugOfLife+2"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Butt Plug of Life +2</color> to Inventory");
                            item.processed = true;
                            break;
                        case (7)://Butt Plug of Power
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_ButtPlugOfPower"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Butt Plug of Power</color> to Inventory");
                            item.processed = true;
                            break;
                        case (8)://Butt Plug of Power +1
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_ButtPlugOfPower+1"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Butt Plug of Power +1</color> to Inventory");
                            item.processed = true;
                            break;
                        case (9)://Butt Plug of Power +2
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_ButtPlugOfPower+2"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Butt Plug of Power +2</color> to Inventory");
                            item.processed = true;
                            break;
                        case (10)://Butt Plug of Wisdom
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_ButtPlugOfWisdom"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Butt Plug of Wisdom</color> to Inventory");
                            item.processed = true;
                            break;
                        case (11)://Chastity Belt
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_ChastityBelt"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Chastity Belt</color> to Inventory");
                            item.processed = true;
                            break;
                        case (12)://Chastity Belt of Love
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_ChastityBeltOfLove"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Chastity Belt of Love</color> to Inventory");
                            item.processed = true;
                            break;
                        case (13)://Diamond Butt Plug
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_DiamondButtPlug"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Diamond Butt Plug</color> to Inventory");
                            item.processed = true;
                            break;
                        case (14)://Dragon Dildo
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_DragonDildo"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Dragon Dildo</color> to Inventory");
                            item.processed = true;
                            break;
                        case (15)://Dragon Dildo +1
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_DragonDildo+1"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Dragon Dildo +1</color> to Inventory");
                            item.processed = true;
                            break;
                        case (16)://Golden Butt Plug
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_GoldenButtPlug"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Golden Butt Plug</color> to Inventory");
                            item.processed = true;
                            break;
                        case (17)://Golden Chastity Belt
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_GoldenChastityBelt"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Golden Chastity Belt</color> to Inventory");
                            item.processed = true;
                            break;
                        case (18)://Icy Dildo
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_IcyDildo"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Icy Dildo</color> to Inventory");
                            item.processed = true;
                            break;
                        case (19)://Leather Collar
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_LeatherCollar"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Leather Collar</color> to Inventory");
                            item.processed = true;
                            break;
                        case (20)://Oceanic Choker
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_OceanicChoker"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Oceanic Choker</color> to Inventory");
                            item.processed = true;
                            break;
                        case (21)://Red Collar
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_RedCollar"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Red Collar</color> to Inventory");
                            item.processed = true;
                            break;
                        case (22)://Red Latex Mask
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_RedLatexMask"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Red Latex Mask</color> to Inventory");
                            item.processed = true;
                            break;
                        case (23)://Rubber Fist
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_RubberFist"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Rubber Fist</color> to Inventory");
                            item.processed = true;
                            break;
                        case (24)://Rubber Mask
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_RubberMask"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Rubber Mask</color> to Inventory");
                            item.processed = true;
                            break;
                        case (25)://Shark Tooth Dildo
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_SharkToothDildo"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Shark Tooth Dildo</color> to Inventory");
                            item.processed = true;
                            break;
                        case (26)://Small Dildo
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_SmallDildo"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Small Dildo</color> to Inventory");
                            item.processed = true;
                            break;
                        case (27)://Spiked Collar
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_SpikedCollar"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Spiked Collar</color> to Inventory");
                            item.processed = true;
                            break;
                        case (28)://Spiked Collar +1
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_SpikedCollar+1"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Spiked Collar +1</color> to Inventory");
                            item.processed = true;
                            break;
                        case (29)://Spiked Collar +2
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_SpikedCollar+2"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Spiked Collar +2</color> to Inventory");
                            item.processed = true;
                            break;
                        case (30)://Spiked Collar +3
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_SpikedCollar+3"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Spiked Collar +3</color> to Inventory");
                            item.processed = true;
                            break;
                        case (31)://Swift Plug
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_SwiftPlug"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Swift Plug</color> to Inventory");
                            item.processed = true;
                            break;
                        case (32)://Swift Plug +1
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_SwiftPlug+1"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Swift Plug +1</color> to Inventory");
                            item.processed = true;
                            break;
                        case (33)://The Ace of Spades
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_TheAceOfSpades"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>The Ace of Spades</color> to Inventory");
                            item.processed = true;
                            break;
                        case (34)://Turtle Shell Collar
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_TurtleShellCollar"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Turtle Shell Collar</color> to Inventory");
                            item.processed = true;
                            break;
                        case (35)://Unicorn Dildo
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_UnicornDildo"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Unicorn Dildo</color> to Inventory");
                            item.processed = true;
                            break;
                        case (36)://Vibrating Willy
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_VibratingWilly"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Vibrating Willy</color> to Inventory");
                            item.processed = true;
                            break;
                        case (37)://Vibrating Willy +1
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_VibratingWilly+1"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Vibrating Willy +1</color> to Inventory");
                            item.processed = true;
                            break;
                        case (38)://Whale Cock Dildo
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Equipment_WhaleCockDildo"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Whale Cock Dildo</color> to Inventory");
                            item.processed = true;
                            break;
                        default:
                            break;
                    }
                }
                else if (items_key_item_start < item.Id && item.Id <= items_potion_start)
                {
                    switch (item.Id - items_key_item_start)
                    {
                        case (1)://Ancient Temple Key
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_AncientTempleKey"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Ancient Temple Key</color> to Inventory");
                            item.processed = true;
                            break;
                        case (2)://Ass Lover Extreme issue 12
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_AssLoversExtremeIssue12"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Ass Lover Extreme issue 12</color> to Inventory");
                            item.processed = true;
                            break;
                        case (3)://Cock Shaped Key
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_CockShapedKey"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Cock Shaped Key</color> to Inventory");
                            item.processed = true;
                            break;
                        case (4)://Cracked Power Crystal
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_CrackedPowerCrystal"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Cracked Power Crystal</color> to Inventory");
                            item.processed = true;
                            break;
                        case (5)://Cum Rag
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_CumRag"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Cum Rag</color> to Inventory");
                            item.processed = true;
                            break;
                        case (6)://Dynamite
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_Dynamite"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Dynamite</color> to Inventory");
                            item.processed = true;
                            break;
                        case (7)://Fancy Suit
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_FancySuit"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Fancy Suit</color> to Inventory");
                            item.processed = true;
                            break;
                        case (8)://Fishing Rod
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_FishingRod"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Fishing Rod</color> to Inventory");
                            item.processed = true;
                            break;
                        case (9)://Fishy Scent
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_FishyScent"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Fishy Scent</color> to Inventory");
                            item.processed = true;
                            break;
                        case (10)://Power Crystal
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_PowerCrystal"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Power Crystal</color> to Inventory");
                            item.processed = true;
                            break;
                        case (11)://Practice Fishing Rod
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_PracticeFishingRod"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Practice Fishing Rod</color> to Inventory");
                            item.processed = true;
                            break;
                        case (12)://Raw Crystal Chunk
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_RawCrystalChunk"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Raw Crystal Chunk</color> to Inventory");
                            item.processed = true;
                            break;
                        case (13)://Red Harmony Crystal
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_RedHarmonyCrystal"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Red Harmony Crystal</color> to Inventory");
                            item.processed = true;
                            break;
                        case (14)://Spirit Handler License
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_SpiritHandlerLicense"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Spirit Handler License</color> to Inventory");
                            item.processed = true;
                            break;
                        case (15)://Stone Key
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_StoneKey"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Stone Key</color> to Inventory");
                            item.processed = true;
                            break;
                        case (16)://Super Secret Orders
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_SuperSecretOrders"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Super Secret Orders</color> to Inventory");
                            item.processed = true;
                            break;
                        case (17)://Testosterone Pills
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_TestosteronePills"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Testosterone Pills</color> to Inventory");
                            item.processed = true;
                            break;
                        case (18)://Video Cassette
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_VideoCasette"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Video Cassette</color> to Inventory");
                            item.processed = true;
                            break;
                        case (19)://Wedding Ring
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_WeddingRing"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Wedding Ring</color> to Inventory");
                            item.processed = true;
                            break;
                        case (20)://Yellow Harmony Crystal
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_YellowHarmonyCrystal"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Yellow Harmony Crystal</color> to Inventory");
                            item.processed = true;
                            break;
                        case (21)://Scent Mixture
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_ScentMixture"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Scent Mixture</color> to Inventory");
                            item.processed = true;
                            break;
                        default:
                            break;
                    }
                }
                else if (items_potion_start < item.Id && item.Id <= items_coins_start)
                {
                    switch (item.Id - items_potion_start)
                    {
                        case (1)://Vial of Health
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_VialOfHealth"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Vial of Health</color> to Inventory");
                            item.processed = true;
                            break;
                        case (2)://Healing Potion
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_HealingPotion"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Healing Potion</color> to Inventory");
                            item.processed = true;
                            break;
                        case (3)://Greater Healing Potion
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_GreaterHealingPotion"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Greater Healing Potion</color> to Inventory");
                            item.processed = true;
                            break;
                        case (4)://Vial of Stamina
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_VialOfStamina"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Vial of Stamina</color> to Inventory");
                            item.processed = true;
                            break;
                        case (5)://Stamina Potion
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_StaminaPotion"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Stamina Potion</color> to Inventory");
                            item.processed = true;
                            break;
                        case (6)://Greater Stamina Potion
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_GreaterStaminaPotion"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Greater Stamina Potion</color> to Inventory");
                            item.processed = true;
                            break;
                        case (7)://Vial of Rejuvenation
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_VialOfRejuvenation"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Vial of Rejuvenation</color> to Inventory");
                            item.processed = true;
                            break;
                        case (8)://Rejuvenation Potion
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_RejuvenationPotion"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Rejuvenation Potion</color> to Inventory");
                            item.processed = true;
                            break;
                        case (9)://Greater Rejuvenation Potion
                            save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_GreaterRejuvenationPotion"), 1, true);
                            ArchipelagoConsole.LogMessage("Added <color=cyan>Greater Rejuvenation Potion</color> to Inventory");
                            item.processed = true;
                            break;
                        default:
                            break;
                    }
                }
                else if (items_coins_start < item.Id && item.Id <= items_warp_id_start)
                {
                    switch (item.Id - items_coins_start)
                    {
                        case (1)://15 coins
                            save.ModifyMoney(15);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>15 coins</color>");
                            item.processed = true;
                            break;
                        case (2)://20 coins
                            save.ModifyMoney(20);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>20 coins</color>");
                            item.processed = true;
                            break;
                        case (3)://25 coins
                            save.ModifyMoney(25);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>25 coins</color>");
                            item.processed = true;
                            break;
                        case (4)://30 coins
                            save.ModifyMoney(30);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>30 coins</color>");
                            item.processed = true;
                            break;
                        case (5)://35 coins
                            save.ModifyMoney(35);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>35 coins</color>");
                            item.processed = true;
                            break;
                        case (6)://50 coins
                            save.ModifyMoney(50);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>50 coins</color>");
                            item.processed = true;
                            break;
                        case (7)://75 coins
                            save.ModifyMoney(75);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>75 coins</color>");
                            item.processed = true;
                            break;
                        case (8)://100 coins
                            save.ModifyMoney(100);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>100 coins</color>");
                            item.processed = true;
                            break;
                        case (9)://150 coins
                            save.ModifyMoney(150);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>150 coins</color>");
                            item.processed = true;
                            break;
                        case (10)://200 coins
                            save.ModifyMoney(200);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>200 coins</color>");
                            item.processed = true;
                            break;
                        case (11)://300 coins
                            save.ModifyMoney(300);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>300 coins</color>");
                            item.processed = true;
                            break;
                        case (12)://500 coins
                            save.ModifyMoney(500);
                            ArchipelagoConsole.LogMessage("Obtained <color=yellow>500 coins</color>");
                            item.processed = true;
                            break;
                        default:
                            break;
                    }
                }
                else if (items_warp_id_start < item.Id)
                {
                    switch (item.Id - items_warp_id_start)
                    {
                        case (1)://OakwoodVillage
                            save.GetWayStoneState("OakwoodVillage").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Oakwood Village Waystone point</color>");
                            item.processed = true;
                            break;
                        case (2)://Greensvale
                            save.GetWayStoneState("Greensvale").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Greensvale Waystone point</color>");
                            item.processed = true;
                            break;
                        case (3)://Trail4
                            save.GetWayStoneState("Trail4").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Trail 04 Waystone point</color>");
                            item.processed = true;
                            break;
                        case (4)://DairyFarm
                            save.GetWayStoneState("DairyFarm").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Dairy Farm Waystone point</color>");
                            item.processed = true;
                            break;
                        case (5)://TumbleweedTown
                            save.GetWayStoneState("TumbleweedTown").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Tumbleweed Town Waystone point</color>");
                            item.processed = true;
                            break;
                        case (6)://CrashSite
                            save.GetWayStoneState("CrashSite").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Crash Site Waystone point</color>");
                            item.processed = true;
                            break;
                        case (7)://CoconutVillage
                            save.GetWayStoneState("CoconutVillage").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Coconut Village Waystone point</color>");
                            item.processed = true;
                            break;
                        case (8)://Trail14
                            save.GetWayStoneState("Trail14").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Trail 14 Waystone point</color>");
                            item.processed = true;
                            break;
                        case (9)://ColdHarbor
                            save.GetWayStoneState("ColdHarbor").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Cold Harbor Waystone point</color>");
                            item.processed = true;
                            break;
                        case (10)://Frostville1
                            save.GetWayStoneState("Frostville1").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Frostville Waystone point</color>");
                            item.processed = true;
                            break;
                        case (11)://AbandonedMine
                            save.GetWayStoneState("AbandonedMine").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Abandoned Mine Waystone point</color>");
                            item.processed = true;
                            break;
                        case (12)://Trail18
                            save.GetWayStoneState("Trail18").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Trail 18 Waystone point</color>");
                            item.processed = true;
                            break;
                        case (13)://Trail19
                            save.GetWayStoneState("Trail19").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Trail 19 Waystone point</color>");
                            item.processed = true;
                            break;
                        case (14)://Trail22
                            save.GetWayStoneState("Trail22").isActive = true;
                            save.isFastTravelUnlocked = true;
                            ArchipelagoConsole.LogMessage("Unlocked <color=cyan>Trail 22 Waystone point</color>");
                            item.processed = true;
                            break;
                        default:
                            break;
                    }
                }
            }

            switch (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["goal"]))
            {
                case 0: //missions
                    if (save.GetActiveMainQuestState() == null) break;
                    if (save.GetActiveMainQuestState().id == "main_quest_55_life_as_a_spirit_warden") ArchipelagoClient.complete();
                    break;
                case 1: //catch all spirits
                    if (save.database.GetCountCaptured() == 75) ArchipelagoClient.complete();
                    break;
                case 2: //catch all rare spirits
                    if (save.database.GetCountRaresCaptured() == 75) ArchipelagoClient.complete();
                    break;
                case 3: //affection

                    int affectionidstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Spirit_Affection_Start"]);
                    bool goal = true;
                    for (int i = 0; i < 75; i++)
                    {
                        if (!ArchipelagoClient.session.Locations.AllLocationsChecked.Contains(affectionidstart + (i * 5) + 5)) { goal = false; break; }
                    }
                    if (goal)
                    {
                        ArchipelagoClient.complete();
                    }
                    break;
            }
        }
    }
}
