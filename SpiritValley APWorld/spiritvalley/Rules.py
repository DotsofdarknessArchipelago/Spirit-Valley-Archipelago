import dataclasses
from typing import Any, override, Iterable

from BaseClasses import LocationProgressType, CollectionState, MultiWorld
from NetUtils import JSONMessagePart
from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, Has, HasAny, True_, CanReachLocation, CanReachRegion, HasAll
from worlds.spiritvalley.Data_Spirits import obtainable_spirit_list
from worlds.spiritvalley.Items import affection_shop_items, spirit_crystal_shop_items
from worlds.spiritvalley.Options import randomise_map, Main_Missions


def SpiritObtain(spirit: str) -> Rule[Any]:
    return Has(f"{spirit} Obtainable") & HasAny(*spirit_crystal_shop_items) & Has("Shop Accessible")

def SpiritRareObtain(spirit: str) -> Rule[Any]:
    return SpiritObtain(spirit) & Has("Elusive Scent Available in Shop")

def SpiritAffection(spirit: str) -> Rule[Any]:
    return SpiritObtain(spirit) & HasAny(*affection_shop_items)


def SpiritObtainAll() -> Rule[Any]:
    r = None
    for spirit in obtainable_spirit_list:
        if r is None:
            r = SpiritObtain(spirit)
        else:
            r = r & SpiritObtain(spirit)
    return r

def SpiritRareObtainAll() -> Rule[Any]:
    r = None
    for spirit in obtainable_spirit_list:
        if r is None:
            r = SpiritRareObtain(spirit)
        else:
            r = r & SpiritRareObtain(spirit)
    return r

def SpiritAffectionAll() -> Rule[Any]:
    r = None
    for spirit in obtainable_spirit_list:
        if r is None:
            r = SpiritAffection(spirit)
        else:
            r = r & SpiritAffection(spirit)
    return r


def SetRules(world):

    #MAIN MISSION RULES
    if world.options.Main_Missions.value:
        #                                             RULE LOCATION                                                                 PREVIOUS MISSION LOCATION                                               ITEM REQUIRED
        #world.set_rule(world.multiworld.get_location("Complete Main Quest: Doctor’s Appointment", world.player),                   True_                                                                   & True_())
        #world.set_rule(world.multiworld.get_location("Complete Main Quest: Captain Maria", world.player),                          CanReachLocation("Complete Main Quest: Doctor’s Appointment")           & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: First Orders", world.player),                            CanReachLocation("Complete Main Quest: Captain Maria")                  & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Crimson Agent", world.player),                           CanReachLocation("Complete Main Quest: First Orders")                   & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Super Secret Orders", world.player),                     CanReachLocation("Complete Main Quest: Crimson Agent")                  & Has("Super Secret Orders"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: First Mission: Success!", world.player),                 CanReachLocation("Complete Main Quest: Super Secret Orders")            & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Onward to Greensvale", world.player),                    CanReachLocation("Complete Main Quest: First Mission: Success!")        & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Temple Investigation", world.player),                    CanReachLocation("Complete Main Quest: Onward to Greensvale")           & Has("Ancient Temple Key"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Harmonious Disturbance", world.player),                  CanReachLocation("Complete Main Quest: Temple Investigation")           & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Consulting Dolly", world.player),                        CanReachLocation("Complete Main Quest: Harmonious Disturbance")         & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Becky can fix it", world.player),                        CanReachLocation("Complete Main Quest: Consulting Dolly")               & Has("Cracked Power Crystal"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Hunt for the chunk", world.player),                      CanReachLocation("Complete Main Quest: Becky can fix it")               & Has("Raw Crystal Chunk"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Bridge crossing", world.player),                         CanReachLocation("Complete Main Quest: Hunt for the chunk")             & Has("Power Crystal"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Dusty Vale awaits", world.player),                       CanReachLocation("Complete Main Quest: Bridge crossing")                & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: An audience with the King", world.player),               CanReachLocation("Complete Main Quest: Dusty Vale awaits")              & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: The Grand Cuckold Challenge", world.player),             CanReachLocation("Complete Main Quest: An audience with the King")      & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: License to battle", world.player),                       CanReachLocation("Complete Main Quest: The Grand Cuckold Challenge")    & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Box pusher", world.player),                              CanReachLocation("Complete Main Quest: License to battle")              & Has("Video Cassette"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Total domination", world.player),                        CanReachLocation("Complete Main Quest: Box pusher")                     & SpiritObtain(world.data["MAIN_QUEST_TOTAL_DOMINATION"]))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: A challenge awaits", world.player),                      CanReachLocation("Complete Main Quest: Total domination")               & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: A new challenger", world.player),                        CanReachLocation("Complete Main Quest: A challenge awaits")             & Has("Spirit Handler License"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Stiff competition", world.player),                       CanReachLocation("Complete Main Quest: A new challenger")               & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Final Fight", world.player),                             CanReachLocation("Complete Main Quest: Stiff competition")              & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Return of the champion", world.player),                  CanReachLocation("Complete Main Quest: Final Fight")                    & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Breeding season", world.player),                         CanReachLocation("Complete Main Quest: Return of the champion")         & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Mission success", world.player),                         CanReachLocation("Complete Main Quest: Breeding season")                & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Quest for the crystal", world.player),                   CanReachLocation("Complete Main Quest: Mission success")                & Has("Stone Key"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: How the Dominoes fall", world.player),                   CanReachLocation("Complete Main Quest: Quest for the crystal")          & Has("Yellow Harmony Crystal"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Big balloon adventure", world.player),                   CanReachLocation("Complete Main Quest: How the Dominoes fall")          & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Welcome to Paradise", world.player),                     CanReachLocation("Complete Main Quest: Big balloon adventure")          & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Coconut Conundrum", world.player),                       CanReachLocation("Complete Main Quest: Welcome to Paradise")            & Has("Fishing Rod"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Lusty Cultists", world.player),                          CanReachLocation("Complete Main Quest: Coconut Conundrum")              & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Savior of Coconut Village", world.player),               CanReachLocation("Complete Main Quest: Lusty Cultists")                 & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Slippery When Wet", world.player),                       CanReachLocation("Complete Main Quest: Savior of Coconut Village")      & Has("Cock Shaped Key"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Glimmering Prize", world.player),                        CanReachLocation("Complete Main Quest: Slippery When Wet")              & Has("Red Harmony Crystal"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Arctic Adventure", world.player),                        CanReachLocation("Complete Main Quest: Glimmering Prize")               & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: The Frigid Maiden", world.player),                       CanReachLocation("Complete Main Quest: Arctic Adventure")               & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Arctic Isles", world.player),                            CanReachLocation("Complete Main Quest: The Frigid Maiden")              & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Paisley Bones", world.player),                           CanReachLocation("Complete Main Quest: Arctic Isles")                   & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Demand for Dynamite", world.player),                     CanReachLocation("Complete Main Quest: Paisley Bones")                  & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Stealing From a Dead Man", world.player),                CanReachLocation("Complete Main Quest: Demand for Dynamite")            & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: The Lewd Exorcist", world.player),                       CanReachLocation("Complete Main Quest: Stealing From a Dead Man")       & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Suit In Hand", world.player),                            CanReachLocation("Complete Main Quest: The Lewd Exorcist")              & Has("Fancy Suit"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Fishing For Treasure", world.player),                    CanReachLocation("Complete Main Quest: Suit In Hand")                   & Has("Wedding Ring"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: The Proposal", world.player),                            CanReachLocation("Complete Main Quest: Fishing For Treasure")           & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Here Comes the Boom", world.player),                     CanReachLocation("Complete Main Quest: The Proposal")                   & Has("Dynamite"))
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Arctic Harmony", world.player),                          CanReachLocation("Complete Main Quest: Here Comes the Boom")            & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Crimson Chase", world.player),                           CanReachLocation("Complete Main Quest: Arctic Harmony")                 & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Through the Portal", world.player),                      CanReachLocation("Complete Main Quest: Crimson Chase")                  & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Sanctuary Shakedown", world.player),                     CanReachLocation("Complete Main Quest: Through the Portal")             & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Hostage Situation", world.player),                       CanReachLocation("Complete Main Quest: Sanctuary Shakedown")            & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Breezie Runs Free", world.player),                       CanReachLocation("Complete Main Quest: Hostage Situation")              & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Desperate Dash", world.player),                          CanReachLocation("Complete Main Quest: Breezie Runs Free")              & True_())
        world.set_rule(world.multiworld.get_location("Complete Main Quest: Battle for Spirit Valley", world.player),                CanReachLocation("Complete Main Quest: Desperate Dash")                 & True_())

    #SIDE MISSION RULES
    if world.options.Side_Missions.value:
        world.set_rule(world.multiworld.get_location("Complete Side Quest: Larry’s Treasure", world.player),                Has("Ass Lover Extreme issue 12"))
        world.set_rule(world.multiworld.get_location("Complete Side Quest: The Art of Fishing", world.player),              Has("Goldfish Available in Shop"))
        world.set_rule(world.multiworld.get_location("Complete Side Quest: Legend of the Valkyrie part 1.", world.player),  Has("Cum Rag"))
        world.set_rule(world.multiworld.get_location("Complete Side Quest: Legend of the Valkyrie part 2.", world.player),  Has("Northern Blowfish Available in Shop"))
        world.set_rule(world.multiworld.get_location("Complete Side Quest: Slithering Menace", world.player),               Has(f"{world.data["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"]} Obtainable"))
        world.set_rule(world.multiworld.get_location("Complete Side Quest: Deadly Waters", world.player),                   HasAll(f"{world.data["SIDE_QUEST_DEADLY_WATERS_SPIRIT"]} Obtainable", "Fishing Rod"))
        world.set_rule(world.multiworld.get_location("Complete Side Quest: Arctic Menace", world.player),                   Has(f"{world.data["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"]} Obtainable"))

        if not world.options.Single_Catch.value:
            world.set_rule(world.multiworld.get_location("Complete Side Quest: Perky Petunia", world.player),                   SpiritObtain(world.data["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"]))
            world.set_rule(world.multiworld.get_location("Complete Side Quest: Starry Eyed Surprise", world.player),            SpiritObtain(world.data["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"]))
            world.set_rule(world.multiworld.get_location("Complete Side Quest: Hunt for the Centiboob part 1.", world.player),  SpiritObtain(world.data["SIDE_QUEST_CENTIBOOB_1_SPIRIT"]))
            world.set_rule(world.multiworld.get_location("Complete Side Quest: Hunt for the Centiboob part 2.", world.player),  SpiritObtain(world.data["SIDE_QUEST_CENTIBOOB_2_SPIRIT"]))
            world.set_rule(world.multiworld.get_location("Complete Side Quest: Hunt for the Centiboob part 3.", world.player),  SpiritObtain(world.data["SIDE_QUEST_CENTIBOOB_3_SPIRIT"]))


    # BOLDER CHEST RULES
    world.set_rule(world.multiworld.get_location("Evergreen Outpost: Chest Behind Pushable Bolder", world.player),        Has("Testosterone Pills"))
    world.set_rule(world.multiworld.get_location("Greensvale: Chest Behind Pushable Bolder In the North", world.player),  Has("Testosterone Pills"))
    world.set_rule(world.multiworld.get_location("Evergreen Caverns: Chest 1 Behind Rawry", world.player),                Has("Testosterone Pills"))
    world.set_rule(world.multiworld.get_location("Evergreen Caverns: Chest 2 Behind Rawry", world.player),                Has("Testosterone Pills"))
    world.set_rule(world.multiworld.get_location("Milly's Farm: Chest Behind Pushable Bolder", world.player),             Has("Testosterone Pills"))
    world.set_rule(world.multiworld.get_location("Sandy Tunnels: Chest North of Chad", world.player),                     Has("Testosterone Pills"))
    world.set_rule(world.multiworld.get_location("Old Masters Hut: Chest in Basement", world.player),                     Has("Testosterone Pills"))



    #ACCESS RULES
    world.set_rule(world.multiworld.get_entrance("Trail16_Top->Trail16", world.player),                     Has("Testosterone Pills"))

    if not world.options.randomise_map.value:
        world.set_rule(world.multiworld.get_entrance("Trail2->Greensvale", world.player),                           CanReachLocation("Complete Main Quest: First Mission: Success!", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))

        world.set_rule(world.multiworld.get_entrance("Trail4->AncientTemple1", world.player),                       CanReachLocation("Complete Main Quest: Onward to Greensvale", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True)
                                                                                                                                 & Has("Ancient Temple Key"))


        #world.set_rule(world.multiworld.get_entrance("EvergreenOutpost->EvergreenOutpost_East", world.player),      CanReachLocation("Complete Main Quest: Bridge crossing", options=[OptionFilter(Main_Missions, 1)])
        world.set_rule(world.multiworld.get_entrance("EvergreenOutpost->EvergreenOutpost_East", world.player),      HasAll("Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", options=[OptionFilter(Main_Missions, 1)])
                                                                                                                                 | Has("Power Crystal", options=[OptionFilter(Main_Missions, 0)]))

        world.set_rule(world.multiworld.get_entrance("Trail9->DesertTemple1", world.player),                        CanReachLocation("Complete Main Quest: Mission success", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True)
                                                                                                                                 & Has("Stone Key"))

        #world.set_rule(world.multiworld.get_entrance("TumbleweedTown->CrashSite", world.player),                    CanReachLocation("Complete Main Quest: Big balloon adventure", options=[OptionFilter(Main_Missions, 1)])
        world.set_rule(world.multiworld.get_entrance("TumbleweedTown->CrashSite", world.player),                    (HasAll("Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", options=[OptionFilter(Main_Missions, 1)]) & SpiritObtain(world.data["MAIN_QUEST_TOTAL_DOMINATION"]))
                                                                                                                                 | Has("Balloon Ride Ticket", options=[OptionFilter(Main_Missions, 0)]))

        world.set_rule(world.multiworld.get_entrance("Trail11->Trail13", world.player),                             Has("Fishing Rod"))

        #world.set_rule(world.multiworld.get_entrance("CoconutVillage_Temple->ColdHarbor", world.player),            CanReachLocation("Complete Main Quest: Arctic Adventure", options=[OptionFilter(Main_Missions, 1)])
        world.set_rule(world.multiworld.get_entrance("CoconutVillage_Temple->ColdHarbor", world.player),            (HasAll("Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal", options=[OptionFilter(Main_Missions, 1)]) & SpiritObtain(world.data["MAIN_QUEST_TOTAL_DOMINATION"]))
                                                                                                                                 | Has("Boat Ride Ticket", options=[OptionFilter(Main_Missions, 0)]))

        world.set_rule(world.multiworld.get_entrance("Frostville1->Trail17", world.player),                         CanReachLocation("Complete Main Quest: Here Comes the Boom", options=[OptionFilter(Main_Missions, 1)])
                                                                                                                                 | Has("Dynamite", options=[OptionFilter(Main_Missions, 0)]))

        #world.set_rule(world.multiworld.get_entrance("Trail18->Trail19", world.player),                             CanReachLocation("Complete Main Quest: Through the Portal", options=[OptionFilter(Main_Missions, 1)])
        world.set_rule(world.multiworld.get_entrance("Trail18->Trail19", world.player),                             (HasAll("Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal", "Fancy Suit", "Wedding Ring", "Dynamite", options=[OptionFilter(Main_Missions, 1)]) & SpiritObtain(world.data["MAIN_QUEST_TOTAL_DOMINATION"]))
                                                                                                                                 | Has("Ancient Warp Core", options=[OptionFilter(Main_Missions, 0)]))

        world.set_rule(world.multiworld.get_entrance("Trail20->Trail20_Right", world.player),                       CanReachLocation("Complete Main Quest: Hostage Situation", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))

        world.set_rule(world.multiworld.get_entrance("OakwoodVillage->OakwoodVillage_Hq", world.player),            CanReachLocation("Complete Main Quest: Battle for Spirit Valley", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))


    else:
        world.set_rule(world.multiworld.get_entrance("Trail2 Left", world.player),                                  CanReachLocation("Complete Main Quest: First Mission: Success!", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))

        world.set_rule(world.multiworld.get_entrance("Trail4 Temple", world.player),                                CanReachLocation("Complete Main Quest: Onward to Greensvale", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True)
                                                                                                                                 & Has("Ancient Temple Key"))

        #world.set_rule(world.multiworld.get_entrance("EvergreenOutpost->EvergreenOutpost_East", world.player),      CanReachLocation("Complete Main Quest: Bridge crossing", parent_region_name="EvergreenOutpost", options=[OptionFilter(Main_Missions, 1)])
        world.set_rule(world.multiworld.get_entrance("EvergreenOutpost->EvergreenOutpost_East", world.player),      (HasAll("Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", options=[OptionFilter(Main_Missions, 1)])
                                                                                                                                 & CanReachRegion("EvergreenOutpost") & CanReachRegion("Trail2") & CanReachRegion("Greensvale") & CanReachRegion("Greensvale_SexShop") & CanReachRegion("AncientTemple3"))
                                                                                                                                 | Has("Power Crystal", options=[OptionFilter(Main_Missions, 0)]))

        world.set_rule(world.multiworld.get_entrance("Trail9 Temple", world.player),                                CanReachLocation("Complete Main Quest: Mission success", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True)
                                                                                                                                 & Has("Stone Key"))

        #world.set_rule(world.multiworld.get_entrance("TumbleweedTown->CrashSite", world.player),                    CanReachLocation("Complete Main Quest: Big balloon adventure", parent_region_name="TumbleweedTown", options=[OptionFilter(Main_Missions, 1)])
        world.set_rule(world.multiworld.get_entrance("TumbleweedTown->CrashSite", world.player),                    (HasAll("Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", options=[OptionFilter(Main_Missions, 1)]) & SpiritObtain(world.data["MAIN_QUEST_TOTAL_DOMINATION"])
                                                                                                                                 & CanReachRegion("EvergreenOutpost") & CanReachRegion("Trail2") & CanReachRegion("Greensvale") & CanReachRegion("Greensvale_SexShop") & CanReachRegion("AncientTemple3") & CanReachRegion("TumbleweedTown") & CanReachRegion("TumbleweedTown_KingsSaloon1") & CanReachRegion("OldMastersHut_Upstairs") & CanReachRegion("DesertTemple2"))
                                                                                                                                 | Has("Balloon Ride Ticket", options=[OptionFilter(Main_Missions, 0)]))

        world.set_rule(world.multiworld.get_entrance("Trail11 pier", world.player),                                 Has("Fishing Rod"))
        #world.set_rule(world.multiworld.get_entrance("Trail11 pier", world.player),                                 Has("Fishing Rod"))

        #world.set_rule(world.multiworld.get_entrance("CoconutVillage_Temple->ColdHarbor", world.player),            CanReachLocation("Complete Main Quest: Glimmering Prize", parent_region_name="CoconutVillage_Temple", options=[OptionFilter(Main_Missions, 1)])
        world.set_rule(world.multiworld.get_entrance("CoconutVillage_Temple->ColdHarbor", world.player),            (HasAll("Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal", options=[OptionFilter(Main_Missions, 1)]) & SpiritObtain(world.data["MAIN_QUEST_TOTAL_DOMINATION"])
                                                                                                                                 & CanReachRegion("EvergreenOutpost") & CanReachRegion("Trail2") & CanReachRegion("Greensvale") & CanReachRegion("Greensvale_SexShop") & CanReachRegion("AncientTemple3") & CanReachRegion("TumbleweedTown") & CanReachRegion("TumbleweedTown_KingsSaloon1") & CanReachRegion("OldMastersHut_Upstairs") & CanReachRegion("DesertTemple2") & CanReachRegion("CoconutVillage_Temple") & CanReachRegion("Trail13") & CanReachRegion("IslandCave2"))
                                                                                                                                 | Has("Boat Ride Ticket", options=[OptionFilter(Main_Missions, 0)]))

        world.set_rule(world.multiworld.get_entrance("Frostville1 Top", world.player),                              CanReachLocation("Complete Main Quest: Here Comes the Boom", options=[OptionFilter(Main_Missions, 1)])
                                                                                                                                 | Has("Dynamite ", options=[OptionFilter(Main_Missions, 0)]))

        #world.set_rule(world.multiworld.get_entrance("Trail18->Trail19", world.player),                             CanReachLocation("Complete Main Quest: Through the Portal", parent_region_name="Trail18", options=[OptionFilter(Main_Missions, 1)])
        world.set_rule(world.multiworld.get_entrance("Trail18->Trail19", world.player),                             (HasAll("Super Secret Orders", "Ancient Temple Key", "Cracked Power Crystal", "Raw Crystal Chunk", "Power Crystal", "Video Cassette", "Spirit Handler License", "Stone Key", "Yellow Harmony Crystal", "Fishing Rod", "Cock Shaped Key", "Red Harmony Crystal", "Fancy Suit", "Wedding Ring", "Dynamite", options=[OptionFilter(Main_Missions, 1)]) & SpiritObtain(world.data["MAIN_QUEST_TOTAL_DOMINATION"])
                                                                                                                                 & CanReachRegion("EvergreenOutpost") & CanReachRegion("Trail2") & CanReachRegion("Greensvale") & CanReachRegion("Greensvale_SexShop") & CanReachRegion("AncientTemple3") & CanReachRegion("TumbleweedTown") & CanReachRegion("TumbleweedTown_KingsSaloon1") & CanReachRegion("OldMastersHut_Upstairs") & CanReachRegion("DesertTemple2") & CanReachRegion("CoconutVillage_Temple") & CanReachRegion("Trail13") & CanReachRegion("IslandCave2") & CanReachRegion("ColdHarbor") & CanReachRegion("Frostville1") & CanReachRegion("Frostville1_Church") & CanReachRegion("Frostville1_House1") & CanReachRegion("AbandonedMine_House1") & CanReachRegion("Trail18") & CanReachRegion("ArcticTemple2"))
                                                                                                                                 | Has("Ancient Warp Core", options=[OptionFilter(Main_Missions, 0)]))

        world.set_rule(world.multiworld.get_entrance("Trail20->Trail20_Right", world.player),                       CanReachLocation("Complete Main Quest: Hostage Situation", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))

        world.set_rule(world.multiworld.get_entrance("OakwoodVillage->OakwoodVillage_Hq", world.player),            CanReachLocation("Complete Main Quest: Battle for Spirit Valley", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))



    # battle access rules
    world.set_rule(world.multiworld.get_location("Evergreen Caverns: Defeat Rawry", world.player),        Has("Testosterone Pills"))

    if world.options.Main_Missions.value:
        world.set_rule(world.multiworld.get_location("Trail 02: Defeat Crimson Agent", world.player),               CanReachLocation("Complete Main Quest: Crimson Agent"))
        world.set_rule(world.multiworld.get_location("Tumbleweed Town: Defeat Willy Wanker", world.player),         CanReachLocation("Complete Main Quest: A new challenger"))
        world.set_rule(world.multiworld.get_location("Tumbleweed Town: Defeat Dick Cummings", world.player),        CanReachLocation("Complete Main Quest: A new challenger"))
        world.set_rule(world.multiworld.get_location("Tumbleweed Town: Defeat Dick Louie", world.player),           CanReachLocation("Complete Main Quest: A new challenger"))
        world.set_rule(world.multiworld.get_location("Frostville: Defeat Mother Evilyn", world.player),             CanReachLocation("Complete Main Quest: The Lewd Exorcist"))
        world.set_rule(world.multiworld.get_location("Trail 21: Defeat Kinley", world.player),                      CanReachLocation("Complete Main Quest: Hostage Situation"))

    world.set_rule(world.multiworld.get_location("Ancient Temple 3: Defeat Valkrie", world.player),             CanReachLocation("Complete Main Quest: Temple Investigation", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))
    world.set_rule(world.multiworld.get_location("Stone Temple 2: Defeat Domino", world.player),                CanReachLocation("Complete Main Quest: Quest for the crystal", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))
    world.set_rule(world.multiworld.get_location("Island Cave 2: Defeat Centiboob", world.player),              CanReachLocation("Complete Main Quest: Lusty Cultists", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))
    world.set_rule(world.multiworld.get_location("Artic Temple 2: Defeat Crimson Countess", world.player),      CanReachLocation("Complete Main Quest: Arctic Harmony", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))
    world.set_rule(world.multiworld.get_location("Inner Grove: Defeat Spirit Mother", world.player),            CanReachLocation("Complete Main Quest: Battle for Spirit Valley", options=[OptionFilter(Main_Missions, 1)], filtered_resolution=True))


    # SPIRIT OBTAIN RULES
    if world.options.Spirit_Locations.value:
        for spirit in obtainable_spirit_list:
            if not world.options.Randomise_Spawns.value and spirit == "EV-3":
                continue

            #set_rule(multiworld.get_location(f"Obtain a {spirit} Spirit", player), lambda state, s=spirit, p=player: spirit_Obtain(state, p, s))
            world.set_rule(world.multiworld.get_location(f"Obtain a {spirit} Spirit", world.player), SpiritObtain(spirit))

            if world.options.Spirit_Obtain_progression.value:
                world.multiworld.get_location(f"Obtain a {spirit} Spirit", world.player).progress_type = LocationProgressType.EXCLUDED

            if world.options.Spirit_Affection.value:
                world.set_rule(world.multiworld.get_location(f"Get {spirit} to Affection LV1", world.player), SpiritAffection(spirit))
                world.set_rule(world.multiworld.get_location(f"Get {spirit} to Affection LV2", world.player), SpiritAffection(spirit))
                world.set_rule(world.multiworld.get_location(f"Get {spirit} to Affection LV3", world.player), SpiritAffection(spirit))
                world.set_rule(world.multiworld.get_location(f"Get {spirit} to Affection LV4", world.player), SpiritAffection(spirit))
                world.set_rule(world.multiworld.get_location(f"Get {spirit} to Affection LV5", world.player), SpiritAffection(spirit))

                if world.options.Spirit_Affection_progression.value:
                    world.multiworld.get_location(f"Get {spirit} to Affection LV1", world.player).progress_type = LocationProgressType.EXCLUDED
                    world.multiworld.get_location(f"Get {spirit} to Affection LV2", world.player).progress_type = LocationProgressType.EXCLUDED
                    world.multiworld.get_location(f"Get {spirit} to Affection LV3", world.player).progress_type = LocationProgressType.EXCLUDED
                    world.multiworld.get_location(f"Get {spirit} to Affection LV4", world.player).progress_type = LocationProgressType.EXCLUDED
                    world.multiworld.get_location(f"Get {spirit} to Affection LV5", world.player).progress_type = LocationProgressType.EXCLUDED

            if world.options.Rare_Locations.value:
                world.set_rule(world.multiworld.get_location(f"Obtain a Rare {spirit} Spirit", world.player), SpiritRareObtain(spirit))

                if world.options.Rare_Spirit_Obtain_progression.value:
                    world.multiworld.get_location(f"Obtain a Rare {spirit} Spirit", world.player).progress_type = LocationProgressType.EXCLUDED

    #GOAL RULES
    if world.options.goal.value == 1:
        world.set_rule(world.multiworld.get_location(f"Catch all Spirits", world.player), SpiritObtainAll())
    elif world.options.goal.value == 2:
        world.set_rule(world.multiworld.get_location(f"Catch all Rare Spirits", world.player), SpiritRareObtainAll())
    elif world.options.goal.value == 3:
        world.set_rule(world.multiworld.get_location(f"Get All Spirits To Affection Lv5", world.player), SpiritAffectionAll())


#testing making a custom Rule
@dataclasses.dataclass()
class ObtainSpirit(Rule["SpiritValley"], game="Spirit Valley"):

    spirit: str
    grassroutes: list[str]
    waterroutes: list[str]

    def __init__(
        self,
        spirit: str,
        data: dict,
        options: Iterable[OptionFilter] = (),
        filtered_resolution: bool = False,
    ) -> None:
        super().__init__(options=options, filtered_resolution=filtered_resolution)
        self.spirit = spirit
        self.grassroutes = []
        self.waterroutes = []
        for grass in data["Grass_spawn"]:
            if spirit in data["Grass_spawn"][grass]:
                self.grassroutes.append(grass)
        for water in data["Water_spawn"]:
            if spirit in data["Water_spawn"][water]:
                self.waterroutes.append(water)

    @override
    def _instantiate(self, world: "SpiritValley") -> Rule.Resolved:
        return self.Resolved(
            spirit=self.spirit,
            grass=tuple(self.grassroutes),
            water=tuple(self.waterroutes),
            player=world.player,
            caching_enabled=getattr(world, "rule_caching_enabled", False),
        )

    class Resolved(Rule.Resolved):

        spirit: str
        grass: tuple
        water: tuple

        @override
        def _evaluate(self, state: CollectionState) -> bool:
            return state.has(f"{self.spirit} Obtainable", self.player) and state.has_any(["Spirit Crystal Available in Shop", "Spirit Crystal +1 Available in Shop", "Spirit Crystal +2 Available in Shop"], self.player) and state.has("Shop Accessible", self.player)

        @override
        def item_dependencies(self) -> dict[str, set[int]]:
            # this function is only required if you have caching enabled
            return {f"{self.spirit} Obtainable": {id(self)},
                    "Spirit Crystal Available in Shop": {id(self)},
                    "Spirit Crystal +1 Available in Shop": {id(self)},
                    "Spirit Crystal +2 Available in Shop": {id(self)},
                    "Fishing Rod": {id(self)},
                    "Fishy Scent": {id(self)},
                    "Scent Mixture": {id(self)},
                    "Shop Accessible": {id(self)}}

        @override
        def region_dependencies(self) -> dict[str, set[int]]:
            g = {f"{item}": {id(self)} for item in self.grass}
            if "Trail16" in self.grass: g["Trail16_Top"] = {id(self)}
            if "Trail20" in self.grass: g["Trail20_Right"] = {id(self)}
            w = {f"{item}": {id(self)} for item in self.water}
            return {**g, **w}

        @override
        def explain_json(self, state: CollectionState | None = None) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations
            if state is None:
                return self.explain_json_none()

            o = []
            o.append({"type": "text", "text": f"{self.spirit} can be found "})
            if len(self.grass)!=0:
                for g in self.grass:
                    if g == "Trail16_Cave":
                        if state.has("Fishy Scent", self.player): o.append({"type": "color", "color": "green" if state.can_reach_region(g, self.player) else "salmon", "text": f"{g} Grass, "})
                        else: o.append({"type": "color", "color": "salmon", "text": f"{g} Grass(MISSING Fishy Scent), "})
                    elif g == "Trail22_Cave":
                        if state.has("Scent Mixture", self.player): o.append({"type": "color", "color": "green" if state.can_reach_region(g, self.player) else "salmon", "text": f"{g} Grass, "})
                        else: o.append({"type": "color", "color": "salmon", "text": f"{g} Grass(MISSING Scent Mixture), "})
                    else:
                        o.append({"type": "color", "color": "green" if state.can_reach_region(g, self.player) else "salmon", "text": f"{g} Grass, "})

            if len(self.water)!=0:
                if state.has("Fishing Rod", self.player):
                    for g in self.water:
                        o.append({"type": "color", "color": "green" if state.can_reach_region(g, self.player) else "salmon", "text": f"{g} Water, "})
                else:
                    for g in self.water:
                        o.append({"type": "color", "color": "green" if state.can_reach_region(g, self.player) else "salmon", "text": f"{g} Water(MISSING Fishing Rod), "})

            if state.has("Shop Accessible", self.player):
                o.append({"type": "color", "color": "green", "text": f"Player CAN Access a Shop, "})
            else:
                o.append({"type": "color", "color": "salmon", "text": f"Player CAN NOT Access a Shop, "})

            if state.has_any(["Spirit Crystal Available in Shop","Spirit Crystal +1 Available in Shop","Spirit Crystal +2 Available in Shop"], self.player):
                o.append({"type": "color", "color": "green", "text": f"Player HAS Crystals Available in the Shop "})
            else:
                o.append({"type": "color", "color": "salmon", "text": f"Player DOES NOT have Crystals Available in the Shop "})
            return o

        def explain_json_none(self) -> list[JSONMessagePart]:
            # this method can be overridden to display custom explanations

            o = []
            o.append({"type": "text", "text": f"{self.spirit} can be found "})
            if len(self.grass)!=0:
                for g in self.grass:
                    o.append({"type": "text", "text": f"{g} Grass, "})
            if len(self.water)!=0:
                for g in self.water:
                    o.append({"type": "text", "text": f"{g} Water, "})

            o.append({"type": "text", "text": f"Player Needs Access to a Shop, "})
            o.append({"type": "text", "text": f"Player needs to have Crystals Available in the Shop "})

            return o

        @override
        def explain_str(self, state: CollectionState | None = None) -> str:
            # this method can be overridden to display custom explanations
            if state is None:
                return self.explain_str_none()

            o = ""
            o = o + f"{self.spirit} can be found "

            for g in self.grass:
                o = o + f"{g} Grass, "
            for g in self.water:
                o = o + f"{g} Water, "

            if state.has("Shop Accessible", self.player):
                o = o + f"Player CAN Access a Shop, "
            else:
                o = o + f"Player CAN NOT Access a Shop, "

            if state.has_any(["Spirit Crystal Available in Shop","Spirit Crystal +1 Available in Shop","Spirit Crystal +2 Available in Shop"], self.player):
                o = o + f"Player HAS Crystals Available in the Shop "
            else:
                o = o + f"Player DOES NOT have Crystals Available in the Shop "
            return o

        @override
        def explain_str_none(self) -> str:
            # this method can be overridden to display custom explanations
            o = ""
            o = o + f"{self.spirit} can be found "

            for g in self.grass:
                o = o + f"{g} Grass, "
            for g in self.water:
                o = o + f"{g} Water, "

            o = o + f"Player Needs Access to a Shop, "
            o = o + f"Player needs to have Crystals Available in the Shop "

            return o

