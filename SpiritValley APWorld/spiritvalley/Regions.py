from BaseClasses import Region, ItemClassification, EntranceType
from rule_builder.rules import Has
from worlds.spiritvalley import spirit_locations, SpiritValleyLocation, spirit_affection_locations, Rare_spirit_locations, spiritItem
from worlds.spiritvalley.Data_Regions import regions, mapid_to_text, transition_areas, specical_transition_areas

disabledmainmissionbattles = ["Trail 02: Defeat Crimson Agent","Tumbleweed Town: Defeat Willy Wanker","Tumbleweed Town: Defeat Dick Cummings","Tumbleweed Town: Defeat Dick Louie","Frostville: Defeat Mother Evilyn","Trail 21: Defeat Kinley"]

def Generate_Map(world):
    hub_region = Region("Menu", world.player, world.multiworld)

    if world.options.goal.value == 1:
        hub_region.add_locations({"Catch all Spirits": world.location_name_to_id["Catch all Spirits"]}, SpiritValleyLocation)
    elif world.options.goal.value == 2:
        hub_region.add_locations({"Catch all Rare Spirits": world.location_name_to_id["Catch all Rare Spirits"]}, SpiritValleyLocation)
    elif world.options.goal.value == 3:
        hub_region.add_locations({"Get All Spirits To Affection Lv5": world.location_name_to_id["Get All Spirits To Affection Lv5"]}, SpiritValleyLocation)

    world.multiworld.regions.append(hub_region)

    is_ut = getattr(world.multiworld, "generation_is_fake", False)

    region_warp = Region("Warp", world.player, world.multiworld)
    world.multiworld.regions.append(region_warp)
    join("Menu", "Warp", world.multiworld, world.player, False)

    if world.options.Spirit_Locations.value:
        region_spirit = Region("Spirits", world.player, world.multiworld)

        if world.options.Randomise_Spawns.value or world.options.goal.value != 0:
            region_spirit.add_locations(spirit_locations, SpiritValleyLocation)
        else:
            sloc = spirit_locations.copy()
            del sloc["Obtain a EV-3 Spirit"]
            region_spirit.add_locations(sloc, SpiritValleyLocation)

        if world.options.Spirit_Affection.value:
            if world.options.Randomise_Spawns.value or world.options.goal.value != 0:
                region_spirit.add_locations(spirit_affection_locations, SpiritValleyLocation)
            else:
                sloc = spirit_affection_locations.copy()
                del sloc["Get EV-3 to Affection LV1"]
                del sloc["Get EV-3 to Affection LV2"]
                del sloc["Get EV-3 to Affection LV3"]
                del sloc["Get EV-3 to Affection LV4"]
                del sloc["Get EV-3 to Affection LV5"]
                region_spirit.add_locations(sloc, SpiritValleyLocation)

        if world.options.Rare_Locations.value:
            if world.options.Randomise_Spawns.value or world.options.goal.value != 0:
                region_spirit.add_locations(Rare_spirit_locations, SpiritValleyLocation)
            else:
                sloc = Rare_spirit_locations.copy()
                del sloc["Obtain a Rare EV-3 Spirit"]
                region_spirit.add_locations(sloc, SpiritValleyLocation)

        world.multiworld.regions.append(region_spirit)
        hub_region.connect(region_spirit, "Menu-Spirit")


    for r in regions:
        map = Region(r.map_id, world.player, world.multiworld)

        if r.warpable:
            map.add_locations({f"{mapid_to_text[r.map_id]} WarpStone": None, f"{mapid_to_text[r.map_id]} WarpStone Activated": world.location_name_to_id[f"{mapid_to_text[r.map_id]} WarpStone Activated"]}, SpiritValleyLocation)
            world.multiworld.get_location(f"{mapid_to_text[r.map_id]} WarpStone", world.player).place_locked_item(spiritItem(f"Warp Obtainable", ItemClassification.progression, None, world.player))
            if world.options.randomise_warps.value:
                region_warp.connect(map, f"Warp->{r.map_id}", lambda state: state.has("Warp Obtainable", world.player) and state.has(f"Warp Cords({r.map_id})", world.player))
                map.connect(region_warp, f"{r.map_id}->Warp", lambda state: state.has("Warp Obtainable", world.player))

        if r.grass and not is_ut:
            if r.map_id == "Trail16_Top":
                for s in world.data["Grass_spawn"]["Trail16"]:
                    map.add_locations({f"{mapid_to_text[r.map_id]} {s} Grass": None}, SpiritValleyLocation)
                    world.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", world.player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, world.player))
            elif r.map_id == "Trail20_Right":
                for s in world.data["Grass_spawn"]["Trail20"]:
                    map.add_locations({f"{mapid_to_text[r.map_id]} {s} Grass": None}, SpiritValleyLocation)
                    world.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", world.player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, world.player))
            else:
                for s in world.data["Grass_spawn"][r.map_id]:
                    map.add_locations({f"{mapid_to_text[r.map_id]} {s} Grass": None}, SpiritValleyLocation)
                    world.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", world.player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, world.player))
                    if r.map_id == "Trail16_Cave":
                        world.set_rule(world.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", world.player), Has("Fishy Scent"))
                    if r.map_id == "Trail22_Cave":
                        world.set_rule(world.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Grass", world.player), Has("Scent Mixture"))

        if r.water and not is_ut:
            for s in world.data["Water_spawn"][r.map_id]:
                map.add_locations({f"{mapid_to_text[r.map_id]} {s} Water": None}, SpiritValleyLocation)
                world.set_rule(world.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Water", world.player), Has("Fishing Rod"))
                world.multiworld.get_location(f"{mapid_to_text[r.map_id]} {s} Water", world.player).place_locked_item(spiritItem(f"{s} Obtainable", ItemClassification.progression, None, world.player))

        if r.chest_locations is not None:
            for l in r.chest_locations:
                map.add_locations({l:world.location_name_to_id[l]}, SpiritValleyLocation)

        if r.trainer_locations is not None:
            for l in r.trainer_locations:
                if l in disabledmainmissionbattles and not world.options.Main_Missions.value:
                    continue
                if l=="Trail 07: Defeat Sally McTits" and not world.options.Side_Missions.value:
                    continue

                map.add_locations({l:world.location_name_to_id[l]}, SpiritValleyLocation)


        if r.quest_locations is not None:
            for l in r.quest_locations:
                if world.options.Single_Catch.value:
                    if l == "Complete Side Quest: Perky Petunia" or l == "Complete Side Quest: Starry Eyed Surprise":
                        continue
                if world.options.goal.value == 0:
                    if l == "Complete Side Quest: Simulated Scuffle" or l == "Complete Side Quest: Gold Plated":
                        continue
                if (l.startswith("Complete Main Quest") and world.options.Main_Missions.value) or (l.startswith("Complete Side Quest") and world.options.Side_Missions.value):
                    map.add_locations({l:world.location_name_to_id[l]}, SpiritValleyLocation)

        if world.options.randomise_map.value:
            for e in r.exits:
                ex = map.create_exit(f"{r.map_id} {e}")
                ex.randomization_type = EntranceType.TWO_WAY

                if is_ut: continue

                en = map.create_er_target(f"{r.map_id} {e}")
                en.randomization_type = EntranceType.TWO_WAY

        if r.map_id in ["Greensvale_Merchant","TumbleweedTown_Merchant","CoconutVillage_Merchant","Frostville1_Merchant"]:
            map.add_locations({f"{mapid_to_text[r.map_id]} Shop": None}, SpiritValleyLocation)
            world.multiworld.get_location(f"{mapid_to_text[r.map_id]} Shop", world.player).place_locked_item(spiritItem(f"Shop Accessible", ItemClassification.progression, None, world.player))


        world.multiworld.regions.append(map)

    join("Menu", "OakwoodVillage", world.multiworld, world.player, True)
    join("OakwoodVillage", "OakwoodVillage_Clinic", world.multiworld, world.player, False)
    join("OakwoodVillage", "OakwoodVillage_Hq", world.multiworld, world.player, False)

    if not world.options.randomise_map.value:
        for t in [*transition_areas,*specical_transition_areas]:
            join(t.scene1_name,t.scene2_name,world.multiworld,world.player,t.oneway)
    else:
        for t in specical_transition_areas:
            join(t.scene1_name,t.scene2_name,world.multiworld,world.player,t.oneway)

def join(r1,r2,multiworld,player,oneway):
    region1 = multiworld.get_region(r1, player)
    region2 = multiworld.get_region(r2, player)

    region1.connect(region2,f"{r1}->{r2}")
    if not oneway:
        region2.connect(region1,f"{r2}->{r1}")