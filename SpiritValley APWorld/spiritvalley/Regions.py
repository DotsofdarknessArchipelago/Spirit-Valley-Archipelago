from BaseClasses import Region, ItemClassification, EntranceType
from worlds.generic.Rules import set_rule
from worlds.spiritvalley import spirit_locations, SpiritValleyLocation, spirit_affection_locations, Rare_spirit_locations, spiritItem
from worlds.spiritvalley.Data_Regions import regions, mapid_to_text, transition_areas, specical_transition_areas


def Generate_Map(multiworld, player, options, loc, data):
    hub_region = Region("Menu", player, multiworld)
    multiworld.regions.append(hub_region)

    is_ut = getattr(multiworld, "generation_is_fake", False)

    region_warp = Region("Warp", player, multiworld)
    multiworld.regions.append(region_warp)
    join("Menu", "Warp", multiworld, player, False)

    if options.Spirit_Locations.value:
        region_spirit = Region("Spirits", player, multiworld)

        if options.Randomise_Spawns.value:
            region_spirit.add_locations(spirit_locations, SpiritValleyLocation)
        else:
            sloc = spirit_locations.copy()
            del sloc["Obtain a EV-3 Spirit"]
            region_spirit.add_locations(sloc, SpiritValleyLocation)

        if options.Spirit_Affection.value:
            if options.Randomise_Spawns.value:
                region_spirit.add_locations(spirit_affection_locations, SpiritValleyLocation)
            else:
                sloc = spirit_affection_locations.copy()
                del sloc["Get EV-3 to Affection LV1"]
                del sloc["Get EV-3 to Affection LV2"]
                del sloc["Get EV-3 to Affection LV3"]
                del sloc["Get EV-3 to Affection LV4"]
                del sloc["Get EV-3 to Affection LV5"]
                region_spirit.add_locations(sloc, SpiritValleyLocation)

        if options.Rare_Locations.value:
            if options.Randomise_Spawns.value:
                region_spirit.add_locations(Rare_spirit_locations, SpiritValleyLocation)
            else:
                sloc = Rare_spirit_locations.copy()
                del sloc["Obtain a Rare EV-3 Spirit"]
                region_spirit.add_locations(sloc, SpiritValleyLocation)

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

        if r.grass and not is_ut:
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

        if r.water and not is_ut:
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
            for e in r.exits:
                ex = map.create_exit(f"{r.map_id} {e}")
                ex.randomization_type = EntranceType.TWO_WAY

                if is_ut: continue

                en = map.create_er_target(f"{r.map_id} {e}")
                en.randomization_type = EntranceType.TWO_WAY

        if r.map_id in ["Greensvale_Merchant","TumbleweedTown_Merchant","CoconutVillage_Merchant","Frostville1_Merchant"]:
            map.add_locations({f"{mapid_to_text[r.map_id]} Shop": None}, SpiritValleyLocation)
            multiworld.get_location(f"{mapid_to_text[r.map_id]} Shop", player).place_locked_item(spiritItem(f"Shop Accessible", ItemClassification.progression, None, player))


        multiworld.regions.append(map)

    join("Menu", "OakwoodVillage", multiworld, player, True)
    join("OakwoodVillage", "OakwoodVillage_Clinic", multiworld, player, False)
    join("OakwoodVillage", "OakwoodVillage_Hq", multiworld, player, False)

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