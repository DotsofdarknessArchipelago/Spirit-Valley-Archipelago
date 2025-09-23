import random
from typing import Mapping, Any

from BaseClasses import Region, ItemClassification, Item
from Utils import visualize_regions
from worlds.AutoWorld import World
from .Data_Maps import water_location_list, grass_location_list, default_grass_locations, default_water_locations
from .Data_Spirits import spirit_list, types, attacking_moves, all_moves, rand_grass_spawn, rand_water_spawn, rand_spirit_list, rand_type_chart, default_type_effective
from .Data_Trainers import Trainer, rand_trainer, Default_Trainers
from .Items import items_list, spiritItem, items_key_item, useful_items_list, items_potion, items_consumable, items_crystal, items_equipment, items_coins, items_consumable_id_start, items_crystal_id_start, items_equipment_id_start, items_key_item_id_start, items_potion_id_start, items_coins_id_start, items_archipelago, items_warp, items_archipelago_id_start, items_warp_id_start
from .Locations import SpiritValleyLocation, location_list, Rare_spirit_locations, spirit_id_start, spirit_affection_id_start, Rare_spirit_id_start, main_quests_id_start, side_quests_id_start, battle_locations_id_start, chest_locations_id_start, spirit_locations, spirit_affection_locations, main_quests, side_quests, battle_locations, chest_locations, warp_locations, warp_locations_id_start
from .Options import SpiritValleyOptions
from .Regions import Generate_Map
from .Rules import set_rules


class SpiritValley(World):
    game = "Spirit Valley"
    worldversion_major = 0
    worldversion_minor = 1
    worldversion_build = 0

    item_name_to_id = items_list
    location_name_to_id = location_list

    numitems = 0
    numlocations = 0

    options_dataclass = SpiritValleyOptions
    options: SpiritValleyOptions

    data = {}

    def generate_early(self):
        self.data = {}
        self.numitems = 0
        self.numlocations = 0

        if self.options.Randomise_Spawns.value:
            self.data["Grass_spawn"] = rand_grass_spawn(self.options.Grass_slots.value)
            self.data["Water_spawn"] = rand_water_spawn(self.options.Water_slots.value)
        else:
            self.data["Grass_spawn"] = default_grass_locations.copy()
            self.data["Water_spawn"] = default_water_locations.copy()

        self.data["SPIRITS"] = rand_spirit_list(self.options.Randomise_Spirit_Moves.value, self.options.Randomise_Spirit_Moves_Amount.value, self.options.Randomise_Spirit_Evo.value, self.options.Randomise_Spirit_Type.value, self.options.Randomise_Spirit_Stats.value)

        if self.options.Randomise_Type_Effective.value:
            self.data["TYPES"] = rand_type_chart()
        else:
            self.data["TYPES"] = default_type_effective.copy()

        self.data["ENEMIES"] = rand_trainer(self.options.Randomise_Enemies.value)

        self.data["MAIN_QUEST_TOTAL_DOMINATION"] = random.choice(self.data["Grass_spawn"]["Cave of Torment"])

        self.data["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"] = random.choice(self.data["Grass_spawn"]["Trail 01"])
        self.data["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"] = random.choice(self.data["Grass_spawn"]["Milly's Farm"])
        self.data["SIDE_QUEST_DEADLY_WATERS_SPIRIT"] = random.choice(self.data["Water_spawn"]["Trail 11"])
        self.data["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"] = random.choice(self.data["Grass_spawn"]["Trail 12"])
        self.data["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"] = random.choice(self.data["Grass_spawn"]["Trail 15"])
        self.data["SIDE_QUEST_CENTIBOOB_1_SPIRIT"] = random.choice(self.data["Grass_spawn"]["Trail 22"])
        self.data["SIDE_QUEST_CENTIBOOB_2_SPIRIT"] = random.choice(self.data["Grass_spawn"]["Trail 22"])
        self.data["SIDE_QUEST_CENTIBOOB_3_SPIRIT"] = random.choice(self.data["Grass_spawn"]["Trail 22"])

        if self.options.Spirit_Locations.value:
            self.numlocations += len(spirit_locations)
        if self.options.Spirit_Affection.value:
            self.numlocations += len(spirit_affection_locations)
        if self.options.Rare_Locations.value and self.options.Spirit_Locations.value:
            self.numlocations += len(Rare_spirit_locations)
        if True:
            self.numlocations += len(main_quests)
        if True:
            self.numlocations += len(side_quests)
        if True:
            self.numlocations += len(battle_locations)
        if True:
            self.numlocations += len(chest_locations)
        if True:
            self.numlocations += len(warp_locations)
        self.numitems = self.numlocations


    def create_regions(self):
        Generate_Map(self.multiworld,self.player,self.options,self.location_name_to_id,self.data)

    def create_item(self, name: str) -> "Item":
        if name in {**items_key_item, **items_archipelago, **items_warp, "Goldfish":self.item_name_to_id["Goldfish"], "Northern Blowfish":self.item_name_to_id["Northern Blowfish"], "victory":self.item_name_to_id["victory"]}:
            return spiritItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)
        if name in useful_items_list:
            return spiritItem(name, ItemClassification.useful, self.item_name_to_id[name], self.player)

        return spiritItem(name, ItemClassification.filler, self.item_name_to_id[name], self.player)

    def create_items(self):
        self.multiworld.get_location("Complete Main Quest: Battle for Spirit Valley", self.player).place_locked_item(self.create_item("victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("victory", self.player)

        filleritems = self.numlocations - len(items_key_item) - len(items_archipelago) - 1
        if not self.options.Rare_Locations.value:
            filleritems =filleritems- len(Rare_spirit_locations)
        if self.options.randomise_warps.value:
            filleritems =filleritems- len(items_warp)

        for i in items_key_item:
            self.multiworld.itempool.append(self.create_item(i))
        for i in items_archipelago:
            self.multiworld.itempool.append(self.create_item(i))
        if self.options.randomise_warps.value:
            for i in items_warp:
                self.multiworld.itempool.append(self.create_item(i))

        filleritemlist = list({**items_potion, **items_consumable, **items_crystal, **items_equipment, **items_coins, }.keys())

        for x in range(filleritems):
            self.multiworld.itempool.append(self.create_item(random.choice(filleritemlist)))

    def set_rules(self):
        set_rules(self.multiworld, self.player, self.options, self.data)
        visualize_regions(self.multiworld.get_region("Oakwood Village", self.player), "spiritvalley.puml", show_entrance_names=True)

    def fill_slot_data(self) -> Mapping[str, Any]:
        outdict = {
            **self.data,

            "Spirit_Id_Start":spirit_id_start,
            "Spirit_Affection_Start":spirit_affection_id_start,
            "Spirit_Rare_Start":Rare_spirit_id_start,
            "Main_Quest_Start":main_quests_id_start,
            "Side_Quest_Start":side_quests_id_start,
            "Battle_Start":battle_locations_id_start,
            "Chest_Start":chest_locations_id_start,
            "warp_locations":warp_locations_id_start,

            "items_consumable_start":items_consumable_id_start,
            "items_crystal_start":items_crystal_id_start,
            "items_equipment_start":items_equipment_id_start,
            "items_key_item_start":items_key_item_id_start,
            "items_potion_start":items_potion_id_start,
            "items_coins_start":items_coins_id_start,
            "items_archipelago_id_start":items_archipelago_id_start,
            "items_warp_id_start":items_warp_id_start,

            "randomise_warps":self.options.randomise_warps.value,
            "Spirit_Locations":self.options.Spirit_Locations.value,
            "Rare_Locations":self.options.Rare_Locations.value,
            "Minigame_Cheat":self.options.Minigame_Cheat.value,
            "Catch_Cheat":self.options.Guaranteed_Catch.value,

            "world_version_major": self.worldversion_major,
            "world_version_minor": self.worldversion_minor,
            "world_version_build": self.worldversion_build,
            "total_locations": self.numlocations,
            "total_items": self.numitems,
        }
        return outdict
