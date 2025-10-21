from BaseClasses import CollectionState, LocationProgressType
from worlds.generic.Rules import set_rule
from worlds.spiritvalley.Data_Spirits import obtainable_spirit_list
from worlds.spiritvalley.Items import affection_shop_items, spirit_crystal_shop_items


def rules_normal(multiworld, player, options, data):
    base_rules(multiworld, player, options, data)

    # MAIN QUEST RULES
    set_rule(multiworld.get_location("Complete Main Quest: Super Secret Orders", player), lambda state: state.has("Super Secret Orders", player))
    set_rule(multiworld.get_location("Complete Main Quest: Temple Investigation", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Becky can fix it", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Hunt for the chunk", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Bridge crossing", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Box pusher", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Total domination", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable"], player))
    set_rule(multiworld.get_location("Complete Main Quest: A new challenger", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Stiff competition", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Final Fight", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Quest for the crystal", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License", "Stone Key"], player))
    set_rule(multiworld.get_location("Complete Main Quest: How the Dominoes fall", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Coconut Conundrum", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Slippery When Wet", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Glimmering Prize", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Suit In Hand", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal", "Fancy Suit"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Fishing For Treasure", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal", "Fancy Suit", "Wedding Ring"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Here Comes the Boom", player), lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", f"{s} Obtainable", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal", "Fancy Suit", "Wedding Ring", "Dynamite"], player))

    # ACCESS RULES
    set_rule(multiworld.get_entrance("Trail2->Greensvale", player), lambda state: state.has_all(["Super Secret Orders"], player))
    set_rule(multiworld.get_entrance("Trail4->AncientTemple1", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key"], player))
    set_rule(multiworld.get_entrance("EvergreenOutpost->EvergreenOutpost_East", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal"], player))
    set_rule(multiworld.get_entrance("Trail9->DesertTemple1", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key"], player))
    set_rule(multiworld.get_entrance("TumbleweedTown->CrashSite", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal"], player))
    set_rule(multiworld.get_entrance("Trail11->Trail13", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod"], player))
    set_rule(multiworld.get_entrance("CoconutVillage_Temple->ColdHarbor", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal"], player))
    set_rule(multiworld.get_entrance("Frostville1->Trail17", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal", "Fancy Suit", "Wedding Ring", "Dynamite"], player))
    set_rule(multiworld.get_entrance("Trail20->Trail20_Right", player), lambda state: state.has_all(["Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal", "Fancy Suit", "Wedding Ring", "Dynamite"], player))





def rules_map_rando(multiworld, player, options, data):
    base_rules(multiworld, player, options, data)

    #"Complete Main Quest: Doctor’s Appointment"
    set_rule(multiworld.get_location("Complete Main Quest: Captain Maria", player),                 lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Doctor’s Appointment", player)))
    set_rule(multiworld.get_location("Complete Main Quest: First Orders", player),                  lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Captain Maria", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Crimson Agent", player),                 lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: First Orders", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Super Secret Orders", player),           lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Crimson Agent", player)))
    set_rule(multiworld.get_location("Complete Main Quest: First Mission: Success!", player),       lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Super Secret Orders", player)) and state.has("Super Secret Orders", player))
    set_rule(multiworld.get_location("Complete Main Quest: Onward to Greensvale", player),          lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: First Mission: Success!", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Temple Investigation", player),          lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Onward to Greensvale", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Harmonious Disturbance", player),        lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Temple Investigation", player)) and state.has("Ancient Temple Key", player))
    set_rule(multiworld.get_location("Complete Main Quest: Consulting Dolly", player),              lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Harmonious Disturbance", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Becky can fix it", player),              lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Consulting Dolly", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Hunt for the chunk", player),            lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Becky can fix it", player)) and state.has("Cracked Power Crystal", player))
    set_rule(multiworld.get_location("Complete Main Quest: Bridge crossing", player),               lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Hunt for the chunk", player)) and state.has("Raw Crystal Chunk", player))
    set_rule(multiworld.get_location("Complete Main Quest: Dusty Vale awaits", player),             lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Bridge crossing", player)) and state.has("Power Crystal", player))
    set_rule(multiworld.get_location("Complete Main Quest: An audience with the King", player),     lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Dusty Vale awaits", player)))
    set_rule(multiworld.get_location("Complete Main Quest: The Grand Cuckold Challenge", player),   lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: An audience with the King", player)))
    set_rule(multiworld.get_location("Complete Main Quest: License to battle", player),             lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: The Grand Cuckold Challenge", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Box pusher", player),                    lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: License to battle", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Total domination", player),              lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Box pusher", player)) and state.has("Video Cassette", player))
    set_rule(multiworld.get_location("Complete Main Quest: A challenge awaits", player),            lambda state, s=data["MAIN_QUEST_TOTAL_DOMINATION"]: state.can_reach(multiworld.get_location("Complete Main Quest: Total domination", player)) and state.has(f"{s} Obtainable", player))
    set_rule(multiworld.get_location("Complete Main Quest: A new challenger", player),              lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: A challenge awaits", player)) and state.has("Spirit Handler License", player))
    set_rule(multiworld.get_location("Complete Main Quest: Stiff competition", player),             lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: A new challenger", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Final Fight", player),                   lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Stiff competition", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Return of the champion", player),        lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Final Fight", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Breeding season", player),               lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Return of the champion", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Mission success", player),               lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Breeding season", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Quest for the crystal", player),         lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Mission success", player)))
    set_rule(multiworld.get_location("Complete Main Quest: How the Dominoes fall", player),         lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Quest for the crystal", player)) and state.has("Stone Key", player))
    set_rule(multiworld.get_location("Complete Main Quest: Big balloon adventure", player),         lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: How the Dominoes fall", player)) and state.has("Yellow Harmony Crystal", player))
    set_rule(multiworld.get_location("Complete Main Quest: Welcome to Paradise", player),           lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Big balloon adventure", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Coconut Conundrum", player),             lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Welcome to Paradise", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Lusty Cultists", player),                lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Coconut Conundrum", player)) and state.has("Fishing Rod", player))
    set_rule(multiworld.get_location("Complete Main Quest: Savior of Coconut Village", player),     lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Lusty Cultists", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Slippery When Wet", player),             lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Savior of Coconut Village", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Glimmering Prize", player),              lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Slippery When Wet", player)) and state.has("Cock Shaped Key", player))
    set_rule(multiworld.get_location("Complete Main Quest: Arctic Adventure", player),              lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Glimmering Prize", player)) and state.has("Red Harmony Crystal", player))
    set_rule(multiworld.get_location("Complete Main Quest: The Frigid Maiden", player),             lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Arctic Adventure", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Arctic Isles", player),                  lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: The Frigid Maiden", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Paisley Bones", player),                 lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Arctic Isles", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Demand for Dynamite", player),           lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Paisley Bones", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Stealing From a Dead Man", player),      lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Demand for Dynamite", player)))
    set_rule(multiworld.get_location("Complete Main Quest: The Lewd Exorcist", player),             lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Stealing From a Dead Man", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Suit In Hand", player),                  lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: The Lewd Exorcist", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Fishing For Treasure", player),          lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Suit In Hand", player)) and state.has("Fancy Suit", player))
    set_rule(multiworld.get_location("Complete Main Quest: The Proposal", player),                  lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Fishing For Treasure", player)) and state.has("Wedding Ring", player))
    set_rule(multiworld.get_location("Complete Main Quest: Here Comes the Boom", player),           lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: The Proposal", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Arctic Harmony", player),                lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Here Comes the Boom", player)) and state.has("Dynamite", player))
    set_rule(multiworld.get_location("Complete Main Quest: Crimson Chase", player),                 lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Arctic Harmony", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Through the Portal", player),            lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Crimson Chase", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Sanctuary Shakedown", player),           lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Through the Portal", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Hostage Situation", player),             lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Sanctuary Shakedown", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Breezie Runs Free", player),             lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Hostage Situation", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Desperate Dash", player),                lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Breezie Runs Free", player)))
    set_rule(multiworld.get_location("Complete Main Quest: Battle for Spirit Valley", player),      lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Desperate Dash", player)))


    # ACCESS RULES
    set_rule(multiworld.get_entrance("Trail2 Left", player), lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: First Mission: Success!", player)))
    set_rule(multiworld.get_entrance("Trail4 Temple", player), lambda state: state.has("Ancient Temple Key", player))#state.can_reach(multiworld.get_location("Complete Main Quest: Temple Investigation", player)) and state.has("Ancient Temple Key", player))
    set_rule(multiworld.get_entrance("EvergreenOutpost->EvergreenOutpost_East", player), lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Bridge crossing", player)) and state.has("Power Crystal", player))
    set_rule(multiworld.get_entrance("Trail9 Temple", player), lambda state: state.has("Stone Key", player))
    set_rule(multiworld.get_entrance("TumbleweedTown->CrashSite", player), lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Big balloon adventure", player)))
    set_rule(multiworld.get_entrance("Trail11 pier", player), lambda state: state.has("Fishing Rod", player))
    set_rule(multiworld.get_entrance("CoconutVillage_Temple->ColdHarbor", player), lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Arctic Adventure", player)))
    set_rule(multiworld.get_entrance("Frostville1 Top", player), lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Here Comes the Boom", player)) and state.has("Dynamite", player))
    set_rule(multiworld.get_entrance("Trail20->Trail20_Right", player), lambda state: state.can_reach(multiworld.get_location("Complete Main Quest: Breezie Runs Free", player)))

def base_rules(multiworld, player, options, data):

    # SIDE QUEST RULES
    set_rule(multiworld.get_location("Complete Side Quest: Larry’s Treasure", player), lambda state: state.has("Ass Lover Extreme issue 12", player))
    set_rule(multiworld.get_location("Complete Side Quest: The Art of Fishing", player), lambda state: state.has("Goldfish Available in Shop", player))
    set_rule(multiworld.get_location("Complete Side Quest: Legend of the Valkyrie part 1.", player), lambda state: state.has("Cum Rag", player))
    set_rule(multiworld.get_location("Complete Side Quest: Legend of the Valkyrie part 2.", player), lambda state: state.has("Northern Blowfish Available in Shop", player))

    set_rule(multiworld.get_location("Complete Side Quest: Perky Petunia", player), lambda state, s=data["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"]: spirit_Obtain(state, player, s))
    set_rule(multiworld.get_location("Complete Side Quest: Slithering Menace", player), lambda state, s=data["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"]: state.has(f"{s} Obtainable", player))
    set_rule(multiworld.get_location("Complete Side Quest: Deadly Waters", player), lambda state, s=data["SIDE_QUEST_DEADLY_WATERS_SPIRIT"]: state.has_all([f"{s} Obtainable", "Fishing Rod"], player))
    set_rule(multiworld.get_location("Complete Side Quest: Starry Eyed Surprise", player), lambda state, s=data["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"]: spirit_Obtain(state, player, s))
    set_rule(multiworld.get_location("Complete Side Quest: Arctic Menace", player), lambda state, s=data["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"]: state.has(f"{s} Obtainable", player))
    set_rule(multiworld.get_location("Complete Side Quest: Hunt for the Centiboob part 1.", player), lambda state, s=data["SIDE_QUEST_CENTIBOOB_1_SPIRIT"]: spirit_Obtain(state, player, s))
    set_rule(multiworld.get_location("Complete Side Quest: Hunt for the Centiboob part 2.", player), lambda state, s=data["SIDE_QUEST_CENTIBOOB_2_SPIRIT"]: spirit_Obtain(state, player, s))
    set_rule(multiworld.get_location("Complete Side Quest: Hunt for the Centiboob part 3.", player), lambda state, s=data["SIDE_QUEST_CENTIBOOB_3_SPIRIT"]: spirit_Obtain(state, player, s))

    # BOLDER CHEST RULES
    set_rule(multiworld.get_location("Evergreen Outpost: Chest Behind Pushable Bolder", player), lambda state: state.has("Testosterone Pills", player))
    set_rule(multiworld.get_location("Greensvale: Chest Behind Pushable Bolder In the North", player), lambda state: state.has("Testosterone Pills", player))
    set_rule(multiworld.get_location("Evergreen Caverns: Chest 1 Behind Rawry", player), lambda state: state.has("Testosterone Pills", player))
    set_rule(multiworld.get_location("Evergreen Caverns: Chest 2 Behind Rawry", player), lambda state: state.has("Testosterone Pills", player))
    set_rule(multiworld.get_location("Milly's Farm: Chest Behind Pushable Bolder", player), lambda state: state.has("Testosterone Pills", player))
    set_rule(multiworld.get_location("Sandy Tunnels: Chest North of Chad", player), lambda state: state.has("Testosterone Pills", player))
    set_rule(multiworld.get_location("Old Masters Hut: Chest in Basement", player), lambda state: state.has("Testosterone Pills", player))

    set_rule(multiworld.get_entrance("Trail16_Top->Trail16", player), lambda state: state.has("Testosterone Pills", player))


    # SPIRIT OBTAIN RULES
    for spirit in obtainable_spirit_list:
        if options.Spirit_Locations.value:
            set_rule(multiworld.get_location(f"Obtain a {spirit} Spirit", player), lambda state, s=spirit, p=player: spirit_Obtain(state, p, s))
            if options.Spirit_Obtain_progression.value:
                multiworld.get_location(f"Obtain a {spirit} Spirit", player).progress_type = LocationProgressType.EXCLUDED
            if options.Spirit_Affection.value:
                set_rule(multiworld.get_location(f"Get {spirit} to Affection LV1", player), lambda state, s=spirit, p=player: spirit_Affection(state, p, s))
                set_rule(multiworld.get_location(f"Get {spirit} to Affection LV2", player), lambda state, s=spirit, p=player: spirit_Affection(state, p, s))
                set_rule(multiworld.get_location(f"Get {spirit} to Affection LV3", player), lambda state, s=spirit, p=player: spirit_Affection(state, p, s))
                set_rule(multiworld.get_location(f"Get {spirit} to Affection LV4", player), lambda state, s=spirit, p=player: spirit_Affection(state, p, s))
                set_rule(multiworld.get_location(f"Get {spirit} to Affection LV5", player), lambda state, s=spirit, p=player: spirit_Affection(state, p, s))
                if options.Spirit_Affection_progression.value:
                    multiworld.get_location(f"Get {spirit} to Affection LV1", player).progress_type = LocationProgressType.EXCLUDED
                    multiworld.get_location(f"Get {spirit} to Affection LV2", player).progress_type = LocationProgressType.EXCLUDED
                    multiworld.get_location(f"Get {spirit} to Affection LV3", player).progress_type = LocationProgressType.EXCLUDED
                    multiworld.get_location(f"Get {spirit} to Affection LV4", player).progress_type = LocationProgressType.EXCLUDED
                    multiworld.get_location(f"Get {spirit} to Affection LV5", player).progress_type = LocationProgressType.EXCLUDED

            if options.Rare_Locations.value:
                set_rule(multiworld.get_location(f"Obtain a Rare {spirit} Spirit", player), lambda state, s=spirit, p=player: spirit_rare_Obtain(state, p, s))
                if options.Rare_Spirit_Obtain_progression.value:
                    multiworld.get_location(f"Obtain a Rare {spirit} Spirit", player).progress_type = LocationProgressType.EXCLUDED


def spirit_Obtain(state: CollectionState, player: int, spirit: str) -> bool:
    return state.has(f"{spirit} Obtainable", player) and state.has_any(spirit_crystal_shop_items, player) and state.has("Shop Accessible", player)


def spirit_rare_Obtain(state: CollectionState, player: int, spirit: str) -> bool:
    return spirit_Obtain(state, player, spirit) and state.has("Elusive Scent Available in Shop", player)


def spirit_Affection(state: CollectionState, player: int, spirit: str) -> bool:
    return spirit_Obtain(state, player, spirit) and state.has_any(affection_shop_items, player) and state.has("Shop Accessible", player)
