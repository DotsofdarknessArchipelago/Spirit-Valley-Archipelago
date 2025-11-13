from typing import Mapping, Any

from BaseClasses import ItemClassification, Item
from Utils import visualize_regions
from entrance_rando import randomize_entrances
from worlds.AutoWorld import World
from worlds.generic.Rules import set_rule
from worlds.spiritvalley.Data_Regions import regions, mapid_to_text
from worlds.spiritvalley.Data_Spirits import spirit_list, types, attacking_moves, all_moves, rand_grass_spawn, rand_water_spawn, rand_spirit_list, rand_type_chart, default_type_effective, default_grass_loc, default_water_loc, rand_move_data, move_data
from worlds.spiritvalley.Data_Trainers import Trainer, rand_trainer, Default_Trainers
from worlds.spiritvalley.Items import items_list, spiritItem, items_key_item, useful_items_list, items_potion, items_consumable, items_crystal, items_equipment, items_coins, items_consumable_id_start, items_crystal_id_start, items_equipment_id_start, items_key_item_id_start, items_potion_id_start, items_coins_id_start, items_archipelago, items_warp, items_archipelago_id_start, items_warp_id_start
from worlds.spiritvalley.Locations import SpiritValleyLocation, location_list, Rare_spirit_locations, spirit_id_start, spirit_affection_id_start, Rare_spirit_id_start, main_quests_id_start, side_quests_id_start, battle_locations_id_start, chest_locations_id_start, spirit_locations, spirit_affection_locations, main_quests, side_quests, battle_locations, chest_locations, warp_locations, warp_locations_id_start
from worlds.spiritvalley.Options import SpiritValleyOptions
from worlds.spiritvalley.Regions import Generate_Map
from worlds.spiritvalley.Rules import rules_normal, rules_map_rando


class SpiritValley(World):
    game = "Spirit Valley"
    worldversion_major = 0
    worldversion_minor = 4
    worldversion_build = 0

    item_name_to_id = items_list
    location_name_to_id = location_list

    numitems = 0
    numlocations = 0

    options_dataclass = SpiritValleyOptions
    options: SpiritValleyOptions

    data = {}
    randolist = []

    def generate_early(self):
        self.randolist = []
        self.data = {}
        self.numitems = 0
        self.numlocations = 0

        if self.options.Char_Gender.value == 0 and self.options.Char_Hairstyle.value == 4:
            self.options.Char_Hairstyle.value = 3

        if self.options.Randomise_Spawns.value:
            self.data["Grass_spawn"] = rand_grass_spawn(self.options.Grass_slots.value, self.random)
            self.data["Water_spawn"] = rand_water_spawn(self.options.Water_slots.value, self.random)
        else:
            self.data["Grass_spawn"] = default_grass_loc.copy()
            self.data["Water_spawn"] = default_water_loc.copy()

        self.data["SPIRITS"] = rand_spirit_list(self.options.Randomise_Spirit_Moves.value, self.options.Randomise_Spirit_Moves_Amount.value, self.options.Randomise_Spirit_Evo.value, self.options.Randomise_Spirit_Type.value, self.options.Randomise_Spirit_Stats.value, self.random)

        if self.options.Randomise_Move_Data.value:
            self.data["MOVES"] = rand_move_data(self.random)
        else:
            self.data["MOVES"] = move_data.copy()

        if self.options.Randomise_Type_Effective.value:
            self.data["TYPES"] = rand_type_chart(self.random)
        else:
            self.data["TYPES"] = default_type_effective.copy()

        self.data["ENEMIES"] = rand_trainer(self.options.Randomise_Enemies.value, self.random)

        self.data["MAIN_QUEST_TOTAL_DOMINATION"] = self.random.choice(self.data["Grass_spawn"]["CaveOfTorment"])

        self.data["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"] = self.random.choice(self.data["Grass_spawn"]["Trail1"])
        self.data["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"] = self.random.choice(self.data["Grass_spawn"]["MillysFarm"])
        self.data["SIDE_QUEST_DEADLY_WATERS_SPIRIT"] = self.random.choice(self.data["Water_spawn"]["Trail11"])
        self.data["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"] = self.random.choice(self.data["Grass_spawn"]["Trail12"])
        self.data["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"] = self.random.choice(self.data["Grass_spawn"]["Trail15"])
        self.data["SIDE_QUEST_CENTIBOOB_1_SPIRIT"] = self.random.choice(self.data["Grass_spawn"]["Trail22"])
        self.data["SIDE_QUEST_CENTIBOOB_2_SPIRIT"] = self.random.choice(self.data["Grass_spawn"]["Trail22"])
        self.data["SIDE_QUEST_CENTIBOOB_3_SPIRIT"] = self.random.choice(self.data["Grass_spawn"]["Trail22"])

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
        Generate_Map(self.multiworld, self.player, self.options, self.location_name_to_id, self.data)

    def connect_entrances(self):
        is_ut = getattr(self.multiworld, "generation_is_fake", False)
        if is_ut: return

        if self.options.randomise_map.value:
            if self.options.randomise_map_option.value == 1:
                TGL = {
                    0: [0],
                    1: [2],
                    2: [1]
                }
            else:
                TGL = {
                    0: [0, 1, 2],
                    1: [0, 1, 2],
                    2: [0, 1, 2]
                }
            self.data["RANDO"] = randomize_entrances(self, True, TGL).pairings
            hello = ""

        visualize_regions(self.multiworld.get_region("Menu", self.player), "spiritvalley.puml", show_entrance_names=True)

    def create_item(self, name: str) -> "Item":
        if name in {**items_key_item, **items_archipelago, **items_warp, "Goldfish": self.item_name_to_id["Goldfish"], "Northern Blowfish": self.item_name_to_id["Northern Blowfish"], "victory": self.item_name_to_id["victory"]}:
            return spiritItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)
        if name in useful_items_list:
            return spiritItem(name, ItemClassification.useful, self.item_name_to_id[name], self.player)

        return spiritItem(name, ItemClassification.filler, self.item_name_to_id[name], self.player)

    def create_items(self):
        self.multiworld.get_location("Complete Main Quest: Battle for Spirit Valley", self.player).place_locked_item(self.create_item("victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("victory", self.player)

        filleritems = self.numlocations - len(items_key_item) - len(items_archipelago) - 1
        if not self.options.Rare_Locations.value:
            filleritems = filleritems - len(Rare_spirit_locations)
        if self.options.randomise_warps.value:
            filleritems = filleritems - len(items_warp)

        for i in items_key_item:
            self.multiworld.itempool.append(self.create_item(i))
        for i in items_archipelago:
            self.multiworld.itempool.append(self.create_item(i))
        if self.options.randomise_warps.value:
            for i in items_warp:
                self.multiworld.itempool.append(self.create_item(i))

        filleritemlist = list({**items_potion, **items_consumable, **items_crystal, **items_equipment, **items_coins, }.keys())

        for x in range(filleritems):
            self.multiworld.itempool.append(self.create_item(self.random.choice(filleritemlist)))

    def set_rules(self):
        if self.options.randomise_map.value:
            rules_map_rando(self.multiworld, self.player, self.options, self.data)
        else:
            rules_normal(self.multiworld, self.player, self.options, self.data)

    def interpret_slot_data(self, slot_data: dict[str, Any]) -> None:
        self.data["Grass_spawn"] = slot_data["Grass_spawn"]
        self.data["Water_spawn"] = slot_data["Water_spawn"]
        self.data["SPIRITS"] = slot_data["SPIRITS"]
        self.data["MOVES"] = slot_data["MOVES"]
        self.data["TYPES"] = slot_data["TYPES"]
        self.data["ENEMIES"] = slot_data["ENEMIES"]
        self.data["MAIN_QUEST_TOTAL_DOMINATION"] = slot_data["MAIN_QUEST_TOTAL_DOMINATION"]
        self.data["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"] = slot_data["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"]
        self.data["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"] = slot_data["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"]
        self.data["SIDE_QUEST_DEADLY_WATERS_SPIRIT"] = slot_data["SIDE_QUEST_DEADLY_WATERS_SPIRIT"]
        self.data["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"] = slot_data["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"]
        self.data["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"] = slot_data["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"]
        self.data["SIDE_QUEST_CENTIBOOB_1_SPIRIT"] = slot_data["SIDE_QUEST_CENTIBOOB_1_SPIRIT"]
        self.data["SIDE_QUEST_CENTIBOOB_2_SPIRIT"] = slot_data["SIDE_QUEST_CENTIBOOB_2_SPIRIT"]
        self.data["SIDE_QUEST_CENTIBOOB_3_SPIRIT"] = slot_data["SIDE_QUEST_CENTIBOOB_3_SPIRIT"]

        if slot_data["randomise_map"]:
            self.connectUTentrencerando(slot_data["RANDO"])

        for r in regions:
            map = self.multiworld.get_region(r.map_id, self.player)
            if r.grass:
                if r.map_id == "Trail16_Top":
                    for s in self.data["Grass_spawn"]["Trail16"]:
                        map.add_locations({f"{mapid_to_text[r.map_id]} {s} Grass": None}, SpiritValleyLocation)
                        self.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", self.player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, self.player))
                elif r.map_id == "Trail20_Right":
                    for s in self.data["Grass_spawn"]["Trail20"]:
                        map.add_locations({f"{mapid_to_text[r.map_id]} {s} Grass": None}, SpiritValleyLocation)
                        self.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", self.player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, self.player))
                else:
                    for s in self.data["Grass_spawn"][r.map_id]:
                        map.add_locations({f"{mapid_to_text[r.map_id]} {s} Grass": None}, SpiritValleyLocation)
                        self.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", self.player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, self.player))
                        if r.map_id == "Trail16_Cave":
                            set_rule(self.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", self.player), lambda state: state.has("Fishy Scent", self.player))
                        if r.map_id == "Trail22_Cave":
                            set_rule(self.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", self.player), lambda state: state.has("Scent Mixture", self.player))

            if r.water:
                for s in self.data["Water_spawn"][r.map_id]:
                    map.add_locations({f"{mapid_to_text[r.map_id]} {s} Water": None}, SpiritValleyLocation)
                    set_rule(self.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Water", self.player), lambda state: state.has("Fishing Rod", self.player))
                    self.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Water", self.player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, self.player))

        self.set_rules()

    def connectUTentrencerando(self, l):
        for i in l:
            m2 = i[1].rsplit(' ')
            self.multiworld.get_entrance(i[0], self.player).connect(self.multiworld.get_region(m2[0], self.player))

    def fill_slot_data(self) -> Mapping[str, Any]:
        outdict = {
            **self.data,

            "Char_Gender": self.options.Char_Gender.value,
            "Char_Skin": self.options.Char_Skin.value,
            "Char_Hairstyle": self.options.Char_Hairstyle.value,
            "Char_Haircolor": self.options.Char_Haircolor.value,
            "Char_Outfit": self.options.Char_Outfit.value,

            "Spirit_Id_Start": spirit_id_start,
            "Spirit_Affection_Start": spirit_affection_id_start,
            "Spirit_Rare_Start": Rare_spirit_id_start,
            "Main_Quest_Start": main_quests_id_start,
            "Side_Quest_Start": side_quests_id_start,
            "Battle_Start": battle_locations_id_start,
            "Chest_Start": chest_locations_id_start,
            "warp_locations": warp_locations_id_start,

            "items_consumable_start": items_consumable_id_start,
            "items_crystal_start": items_crystal_id_start,
            "items_equipment_start": items_equipment_id_start,
            "items_key_item_start": items_key_item_id_start,
            "items_potion_start": items_potion_id_start,
            "items_coins_start": items_coins_id_start,
            "items_archipelago_id_start": items_archipelago_id_start,
            "items_warp_id_start": items_warp_id_start,

            "Spirit_Locations": self.options.Spirit_Locations.value,
            "Spirit_Affection": self.options.Spirit_Affection.value,
            "Rare_Locations": self.options.Rare_Locations.value,

            "Randomise_Move_Data": self.options.Randomise_Move_Data.value,

            "randomise_map": self.options.randomise_map.value,
            "randomise_warps": self.options.randomise_warps.value,

            "Minigame_Cheat": self.options.Minigame_Cheat.value,
            "Catch_Cheat": self.options.Guaranteed_Catch.value,
            "Xp_Modifer": self.options.Xp_Modifer.value,

            "world_version_major": self.worldversion_major,
            "world_version_minor": self.worldversion_minor,
            "world_version_build": self.worldversion_build,
            "total_locations": self.numlocations,
            "total_items": self.numitems,
        }
        return outdict
