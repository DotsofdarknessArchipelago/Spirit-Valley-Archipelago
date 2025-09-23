from BaseClasses import CollectionState, LocationProgressType
from worlds.generic.Rules import set_rule
from .Data_Spirits import obtainable_spirit_list
from .Items import affection_shop_items, spirit_crystal_shop_items


def set_rules(multiworld, player, options, data):

    #MAIN QUEST RULES
    set_rule(multiworld.get_location("Complete Main Quest: Super Secret Orders", player), lambda state: state.has("Super Secret Orders", player))
    set_rule(multiworld.get_location("Complete Main Quest: Temple Investigation", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Hunt for the chunk", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Bridge crossing", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Box pusher", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette"], player))
    set_rule(multiworld.get_location("Complete Main Quest: A new challenger", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Stiff competition", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Final Fight", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Quest for the crystal", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key"], player))
    set_rule(multiworld.get_location("Complete Main Quest: How the Dominoes fall", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Coconut Conundrum", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal","Fishing Rod"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Slippery When Wet", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal","Fishing Rod","Cock Shaped Key"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Glimmering Prize", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal","Fishing Rod","Cock Shaped Key","Red Harmony Crystal"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Suit In Hand", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal","Fishing Rod","Cock Shaped Key","Red Harmony Crystal","Fancy Suit"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Fishing For Treasure", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal","Fishing Rod","Cock Shaped Key","Red Harmony Crystal","Fancy Suit","Wedding Ring"], player))
    set_rule(multiworld.get_location("Complete Main Quest: Here Comes the Boom", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal","Fishing Rod","Cock Shaped Key","Red Harmony Crystal","Fancy Suit","Wedding Ring","Dynamite"], player))

    #SIDE QUEST RULES
    set_rule(multiworld.get_location("Complete Side Quest: Larry’s Treasure", player), lambda state: state.has("Ass Lover Extreme issue 12", player))
    set_rule(multiworld.get_location("Complete Side Quest: The Art of Fishing", player), lambda state: state.has("Goldfish Available in Shop", player))
    set_rule(multiworld.get_location("Complete Side Quest: Legend of the Valkyrie part 1.", player), lambda state: state.has("Cum Rag", player))
    set_rule(multiworld.get_location("Complete Side Quest: Legend of the Valkyrie part 2.", player), lambda state: state.has("Northern Blowfish Available in Shop", player))

    set_rule(multiworld.get_location("Complete Side Quest: Perky Petunia", player), lambda state, s=data["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"]: spirit_Obtain(state, player, s))
    set_rule(multiworld.get_location("Complete Side Quest: Slithering Menace", player), lambda state, s=data["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"]: state.has(f"{s} Obtainable", player))
    set_rule(multiworld.get_location("Complete Side Quest: Deadly Waters", player), lambda state, s=data["SIDE_QUEST_DEADLY_WATERS_SPIRIT"]: state.has_all([f"{s} Obtainable","Fishing Rod"], player))
    set_rule(multiworld.get_location("Complete Side Quest: Starry Eyed Surprise", player), lambda state, s=data["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"]: spirit_Obtain(state, player, s))
    set_rule(multiworld.get_location("Complete Side Quest: Arctic Menace", player), lambda state, s=data["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"]: state.has(f"{s} Obtainable", player))
    set_rule(multiworld.get_location("Complete Side Quest: Hunt for the Centiboob part 1.", player), lambda state, s=data["SIDE_QUEST_CENTIBOOB_1_SPIRIT"]: spirit_Obtain(state, player, s))
    set_rule(multiworld.get_location("Complete Side Quest: Hunt for the Centiboob part 2.", player), lambda state, s=data["SIDE_QUEST_CENTIBOOB_2_SPIRIT"]: spirit_Obtain(state, player, s))
    set_rule(multiworld.get_location("Complete Side Quest: Hunt for the Centiboob part 3.", player), lambda state, s=data["SIDE_QUEST_CENTIBOOB_3_SPIRIT"]: spirit_Obtain(state, player, s))

    #BOLDER CHEST RULES
    set_rule(multiworld.get_location("Evergreen Outpost: Chest Behind Pushable Bolder", player), lambda state: state.has("Testosterone Pills", player))
    set_rule(multiworld.get_location("Milly's Farm: Chest Behind Pushable Bolder", player), lambda state: state.has("Testosterone Pills", player))
    set_rule(multiworld.get_location("Sandy Tunnels: Chest North of Chad", player), lambda state: state.has("Testosterone Pills", player))
    set_rule(multiworld.get_location("Old Masters Hut: Chest in House Basement", player), lambda state: state.has("Testosterone Pills", player))


    #ACCESS RULES TODO FIX WHEN DOING ENTRENCE RANDO
    set_rule(multiworld.get_entrance("Trail_02-Greensvale", player), lambda state: state.has_all(["Super Secret Orders"], player))
    set_rule(multiworld.get_entrance("Trail_04-Ancient_Temple", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key"], player))
    set_rule(multiworld.get_entrance("Evergreen_Outpost-Trail_05", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal"], player))
    set_rule(multiworld.get_entrance("Trail_09-Stone_Temple", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key"], player))
    set_rule(multiworld.get_entrance("Tumbleweed_Town-Crash_Site", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal"], player))
    set_rule(multiworld.get_entrance("Trail_10-Trail_13", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal","Fishing Rod"], player))
    set_rule(multiworld.get_entrance("Coconut_Village-Cold_Harbour", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal","Fishing Rod","Cock Shaped Key","Red Harmony Crystal"], player))
    set_rule(multiworld.get_entrance("Frostville-Trail_17", player), lambda state: state.has_all(["Super Secret Orders","Ancient Temple Key","Raw Crystal Chunk","Power Crystal","Video Cassette","Spirit Handler License","Stone Key","Yellow Harmony Crystal","Fishing Rod","Cock Shaped Key","Red Harmony Crystal","Fancy Suit","Wedding Ring","Dynamite"], player))

    set_rule(multiworld.get_entrance("Trail_16-Trail_16_Cave", player), lambda state: state.has("Fishy Scent", player))
    set_rule(multiworld.get_entrance("Trail_22-Trail_22_Cave", player), lambda state: state.has("Scent Mixture", player))


    #WARP RULES TODO ADD WARP STUFF AND LOGIC
    if options.randomise_warps.value:
        set_rule(multiworld.get_entrance("Warp-Oakwood_Village", player), lambda state: state.has("Warp Cords(Oakwood Village)", player))
        set_rule(multiworld.get_entrance("Warp-Greensvale", player), lambda state: state.has("Warp Cords(Greensvale)", player))
        set_rule(multiworld.get_entrance("Warp-Trail_04", player), lambda state: state.has("Warp Cords(Trail 04)", player))
        set_rule(multiworld.get_entrance("Warp-Dairy_Farm", player), lambda state: state.has("Warp Cords(Dairy Farm)", player))
        set_rule(multiworld.get_entrance("Warp-Tumbleweed_Town", player), lambda state: state.has("Warp Cords(Tumbleweed Town)", player))
        set_rule(multiworld.get_entrance("Warp-Crash_Site", player), lambda state: state.has("Warp Cords(Crash Site)", player))
        set_rule(multiworld.get_entrance("Warp-Coconut_Village", player), lambda state: state.has("Warp Cords(Coconut Village)", player))
        set_rule(multiworld.get_entrance("Warp-Trail_14", player), lambda state: state.has("Warp Cords(Trail 14)", player))
        set_rule(multiworld.get_entrance("Warp-Cold_Harbour", player), lambda state: state.has("Warp Cords(Cold Harbour)", player))
        set_rule(multiworld.get_entrance("Warp-Frostville", player), lambda state: state.has("Warp Cords(Frostville)", player))
        set_rule(multiworld.get_entrance("Warp-Abandoned_Mine", player), lambda state: state.has("Warp Cords(Abandoned Mine)", player))
        set_rule(multiworld.get_entrance("Warp-Trail_18", player), lambda state: state.has("Warp Cords(Trail 18)", player))
        set_rule(multiworld.get_entrance("Warp-Trail_19", player), lambda state: state.has("Warp Cords(Trail 19)", player))
        set_rule(multiworld.get_entrance("Warp-Trail_22", player), lambda state: state.has("Warp Cords(Trail 22)", player))

    #SPIRIT OBTAIN RULES
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
