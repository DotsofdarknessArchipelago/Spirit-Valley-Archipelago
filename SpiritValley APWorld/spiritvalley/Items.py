from BaseClasses import Item


class spiritItem(Item):
    game = "Spirit Valley"

items_consumable_id_start = 0
items_consumable = {
    "Antidote": items_consumable_id_start + 1,
    "Arctic Cod": items_consumable_id_start + 2,
    "Candy cane": items_consumable_id_start + 3,
    "Chocolate cake": items_consumable_id_start + 4,
    "Chocolate Starfish": items_consumable_id_start + 5,
    "Cleansing Tonic": items_consumable_id_start + 6,
    "Cupcake": items_consumable_id_start + 7,
    "Donut": items_consumable_id_start + 8,
    "Elusive Scent": items_consumable_id_start + 9,
    "Evolution Charm": items_consumable_id_start + 10,
    "Fallen Star": items_consumable_id_start + 11,
    "Golden Seed of Life": items_consumable_id_start + 12,
    "Goldfish": items_consumable_id_start + 13,
    "Infinity Charm": items_consumable_id_start + 14,
    "Lollipop": items_consumable_id_start + 15,
    "Northern Blowfish": items_consumable_id_start + 16,
    "Potent Scent": items_consumable_id_start + 17,
    "Sea Cucumber": items_consumable_id_start + 18,
    "Seed of Life": items_consumable_id_start + 19,
    "Spirit Repellent": items_consumable_id_start + 20,
    "Strawberry cake": items_consumable_id_start + 21,
    "XP Boosters": items_consumable_id_start + 22,
}

items_crystal_id_start = items_consumable_id_start + 22
items_crystal = {
    "Spirit Crystal": items_crystal_id_start + 1, #12
    "Spirit Crystal +1": items_crystal_id_start + 2, #30
    "Spirit Crystal +2": items_crystal_id_start + 3, #35
}

items_equipment_id_start = items_crystal_id_start + 3
items_equipment = {
    "Ball Gag": items_equipment_id_start + 1,
    "Ball Gag +1": items_equipment_id_start + 2,
    "Ball Gag +2": items_equipment_id_start + 3,
    "Butt Plug of Life": items_equipment_id_start + 4,
    "Butt Plug of Life +1": items_equipment_id_start + 5,
    "Butt Plug of Life +2": items_equipment_id_start + 6,
    "Butt Plug of Power": items_equipment_id_start + 7,
    "Butt Plug of Power +1": items_equipment_id_start + 8,
    "Butt Plug of Power +2": items_equipment_id_start + 9,
    "Butt Plug of Wisdom": items_equipment_id_start + 10,
    "Chastity Belt": items_equipment_id_start + 11,
    "Chastity Belt of Love": items_equipment_id_start + 12,
    "Diamond Butt Plug": items_equipment_id_start + 13,
    "Dragon Dildo": items_equipment_id_start + 14,
    "Dragon Dildo +1": items_equipment_id_start + 15,
    "Golden Butt Plug": items_equipment_id_start + 16,
    "Golden Chastity Belt": items_equipment_id_start + 17,
    "Icy Dildo": items_equipment_id_start + 18,
    "Leather Collar": items_equipment_id_start + 19,
    "Oceanic Choker": items_equipment_id_start + 20,
    "Red Collar": items_equipment_id_start + 21,
    "Red Latex Mask": items_equipment_id_start + 22,
    "Rubber Fist": items_equipment_id_start + 23,
    "Rubber Mask": items_equipment_id_start + 24,
    "Shark Tooth Dildo": items_equipment_id_start + 25,
    "Small Dildo": items_equipment_id_start + 26,
    "Spiked Collar": items_equipment_id_start + 27,
    "Spiked Collar +1": items_equipment_id_start + 28,
    "Spiked Collar +2": items_equipment_id_start + 29,
    "Spiked Collar +3": items_equipment_id_start + 30,
    "Swift Plug": items_equipment_id_start + 31,
    "Swift Plug +1": items_equipment_id_start + 32,
    "The Ace of Spades": items_equipment_id_start + 33,
    "Turtle Shell Collar": items_equipment_id_start + 34,
    "Unicorn Dildo": items_equipment_id_start + 35,
    "Vibrating Willy": items_equipment_id_start + 36,
    "Vibrating Willy +1": items_equipment_id_start + 37,
    "Whale Cock Dildo": items_equipment_id_start + 38,
}

items_key_item_id_start = items_equipment_id_start + 38
items_key_item = {
    "Ancient Temple Key": items_key_item_id_start + 1,
    "Ass Lover Extreme issue 12": items_key_item_id_start + 2,
    "Cock Shaped Key": items_key_item_id_start + 3,
    "Cracked Power Crystal": items_key_item_id_start + 4,
    "Cum Rag": items_key_item_id_start + 5,
    "Dynamite": items_key_item_id_start + 6,
    "Fancy Suit": items_key_item_id_start + 7,
    "Fishing Rod": items_key_item_id_start + 8,
    "Fishy Scent": items_key_item_id_start + 9,
    "Power Crystal": items_key_item_id_start + 10,
    "Practice Fishing Rod": items_key_item_id_start + 11,
    "Raw Crystal Chunk": items_key_item_id_start + 12,
    "Red Harmony Crystal": items_key_item_id_start + 13,
    "Spirit Handler License": items_key_item_id_start + 14,
    "Stone Key": items_key_item_id_start + 15,
    "Super Secret Orders": items_key_item_id_start + 16,
    "Testosterone Pills": items_key_item_id_start + 17,
    "Video Cassette": items_key_item_id_start + 18,
    "Wedding Ring": items_key_item_id_start + 19,
    "Yellow Harmony Crystal": items_key_item_id_start + 20,
    "Scent Mixture": items_key_item_id_start + 21,
}

items_potion_id_start = items_key_item_id_start + 21
items_potion = {
    "Vial of Health": items_potion_id_start + 1,
    "Healing Potion": items_potion_id_start + 2,
    "Greater Healing Potion": items_potion_id_start + 3,
    "Vial of Stamina": items_potion_id_start + 4,
    "Stamina Potion": items_potion_id_start + 5,
    "Greater Stamina Potion": items_potion_id_start + 6,
    "Vial of Rejuvenation": items_potion_id_start + 7,
    "Rejuvenation Potion": items_potion_id_start + 8,
    "Greater Rejuvenation Potion": items_potion_id_start + 9,
}

items_coins_id_start = items_potion_id_start + 9
items_coins = {
    "15 Coins": items_coins_id_start + 1,
    "20 Coins": items_coins_id_start + 2,
    "25 Coins": items_coins_id_start + 3,
    "30 Coins": items_coins_id_start + 4,
    "35 Coins": items_coins_id_start + 5,
    "50 Coins": items_coins_id_start + 6,
    "75 Coins": items_coins_id_start + 7,
    "100 Coins": items_coins_id_start + 8,
    "150 Coins": items_coins_id_start + 9,
    "200 Coins": items_coins_id_start + 10,
    "300 Coins": items_coins_id_start + 11,
    "500 Coins": items_coins_id_start + 12,
}

items_archipelago_id_start = items_coins_id_start+12
items_archipelago = {
    "Spirit Crystal Available in Shop": items_archipelago_id_start + 1,
    "Spirit Crystal +1 Available in Shop": items_archipelago_id_start + 2,
    "Spirit Crystal +2 Available in Shop": items_archipelago_id_start + 3,
    "Health Potion's Available in Shop": items_archipelago_id_start + 4,
    "Stamina Potion's Available in Shop": items_archipelago_id_start + 5,
    "Rejuvenation Potion's Available in Shop": items_archipelago_id_start + 6,
    "Seed of Life Available in Shop": items_archipelago_id_start + 7,
    "Golden Seed of Life Available in Shop": items_archipelago_id_start + 8,
    "Donut Available in Shop": items_archipelago_id_start + 9,
    "Cupcake Available in Shop": items_archipelago_id_start + 10,
    "Lollipop Available in Shop": items_archipelago_id_start + 11,
    "Candy cane Available in Shop": items_archipelago_id_start + 12,
    "Strawberry cake Available in Shop": items_archipelago_id_start + 13,
    "Chocolate cake Available in Shop": items_archipelago_id_start + 14,
    "Goldfish Available in Shop": items_archipelago_id_start + 15,
    "Chocolate Starfish Available in Shop": items_archipelago_id_start + 16,
    "Arctic Cod Available in Shop": items_archipelago_id_start + 17,
    "Northern Blowfish Available in Shop": items_archipelago_id_start + 18,
    "Sea Cucumber Available in Shop": items_archipelago_id_start + 19,
    "Elusive Scent Available in Shop": items_archipelago_id_start + 20,
    "Potent Scent Available in Shop": items_archipelago_id_start + 21,
    "Spirit Repellent Available in Shop": items_archipelago_id_start + 22,
    "Xp Booster Available in Shop": items_archipelago_id_start + 23,
    "Cleansing Tonic Available in Shop": items_archipelago_id_start + 24,
}

items_warp_id_start = items_archipelago_id_start+24
items_warp = {
    "Warp Cords(Oakwood Village)": items_warp_id_start + 1,
    "Warp Cords(Greensvale)": items_warp_id_start + 2,
    "Warp Cords(Trail 04)": items_warp_id_start + 3,
    "Warp Cords(Dairy Farm)": items_warp_id_start + 4,
    "Warp Cords(Tumbleweed Town)": items_warp_id_start + 5,
    "Warp Cords(Crash Site)": items_warp_id_start + 6,
    "Warp Cords(Coconut Village)": items_warp_id_start + 7,
    "Warp Cords(Trail 14)": items_warp_id_start + 8,
    "Warp Cords(Cold Harbour)": items_warp_id_start + 9,
    "Warp Cords(Frostville)": items_warp_id_start + 10,
    "Warp Cords(Abandoned Mine)": items_warp_id_start + 11,
    "Warp Cords(Trail 18)": items_warp_id_start + 12,
    "Warp Cords(Trail 19)": items_warp_id_start + 13,
    "Warp Cords(Trail 22)": items_warp_id_start + 14,
}

item_list_id_start = items_warp_id_start+14
items_list = {
    **items_potion,
    **items_consumable,
    **items_crystal,
    **items_equipment,
    **items_key_item,
    **items_coins,
    **items_archipelago,
    **items_warp,
    "victory": item_list_id_start+1
}

affection_items = [
    "Donut",#+300
    "Cupcake",#+200
    "Lollipop",#+100
    "Candy cane",#+sex
    "Strawberry cake",#+500
    "Chocolate cake",#+750
    "Goldfish",#+30
    "Chocolate Starfish",#+50
    "Arctic Cod",#+100
    "Northern Blowfish",#+125
    "Sea Cucumber",#+75
]

affection_shop_items = [
    "Donut Available in Shop",
    "Cupcake Available in Shop",
    "Lollipop Available in Shop",
    "Candy cane Available in Shop",
    "Strawberry cake Available in Shop",
    "Chocolate cake Available in Shop",
    "Goldfish Available in Shop",
    "Chocolate Starfish Available in Shop",
    "Arctic Cod Available in Shop",
    "Northern Blowfish Available in Shop",
    "Sea Cucumber Available in Shop",
]

spirit_crystal_shop_items = [
    "Spirit Crystal Available in Shop",
    "Spirit Crystal +1 Available in Shop",
    "Spirit Crystal +2 Available in Shop",
]

useful_items_list = [
    "Butt Plug of Wisdom",
    "Spirit Crystal",
    "Spirit Crystal +1",
    "Spirit Crystal +2",
    *items_archipelago,
    *items_warp,
]

filler_item = [
    *items_consumable,
    *items_crystal,
    *items_equipment,
    *items_potion,
    *items_coins,
]