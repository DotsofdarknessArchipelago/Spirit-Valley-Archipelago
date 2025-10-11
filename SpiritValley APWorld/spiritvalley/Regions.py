from BaseClasses import Region, ItemClassification, EntranceType, Entrance
from entrance_rando import randomize_entrances
from worlds.generic.Rules import set_rule
from worlds.spiritvalley import spirit_locations, SpiritValleyLocation, spirit_affection_locations, Rare_spirit_locations, spiritItem
from worlds.spiritvalley.Data_Regions import regions, mapid_to_text, transition_areas, specical_transition_areas


def Generate_Map(multiworld, player, options, loc, data):
    hub_region = Region("Menu", player, multiworld)
    multiworld.regions.append(hub_region)

    region_warp = Region("Warp", player, multiworld)
    multiworld.regions.append(region_warp)
    join("Menu", "Warp", multiworld, player, False)

    if options.Spirit_Locations.value:
        region_spirit = Region("Spirits", player, multiworld)
        region_spirit.add_locations(spirit_locations, SpiritValleyLocation)
        if options.Spirit_Affection.value:
            region_spirit.add_locations(spirit_affection_locations, SpiritValleyLocation)
        if options.Rare_Locations.value:
            region_spirit.add_locations(Rare_spirit_locations, SpiritValleyLocation)
        multiworld.regions.append(region_spirit)
        hub_region.connect(region_spirit, "Menu-Spirit")


    for r in regions:
        map = Region(r.map_id, player, multiworld)

        if r.warpable:
            map.add_locations({f"{mapid_to_text[r.map_id]} WarpStone": None, f"{mapid_to_text[r.map_id]} WarpStone Activated": loc[f"{mapid_to_text[r.map_id]} WarpStone Activated"]}, SpiritValleyLocation)
            multiworld.get_location(f"{mapid_to_text[r.map_id]} WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
            if options.randomise_warps.value:
                region_warp.connect(map, f"Warp->{r.map_id}", lambda state: state.has("Warp Obtainable", player) and state.has(f"Warp Cords({r.map_id})", player))
                map.connect(region_warp, f"{r.map_id}->Warp", lambda state: state.has("Warp Obtainable", player))

        if r.grass:
            if r.map_id == "Trail16_Top":
                for s in data["Grass_spawn"]["Trail16"]:
                    map.add_locations({f"{mapid_to_text[r.map_id]} {s} Grass": None}, SpiritValleyLocation)
                    multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
            elif r.map_id == "Trail20_Right":
                for s in data["Grass_spawn"]["Trail20"]:
                    map.add_locations({f"{mapid_to_text[r.map_id]} {s} Grass": None}, SpiritValleyLocation)
                    multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
            else:
                for s in data["Grass_spawn"][r.map_id]:
                    map.add_locations({f"{mapid_to_text[r.map_id]} {s} Grass": None}, SpiritValleyLocation)
                    multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
                    if r.map_id == "Trail16_Cave":
                        set_rule(multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", player),  lambda state: state.has("Fishy Scent", player))
                    if r.map_id == "Trail22_Cave":
                        set_rule(multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", player),  lambda state: state.has("Scent Mixture", player))

        if r.water:
            for s in data["Water_spawn"][r.map_id]:
                map.add_locations({f"{mapid_to_text[r.map_id]} {s} Water": None}, SpiritValleyLocation)
                set_rule(multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Water", player), lambda state: state.has("Fishing Rod", player))
                multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

        if r.chest_locations is not None:
            for l in r.chest_locations:
                map.add_locations({l:loc[l]}, SpiritValleyLocation)

        if r.trainer_locations is not None:
            for l in r.trainer_locations:
                map.add_locations({l:loc[l]}, SpiritValleyLocation)

        if r.quest_locations is not None:
            for l in r.quest_locations:
                map.add_locations({l:loc[l]}, SpiritValleyLocation)

        if options.randomise_map.value:
            for e in r.entry:
                ex = map.create_exit(f"{r.map_id} {e}")
                en = map.create_er_target(f"{r.map_id} {e}")
                if e in r.exits:
                    ex.randomization_type = EntranceType.TWO_WAY
                    en.randomization_type = EntranceType.TWO_WAY

        if r.map_id in ["Greensvale_Merchant","TumbleweedTown_Merchant","CoconutVillage_Merchant","Frostville1_Merchant"]:
            map.add_locations({f"{mapid_to_text[r.map_id]} Shop": None}, SpiritValleyLocation)
            multiworld.get_location(f"{mapid_to_text[r.map_id]} Shop", player).place_locked_item(spiritItem(f"Shop Accessible", ItemClassification.progression, None, player))


        multiworld.regions.append(map)

    join("Menu", "OakwoodVillage", multiworld, player, True)
    join("OakwoodVillage", "OakwoodVillage_Clinic", multiworld, player, False)

    if not options.randomise_map.value:
        for t in [*transition_areas,*specical_transition_areas]:
            join(t.scene1_name,t.scene2_name,multiworld,player,t.oneway)
    else:
        for t in specical_transition_areas:
            join(t.scene1_name,t.scene2_name,multiworld,player,t.oneway)

def join(r1,r2,multiworld,player,oneway):
    region1 = multiworld.get_region(r1, player)
    region2 = multiworld.get_region(r2, player)

    region1.connect(region2,f"{r1}->{r2}")
    if not oneway:
        region2.connect(region1,f"{r2}->{r1}")

    """
    hub_region = Region("Menu", player, multiworld)
    multiworld.regions.append(hub_region)

    region_warp = Region("Warp", player, multiworld)
    hub_region.connect(region_warp, "Menu-Warp")

    if options.Spirit_Locations.value:
        region_spirit = Region("Spirits", player, multiworld)
        region_spirit.add_locations(spirit_locations, SpiritValleyLocation)
        if options.Spirit_Affection.value:
            region_spirit.add_locations(spirit_affection_locations, SpiritValleyLocation)
        if options.Rare_Locations.value:
            region_spirit.add_locations(Rare_spirit_locations, SpiritValleyLocation)
        hub_region.connect(region_spirit, "Menu-Spirit")

    # ------------------------------------------------------------------------------------------------------------

    region_oakwood = Region("Oakwood Village", player, multiworld)
    region_oakwood.add_locations({
        "Oakwood Village: Chest In Uncles House": loc["Oakwood Village: Chest In Uncles House"],
    }, SpiritValleyLocation)
    region_oakwood.add_locations({
        "Complete Side Quest: Sparring Match": loc["Complete Side Quest: Sparring Match"],
    }, SpiritValleyLocation)
    region_oakwood.add_locations({
        "Oakwood Village: Defeat Robbie": loc["Oakwood Village: Defeat Robbie"],
    }, SpiritValleyLocation)
    region_oakwood.add_locations({
        "Complete Main Quest: Doctor’s Appointment": loc["Complete Main Quest: Doctor’s Appointment"],
        "Complete Main Quest: Captain Maria": loc["Complete Main Quest: Captain Maria"],
        "Complete Main Quest: First Mission: Success!": loc["Complete Main Quest: First Mission: Success!"],
        "Complete Main Quest: Consulting Dolly": loc["Complete Main Quest: Consulting Dolly"],
    }, SpiritValleyLocation)

    region_oakwood.add_locations({f"Oakwood Village WarpStone": None, "Oakwood Village WarpStone Activated": loc["Oakwood Village WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Oakwood Village WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_oakwood, "Warp-Oakwood_Village", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Oakwood Village)", player))

    hub_region.connect(region_oakwood, "Menu-Oakwood_Village")
    multiworld.regions.append(region_oakwood)

    # ------------------------------------------------------------------------------------------------------------

    region_trail01 = Region("Trail 01", player, multiworld)
    region_trail01.add_locations({
        "Trail 01: Chest Near Piper": loc["Trail 01: Chest Near Piper"],
        "Trail 01: Chest North of Piper": loc["Trail 01: Chest North of Piper"],
        "Trail 01: Potion From Jane": loc["Trail 01: Potion From Jane"],
    }, SpiritValleyLocation)
    region_trail01.add_locations({
        "Complete Side Quest: Perky Petunia": loc["Complete Side Quest: Perky Petunia"],
    }, SpiritValleyLocation)
    for s in data["Grass_spawn"]["Trail 01"]:
        region_trail01.add_locations({f"Trail 01 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 01 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_oakwood.connect(region_trail01, "Oakwood_Village->Trail_01")
    region_trail01.connect(region_oakwood, "Oakwood_Village<-Trail_01")#TODO ENTRENCE RANDO NEED TO RENAME ALL
    multiworld.regions.append(region_trail01)

    # ------------------------------------------------------------------------------------------------------------

    region_evergreen_outpost = Region("Evergreen Outpost", player, multiworld)
    region_evergreen_outpost.add_locations({
        "Evergreen Outpost: Chest Near Medic": loc["Evergreen Outpost: Chest Near Medic"],
        "Evergreen Outpost: Chest Above Grass Patch": loc["Evergreen Outpost: Chest Above Grass Patch"],
        "Evergreen Outpost: Chest Behind Pushable Bolder": loc["Evergreen Outpost: Chest Behind Pushable Bolder"],
    }, SpiritValleyLocation)
    region_evergreen_outpost.add_locations({
        "Complete Side Quest: Larry’s Treasure": loc["Complete Side Quest: Larry’s Treasure"],
    }, SpiritValleyLocation)
    region_evergreen_outpost.add_locations({
        "Evergreen Outpost: Defeat Elise": loc["Evergreen Outpost: Defeat Elise"],
    }, SpiritValleyLocation)
    region_evergreen_outpost.add_locations({
        "Complete Main Quest: First Orders": loc["Complete Main Quest: First Orders"],
        "Complete Main Quest: Super Secret Orders": loc["Complete Main Quest: Super Secret Orders"],
        "Complete Main Quest: Bridge crossing": loc["Complete Main Quest: Bridge crossing"],
    }, SpiritValleyLocation)
    for s in data["Grass_spawn"]["Evergreen Outpost"]:
        region_evergreen_outpost.add_locations({f"Evergreen Outpost {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Evergreen Outpost {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail01.connect(region_evergreen_outpost, "Trail_01-Evergree_Outpost")
    multiworld.regions.append(region_evergreen_outpost)

    # ------------------------------------------------------------------------------------------------------------

    region_trail02 = Region("Trail 02", player, multiworld)
    region_trail02.add_locations({
        "Trail 02: Chest Near Billy": loc["Trail 02: Chest Near Billy"],
        "Trail 02: Chest in Hidden Path Next to Macy": loc["Trail 02: Chest in Hidden Path Next to Macy"],
        "Trail 02: Chest East of Macy": loc["Trail 02: Chest East of Macy"],
        "Trail 02: Chest Near Skyler": loc["Trail 02: Chest Near Skyler"],
    }, SpiritValleyLocation)
    region_trail02.add_locations({
        "Trail 02: Defeat Billy": loc["Trail 02: Defeat Billy"],
        "Trail 02: Defeat Macy": loc["Trail 02: Defeat Macy"],
        "Trail 02: Defeat Skyler": loc["Trail 02: Defeat Skyler"],
        "Trail 02: Defeat Crimson Agent": loc["Trail 02: Defeat Crimson Agent"],
    }, SpiritValleyLocation)
    region_trail02.add_locations({
        "Complete Main Quest: Crimson Agent": loc["Complete Main Quest: Crimson Agent"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 02"]:
        region_trail02.add_locations({f"Trail 02 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 02 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_evergreen_outpost.connect(region_trail02, "Evergreen_Outpost-Trail_02")
    multiworld.regions.append(region_trail02)

    # ------------------------------------------------------------------------------------------------------------

    region_greensvale = Region("Greensvale", player, multiworld)
    region_greensvale.add_locations({
        "Greensvale: Chest South of Waystone": loc["Greensvale: Chest South of Waystone"],
        "Greensvale: Chest in Red House": loc["Greensvale: Chest in Red House"],
        "Greensvale: Chest Next To XXX Shop": loc["Greensvale: Chest Next To XXX Shop"],
        "Greensvale: Chest Behind Pushable Bolder In the North": loc["Greensvale: Chest Behind Pushable Bolder In the North"],
    }, SpiritValleyLocation)
    region_greensvale.add_locations({
        "Complete Main Quest: Onward to Greensvale": loc["Complete Main Quest: Onward to Greensvale"],
        "Complete Main Quest: Harmonious Disturbance": loc["Complete Main Quest: Harmonious Disturbance"],
        "Complete Main Quest: Becky can fix it": loc["Complete Main Quest: Becky can fix it"],
        "Complete Main Quest: Hunt for the chunk": loc["Complete Main Quest: Hunt for the chunk"],
    }, SpiritValleyLocation)
    region_greensvale.add_locations({f"Greensvale Shop": None}, SpiritValleyLocation)
    multiworld.get_location(f"Greensvale Shop", player).place_locked_item(spiritItem(f"Shop Accessible", ItemClassification.progression, None, player))

    region_greensvale.add_locations({f"Greensvale WarpStone": None, "Greensvale WarpStone Activated": loc["Greensvale WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Greensvale WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_greensvale, "Warp-Greensvale", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Greensvale)", player))

    region_evergreen_outpost.connect(region_greensvale, "Trail_02-Greensvale")
    multiworld.regions.append(region_greensvale)

    # ------------------------------------------------------------------------------------------------------------

    region_millys_farm = Region("Milly's Farm", player, multiworld)
    region_millys_farm.add_locations({
        "Milly's Farm: Chest Behind Pushable Bolder": loc["Milly's Farm: Chest Behind Pushable Bolder"],
    }, SpiritValleyLocation)
    region_millys_farm.add_locations({
        "Complete Side Quest: Slithering Menace": loc["Complete Side Quest: Slithering Menace"]
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Milly's Farm"]:
        region_millys_farm.add_locations({f"Milly's Farm {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Milly's Farm {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_greensvale.connect(region_millys_farm, "Greensvale-Millys_Farm")
    multiworld.regions.append(region_millys_farm)

    # ------------------------------------------------------------------------------------------------------------

    region_trail03 = Region("Trail 03", player, multiworld)
    region_trail03.add_locations({
        "Trail 03: Chest North of Miriam": loc["Trail 03: Chest North of Miriam"],
        "Trail 03: Chest South of Miriam": loc["Trail 03: Chest South of Miriam"],
        "Trail 03: Chest Chest Before Evergreen Caverns Entrance": loc["Trail 03: Chest Chest Before Evergreen Caverns Entrance"],
    }, SpiritValleyLocation)
    region_trail03.add_locations({
        "Complete Side Quest: Pleasuring Pusseen": loc["Complete Side Quest: Pleasuring Pusseen"],
    }, SpiritValleyLocation)
    region_trail03.add_locations({
        "Trail 03: Defeat Cheese": loc["Trail 03: Defeat Cheese"],
        "Trail 03: Defeat Miriam": loc["Trail 03: Defeat Miriam"],
        "Trail 03: Defeat Jenna": loc["Trail 03: Defeat Jenna"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 03"]:
        region_trail03.add_locations({f"Trail 03 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 03 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_greensvale.connect(region_trail03, "Greensvale-Trail_03")
    multiworld.regions.append(region_trail03)

    # ------------------------------------------------------------------------------------------------------------

    region_evergreen_caverns = Region("Evergreen Caverns", player, multiworld)
    region_evergreen_caverns.add_locations({
        "Evergreen Caverns: Chest West of Stu": loc["Evergreen Caverns: Chest West of Stu"],
        "Evergreen Caverns: Chest South of Nicole": loc["Evergreen Caverns: Chest South of Nicole"],
        "Evergreen Caverns: Chest 1 Behind Rawry": loc["Evergreen Caverns: Chest 1 Behind Rawry"],
        "Evergreen Caverns: Chest 2 Behind Rawry": loc["Evergreen Caverns: Chest 2 Behind Rawry"],
    }, SpiritValleyLocation)
    region_evergreen_caverns.add_locations({
        "Evergreen Caverns: Defeat Stu": loc["Evergreen Caverns: Defeat Stu"],
        "Evergreen Caverns: Defeat Nicole": loc["Evergreen Caverns: Defeat Nicole"],
        "Evergreen Caverns: Defeat Rawry": loc["Evergreen Caverns: Defeat Rawry"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Evergreen Caverns"]:
        region_evergreen_caverns.add_locations({f"Evergreen Caverns {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Evergreen Caverns {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail03.connect(region_evergreen_caverns, "Trail_03-Evergreen_Caverns")
    multiworld.regions.append(region_evergreen_caverns)
    # ------------------------------------------------------------------------------------------------------------

    region_trail04 = Region("Trail 04", player, multiworld)
    region_trail04.add_locations({
        "Trail 04: Chest West of Evergreen Caverns Entrance": loc["Trail 04: Chest West of Evergreen Caverns Entrance"],
        "Trail 04: Chest West Side of Map": loc["Trail 04: Chest West Side of Map"],
        "Trail 04: Chest Near Waystone": loc["Trail 04: Chest Near Waystone"],
    }, SpiritValleyLocation)

    region_trail04.add_locations({f"Trail 04 WarpStone": None, "Trail 04 WarpStone Activated": loc["Trail 04 WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Trail 04 WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_trail04, "Warp-Trail_04", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Trail 04)", player))

    for s in data["Grass_spawn"]["Trail 04"]:
        region_trail04.add_locations({f"Trail 04 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 04 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_evergreen_caverns.connect(region_trail04, "Evergreen_Caverns-Trail_04")
    multiworld.regions.append(region_trail04)

    # ------------------------------------------------------------------------------------------------------------

    region_ancient_temple = Region("Ancient Temple", player, multiworld)
    region_ancient_temple.add_locations({
        "Ancient Temple 1: Chest Near 3rd Crimson Cloak": loc["Ancient Temple 1: Chest Near 3rd Crimson Cloak"],
        "Ancient Temple 1: Chest in Path Loop": loc["Ancient Temple 1: Chest in Path Loop"],
        "Ancient Temple 1: Chest Near 6th Crimson Cloak": loc["Ancient Temple 1: Chest Near 6th Crimson Cloak"],
    }, SpiritValleyLocation)
    region_ancient_temple.add_locations({
        "Ancient Temple 1: Defeat 1st Crimson Cloak": loc["Ancient Temple 1: Defeat 1st Crimson Cloak"],
        "Ancient Temple 1: Defeat 2nd Crimson Cloak": loc["Ancient Temple 1: Defeat 2nd Crimson Cloak"],
        "Ancient Temple 1: Defeat 3rd Crimson Cloak": loc["Ancient Temple 1: Defeat 3rd Crimson Cloak"],
        "Ancient Temple 1: Defeat 4th Crimson Cloak": loc["Ancient Temple 1: Defeat 4th Crimson Cloak"],
        "Ancient Temple 1: Defeat 5th Crimson Cloak": loc["Ancient Temple 1: Defeat 5th Crimson Cloak"],
        "Ancient Temple 1: Defeat 6th Crimson Cloak": loc["Ancient Temple 1: Defeat 6th Crimson Cloak"],
    }, SpiritValleyLocation)
    region_ancient_temple.add_locations({
        "Ancient Temple 2: Chest West Side of Room": loc["Ancient Temple 2: Chest West Side of Room"],
        "Ancient Temple 2: Chest East side of Room": loc["Ancient Temple 2: Chest East side of Room"],
        "Ancient Temple 2: Chest in Middle Area of Room": loc["Ancient Temple 2: Chest in Middle Area of Room"],
    }, SpiritValleyLocation)
    region_ancient_temple.add_locations({
        "Ancient Temple 2: Defeat Crimson Cloak": loc["Ancient Temple 2: Defeat Crimson Cloak"],
    }, SpiritValleyLocation)
    region_ancient_temple.add_locations({
        "Ancient Temple 3: Defeat Valkrie": loc["Ancient Temple 3: Defeat Valkrie"],
    }, SpiritValleyLocation)
    region_ancient_temple.add_locations({
        "Complete Main Quest: Temple Investigation": loc["Complete Main Quest: Temple Investigation"],
    }, SpiritValleyLocation)
    region_trail04.connect(region_ancient_temple, "Trail_04-Ancient_Temple")
    multiworld.regions.append(region_ancient_temple)

    # ------------------------------------------------------------------------------------------------------------

    region_trail05 = Region("Trail 05", player, multiworld)
    region_trail05.add_locations({
        "Trail 05: Chest Near Evergreen Outpost Entrance": loc["Trail 05: Chest Near Evergreen Outpost Entrance"],
        "Trail 05: Chest East of Mila": loc["Trail 05: Chest East of Mila"],
        "Trail 05: Chest West of Roy": loc["Trail 05: Chest West of Roy"],
        "Trail 05: Chest East of Lulu": loc["Trail 05: Chest East of Lulu"],
    }, SpiritValleyLocation)
    region_trail05.add_locations({
        "Trail 05: Defeat Mila": loc["Trail 05: Defeat Mila"],
        "Trail 05: Defeat Roy": loc["Trail 05: Defeat Roy"],
        "Trail 05: Defeat Lulu": loc["Trail 05: Defeat Lulu"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 05"]:
        region_trail05.add_locations({f"Trail 05 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 05 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_evergreen_outpost.connect(region_trail05, "Evergreen_Outpost-Trail_05")
    multiworld.regions.append(region_trail05)

    # ------------------------------------------------------------------------------------------------------------

    region_sandy_tunnels = Region("Sandy Tunnels", player, multiworld)
    region_sandy_tunnels.add_locations({
        "Sandy Tunnels: Chest South of Chad": loc["Sandy Tunnels: Chest South of Chad"],
        "Sandy Tunnels: Chest North of Chad": loc["Sandy Tunnels: Chest North of Chad"],
        "Sandy Tunnels: Healing Potion From Jessica": loc["Sandy Tunnels: Healing Potion From Jessica"],
    }, SpiritValleyLocation)
    region_sandy_tunnels.add_locations({
        "Sandy Tunnels: Chest West of Destiny": loc["Sandy Tunnels: Chest West of Destiny"],
        "Sandy Tunnels: Defeat Chad": loc["Sandy Tunnels: Defeat Chad"],
        "Sandy Tunnels: Defeat Destiny": loc["Sandy Tunnels: Defeat Destiny"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Sandy Tunnels"]:
        region_sandy_tunnels.add_locations({f"Sandy Tunnels {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Sandy Tunnels {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail05.connect(region_sandy_tunnels, "Trail_05-Sandy_Tunnels")
    multiworld.regions.append(region_sandy_tunnels)

    # ------------------------------------------------------------------------------------------------------------

    region_trail06 = Region("Trail 06", player, multiworld)
    region_trail06.add_locations({
        "Trail 06: Chest West of Sandy Tunnels Entrance": loc["Trail 06: Chest West of Sandy Tunnels Entrance"],
        "Trail 06: Chest East of Kelsie": loc["Trail 06: Chest East of Kelsie"],
        "Trail 06: Chest South of Hayden": loc["Trail 06: Chest South of Hayden"],
    }, SpiritValleyLocation)
    region_trail06.add_locations({
        "Trail 06: Defeat Kelsie": loc["Trail 06: Defeat Kelsie"],
        "Trail 06: Defeat Hayden": loc["Trail 06: Defeat Hayden"],
        "Trail 06: Defeat Juliet": loc["Trail 06: Defeat Juliet"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 06"]:
        region_trail06.add_locations({f"Trail 06 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 06 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_sandy_tunnels.connect(region_trail06, "Sandy_Tunnels-Trail_06")
    multiworld.regions.append(region_trail06)

    # ------------------------------------------------------------------------------------------------------------

    region_dairy_farm = Region("Dairy Farm", player, multiworld)
    region_dairy_farm.add_locations({
        "Dairy Farm: Chest North of Waystone": loc["Dairy Farm: Chest North of Waystone"],
        "Dairy Farm: Chest South of Waystone": loc["Dairy Farm: Chest South of Waystone"],
        "Dairy Farm: Chest Next to House": loc["Dairy Farm: Chest Next to House"],
        "Dairy Farm: Chest North-East of House": loc["Dairy Farm: Chest North-East of House"],
    }, SpiritValleyLocation)
    region_dairy_farm.add_locations({
        "Complete Side Quest: Cattle Thieves": loc["Complete Side Quest: Cattle Thieves"],
    }, SpiritValleyLocation)

    region_dairy_farm.add_locations({f"Dairy Farm WarpStone": None, "Dairy Farm WarpStone Activated": loc["Dairy Farm WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Dairy Farm WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_dairy_farm, "Warp-Dairy_Farm", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Dairy Farm)", player))

    for s in data["Grass_spawn"]["Dairy Farm"]:
        region_dairy_farm.add_locations({f"Dairy Farm {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Dairy Farm {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail06.connect(region_dairy_farm, "Trail_06-Dairy_Farm")
    multiworld.regions.append(region_dairy_farm)

    # ------------------------------------------------------------------------------------------------------------

    region_trail07 = Region("Trail 07", player, multiworld)
    region_trail07.add_locations({
        "Trail 07: Chest Near Dairy Farm Entrance": loc["Trail 07: Chest Near Dairy Farm Entrance"],
        "Trail 07: Chest North of Bella": loc["Trail 07: Chest North of Bella"],
        "Trail 07: Chest South of Bella": loc["Trail 07: Chest South of Bella"],
        "Trail 07: Chest South of Dakota": loc["Trail 07: Chest South of Dakota"],
    }, SpiritValleyLocation)
    region_trail07.add_locations({
        "Trail 07: Defeat Sally McTits": loc["Trail 07: Defeat Sally McTits"],
        "Trail 07: Defeat Bella": loc["Trail 07: Defeat Bella"],
        "Trail 07: Defeat Dakota": loc["Trail 07: Defeat Dakota"],
        "Trail 07: Defeat Cassidy": loc["Trail 07: Defeat Cassidy"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 07"]:
        region_trail07.add_locations({f"Trail 07 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 07 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_dairy_farm.connect(region_trail07, "Dairy_Farm-Trail_07")
    multiworld.regions.append(region_trail07)

    # ------------------------------------------------------------------------------------------------------------

    region_tumbleweed_town = Region("Tumbleweed Town", player, multiworld)
    region_tumbleweed_town.add_locations({
        "Tumbleweed Town: Chest South of Town": loc["Tumbleweed Town: Chest South of Town"],
        "Tumbleweed Town: Chest North-West of Town": loc["Tumbleweed Town: Chest North-West of Town"],
        "Tumbleweed Town: Chest in House Next to Shop": loc["Tumbleweed Town: Chest in House Next to Shop"],
    }, SpiritValleyLocation)
    region_tumbleweed_town.add_locations({
        "Tumbleweed Town: Defeat Willy Wanker": loc["Tumbleweed Town: Defeat Willy Wanker"],
        "Tumbleweed Town: Defeat Dick Cummings": loc["Tumbleweed Town: Defeat Dick Cummings"],
        "Tumbleweed Town: Defeat Dick Louie": loc["Tumbleweed Town: Defeat Dick Louie"],
    }, SpiritValleyLocation)
    region_tumbleweed_town.add_locations({
        "Complete Main Quest: Dusty Vale awaits": loc["Complete Main Quest: Dusty Vale awaits"],
        "Complete Main Quest: An audience with the King": loc["Complete Main Quest: An audience with the King"],
        "Complete Main Quest: The Grand Cuckold Challenge": loc["Complete Main Quest: The Grand Cuckold Challenge"],
        "Complete Main Quest: A challenge awaits": loc["Complete Main Quest: A challenge awaits"],
        "Complete Main Quest: A new challenger": loc["Complete Main Quest: A new challenger"],
        "Complete Main Quest: Stiff competition": loc["Complete Main Quest: Stiff competition"],
        "Complete Main Quest: Final Fight": loc["Complete Main Quest: Final Fight"],
        "Complete Main Quest: Return of the champion": loc["Complete Main Quest: Return of the champion"],
        "Complete Main Quest: Breeding season": loc["Complete Main Quest: Breeding season"],
        "Complete Main Quest: Mission success": loc["Complete Main Quest: Mission success"],
        "Complete Main Quest: How the Dominoes fall": loc["Complete Main Quest: How the Dominoes fall"],
        "Complete Main Quest: Big balloon adventure": loc["Complete Main Quest: Big balloon adventure"],
    }, SpiritValleyLocation)
    region_tumbleweed_town.add_locations({f"Tumbleweed Town Shop": None}, SpiritValleyLocation)
    multiworld.get_location(f"Tumbleweed Town Shop", player).place_locked_item(spiritItem(f"Shop Accessible", ItemClassification.progression, None, player))

    region_tumbleweed_town.add_locations({f"Tumbleweed Town WarpStone": None, "Tumbleweed Town WarpStone Activated": loc["Tumbleweed Town WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Tumbleweed Town WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_tumbleweed_town, "Warp-Tumbleweed_Town", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Tumbleweed Town)", player))

    region_trail07.connect(region_tumbleweed_town, "Trail_07-Tumbleweed_Town")
    multiworld.regions.append(region_tumbleweed_town)

    # ------------------------------------------------------------------------------------------------------------

    region_trail08 = Region("Trail 08", player, multiworld)
    region_trail08.add_locations({
        "Trail 08: Chest West of Tumbleweed Town Entrance": loc["Trail 08: Chest West of Tumbleweed Town Entrance"],
        "Trail 08: Chest South of Marisa": loc["Trail 08: Chest South of Marisa"],
        "Trail 08: Chest Near Dusty Grotto Entrance": loc["Trail 08: Chest Near Dusty Grotto Entrance"],
    }, SpiritValleyLocation)
    region_trail08.add_locations({
        "Trail 08: Defeat Marisa": loc["Trail 08: Defeat Marisa"],
        "Trail 08: Defeat Jenni": loc["Trail 08: Defeat Jenni"],
        "Trail 08: Defeat Alanna": loc["Trail 08: Defeat Alanna"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 08"]:
        region_trail08.add_locations({f"Trail 08 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 08 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_tumbleweed_town.connect(region_trail08, "Tumbleweed_Town-Trail_08")
    multiworld.regions.append(region_trail08)

    # ------------------------------------------------------------------------------------------------------------

    region_dusty_grotto = Region("Dusty Grotto", player, multiworld)
    region_dusty_grotto.add_locations({
        "Dusty Grotto: Chest Near Crystal": loc["Dusty Grotto: Chest Near Crystal"],
        "Dusty Grotto: Chest West of Skye": loc["Dusty Grotto: Chest West of Skye"],
    }, SpiritValleyLocation)
    region_dusty_grotto.add_locations({
        "Dusty Grotto: Defeat Arnie": loc["Dusty Grotto: Defeat Arnie"],
        "Dusty Grotto: Defeat Crystal": loc["Dusty Grotto: Defeat Crystal"],
        "Dusty Grotto: Defeat Skye": loc["Dusty Grotto: Defeat Skye"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Dusty Grotto"]:
        region_dusty_grotto.add_locations({f"Dusty Grotto {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Dusty Grotto {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail08.connect(region_dusty_grotto, "Trail_08-Dusty_Grotto")
    multiworld.regions.append(region_dusty_grotto)

    # ------------------------------------------------------------------------------------------------------------

    region_old_masters_hut = Region("Old Masters Hut", player, multiworld)
    region_old_masters_hut.add_locations({
        "Old Masters Hut: Chest North of House": loc["Old Masters Hut: Chest North of House"],
        "Old Masters Hut: Chest Next to House": loc["Old Masters Hut: Chest Next to House"],
        "Old Masters Hut: Chest in House": loc["Old Masters Hut: Chest in House"],
        "Old Masters Hut: Chest in House Basement": loc["Old Masters Hut: Chest in House Basement"],
    }, SpiritValleyLocation)
    region_old_masters_hut.add_locations({
        "Complete Main Quest: License to battle": loc["Complete Main Quest: License to battle"],
        "Complete Main Quest: Box pusher": loc["Complete Main Quest: Box pusher"],
        "Complete Main Quest: Total domination": loc["Complete Main Quest: Total domination"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Old Masters Hut"]:
        region_old_masters_hut.add_locations({f"Old Masters Hut {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Old Masters Hut {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_dusty_grotto.connect(region_old_masters_hut, "Dusty_Grotto-Old_Masters_House")
    multiworld.regions.append(region_old_masters_hut)

    # ------------------------------------------------------------------------------------------------------------

    region_cave_of_torment = Region("Cave of Torment", player, multiworld)
    region_cave_of_torment.add_locations({
        "Cave of Torment: Chest East Side of Cave": loc["Cave of Torment: Chest East Side of Cave"],
        "Cave of Torment: Chest North Side of Cave": loc["Cave of Torment: Chest North Side of Cave"],
        "Cave of Torment: Chest West Side of Cave": loc["Cave of Torment: Chest West Side of Cave"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Cave of Torment"]:
        region_cave_of_torment.add_locations({f"Cave of Torment {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Cave of Torment {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_old_masters_hut.connect(region_cave_of_torment, "Old_Masters_Hut-Cave_of_Torment")
    multiworld.regions.append(region_cave_of_torment)

    # ------------------------------------------------------------------------------------------------------------

    region_trail09 = Region("Trail 09", player, multiworld)
    region_trail09.add_locations({
        "Trail 09: Chest near Clementine": loc["Trail 09: Chest near Clementine"],
        "Trail 09: Chest North of Mike": loc["Trail 09: Chest North of Mike"],
        "Trail 09: Chest Near Stone Temple Back Entrance Ledge": loc["Trail 09: Chest Near Stone Temple Back Entrance Ledge"],
    }, SpiritValleyLocation)
    region_trail09.add_locations({
        "Trail 09: Defeat Mike": loc["Trail 09: Defeat Mike"],
        "Trail 09: Defeat Clementine": loc["Trail 09: Defeat Clementine"],
        "Trail 09: Defeat Bonnie": loc["Trail 09: Defeat Bonnie"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 09"]:
        region_trail09.add_locations({f"Trail 09 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 09 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_tumbleweed_town.connect(region_trail09, "Tumbleweed_Town-Trail_09")
    multiworld.regions.append(region_trail09)

    # ------------------------------------------------------------------------------------------------------------

    region_stone_temple = Region("Stone Temple", player, multiworld)
    region_stone_temple.add_locations({
        "Stone Temple 1: Chest Near Trail 09 Entrence": loc["Stone Temple 1: Chest Near Trail 09 Entrence"],
        "Stone Temple 1: Chest Near 6th Crimson Cloak": loc["Stone Temple 1: Chest Near 6th Crimson Cloak"],
        "Stone Temple 1: Chest Near Stone Temple 2 Entrance": loc["Stone Temple 1: Chest Near Stone Temple 2 Entrance"],
    }, SpiritValleyLocation)
    region_stone_temple.add_locations({
        "Stone Temple 1: Defeat 1st Crimson Cloak": loc["Stone Temple 1: Defeat 1st Crimson Cloak"],
        "Stone Temple 1: Defeat 2nd Crimson Cloak": loc["Stone Temple 1: Defeat 2nd Crimson Cloak"],
        "Stone Temple 1: Defeat 3rd Crimson Cloak": loc["Stone Temple 1: Defeat 3rd Crimson Cloak"],
        "Stone Temple 1: Defeat 4th Crimson Cloak": loc["Stone Temple 1: Defeat 4th Crimson Cloak"],
        "Stone Temple 1: Defeat 5th Crimson Cloak": loc["Stone Temple 1: Defeat 5th Crimson Cloak"],
        "Stone Temple 1: Defeat 6th Crimson Cloak": loc["Stone Temple 1: Defeat 6th Crimson Cloak"],
    }, SpiritValleyLocation)
    region_stone_temple.add_locations({
        "Stone Temple 2: Defeat Domino": loc["Stone Temple 2: Defeat Domino"],
    }, SpiritValleyLocation)
    region_stone_temple.add_locations({
        "Complete Main Quest: Quest for the crystal": loc["Complete Main Quest: Quest for the crystal"],
    }, SpiritValleyLocation)
    region_trail09.connect(region_stone_temple, "Trail_09-Stone_Temple")
    multiworld.regions.append(region_stone_temple)

    # ------------------------------------------------------------------------------------------------------------

    region_crash_site = Region("Crash Site", player, multiworld)
    region_crash_site.add_locations({
        "Crash Site: Chest East of Athena": loc["Crash Site: Chest East of Athena"],
        "Crash Site: Chest West of Janet": loc["Crash Site: Chest West of Janet"],
        "Crash Site: Chest South of Janet": loc["Crash Site: Chest South of Janet"],
    }, SpiritValleyLocation)
    region_crash_site.add_locations({
        "Crash Site: Defeat Athena": loc["Crash Site: Defeat Athena"],
        "Crash Site: Defeat Janet": loc["Crash Site: Defeat Janet"],
    }, SpiritValleyLocation)

    region_crash_site.add_locations({f"Crash Site WarpStone": None, "Crash Site WarpStone Activated": loc["Crash Site WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Crash Site WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_crash_site, "Warp-Crash_Site", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Crash Site)", player))

    for s in data["Grass_spawn"]["Crash Site"]:
        region_crash_site.add_locations({f"Crash Site {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Crash Site {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_tumbleweed_town.connect(region_crash_site, "Tumbleweed_Town-Crash_Site")
    multiworld.regions.append(region_crash_site)

    # ------------------------------------------------------------------------------------------------------------

    region_trail10 = Region("Trail 10", player, multiworld)
    region_trail10.add_locations({
        "Trail 10: Chest West of Crash Site Entrance": loc["Trail 10: Chest West of Crash Site Entrance"],
        "Trail 10: Chest Near Eve": loc["Trail 10: Chest Near Eve"],
        "Trail 10: Chest South of Bailee": loc["Trail 10: Chest South of Bailee"],
    }, SpiritValleyLocation)
    region_trail10.add_locations({
        "Trail 10: Defeat Bailee": loc["Trail 10: Defeat Bailee"],
        "Trail 10: Defeat Eve": loc["Trail 10: Defeat Eve"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 10"]:
        region_trail10.add_locations({f"Trail 10 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 10 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Trail 10"]:
        region_trail10.add_locations({f"Trail 10 {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Trail 10 {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Trail 10 {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_crash_site.connect(region_trail10, "Crash_Site-Trail_10")
    multiworld.regions.append(region_trail10)

    # ------------------------------------------------------------------------------------------------------------

    region_coconut_village = Region("Coconut Village", player, multiworld)
    region_coconut_village.add_locations({
        "Coconut Village: Chest North-East in Village": loc["Coconut Village: Chest North-East in Village"],
        "Coconut Village: Chest East of Village": loc["Coconut Village: Chest East of Village"],
        "Coconut Village: Chest in House in the South-East": loc["Coconut Village: Chest in House in the South-East"],
        "Coconut Village: Chest in Temple": loc["Coconut Village: Chest in Temple"],
        "Coconut Village: Chest In Temple After Locked Door": loc["Coconut Village: Chest In Temple After Locked Door"],
    }, SpiritValleyLocation)
    region_coconut_village.add_locations({
        "Complete Side Quest: Professional Pleasurer": loc["Complete Side Quest: Professional Pleasurer"],
    }, SpiritValleyLocation)
    region_coconut_village.add_locations({
        "Complete Main Quest: Welcome to Paradise": loc["Complete Main Quest: Welcome to Paradise"],
        "Complete Main Quest: Savior of Coconut Village": loc["Complete Main Quest: Savior of Coconut Village"],
        "Complete Main Quest: Slippery When Wet": loc["Complete Main Quest: Slippery When Wet"],
        "Complete Main Quest: Glimmering Prize": loc["Complete Main Quest: Glimmering Prize"],
        "Complete Main Quest: Arctic Adventure": loc["Complete Main Quest: Arctic Adventure"],
    }, SpiritValleyLocation)
    region_coconut_village.add_locations({f"Coconut Village Shop": None}, SpiritValleyLocation)
    multiworld.get_location(f"Coconut Village Shop", player).place_locked_item(spiritItem(f"Shop Accessible", ItemClassification.progression, None, player))

    region_coconut_village.add_locations({f"Coconut Village WarpStone": None, "Coconut Village WarpStone Activated": loc["Coconut Village WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Coconut Village WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_coconut_village, "Warp-Coconut_Village", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Coconut Village)", player))

    region_trail10.connect(region_coconut_village, "Trail_10-Coconut_Village")
    multiworld.regions.append(region_coconut_village)

    # ------------------------------------------------------------------------------------------------------------

    region_trail11 = Region("Trail 11", player, multiworld)
    region_trail11.add_locations({
        "Trail 11: Chest Near Alice": loc["Trail 11: Chest Near Alice"],
        "Trail 11: Chest Near Pier": loc["Trail 11: Chest Near Pier"],
        "Trail 11: Chest East of Emilia": loc["Trail 11: Chest East of Emilia"],
        "Trail 11: Chest South of Sydney": loc["Trail 11: Chest South of Sydney"],
    }, SpiritValleyLocation)
    region_trail11.add_locations({
        "Complete Side Quest: Fishmaster’s Challenge": loc["Complete Side Quest: Fishmaster’s Challenge"],
        "Complete Side Quest: Deadly Waters": loc["Complete Side Quest: Deadly Waters"],
    }, SpiritValleyLocation)
    region_trail11.add_locations({
        "Trail 11: Defeat Alice": loc["Trail 11: Defeat Alice"],
        "Trail 11: Defeat Emilia": loc["Trail 11: Defeat Emilia"],
        "Trail 11: Defeat Sydney": loc["Trail 11: Defeat Sydney"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 11"]:
        region_trail11.add_locations({f"Trail 11 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 11 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Trail 11"]:
        region_trail11.add_locations({f"Trail 11 {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Trail 11 {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Trail 11 {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_coconut_village.connect(region_trail11, "Coconut_Village-Trail_11")
    multiworld.regions.append(region_trail11)

    # ------------------------------------------------------------------------------------------------------------

    region_trail12 = Region("Trail 12", player, multiworld)
    region_trail12.add_locations({
        "Trail 12: Chest North of Sophie": loc["Trail 12: Chest North of Sophie"],
        "Trail 12: Chest North of Ciara": loc["Trail 12: Chest North of Ciara"],
    }, SpiritValleyLocation)
    region_trail12.add_locations({
        "Complete Side Quest: Starry Eyed Surprise": loc["Complete Side Quest: Starry Eyed Surprise"],
    }, SpiritValleyLocation)
    region_trail12.add_locations({
        "Trail 12: Defeat Sophie": loc["Trail 12: Defeat Sophie"],
        "Trail 12: Defeat Ciara": loc["Trail 12: Defeat Ciara"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 12"]:
        region_trail12.add_locations({f"Trail 12 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 12 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Trail 12"]:
        region_trail12.add_locations({f"Trail 12 {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Trail 12 {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Trail 12 {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail11.connect(region_trail12, "Trail_11-Trail_12")
    multiworld.regions.append(region_trail12)

    # ------------------------------------------------------------------------------------------------------------

    region_fishing_hut = Region("Fishing Hut", player, multiworld)
    region_fishing_hut.add_locations({
        "Fishing Hut: Chest North-West on the Beach": loc["Fishing Hut: Chest North-West on the Beach"],
        "Fishing Hut: Chest Next to House": loc["Fishing Hut: Chest Next to House"],
        "Fishing Hut: Chest East on the Beach": loc["Fishing Hut: Chest East on the Beach"],
        "Fishing Hut: Chest Eastern Side of Map": loc["Fishing Hut: Chest Eastern Side of Map"],
    }, SpiritValleyLocation)
    region_fishing_hut.add_locations({
        "Complete Side Quest: Fishy Duel": loc["Complete Side Quest: Fishy Duel"],
        "Complete Side Quest: The Art of Fishing": loc["Complete Side Quest: The Art of Fishing"],
    }, SpiritValleyLocation)
    region_fishing_hut.add_locations({
        "Fishing Hut: Defeat Bonnie Baiter": loc["Fishing Hut: Defeat Bonnie Baiter"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Fishing Hut"]:
        region_fishing_hut.add_locations({f"Fishing Hut {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Fishing Hut {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail12.connect(region_fishing_hut, "Trail_12-Fishing_Hut")
    multiworld.regions.append(region_fishing_hut)

    # ------------------------------------------------------------------------------------------------------------

    region_trail13 = Region("Trail 13", player, multiworld)
    region_trail13.add_locations({
        "Trail 13: Chest South-West of 1st Cultist": loc["Trail 13: Chest South-West of 1st Cultist"],
        "Trail 13: Chest North of 1st Cultist": loc["Trail 13: Chest North of 1st Cultist"],
    }, SpiritValleyLocation)
    region_trail13.add_locations({
        "Trail 13: Defeat 1st Cultist": loc["Trail 13: Defeat 1st Cultist"],
        "Trail 13: Defeat 2nd Cultist": loc["Trail 13: Defeat 2nd Cultist"],
    }, SpiritValleyLocation)
    region_trail13.add_locations({
        "Complete Main Quest: Coconut Conundrum": loc["Complete Main Quest: Coconut Conundrum"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 13"]:
        region_trail13.add_locations({f"Trail 13 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 13 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Trail 13"]:
        region_trail13.add_locations({f"Trail 13 {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Trail 13 {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Trail 13 {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail10.connect(region_trail13, "Trail_10-Trail_13")
    multiworld.regions.append(region_trail13)

    # ------------------------------------------------------------------------------------------------------------

    region_trail14 = Region("Trail 14", player, multiworld)
    region_trail14.add_locations({
        "Trail 14: Chest North-West of 1st Cultist": loc["Trail 14: Chest North-West of 1st Cultist"],
        "Trail 14: Chest East of 1st Cultist": loc["Trail 14: Chest East of 1st Cultist"],
        "Trail 14: Chest East of Waystone": loc["Trail 14: Chest East of Waystone"],
    }, SpiritValleyLocation)
    region_trail14.add_locations({
        "Trail 14: Defeat 1st Cultist": loc["Trail 14: Defeat 1st Cultist"],
        "Trail 14: Defeat 2nd Cultist": loc["Trail 14: Defeat 2nd Cultist"],
    }, SpiritValleyLocation)

    region_trail14.add_locations({f"Trail 14 WarpStone": None, "Trail 14 WarpStone Activated": loc["Trail 14 WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Trail 14 WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_trail14, "Warp-Trail_14", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Trail 14)", player))

    for s in data["Grass_spawn"]["Trail 14"]:
        region_trail14.add_locations({f"Trail 14 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 14 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Trail 14"]:
        region_trail14.add_locations({f"Trail 14 {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Trail 14 {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Trail 14 {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail13.connect(region_trail14, "Trail_13-Trail_14")
    multiworld.regions.append(region_trail14)

    # ------------------------------------------------------------------------------------------------------------

    region_island_cave = Region("Island Cave", player, multiworld)
    region_island_cave.add_locations({
        "Island Cave 1: Chest North-West After 1st Cultist": loc["Island Cave 1: Chest North-West After 1st Cultist"],
        "Island Cave 1: Chest East After 2st Cultist": loc["Island Cave 1: Chest East After 2st Cultist"],
        "Island Cave 1: Chest West After 2nd Cultist": loc["Island Cave 1: Chest West After 2nd Cultist"],
        "Island Cave 1: Chest Near 3rd Cultist": loc["Island Cave 1: Chest Near 3rd Cultist"],
    }, SpiritValleyLocation)
    region_island_cave.add_locations({
        "Island Cave 1: Defeat 1st Cultist": loc["Island Cave 1: Defeat 1st Cultist"],
        "Island Cave 1: Defeat 2nd Cultist": loc["Island Cave 1: Defeat 2nd Cultist"],
        "Island Cave 1: Defeat 3rd Cultist": loc["Island Cave 1: Defeat 3rd Cultist"],
        "Island Cave 1: Defeat 4th Cultist": loc["Island Cave 1: Defeat 4th Cultist"],
    }, SpiritValleyLocation)
    region_island_cave.add_locations({
        "Island Cave 2: Defeat Centiboob": loc["Island Cave 2: Defeat Centiboob"]
    }, SpiritValleyLocation)
    region_island_cave.add_locations({
        "Complete Main Quest: Lusty Cultists": loc["Complete Main Quest: Lusty Cultists"]
    }, SpiritValleyLocation)
    region_trail13.connect(region_island_cave, "Trail_13-Island_Cave")
    multiworld.regions.append(region_island_cave)

    # ------------------------------------------------------------------------------------------------------------

    region_cold_harbour = Region("Cold Harbour", player, multiworld)
    region_cold_harbour.add_locations({
        "Cold Harbour: Chest North-East of Waystone": loc["Cold Harbour: Chest North-East of Waystone"],
        "Cold Harbour: Chest East of Iris": loc["Cold Harbour: Chest East of Iris"],
    }, SpiritValleyLocation)
    region_cold_harbour.add_locations({
        "Cold Harbour: Defeat Vanessa": loc["Cold Harbour: Defeat Vanessa"],
        "Cold Harbour: Defeat Iris": loc["Cold Harbour: Defeat Iris"],
    }, SpiritValleyLocation)
    region_cold_harbour.add_locations({
        "Complete Main Quest: The Frigid Maiden": loc["Complete Main Quest: The Frigid Maiden"],
    }, SpiritValleyLocation)

    region_cold_harbour.add_locations({f"Cold Harbour WarpStone": None, "Cold Harbour WarpStone Activated": loc["Cold Harbour WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Cold Harbour WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_cold_harbour, "Warp-Cold_Harbour", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Cold Harbour)", player))

    for s in data["Grass_spawn"]["Cold Harbour"]:
        region_cold_harbour.add_locations({f"Cold Harbour {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Cold Harbour {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Cold Harbour"]:
        region_cold_harbour.add_locations({f"Cold Harbour {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Cold Harbour {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Cold Harbour {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_coconut_village.connect(region_cold_harbour, "Coconut_Village-Cold_Harbour")
    multiworld.regions.append(region_cold_harbour)
    # ------------------------------------------------------------------------------------------------------------

    region_frostville = Region("Frostville", player, multiworld)
    region_frostville.add_locations({
        "Frostville: Chest North of Waystone": loc["Frostville: Chest North of Waystone"],
        "Frostville: Chest South of Waystone": loc["Frostville: Chest South of Waystone"],
        "Frostville: Chest West of Town": loc["Frostville: Chest West of Town"],
    }, SpiritValleyLocation)
    region_frostville.add_locations({
        "Frostville: Defeat Mother Evilyn": loc["Frostville: Defeat Mother Evilyn"],
    }, SpiritValleyLocation)
    region_frostville.add_locations({
        "Complete Main Quest: Arctic Isles": loc["Complete Main Quest: Arctic Isles"],
        "Complete Main Quest: Paisley Bones": loc["Complete Main Quest: Paisley Bones"],
        "Complete Main Quest: Stealing From a Dead Man": loc["Complete Main Quest: Stealing From a Dead Man"],
        "Complete Main Quest: The Lewd Exorcist": loc["Complete Main Quest: The Lewd Exorcist"],
        "Complete Main Quest: The Proposal": loc["Complete Main Quest: The Proposal"],
        "Complete Main Quest: Here Comes the Boom": loc["Complete Main Quest: Here Comes the Boom"],
    }, SpiritValleyLocation)
    region_frostville.add_locations({f"Frostville Shop": None}, SpiritValleyLocation)
    multiworld.get_location(f"Frostville Shop", player).place_locked_item(spiritItem(f"Shop Accessible", ItemClassification.progression, None, player))

    region_frostville.add_locations({f"Frostville WarpStone": None, "Frostville WarpStone Activated": loc["Frostville WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Frostville WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_frostville, "Warp-Frostville", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Frostville)", player))

    region_cold_harbour.connect(region_frostville, "Cold_Harbour-Frostville")
    multiworld.regions.append(region_frostville)

    # ------------------------------------------------------------------------------------------------------------

    region_trail15 = Region("Trail 15", player, multiworld)
    region_trail15.add_locations({
        "Trail 15: Chest South of Frostville Entrence": loc["Trail 15: Chest South of Frostville Entrence"],
        "Trail 15: Chest West of Mia": loc["Trail 15: Chest West of Mia"],
        "Trail 15: Chest South-West of Olga": loc["Trail 15: Chest South-West of Olga"],
    }, SpiritValleyLocation)
    region_trail15.add_locations({
        "Complete Side Quest: Arctic Menace": loc["Complete Side Quest: Arctic Menace"],
    }, SpiritValleyLocation)
    region_trail15.add_locations({
        "Trail 15: Defeat Mia": loc["Trail 15: Defeat Mia"],
        "Trail 15: Defeat Olga": loc["Trail 15: Defeat Olga"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 15"]:
        region_trail15.add_locations({f"Trail 15 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 15 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_frostville.connect(region_trail15, "Frostville-Trail_15")
    multiworld.regions.append(region_trail15)

    # ------------------------------------------------------------------------------------------------------------

    region_trail16 = Region("Trail 16", player, multiworld)
    region_trail16.add_locations({
        "Trail 16: Chest Near Northern Trail 15 Entrence": loc["Trail 16: Chest Near Northern Trail 15 Entrence"],
        "Trail 16: Chest North of Karin": loc["Trail 16: Chest North of Karin"],
        "Trail 16: Chest North-West of Karin": loc["Trail 16: Chest North-West of Karin"],
        "Trail 16: Chest East of Dahlia": loc["Trail 16: Chest East of Dahlia"],
    }, SpiritValleyLocation)
    region_trail16.add_locations({
        "Trail 16: Defeat Karin": loc["Trail 16: Defeat Karin"],
        "Trail 16: Defeat Dahlia": loc["Trail 16: Defeat Dahlia"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 16"]:
        region_trail16.add_locations({f"Trail 16 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 16 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Trail 16"]:
        region_trail16.add_locations({f"Trail 16 {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Trail 16 {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Trail 16 {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail15.connect(region_trail16, "Trail_15-Trail-16")
    multiworld.regions.append(region_trail16)

    # ------------------------------------------------------------------------------------------------------------

    region_trail16_cave = Region("Trail 16 Cave", player, multiworld)
    for s in data["Grass_spawn"]["Trail 16 Cave"]:
        region_trail16_cave.add_locations({f"Trail 16 Cave {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 16 Cave {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail16.connect(region_trail16_cave, "Trail_16-Trail_16_Cave")
    multiworld.regions.append(region_trail16_cave)

    # ------------------------------------------------------------------------------------------------------------

    region_abandoned_mine = Region("Abandoned Mine", player, multiworld)
    region_abandoned_mine.add_locations({
        "Abandoned Mine: Chest North of Trail 16 Entrence": loc["Abandoned Mine: Chest North of Trail 16 Entrence"],
        "Abandoned Mine: Chest South-West of House": loc["Abandoned Mine: Chest South-West of House"],
    }, SpiritValleyLocation)
    region_abandoned_mine.add_locations({
        "Complete Main Quest: Demand for Dynamite": loc["Complete Main Quest: Demand for Dynamite"],
        "Complete Main Quest: Suit In Hand": loc["Complete Main Quest: Suit In Hand"],
        "Complete Main Quest: Fishing For Treasure": loc["Complete Main Quest: Fishing For Treasure"],
    }, SpiritValleyLocation)

    region_abandoned_mine.add_locations({f"Abandoned Mine WarpStone": None, "Abandoned Mine WarpStone Activated": loc["Abandoned Mine WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Abandoned Mine WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_abandoned_mine, "Warp-Abandoned_Mine", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Abandoned Mine)", player))

    for s in data["Grass_spawn"]["Abandoned Mine"]:
        region_abandoned_mine.add_locations({f"Abandoned Mine {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Abandoned Mine {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Abandoned Mine"]:
        region_abandoned_mine.add_locations({f"Abandoned Mine {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Abandoned Mine {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Abandoned Mine {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail16.connect(region_abandoned_mine, "Trail_16-Abandoned_Mine")
    multiworld.regions.append(region_abandoned_mine)

    # ------------------------------------------------------------------------------------------------------------

    region_trail17 = Region("Trail 17", player, multiworld)
    region_trail17.add_locations({
        "Trail 17: Chest North of Clara": loc["Trail 17: Chest North of Clara"],
        "Trail 17: Chest South-East of Liv": loc["Trail 17: Chest South-East of Liv"],
        "Trail 17: Chest North-East of Karly": loc["Trail 17: Chest North-East of Karly"],
    }, SpiritValleyLocation)
    region_trail17.add_locations({
        "Complete Side Quest: Legend of the Valkyrie part 1.": loc["Complete Side Quest: Legend of the Valkyrie part 1."],
        "Complete Side Quest: Legend of the Valkyrie part 2.": loc["Complete Side Quest: Legend of the Valkyrie part 2."],
    }, SpiritValleyLocation)
    region_trail17.add_locations({
        "Trail 17: Defeat Clara": loc["Trail 17: Defeat Clara"],
        "Trail 17: Defeat Liv": loc["Trail 17: Defeat Liv"],
        "Trail 17: Defeat Karly": loc["Trail 17: Defeat Karly"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 17"]:
        region_trail17.add_locations({f"Trail 17 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 17 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Trail 17"]:
        region_trail17.add_locations({f"Trail 17 {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Trail 17 {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Trail 17 {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_frostville.connect(region_trail17, "Frostville-Trail_17")
    multiworld.regions.append(region_trail17)

    # ------------------------------------------------------------------------------------------------------------

    region_trail18 = Region("Trail 18", player, multiworld)
    region_trail18.add_locations({
        "Trail 18: Chest South of Anabelle": loc["Trail 18: Chest South of Anabelle"],
        "Trail 18: Chest in North Part of Map": loc["Trail 18: Chest in North Part of Map"],
        "Trail 18: Chest North of Ingrid": loc["Trail 18: Chest North of Ingrid"],
    }, SpiritValleyLocation)
    region_trail18.add_locations({
        "Trail 18: Defeat Stacy": loc["Trail 18: Defeat Stacy"],
        "Trail 18: Defeat Anabelle": loc["Trail 18: Defeat Anabelle"],
        "Trail 18: Defeat Ingrid": loc["Trail 18: Defeat Ingrid"],
    }, SpiritValleyLocation)
    region_trail18.add_locations({
        "Complete Main Quest: Crimson Chase": loc["Complete Main Quest: Crimson Chase"],
    }, SpiritValleyLocation)

    region_trail18.add_locations({f"Trail 18 WarpStone": None, "Trail 18 WarpStone Activated": loc["Trail 18 WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Trail 18 WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_trail18, "Warp-Trail_18", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Trail 18)", player))

    for s in data["Grass_spawn"]["Trail 18"]:
        region_trail18.add_locations({f"Trail 18 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 18 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Trail 18"]:
        region_trail18.add_locations({f"Trail 18 {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Trail 18 {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Trail 18 {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail17.connect(region_trail18, "Trail_17-Trail_18")
    multiworld.regions.append(region_trail18)

    # ------------------------------------------------------------------------------------------------------------

    region_artic_temple = Region("Artic Temple", player, multiworld)
    region_artic_temple.add_locations({
        "Artic Temple: Chest in South-East": loc["Artic Temple: Chest in South-East"],
        "Artic Temple: Chest in West": loc["Artic Temple: Chest in West"],
        "Artic Temple: Chest in North-West": loc["Artic Temple: Chest in North-West"],
    }, SpiritValleyLocation)
    region_artic_temple.add_locations({
        "Artic Temple 1: Defeat 1st Crimson Cloak": loc["Artic Temple 1: Defeat 1st Crimson Cloak"],
        "Artic Temple 1: Defeat 2nd Crimson Cloak": loc["Artic Temple 1: Defeat 2nd Crimson Cloak"],
        "Artic Temple 1: Defeat 3rd Crimson Cloak": loc["Artic Temple 1: Defeat 3rd Crimson Cloak"],
        "Artic Temple 1: Defeat 4th Crimson Cloak": loc["Artic Temple 1: Defeat 4th Crimson Cloak"],
        "Artic Temple 1: Defeat 5th Crimson Cloak": loc["Artic Temple 1: Defeat 5th Crimson Cloak"],
        "Artic Temple 2: Defeat Crimson Countess": loc["Artic Temple 2: Defeat Crimson Countess"],
    }, SpiritValleyLocation)
    region_artic_temple.add_locations({
        "Complete Main Quest: Arctic Harmony": loc["Complete Main Quest: Arctic Harmony"],
    }, SpiritValleyLocation)

    region_trail18.connect(region_artic_temple, "Trail_18-Artic_Temple")
    multiworld.regions.append(region_artic_temple)

    # ------------------------------------------------------------------------------------------------------------

    region_trail19 = Region("Trail 19", player, multiworld)
    region_trail19.add_locations({
        "Trail 19: Chest Near Start": loc["Trail 19: Chest Near Start"],
        "Trail 19: Chest South of 1st Crimson Cloak": loc["Trail 19: Chest South of 1st Crimson Cloak"],
        "Trail 19: Chest East of 2nd Crimson Cloak": loc["Trail 19: Chest East of 2nd Crimson Cloak"],
    }, SpiritValleyLocation)
    region_trail19.add_locations({
        "Trail 19: Defeat 1st Crimson Cloak": loc["Trail 19: Defeat 1st Crimson Cloak"],
        "Trail 19: Defeat 2nd Crimson Cloak": loc["Trail 19: Defeat 2nd Crimson Cloak"],
        "Trail 19: Defeat 3rd Crimson Cloak": loc["Trail 19: Defeat 3rd Crimson Cloak"],
    }, SpiritValleyLocation)
    region_trail19.add_locations({
        "Complete Main Quest: Through the Portal": loc["Complete Main Quest: Through the Portal"],
    }, SpiritValleyLocation)

    region_trail19.add_locations({f"Trail 19 WarpStone": None, "Trail 19 WarpStone Activated": loc["Trail 19 WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Trail 19 WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_trail19, "Warp-Trail_19", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Trail 19)", player))

    for s in data["Grass_spawn"]["Trail 19"]:
        region_trail19.add_locations({f"Trail 19 Grass - {s}": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 19 Grass - {s}", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail18.connect(region_trail19, "Trail_18-Trail_19")
    multiworld.regions.append(region_trail19)

    # ------------------------------------------------------------------------------------------------------------

    region_trail20 = Region("Trail 20", player, multiworld)

    region_trail20.add_locations({
        "Trail 20: Chest Near 1st Crimson Cloak": loc["Trail 20: Chest Near 1st Crimson Cloak"],
        "Trail 20: Chest Near 2nd Crimson Cloak": loc["Trail 20: Chest Near 2nd Crimson Cloak"],
        "Trail 20: Chest Near Cave Entrance": loc["Trail 20: Chest Near Cave Entrance"],
    }, SpiritValleyLocation)
    region_trail20.add_locations({
        "Trail 20: Defeat 1st Crimson Cloak": loc["Trail 20: Defeat 1st Crimson Cloak"],
        "Trail 20: Defeat 2nd Crimson Cloak": loc["Trail 20: Defeat 2nd Crimson Cloak"],
        "Trail 20: Defeat 3rd Crimson Cloak": loc["Trail 20: Defeat 3rd Crimson Cloak"],
    }, SpiritValleyLocation)
    region_trail20.add_locations({
        "Complete Main Quest: Sanctuary Shakedown": loc["Complete Main Quest: Sanctuary Shakedown"],
        "Complete Main Quest: Breezie Runs Free": loc["Complete Main Quest: Breezie Runs Free"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 20"]:
        region_trail20.add_locations({f"Trail 20 Grass - {s}": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 20 Grass - {s}", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail19.connect(region_trail20, "Trail_19-Trail_20")
    multiworld.regions.append(region_trail20)

    # ------------------------------------------------------------------------------------------------------------

    region_trail21 = Region("Trail 21", player, multiworld)

    region_trail21.add_locations({
        "Trail 21: Chest Near Pushable Bolder": loc["Trail 21: Chest Near Pushable Bolder"],
        "Trail 21: Chest North of Pond": loc["Trail 21: Chest North of Pond"],
        "Trail 21: Chest South area of map": loc["Trail 21: Chest South area of map"],
    }, SpiritValleyLocation)
    region_trail21.add_locations({
        "Trail 21: Defeat 1st Crimson Cloak": loc["Trail 21: Defeat 1st Crimson Cloak"],
        "Trail 21: Defeat 2nd Crimson Cloak": loc["Trail 21: Defeat 2nd Crimson Cloak"],
        "Trail 21: Defeat Kinley": loc["Trail 21: Defeat Kinley"],
    }, SpiritValleyLocation)
    region_trail21.add_locations({
        "Complete Main Quest: Hostage Situation": loc["Complete Main Quest: Hostage Situation"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 21"]:
        region_trail21.add_locations({f"Trail 21 {s} Grass": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 21 {s} Grass", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))
    for s in data["Water_spawn"]["Trail 21"]:
        region_trail21.add_locations({f"Trail 21 {s} Water": None}, SpiritValleyLocation)
        set_rule(multiworld.get_location(f"Trail 21 {s} Water", player), lambda state: state.has("Fishing Rod", player))
        multiworld.get_location(f"Trail 21 {s} Water", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail20.connect(region_trail21, "Trail_20-Trail_21")
    multiworld.regions.append(region_trail21)

    # ------------------------------------------------------------------------------------------------------------

    region_spirit_passage = Region("Spirit Passage", player, multiworld)
    region_spirit_passage.add_locations({
        "Trail Spirit Passage: Chest north of first fork in path": loc["Trail Spirit Passage: Chest north of first fork in path"],
        "Trail Spirit Passage: Chest in first loop area": loc["Trail Spirit Passage: Chest in first loop area"],
        "Trail Spirit Passage: Chest north of first loop area": loc["Trail Spirit Passage: Chest north of first loop area"],
        "Trail Spirit Passage: Chest near 5th Crimson Cloak": loc["Trail Spirit Passage: Chest near 5th Crimson Cloak"],
    }, SpiritValleyLocation)
    region_spirit_passage.add_locations({
        "Trail Spirit Passage: Defeat 1st Crimson Cloak": loc["Trail Spirit Passage: Defeat 1st Crimson Cloak"],
        "Trail Spirit Passage: Defeat 2nd Crimson Cloak": loc["Trail Spirit Passage: Defeat 2nd Crimson Cloak"],
        "Trail Spirit Passage: Defeat 3rd Crimson Cloak": loc["Trail Spirit Passage: Defeat 3rd Crimson Cloak"],
        "Trail Spirit Passage: Defeat 4th Crimson Cloak": loc["Trail Spirit Passage: Defeat 4th Crimson Cloak"],
        "Trail Spirit Passage: Defeat 5th Crimson Cloak": loc["Trail Spirit Passage: Defeat 5th Crimson Cloak"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Spirit Passage"]:
        region_trail21.add_locations({f"Spirit Passage Grass - {s}": None}, SpiritValleyLocation)
        multiworld.get_location(f"Spirit Passage Grass - {s}", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail20.connect(region_spirit_passage, "Trail_20-Spirit_Passage")
    multiworld.regions.append(region_spirit_passage)

    # ------------------------------------------------------------------------------------------------------------

    region_trail22 = Region("Trail 22", player, multiworld)
    region_trail22.add_locations({
        "Trail 22: Chest north west of pond": loc["Trail 22: Chest north west of pond"],
        "Trail 22: Chest north path before large grass patch": loc["Trail 22: Chest north path before large grass patch"],
        "Trail 22: Chest north of large grass patch": loc["Trail 22: Chest north of large grass patch"],
        "Trail 22: Chest west side of lake near waypoint": loc["Trail 22: Chest west side of lake near waypoint"],
    }, SpiritValleyLocation)
    region_trail22.add_locations({
        "Trail 22: Defeat 1st Crimson Cloak": loc["Trail 22: Defeat 1st Crimson Cloak"],
        "Trail 22: Defeat 2nd Crimson Cloak": loc["Trail 22: Defeat 2nd Crimson Cloak"],
        "Trail 22: Defeat 3rd Crimson Cloak": loc["Trail 22: Defeat 3rd Crimson Cloak"],
    }, SpiritValleyLocation)
    region_trail22.add_locations({
        "Complete Main Quest: Desperate Dash": loc["Complete Main Quest: Desperate Dash"],
        "Complete Side Quest: Hunt for the Centiboob part 1.": loc["Complete Side Quest: Hunt for the Centiboob part 1."],
        "Complete Side Quest: Hunt for the Centiboob part 2.": loc["Complete Side Quest: Hunt for the Centiboob part 2."],
        "Complete Side Quest: Hunt for the Centiboob part 3.": loc["Complete Side Quest: Hunt for the Centiboob part 3."],
    }, SpiritValleyLocation)

    region_trail22.add_locations({f"Trail 22 WarpStone": None, "Trail 22 WarpStone Activated": loc["Trail 22 WarpStone Activated"]}, SpiritValleyLocation)
    multiworld.get_location(f"Trail 22 WarpStone", player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, player))
    if options.randomise_warps.value:
        region_warp.connect(region_trail22, "Warp-Trail_22", lambda state: state.has("Warp Obtainable", player) and state.has("Warp Cords(Trail 22)", player))

    for s in data["Grass_spawn"]["Trail 22"]:
        region_trail22.add_locations({f"Trail 22 Grass - {s}": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 22 Grass - {s}", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_spirit_passage.connect(region_trail22, "Spirit_Passage-Trail_22")
    multiworld.regions.append(region_trail22)

    # ------------------------------------------------------------------------------------------------------------

    region_trail22_cave = Region("Trail 22 Cave", player, multiworld)
    region_trail22_cave.add_locations({
        "Trail 22 Cave: Chest": loc["Trail 22 Cave: Chest"],
    }, SpiritValleyLocation)

    for s in data["Grass_spawn"]["Trail 22 Cave"]:
        region_trail22_cave.add_locations({f"Trail 22 Cave Grass - {s}": None}, SpiritValleyLocation)
        multiworld.get_location(f"Trail 22 Cave Grass - {s}", player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, player))

    region_trail22.connect(region_trail22_cave, "Trail_22-Trail_22_Cave")
    multiworld.regions.append(region_trail22_cave)

    # ------------------------------------------------------------------------------------------------------------

    region_inner_grove = Region("Inner Grove", player, multiworld)
    region_inner_grove.add_locations({
        "Inner Grove: Defeat Spirit Mother": loc["Inner Grove: Defeat Spirit Mother"],
    }, SpiritValleyLocation)
    region_inner_grove.add_locations({
        "Complete Main Quest: Battle for Spirit Valley": loc["Complete Main Quest: Battle for Spirit Valley"],
    }, SpiritValleyLocation)

    region_trail22.connect(region_inner_grove, "Trail_22-Inner_Grove")
    multiworld.regions.append(region_inner_grove)

    # ------------------------------------------------------------------------------------------------------------
"""
