class Map_Region:
    map_id: str

    warpable: bool

    grass: bool
    grass_slots: [str]  # TODO FIX PROPERLY
    grass_lv_range: [int]

    water: bool
    water_slots: [str]  # TODO FIX PROPERLY
    water_lv_range: [int]

    chest_locations: [str]
    trainer_locations: [str]
    quest_locations: [str]

    entry: [str]
    exits: [str]

    def __init__(self, map_id, warpable, grass, grass_slots, grass_lv_range, water, water_slots, water_lv_range, chest_locations, trainer_locations, quest_locations, entry, exit):
        self.map_id = map_id
        self.warpable = warpable
        self.grass = grass
        self.grass_slots = grass_slots
        self.grass_lv_range = grass_lv_range
        self.water = water
        self.water_slots = water_slots
        self.water_lv_range = water_lv_range
        self.chest_locations = chest_locations
        self.trainer_locations = trainer_locations
        self.quest_locations = quest_locations
        self.entry = entry
        self.exits = exit


class transititon:
    scene1_name: str
    scene1_area_id: str

    scene2_name: str
    scene2_area_id: str

    oneway: bool

    def __init__(self, s1_name, s1_area_id, s2_name, s2_area_id, oneway):
        self.scene1_name = s1_name
        self.scene1_area_id = s1_area_id
        self.scene2_name = s2_name
        self.scene2_area_id = s2_area_id
        self.oneway = oneway


regions = [
    Map_Region("OakwoodVillage",
               True,
               False, None, None,
               False, None, None,
               None,
               [
                   "Oakwood Village: Defeat Robbie"  # NPC SCRIPTED   61822611-267a-4366-b99c-fadc5a23ad01 [{"Wolfy":3}]
               ],
               [
                   "Complete Side Quest: Sparring Match",
                   "Complete Main Quest: Captain Maria",
                   "Complete Main Quest: First Mission: Success!",
               ],
               ["Top",  "FarmHouseOut"],#"ClinicOut",HqOut
               ["Top",  "FarmHouseOut"]),#"ClinicOut",HqOut

    Map_Region("OakwoodVillage_Clinic", False, False, None, None, False, None, None, None, None,
               [
                   "Complete Main Quest: Doctor’s Appointment",
                   "Complete Main Quest: Consulting Dolly",
               ],
               [],[]),#["Bottom"], ["Bottom"]),

    Map_Region("OakwoodVillage_FarmHouse", False, False, None, None, False, None, None,
               ["Oakwood Village House: Chest House"],  # b9f52b5c-fd8d-43b8-9f5c-85a5b3686a6a ["Chastity belt"]
               None, None, ["Bottom"], ["Bottom"]),

    Map_Region("OakwoodVillage_Hq", False, False, None, None, False, None, None, None, None, None, [],[]),#["Bottom"], ["Bottom"]),

    Map_Region("Trail1", False,
               True, ["Petunia", "Beebee", "Slimee"], [3, 3],
               False, None, None,
               [
                   "Trail 01: Chest Near Piper",  # #33bdf3c7-7b56-4578-b038-3d9f10a7c978 ["2x spirit crystal","25 coins"]
                   "Trail 01: Chest North of Piper",  # 33a2ce7f-9568-4435-ac78-a4e3660948fe ["2x Spirit repelent"]
                   "Trail 01: Potion From Jane",  # 3019ab50-bd67-4887-9865-cdc2fa604f55 ["Potion"]
               ],
               None,
               ["Complete Side Quest: Perky Petunia"],
               ["Top", "Bottom"],
               ["Top", "Bottom"]),

    Map_Region("EvergreenOutpost", False,
               True, ["Petunia", "Beebee", "Slimee", "Bunni", "Wolfy"], [3, 4],
               False, None, None,
               [
                   "Evergreen Outpost: Chest Near Medic",  # 7c0b0138-7aa6-49ea-a1eb-015e33731f51 ["Butt plug of wisdom"]
                   "Evergreen Outpost: Chest Above Grass Patch",  # 49a27369-563a-444d-9112-45ff04198979 ["vial of health", "2x antidote"]
                   "Evergreen Outpost: Chest Behind Pushable Bolder",  # 576ccf5e-ee72-49c4-930c-a3e4acf6c1b7 ["200x coin", "2x spirit crystal +1"]
               ],
               [
                   "Evergreen Outpost: Defeat Elise"  # 19c75671-2314-414f-b500-ef28c011d8d2 [{"Beebee":3}]
               ],
               [
                   "Complete Side Quest: Larry’s Treasure",
                   "Complete Main Quest: First Orders",
                   "Complete Main Quest: Super Secret Orders",
                   "Complete Main Quest: Bridge crossing",
               ],
               ["Left", "Bottom"],
               ["Left", "Bottom"]),
    # ADDED REGION DUE TO INACCESSIBILITY BEFORE QUEST IS COMPLETE
    Map_Region("EvergreenOutpost_East", False, False, None, None, False, None, None, None, None, None, ["Right"], ["Right"]),

    Map_Region("Trail2", False,
               True, ["Petunia", "Beebee", "Slimee", "Wolfy", "Bunni", "Ursie", "Gloria"], [3, 4],
               False, None, None,
               [
                   "Trail 02: Chest Near Billy",  # e129287a-733f-4761-b12d-d4f6265d3e38 ["cupcake", "20x coins"]
                   "Trail 02: Chest in Hidden Path Next to Macy",  # d36a4079-4dc5-4cbf-92ec-fbb4e5e5a674 ["Ass lovers Extreme issue 12"]
                   "Trail 02: Chest East of Macy",  # a6673de2-6794-43ee-b1c3-cc7e7468c7f9 ["15x coins", "2x vial of stanima"]
                   "Trail 02: Chest Near Skyler",  # 5c0b8d8e-e4fe-4505-871c-d2c3964b75b5 ["2x potent sent"]
               ],
               [
                   "Trail 02: Defeat Billy",  # 0a40a301-741a-4843-8008-799f4ba37287 [{"Gloria":3}, {"Petunia":2}]
                   "Trail 02: Defeat Macy",  # bf261ea7-7b93-4c0b-89a8-da7c93550808 [{"Ursie":4}]
                   "Trail 02: Defeat Skyler",  # a79a0909-43a5-47ff-b990-a1632a224e83 [{"Slimee":3}, {"Beebee":3}]
                   "Trail 02: Defeat Crimson Agent",  # 53af4c29-1d1b-4655-a1db-9ed89c32a981 [{"Wolfy":4}, {"Petunia":3}]
               ],
               [
                   "Complete Main Quest: Crimson Agent"
               ],
               ["Left", "Right"],
               ["Left", "Right"]),

    Map_Region("Greensvale", True,
               False, None, None,
               False, None, None,
               [
                   "Greensvale: Chest South of Waystone",  # e5139fe4-aae0-4c8c-9591-94cd9405a8cb ["2x vial of rejuvination"]
                   "Greensvale: Chest Next To XXX Shop",  # 23d8f4fb-7284-483c-a145-ed500c426339 ["lollypop", "15x coins"]
                   "Greensvale: Chest Behind Pushable Bolder In the North",  # c0fa6732-bee2-47c2-9853-1ffa3e6a98e0 ["butt plug of life +1"]
               ],
               None,
               [
                   "Complete Main Quest: Onward to Greensvale",
                   "Complete Main Quest: Harmonious Disturbance",
               ],
               ["Right", "Top", "Bottom", "ClinicOut", "MerchantOut", "SexShopOut", "SmallHouseOut"],
               ["Right", "Top", "Bottom", "ClinicOut", "MerchantOut", "SexShopOut", "SmallHouseOut"]),

    Map_Region("Greensvale_Clinic", False, False, None, None, False, None, None, None, None, None, ["Bottom"], ["Bottom"]),

    Map_Region("Greensvale_Merchant", False, False, None, None, False, None, None, None, None, None, ["Bottom"], ["Bottom"]),

    Map_Region("Greensvale_SexShop", False, False, None, None, False, None, None, None, None,
               [
                   "Complete Main Quest: Becky can fix it",
                   "Complete Main Quest: Hunt for the chunk",
               ],
               ["Bottom"], ["Bottom"]),

    Map_Region("Greensvale_SmallHouse", False, False, None, None, False, None, None,
               ["Greensvale House: Chest in House"],  # 64386704-ba0e-461c-ad5d-36327d902e9b ["spirit crystal", "25x coins"]
               None, None, ["Bottom"], ["Bottom"]),

    Map_Region("MillysFarm", False,
               True, ["Serpentia"], [5, 6],
               False, None, None,
               ["Milly's Farm: Chest Behind Pushable Bolder"],  # e21093f1-32a4-4e08-ba6c-7090002ccdd9 ["seed of life"]
               None,
               ["Complete Side Quest: Slithering Menace"],
               ["Top"],
               ["Top"]),

    Map_Region("Trail3", False,
               True, ["Beebee", "Gloria", "Ursie", "Wolfy", "Belle", "Oakie", "trissy"], [5, 7],
               False, None, None,
               [
                   "Trail 03: Chest North of Miriam",  # 44683738-a42b-4c9c-b200-e4742152e790 ["2x vial of health", "cleansing tonic"]
                   "Trail 03: Chest South of Miriam",  # 4d2efd45-b043-46de-9a27-e75da0caec9f ["25x coin", "candy cane"]
                   "Trail 03: Chest Chest Before Evergreen Caverns Entrance",  # 0ab8b8d9-28b6-4bfe-9a4c-188297627ed3 ["rejuvination potion"]
               ],
               [
                   "Trail 03: Defeat Cheese",  # b40b0778-da74-4660-b0a1-fba6d1d16bdd [{"Oakie":6}, {"Beebee":5}]
                   "Trail 03: Defeat Miriam",  # c029e36a-14ec-4d07-a45b-b7b57f406575 [{"Petunia":7}, {"Wolfy":6}]
                   "Trail 03: Defeat Jenna",  # 6778b3a1-97d4-457d-adc1-c324dbad017e [{"Ursie":6}]
               ],
               ["Complete Side Quest: Pleasuring Pusseen"],
               ["Bottom", "Cave"],
               ["Bottom", "Cave"]),

    Map_Region("EvergreenCaverns", False,
               True, ["Slimee", "Serpentia", "Spinnie", "Octopussy"], [6, 9],
               False, None, None,
               [
                   "Evergreen Caverns: Chest West of Stu",  # 0b29ff75-0e24-4378-9053-db03ca077e79 ["2x vial of stamina"]
                   "Evergreen Caverns: Chest South of Nicole",  # 9396ff11-ac75-4b7c-8999-286ff2c84f75 ["15x coin", "vial of health", "antidote"]
                   "Evergreen Caverns: Chest 1 Behind Rawry",  # f4de6097-3346-4921-849f-b099ee698aa2 ["raw crystal chunk"]
                   "Evergreen Caverns: Chest 2 Behind Rawry",  # 42de807c-00fe-4570-91ee-8ef1a1241777 ["150x coin", "dragon dildo"]
               ],
               [
                   "Evergreen Caverns: Defeat Stu",  # e6929a89-5dc3-4118-bcf9-ff20df7ed4af [{"Serpentia":7}, {"Gloria":6}]
                   "Evergreen Caverns: Defeat Nicole",  # 364ef3fd-dfe9-41bb-aa8c-9583af54d8f8 [{"Octopussy":8}, {"Slimee":6}]
                   "Evergreen Caverns: Defeat Rawry",  # 72e0b641-b787-46cb-8fe8-eb17f93073fa [{"Rawry":15}]
               ],
               None,
               ["Top", "Bottom"],
               ["Top", "Bottom"]),

    Map_Region("Trail4", True,
               True, ["Ursie", "Gloria", "Belle", "Oakie", "Trissy", "Serpentia", "Chubbie", "Pusseen"], [7, 10],
               False, None, None,
               [
                   "Trail 04: Chest West of Evergreen Caverns Entrance",  # 0471dbe1-259d-4067-a0a3-ef54917278ad ["2x cupcake", "25x coin", "fallen star"]
                   "Trail 04: Chest West Side of Map",  # 32d13c92-6c2f-4386-8a6c-e3d6849fbcf8 ["small dildo"]
                   "Trail 04: Chest Near Waystone",  # 19a41d7a-cd3b-4e23-b71a-67f28af913e1 ["2x elusive Sent"]
               ],
               None,
               None,
               ["Cave", "Temple"],#, "TempleBackDoor"
               ["Cave", "Temple"]),#, "TempleBackDoor"

    Map_Region("AncientTemple1", False,
               False, None, None,
               False, None, None,
               [
                   "Ancient Temple 1: Chest Near 3rd Crimson Cloak",  # 84c4ca3f-c75c-404d-a348-fb7969103347 ["seed of life", "cleansing Tonic"]
                   "Ancient Temple 1: Chest in Path Loop",  # d62d3ed0-99f1-4c84-9c89-cdee2fbcda22 ["150x coin", "infinity charm"]
                   "Ancient Temple 1: Chest Near 6th Crimson Cloak",  # 36739a3e-47ec-4785-a0e7-6c71bc38f964 ["2x rejuvenation potion"]
               ],
               [
                   "Ancient Temple 1: Defeat 1st Crimson Cloak",  # 5efd2110-61ad-4bea-9551-2bffee802492 [{"Spinnie":8}]
                   "Ancient Temple 1: Defeat 2nd Crimson Cloak",  # 27d2018d-9706-4b17-981d-e408d42e1041 [{"Trissy":8}, {"chubbie":7}]
                   "Ancient Temple 1: Defeat 3rd Crimson Cloak",  # cae4d216-6d69-470b-a721-3d83290c0de6 [{"Serpentia":9}, {"Belle":6}]
                   "Ancient Temple 1: Defeat 4th Crimson Cloak",  # 2174dd35-f25f-4d1a-86a3-c1f46f576ff9 [{"Wolfy":8}, {"Beebee":7}]
                   "Ancient Temple 1: Defeat 5th Crimson Cloak",  # 677f47ac-c833-42c8-a19a-4d99d5985fdd [{"Trissy":9}]
                   "Ancient Temple 1: Defeat 6th Crimson Cloak",  # 7c73c737-4fd5-4266-92ea-caf02f8c9320 [{"Ursie":8}, {"Oakie":6}]
               ],
               None,
               ["Top", "Bottom"],
               ["Top", "Bottom"]),

    Map_Region("AncientTemple2", False,
               False, None, None,
               False, None, None,
               [
                   "Ancient Temple 2: Chest West Side of Room",  # 0b46cb8f-5eb2-4a50-8586-07f94fa07c80 ["Butt plug of power +1"]
                   "Ancient Temple 2: Chest East side of Room",  # c6b0df02-8d68-414d-9a25-8b9dd4c854f6 ["2x Spirit Crystal"]
                   "Ancient Temple 2: Chest in Middle Area of Room",  # 920a56c1-5bda-41ae-8935-c29d33c2c6f1 ["Healing potion", "25x coin"]
               ],
               [
                   "Ancient Temple 2: Defeat Crimson Cloak",  # 122ab3e7-c278-402b-a741-c83633c93626 [{"Octopussy":8}, {"Serpentia":6}, {"Spinnie":7}]
               ],
               None,
               ["Top", "Bottom"],
               ["Top", "Bottom"]),

    Map_Region("AncientTemple3", False,
               False, None, None,
               False, None, None,
               None,
               [
                   "Ancient Temple 3: Defeat Valkrie",  # NPC SCRIPTED [{"Valkrie":11}]
               ],
               [
                   "Complete Main Quest: Temple Investigation"
               ],
               ["Top", "Bottom"],
               ["Top", "Bottom"]),

    Map_Region("Trail5", False,
               True, ["Oakie", "Trissy", "Chubbie", "Pusseen", "Boobae", "Tinky"], [10, 12],
               False, None, None,
               [
                   "Trail 05: Chest Near Evergreen Outpost Entrance",  # 4c8940eb-e49c-40dc-8a26-d4f60f4bc9c2 ["2x elusive sent"]
                   "Trail 05: Chest East of Mila",  # 816a4058-20a0-4996-9648-145ad9597850 ["2x strawberry cake", "35x coins"]
                   "Trail 05: Chest West of Roy",  # 653e6c73-99ab-4b7b-93b3-6b94301378db ["ball gag"]
                   "Trail 05: Chest East of Lulu",  # 854bb842-23cc-4f46-ae38-7be9f17a2a4b ["2x spirit crystal +1", "2x rejuvenation potion", "evolution charm"]
               ],
               [
                   "Trail 05: Defeat Mila",  # 83b06037-1fe2-47d9-8887-479a7b0104d6 [{"Pusseen":9}, {"Slimee":7}]
                   "Trail 05: Defeat Roy",  # e6cda171-22b9-43fb-9ca0-f2411e2e4226 [{"Rawry":10}]
                   "Trail 05: Defeat Lulu",  # 72a096dd-0fe8-4146-9bf0-c7d5e5234b98 [{"Boobae":10}, {"Beebee":7}]
               ],
               None,
               ["Left", "TunnelsOut"],
               ["Left", "TunnelsOut"]),

    Map_Region("SandyTunnels", False,
               True, ["Spinnie", "Octopussy", "Chubbie", "Rawry", "Serpentax"], [10, 13],
               False, None, None,
               [
                   "Sandy Tunnels: Chest South of Chad",  # ba7ef7c4-2cbe-48ef-b777-c9c279d3a8f3 ["2x healing potion", "50x coin", "fallen star"]
                   "Sandy Tunnels: Chest North of Chad",  # 323a990d-8933-4c80-839b-1c40a3eeaaf9 ["chastity belt of love"]
                   "Sandy Tunnels: Chest West of Destiny",  # 0cceeb16-b7e3-4440-916f-c08d6662a535 ["2x stamina potion"]
                   "Sandy Tunnels: Healing Potion From Jessica",  # c135099c-4730-4f32-a9c8-1c79ac82945b ["healing potion"]
               ],
               [
                   "Sandy Tunnels: Defeat Chad",  # 666003ef-c69e-4279-809a-e757e8cb60b2 [{"Octopussy":10}]
                   "Sandy Tunnels: Defeat Destiny",  # 265abaf4-18eb-45fd-8aba-6bc4f8844f81 [{"Oakie":9}, {"Serpentina":7}]
               ],
               None,
               ["Top", "Bottom"],
               ["Top", "Bottom"]),

    Map_Region("Trail6", False,
               True, ["Serpentax", "Boobae", "Rawry", "Birdy", "Cactee", "Twerky"], [11, 13],
               False, None, None,
               [
                   "Trail 06: Chest West of Sandy Tunnels Entrance",  # 002d680f-44a9-4e90-8827-c57cc8f69e65 ["2x healing potion", "candy cane"]
                   "Trail 06: Chest East of Kelsie",  # be999696-f2d3-4379-adf3-7d16693a5e5f ["2x cupcake", "30x coin"]
                   "Trail 06: Chest South of Hayden",  # 2c975ba2-b3a3-4cea-adb9-b66ddf3c42fc ["red collar"]
               ],
               [
                   "Trail 06: Defeat Kelsie",  # acd2e86c-2cdd-48e9-aaed-ba84a84d70a3 [{"Serpentax":10}, {"Wolfy":8}]
                   "Trail 06: Defeat Hayden",  # 8cad5228-7db2-49cd-9fcc-e625029e6817 [{"Beebee":9}]
                   "Trail 06: Defeat Juliet",  # 4cc138d0-8b3d-4ea6-8dd4-e593ae0d9aef [{"Spinnie":10}, {"Tinky":7}]
               ],
               None,
               ["TunnelsOut", "Right"],
               ["TunnelsOut", "Right"]),

    Map_Region("DairyFarm", True,
               True, ["Serpentax", "Birdy", "Cactee", "Twerky", "Bovina", "lacteena", "Flora"], [11, 14],
               False, None, None,
               [
                   "Dairy Farm: Chest North of Waystone",  # 303be291-de84-4fae-b055-822959b7cc0a ["100x coin"]
                   "Dairy Farm: Chest South of Waystone",  # d27f5dea-d45b-4cb8-9df8-67538b55548d ["rejuvination potion", "infinity charm"]
                   "Dairy Farm: Chest Next to House",  # f54b3d20-a63e-4f8b-ac30-4c6d8875dd61 ["candy cane"]
                   "Dairy Farm: Chest North-East of House",  # d6f46d56-9a4b-4225-a4ca-a01067840674 ["2x cocolate cake", "cleansing tonic"]
               ],
               None,
               ["Complete Side Quest: Cattle Thieves"],
               ["Left", "Right"],
               ["Left", "Right"]),

    Map_Region("Trail7", False,
               True, ["Bovina", "Lacteena", "Flora", "Birdy", "Hornie", "Buzzeena", "Bellend"], [12, 14],
               False, None, None,
               [
                   "Trail 07: Chest Near Dairy Farm Entrance",  # 38122e15-ff3c-4777-be9f-53b2e7c8c73c ["2x spirit repelent"]
                   "Trail 07: Chest North of Bella",  # add11e84-b206-48ba-b2dd-2ff56262eabc ["rubber fist"]
                   "Trail 07: Chest South of Bella",  # d834c481-c66d-4f5a-a3f3-376b6239c4a0 ["2x spirit crystal+1", "25x coin"]
                   "Trail 07: Chest South of Dakota",  # c22c51bc-6eaf-40ed-9f4b-62a6e1268a88 ["75x coin"]
               ],
               [
                   "Trail 07: Defeat Sally McTits",  # 6db1fd7b-c78b-4de1-967c-ce67e656236e [{"Dripsy":14}, {"Gloreen":13}, {"Kittypus":13}, {"Boobae":11}]
                   "Trail 07: Defeat Bella",  # 56c3e787-d36a-4e11-aead-ea47f500e261 [{"Serpentax":13}, {"cactee":10}, {"Bovina":11}]
                   "Trail 07: Defeat Dakota",  # ab480291-fa67-4ec2-a724-c048b4537914 [{"Birdy":12}, {"Flora":11}]
                   "Trail 07: Defeat Cassidy",  # 0f05b20d-99cf-4cee-852e-7e5edac5a456 [{"Twerky":11}, {"Buzzeena":13}, {"Tinky":10}, {"Octopussy":11}]
               ],
               None,
               ["Left", "Right"],
               ["Left", "Right"]),

    Map_Region("TumbleweedTown", True,
               False, None, None,
               False, None, None,
               [
                   "Tumbleweed Town: Chest South of Town",  # e4d4ae3a-d411-488f-819d-a9624148a5ed ["2x rejuvination potion", "fallen star"]
                   "Tumbleweed Town: Chest North-West of Town",  # b0973844-878a-47e9-8ab2-bea68625ace0 ["swift plug"]
               ],
               [
                   "Tumbleweed Town: Defeat Willy Wanker",  # MODIFY SASSY NPC ??? 2aefb292-7d0d-4674-a0bd-eb5e487b1272 [{"Bearboo":17}, {"Kittypus":17}, {"Bunni":16}]
                   "Tumbleweed Town: Defeat Dick Cummings",  # MODIFY SASSY NPC ??? 2aefb292-7d0d-4674-a0bd-eb5e487b1272 [{"Lacteena":18}, {"Megaboob":20}, {"Triboobe":17}, {"Bovina":17}]
                   "Tumbleweed Town: Defeat Dick Louie",  # MODIFY SASSY NPC ??? 2aefb292-7d0d-4674-a0bd-eb5e487b1272 [{"Buzzeena":19}, {"Flora":18}, {"Gloreen":19}, {"Thiccsie":18}, {"Spinnie":17}]
               ],
               [
                   "Complete Main Quest: Dusty Vale awaits",
                   "Complete Main Quest: The Grand Cuckold Challenge",
                   "Complete Main Quest: A challenge awaits",
                   "Complete Main Quest: A new challenger",
                   "Complete Main Quest: Stiff competition",
                   "Complete Main Quest: Final Fight",
                   "Complete Main Quest: Mission success",
                   "Complete Main Quest: How the Dominoes fall",
                   "Complete Main Quest: Big balloon adventure",
               ],
               ["Left", "Bottom", "Top", "ClinicOut", "KingsSaloonOut", "MerchantOut", "SmallHouseOut"],
               ["Left", "Bottom", "Top", "ClinicOut", "KingsSaloonOut", "MerchantOut", "SmallHouseOut"]),

    Map_Region("TumbleweedTown_Clinic", False, False, None, None, False, None, None, None, None, None, ["Bottom"], ["Bottom"]),

    Map_Region("TumbleweedTown_KingsSaloon1", False, False, None, None, False, None, None, None, None,
               [
                   "Complete Main Quest: An audience with the King",
                   "Complete Main Quest: Return of the champion",
                   "Complete Main Quest: Breeding season",
               ],
               ["Bottom"], ["Bottom"]),

    Map_Region("TumbleweedTown_Merchant", False, False, None, None, False, None, None, None, None, None, ["Bottom"], ["Bottom"]),

    Map_Region("TumbleweedTown_SmallHouse1", False, False, None, None, False, None, None,
               [
                   "Tumbleweed Town House: Chest in House",  # 71627b20-173d-4c34-8242-82806333e7b5 ["2x strawberry cake", "30x coin"]
               ],
               None, None, ["Bottom"], ["Bottom"]),

    Map_Region("Trail8", False,
               True, ["Cactee", "Birdy", "Buzzeena", "Bellend", "Flora", "Gloreen", "Triboobe", "Kittypus"], [13, 15],
               False, None, None,
               [
                   "Trail 08: Chest West of Tumbleweed Town Entrance",  # 24c5ce52-ec0f-492f-9447-401df4f6c100 ["healing potion", "25x coin"]
                   "Trail 08: Chest South of Marisa",  # baea8603-5e88-4935-95a9-ef10c47e8bad ["butt plug of life +1"]
                   "Trail 08: Chest Near Dusty Grotto Entrance",  # 54012631-5481-4e97-85b3-835e6f2128ab ["potent scent", "elusive scent"]
               ],
               [
                   "Trail 08: Defeat Marisa",  # e07a91ad-6fd5-4d54-8b05-36c3f9d090c1 [{"Lacteena":13}, {"Hornie":13}]
                   "Trail 08: Defeat Jenni",  # bd2e9de2-30db-42f2-aa44-678cf71649ea [{"Gloreen":14}, {"Birdy":12}]
                   "Trail 08: Defeat Alanna",  # 163d96da-8b46-4b1e-baf6-e46708072abe [{"Buzzeena":14}, {"Serpentax":13}, {"Flora":13}]
               ],
               None,
               ["Top", "Tunnel"],
               ["Top", "Tunnel"]),

    Map_Region("DustyGrotto", False,
               True, ["Serpentax", "Twerky", "Hornie", "Dripsy", "Octocunt", "Bearboo"], [13, 16],
               False, None, None,
               [
                   "Dusty Grotto: Chest Near Crystal",  # 25d61715-32da-4887-a04d-381b74e7fd70 ["seed of life", "100x coin", "infinity charm"]
                   "Dusty Grotto: Chest West of Skye",  # b859600e-fad1-486c-9879-5d0782077bc3 ["2x spirit crystal+1", "candy cane"]
               ],
               [
                   "Dusty Grotto: Defeat Arnie",  # af5b25fb-7066-4fca-b1fa-c94fb7e5f330 [{"Chubbie":14}, {"Bunni":12}, {"Hornie":15}]
                   "Dusty Grotto: Defeat Crystal",  # cf1d4fc7-2757-41ea-8198-322dda687398 [{"Buzzeena":15}, {"Cactee":12}]
                   "Dusty Grotto: Defeat Skye",  # 176d7645-f963-47ca-9af5-344d1c2e8dc0 [{"Lacteena":13}, {"Serpentax":14}, {"Rawry":13}]
               ],
               None,
               ["Top", "Bottom"],
               ["Top", "Bottom"]),

    Map_Region("OldMastersHut", False,
               True, ["Dripsy", "Cactee", "Triboobe", "Lacteena", "Harlie", "Growleen"], [15, 17],
               False, None, None,
               [
                   "Old Masters Hut: Chest North of House",  # 33323326-8c5c-448e-acac-2f50cba62286 ["stamina potion", "50x coin"]
                   "Old Masters Hut: Chest Next to House",  # 7410e48c-cf0e-42da-9760-e0d756ec5856 ["2x rejuvination potion", "3x spirit crystal+1"]
               ],
               None,
               None,
               ["HutOut", "Tunnel", "Cave"],
               ["HutOut", "Tunnel", "Cave"]),

    Map_Region("OldMastersHut_Upstairs", False,
               False, None, None,
               False, None, None,
               [
                   "Old Masters Hut: Chest in House",  # bbef9238-1d46-4d89-8f42-3f086d169e35 ["2x spirit crystal+1"]
               ],
               None,
               [
                   "Complete Main Quest: License to battle",
                   "Complete Main Quest: Box pusher",
                   "Complete Main Quest: Total domination",
               ],
               ["Bottom", "Basement"],
               ["Bottom", "Basement"]),

    Map_Region("OldMastersHut_Basement", False,
               False, None, None,
               False, None, None,
               [
                   "Old Masters Hut: Chest in Basement",  # 0feafe23-7fc6-4175-b8b1-90d2323095ce ["video cassette"]
               ],
               None,
               None,
               ["Bottom"],
               ["Bottom"]),

    Map_Region("CaveOfTorment", False,
               True, ["Hornie", "Octocunt", "Domina", "Dracoomer"], [15, 17],
               False, None, None,
               [
                   "Cave of Torment: Chest East Side of Cave",  # 52ca3362-6a85-4eba-9a4e-64d29dca413e ["150x coin", "infinity charm"]
                   "Cave of Torment: Chest North Side of Cave",  # f6f9100f-d007-4407-8273-bb8ac9fc98a7 ["golden seed of life"]
                   "Cave of Torment: Chest West Side of Cave",  # e44bc915-f705-4b68-8a9d-a3527264dad8 ["spiked collar"]
               ],
               None,
               None,
               ["Bottom"],
               ["Bottom"]),

    Map_Region("Trail9", False,
               True, ["Lacteena", "Growleen", "Harlie", "Dracoomer", "Triboobe", "Thiccsie", "Megaboob"], [16, 18],
               False, None, None,
               [
                   "Trail 09: Chest near Clementine",  # 369c6ee5-6b6a-4433-ae92-e5f4b9e911e1 ["2x chocolate cake"]
                   "Trail 09: Chest North of Mike",  # 1457c1a2-8177-4571-b438-f53cb9c6cd34 ["2x spirit crystal +1"]
                   "Trail 09: Chest Near Stone Temple Back Entrance Ledge",  # 8af95e31-a76f-4004-9ed4-d208fb94efb3 ["2x candy cane"]
               ],
               [
                   "Trail 09: Defeat Mike",  # f792e755-6771-4f50-8dca-8d3cf8b6017a [{"Birdy":16}, {"Buzzeena":15}]
                   "Trail 09: Defeat Clementine",  # 00c525ca-41d2-40ba-a68e-c40f8990652c [{"Bovina":14}, {"Gloreen":16}]
                   "Trail 09: Defeat Bonnie",  # b4d3fec1-9f7f-4b2e-a3de-cf25bc3fe399 [{"Octocunt":17}, {"Buxzzeena":16}, {"Growleen":16}]
               ],
               None,
               ["Bottom", "Temple"],#, "TempleBackdoor"
               ["Bottom", "Temple"]),#, "TempleBackdoor"

    Map_Region("DesertTemple1", False,
               False, None, None,
               False, None, None,
               [
                   "Stone Temple 1: Chest Near Trail 09 Entrence",  # 515e573f-cf67-473f-a241-7177098013c1 ["2x cupcake", "seed of life", "50x coin"]
                   "Stone Temple 1: Chest Near 6th Crimson Cloak",  # 1f27c663-1dce-47e0-821c-8fd1aae55a46 ["turtle chell collar", "fallen star"]
                   "Stone Temple 1: Chest Near Stone Temple 2 Entrance",  # 57db7ff2-69b0-4c98-a81b-79b30eb2dd88 ["2x healing potion", "50x coin"]
               ],
               [
                   "Stone Temple 1: Defeat 1st Crimson Cloak",  # 48a6856e-4dbd-4ca9-b6d5-066b5a55d783 [{"Domina":19}, {"Growleen":18}]
                   "Stone Temple 1: Defeat 2nd Crimson Cloak",  # 7b40e4f2-990b-4a2c-8ccc-aa283653436a [{"Buzzeena":17}]
                   "Stone Temple 1: Defeat 3rd Crimson Cloak",  # b3ab8b9c-5260-47a6-befc-d99487a2a53f [{"Kittypus":16}, {"Flora":17}, {"Dripsy":15}]
                   "Stone Temple 1: Defeat 4th Crimson Cloak",  # bf8484cc-5889-45ce-8b18-c35b96e0d0e7 [{"Harlie":18}]
                   "Stone Temple 1: Defeat 5th Crimson Cloak",  # 02067b08-1777-4713-af0d-123bb86102fe [{"Lacteena":20}, {"Octocunt":18}]
                   "Stone Temple 1: Defeat 6th Crimson Cloak",  # a0268c7e-1417-41cb-aa2a-109240ff2eac [{"Megaboob":18}]
               ],
               None,
               ["Bottom", "Top"],
               ["Bottom", "Top"]),

    Map_Region("DesertTemple2", False,
               False, None, None,
               False, None, None,
               None,
               [
                   "Stone Temple 2: Defeat Domino"  # [{"Octocunt":18}, {"Serpentax":19}, {"Harlie":18}, {"Hornie":17}, {"Bearboo":17}]
               ],
               ["Complete Main Quest: Quest for the crystal"],
               ["Bottom", "Top"],
               ["Bottom", "Top"]),

    Map_Region("CrashSite", True,
               True, ["Thiccsie", "Megaboob", "Kittypus", "Sexybun", "Mamaoak"], [19, 20],
               False, None, None,
               [
                   "Crash Site: Chest East of Athena",  # 20af0b9d-a48e-4dff-995e-53758e7d61f3 ["150x coins", "2x healing potion"]
                   "Crash Site: Chest West of Janet",  # c6f2ad98-a787-4805-9c9b-fca34bd7dee3 ["2x spirit crystal +1"]
                   "Crash Site: Chest South of Janet",  # 2300e642-581b-43e8-bc83-c78a246fe948 ["candy cane"]
               ],
               [
                   "Crash Site: Defeat Athena",  # ae458556-c336-43a7-a7c3-be76c84f0a48 [{"Pinchie":18}, {"Dracoomer":17}, {"Cactee":15}]
                   "Crash Site: Defeat Janet",  # ef863488-65f8-4827-9e80-0e1c6a42b681 [{"Mamaoak":21}, {"Bearboo":16}]
               ],
               None,
               ["Bottom"],
               ["Bottom"]),

    Map_Region("Trail10", False,
               True, ["Megaboob", "Growleen", "Sexybun", "Mamaoak", "Pinchie"], [19, 21],
               True, ["Marinel", "Pinchie"], [19, 20],
               [
                   "Trail 10: Chest West of Crash Site Entrance",  # cbbdd4da-69d4-41c2-9165-ea07e647a369 ["100x coins", "infinity charm"]
                   "Trail 10: Chest Near Eve",  # 545492fc-2eea-4a81-b1db-12825748f4a0 ["2x stamina potion"]
                   "Trail 10: Chest South of Bailee",  # 5c21066a-081c-4c75-8a0f-1694ccddbe1f ["ball gag +1", "fallen star"]
               ],
               [
                   "Trail 10: Defeat Bailee",  # b15889a3-63eb-490f-8f7b-e14555ac9d97 [{"Amazona":20}, {"Octocunt":17}]
                   "Trail 10: Defeat Eve",  # 6ee5a399-6614-482d-8e07-00abcf34d10e [{"Domina":17}, {"Sexybun":21}]
               ],
               None,
               ["Top", "Left"],
               ["Top", "Left"]),

    Map_Region("CoconutVillage", True,
               False, None, None,
               False, None, None,
               [
                   "Coconut Village: Chest North-East in Village",  # 9b0fd14d-0aec-4790-900f-553f98af0eb1 ["Butt Plug of Power +1"]
                   "Coconut Village: Chest East of Village",  # 56fa7c21-327e-4f5f-8fe2-1b1d35da3dc9 ["50x coin", "red latex mask"]
               ],
               None,
               [
               ],
               ["Right", "Left", "ClinicOut", "MerchantOut", "TempleOut", "House1Out", "House2Out"],
               ["Right", "Left", "ClinicOut", "MerchantOut", "TempleOut", "House1Out", "House2Out"]),

    Map_Region("CoconutVillage_Clinic", False, False, None, None, False, None, None, None, None, None, ["Bottom"], ["Bottom"]),

    Map_Region("CoconutVillage_Merchant", False, False, None, None, False, None, None, None, None, None, ["Bottom"], ["Bottom"]),

    Map_Region("CoconutVillage_Temple", False, False, None, None, False, None, None,
               [
                   "Coconut Village: Chest in Temple",  # e68357b4-2017-4962-9935-febbb8afa19e ["2x greater healing potion"]
                   "Coconut Village: Chest In Temple After Locked Door",  # 11a5f5c0-f303-469e-96f0-d0df45d2e631 ["red harmony crystal"]
               ],
               None,
               [
                   "Complete Main Quest: Welcome to Paradise",
                   "Complete Main Quest: Savior of Coconut Village",
                   "Complete Main Quest: Slippery When Wet",
                   "Complete Main Quest: Glimmering Prize",
                   "Complete Main Quest: Arctic Adventure",
               ],
               ["Bottom"], ["Bottom"]),

    Map_Region("CoconutVillage_House1", False, False, None, None, False, None, None,
               [
                   "Coconut Village House: Chest in House",  # 8a4cdd76-b0a6-4256-a9d4-5797167f7ae5 ["Seed of Life", "50x coins"]
               ],
               None, None, ["Bottom"], ["Bottom"]),

    Map_Region("CoconutVillage_House2", False, False, None, None, False, None, None, None, None,
               [
                   "Complete Side Quest: Professional Pleasurer"
               ],
               ["Bottom"], ["Bottom"]),

    Map_Region("Trail11", False,
               True, ["Octocunt", "Pinchie", "Sexybun", "Mamaoak", "Udderella"], [21, 22],
               True, ["Sharky", "Marinel"], [21, 22],
               [
                   "Trail 11: Chest Near Alice",  # 7e5e1b32-a395-449e-8524-85100357f829 ["Strawberry cake"]
                   "Trail 11: Chest Near Pier",  # fc2ae356-2928-4f20-b00a-882f8498ebfc ["2x spirit crystal +1"]
                   "Trail 11: Chest East of Emilia",  # 1eb894db-663f-4ef8-8bec-9eff702f539b ["2x spirit repellent"]
                   "Trail 11: Chest South of Sydney",  # f54d4a60-9550-4505-962d-917242c1853e ["2x elusive scent"]
               ],
               [
                   "Trail 11: Defeat Alice",  # NPC [{"Marinel":21}, {"Pinchie":20}, {"Sharky":22}]
                   "Trail 11: Defeat Emilia",  # cc69f7aa-a078-448c-ab25-00c8f774926f [{"Hornie":17}, {"Marinel":19}]
                   "Trail 11: Defeat Sydney",  # 2bf2f7ed-e375-4747-875c-3bd1b2048e46 [{"Octocunt":16}, {"Mamaoak":20}, {"Serpentax":17}]
               ],
               [
                   "Complete Side Quest: Fishmaster’s Challenge",
                   "Complete Side Quest: Deadly Waters"
               ],
               ["Right", "Bottom", "pier"],
               ["Right", "Bottom", "pier"]),

    Map_Region("Trail12", False,
               True, ["Octocunt", "Pinchie", "Dracoomer", "Udderella", "Faerie"], [21, 23],
               True, ["Marinel", "Pinchie", "Chocostar", "Octocunt"], [21, 23],
               [
                   "Trail 12: Chest North of Sophie",  # e2598159-fb05-4e8f-88a4-cbb55d12546f ["2x cleansing tonic", "50x coins"]
                   "Trail 12: Chest North of Ciara",  # df5ab9f9-17b1-4629-a683-8e1c6ff122e4 ["evolution charm", "50x coins"]
               ],
               [
                   "Trail 12: Defeat Sophie",  # ddc0cee9-5a37-431b-baf8-8653a97f13a0 [{"Harlie":17}, {"Faerie":21}]
                   "Trail 12: Defeat Ciara",  # 961a23f5-023b-4d31-ab65-b8d227a52ded [{"Grewleen":17}, {"Dracoomer":17}, {"Sharky":20}]
               ],
               ["Complete Side Quest: Starry Eyed Surprise"],
               ["Bottom", "Top"],
               ["Bottom", "Top"]),

    Map_Region("FishingHut", False,
               True, ["Pinchie", "Thiccsie", "Faerie", "Twerqueen"], [21, 23],
               False, None, None,
               [
                   "Fishing Hut: Chest North-West on the Beach",  # ed0b2740-17bd-49bb-b431-8ee30ffee485 ["dragon dildo +1"]
                   "Fishing Hut: Chest Next to House",  # 570c6d8b-0f44-4611-8c16-676ea4f2dcf7 ["100x coins", "2x stamina potion"]
                   "Fishing Hut: Chest East on the Beach",  # 38a94edd-1946-4076-8ddf-c9e9bf6b3358 ["2x rejuvenation potion"]
                   "Fishing Hut: Chest Eastern Side of Map",  # 8fa902d2-fc53-4502-b2a4-edd4c2fcdbba ["greater healing potion"]
               ],
               [
                   "Fishing Hut: Defeat Bonnie Baiter",  # 05ba33a6-2693-49ba-b570-543c25feeeb2 #NPC [{"chocostar":21}, {"Mamaoak":20}, {"Marinel":20}]
               ],
               [
                   "Complete Side Quest: Fishy Duel",
                   "Complete Side Quest: The Art of Fishing"
               ],
               ["Top"],
               ["Top"]),

    Map_Region("Trail13", False,
               True, ["Twerqueen", "Faerie", "Sexybun", "Amazona"], [22, 24],
               True, ["Jellygal", "Sharky", "Chocostar"], [22, 24],
               [
                   "Trail 13: Chest South-West of 1st Cultist",  # 2432ca26-daf4-4f91-b0f5-65094ef2f236 ["butt plug of life +1", "infinity charm"]
                   "Trail 13: Chest North of 1st Cultist",  # e349a432-ea25-48fa-b78a-4f7e24a1a21e ["150x coins", "antidote", "fallen star"]
               ],
               [
                   "Trail 13: Defeat 1st Cultist",  # a4a13dee-d151-407c-8ed1-8db2d45efdf2 [{"Gloreen":23}, {"Mamaoak":21}, {"Sharky":20}]
                   "Trail 13: Defeat 2nd Cultist",  # b4a8bd50-ab01-4e3c-8aba-0469ada1c52f [{"Triboobe":21}, {"Dripsy":23}]
               ],
               ["Complete Main Quest: Coconut Conundrum"],
               ["Left", "pier"],
               ["Left", "pier"]),

    Map_Region("Trail14", True,
               True, ["Faerie", "Amazona", "Mamaoak", "Harpie"], [23, 25],
               True, ["Marinel", "Jellygal", "Sharky"], [23, 25],
               [
                   "Trail 14: Chest North-West of 1st Cultist",  # 5fb24dfe-bb8f-4e3d-b5d2-f18331df4040 ["Spiked Collar +1"]
                   "Trail 14: Chest East of 1st Cultist",  # 4e89c1b8-d75b-4dd1-b333-c091f0683bd8 ["chocolate cake", "2x candy cane"]
                   "Trail 14: Chest East of Waystone",  # 7b172b42-b00c-4e6b-a6d2-3176cac758d3 ["2x rejuvenation potion", "2x stamina potion"]
               ],
               [
                   "Trail 14: Defeat 1st Cultist",  # 38dd508c-5633-47c3-b142-846c3915716d [{"Kittypus":18}, {"Thiccsie":20}, {"Jellygal":22}]
                   "Trail 14: Defeat 2nd Cultist",  # 9b009cf3-5fad-4076-88d2-3e43e004efec [{"Buzzeena":18}, {"Sexybun":22}, {"Twerqueen":24}, {"Chocostar":20}]
               ],
               None,
               ["Right", "CaveIn"],#, "CaveOut"
               ["Right", "CaveIn"]),#, "CaveOut"

    Map_Region("IslandCave", False,
               True, ["Amazona", "Harpie", "Twerqueen", "Arachna", "Succubae"], [23, 25],
               False, None, None,
               [
                   "Island Cave 1: Chest North-West After 1st Cultist",  # be99f6ef-4289-45b9-b8ca-c6432f64c982 ["Golden Chastity belt"]
                   "Island Cave 1: Chest East After 2st Cultist",  # 1ffad415-a599-4752-a847-c093e51cbcbe ["2x greater healing potion"]
                   "Island Cave 1: Chest West After 2nd Cultist",  # 78734a81-9888-4e7f-97a8-1b68f590ef43 ["evolution charm", "200x coin"]
                   "Island Cave 1: Chest Near 3rd Cultist",  # 9ad68fef-4f77-4490-9ccd-5d779083bddb ["seed of life", "the ace of spades"]
               ],
               [
                   "Island Cave 1: Defeat 1st Cultist",  # 5fbd94fe-f5dc-42bb-9f57-dbaec4d8d3c3 [{"Bovina":18}, {"Mamaoak":22}]
                   "Island Cave 1: Defeat 2nd Cultist",  # 1ad60dfe-2454-431e-8f8a-8f512003aa1d [{"Harpie":23}, {"Twerqueen":23}, {"Amazona":20}]
                   "Island Cave 1: Defeat 3rd Cultist",  # 46a60f99-3cb9-42cf-860f-9e471707e263 [{"Lacteena":22}, {"Jellygal":24}]
                   "Island Cave 1: Defeat 4th Cultist",  # 5f53e18a-e6b1-473a-8252-f0d68286ca57 [{"Succubae":25}, {"Udderella":22}]
               ],
               None,
               ["Bottom", "Top"],
               ["Bottom", "Top"]),

    Map_Region("IslandCave2", False,
               False, None, None,
               False, None, None,
               None,
               [
                   "Island Cave 2: Defeat Centiboob",  # NPC SCRIPTED [{"Centiboob":26}]
               ],
               ["Complete Main Quest: Lusty Cultists"],
               ["Bottom", "Top"],
               ["Bottom", "Top"]),

    Map_Region("ColdHarbor", True,
               True, ["Harpie", "Pinchie", "Gangfang", "Octomommy", "Snowbae"], [25, 27],
               True, ["Chocostar", "Pinchie"], [25, 27],
               [
                   "Cold Harbour: Chest North-East of Waystone",  # 4f0e46a1-ad29-4472-a6a9-24120c07535c ["2x spirit crystal +2", "greater rejuvenation potion"]
                   "Cold Harbour: Chest East of Iris",  # 4b5bceb4-7cff-4419-8116-cf5dd4e6dcb8 ["200x coins", "2x XP Boosters"]
               ],
               [
                   "Cold Harbour: Defeat Vanessa",  # 323cbfec-0db2-43c2-a538-e3b4cf02d260 [{"Harpie":25}, {"Gangfang":26}]
                   "Cold Harbour: Defeat Iris",  # c34254a6-6f54-4643-8319-75636a798542 [{"Amazona":22}, {"Polaria":26}, {"Snowbae":23}]
               ],
               ["Complete Main Quest: The Frigid Maiden"],
               ["Top"],
               ["Top"]),

    Map_Region("Frostville1", True,
               False, None, None,
               False, None, None,
               [
                   "Frostville: Chest North of Waystone",  # dd42f2b7-841c-4726-a597-a8e197e384f4 ["2x greater healing potions"]
                   "Frostville: Chest South of Waystone",  # d4f07026-13b3-4b49-ae53-57764bed39a6 ["3x spirit crystal +2", "fallen star"]
                   "Frostville: Chest West of Town",  # 4c13b886-9a90-4896-b235-d013e69c60e6 ["ball gag +2"]
               ],
               [
               ],
               [
                   "Complete Main Quest: Arctic Isles",
                   "Complete Main Quest: Paisley Bones",
                   "Complete Main Quest: Here Comes the Boom",
               ],
               ["Bottom", "Top", "Left", "ClinicOut", "MerchantOut", "Church", "House1"],
               ["Bottom", "Top", "Left", "ClinicOut", "MerchantOut", "Church", "House1"]),

    Map_Region("Frostville1_Clinic", False, False, None, None, False, None, None, None, None, None, ["Bottom"], ["Bottom"]),

    Map_Region("Frostville1_Merchant", False, False, None, None, False, None, None, None, None, None, ["Bottom"], ["Bottom"]),

    Map_Region("Frostville1_Church", False, False, None, None, False, None, None, None,
               [
                   "Frostville: Defeat Mother Evilyn",  # aa1ce20e-a988-48c9-8a4b-e246fb163402 [{"Hornie":29}, {"Arachna":32}, {"Octomommy":31}]
               ],
               [
                   "Complete Main Quest: Stealing From a Dead Man",
                   "Complete Main Quest: The Lewd Exorcist",
               ],
               ["Bottom"], ["Bottom"]),

    Map_Region("Frostville1_House1", False, False, None, None, False, None, None, None, None,
               [
                   "Complete Main Quest: The Proposal",
               ],
               ["Bottom"], ["Bottom"]),

    Map_Region("Trail15", False,
               True, ["Archna", "Gangfang", "Octomommy", "Snowbae", "Polaria", "Deardeer"], [26, 27],
               False, None, None,
               [
                   "Trail 15: Chest South of Frostville Entrence",  # 18ec8ed3-304e-47a1-8311-b53e9e76ceee ["chocolate cake", "150x coins"]
                   "Trail 15: Chest West of Mia",  # c8875e05-570c-4b7c-a3a6-3939a80e373d ["2x greater rejuvenation potion", "2x cleansing tonic"]
                   "Trail 15: Chest South-West of Olga",  # 334ebd4f-e47e-494a-9010-f0e431e93cd3 ["Spiked Collar +2"]
               ],
               [
                   "Trail 15: Defeat Mia",  # 705f45eb-9221-4c47-b339-e8d2b2f6d862 [{"Deardeer":25}, {"Chocostar":25}]
                   "Trail 15: Defeat Olga",  # 9f573d72-be6e-48dc-9ffd-50044176a86c [{"Pinchie":24}, {"Polaria":27}, {"Harpie":26}]
               ],
               ["Complete Side Quest: Arctic Menace"],
               ["Right", "Left", "Left2"],
               ["Right", "Left", "Left2"]),

    Map_Region("Trail16", False,
               True, ["Gangfang", "Polaria", "Octomommy", "Snowbae", "Deardeer", "Slithereen"], [27, 28],
               True, ["Jawsy"], [27, 28],
               [
                   "Trail 16: Chest North of Karin",  # f55efa41-a0da-4307-aa3b-584c1238ddaf ["2x spirit crystal +2"]
                   "Trail 16: Chest North-West of Karin",  # 97595abc-e511-4733-827e-e6180c716210 ["2x greater stamina potion"]
                   "Trail 16: Chest East of Dahlia",  # e89b33c2-ef03-4abd-b216-81df8d7e0f65 ["2x spirit repellent", "xp boosters"]
               ],
               [
                   "Trail 16: Defeat Karin",  # 911604b8-a719-4eb6-af17-42bd8dc35a9b [{"Mamaoak":21}, {"Gangfang":26}]
                   "Trail 16: Defeat Dahlia",  # 1e4eb581-53ee-4f87-b021-ff0ebc931798 [{"Snowbae":25}, {"Chocostar":23}, {"Polaria":28}]
               ],
               None,
               ["Right", "Left"],
               ["Right", "Left"]),

    Map_Region("Trail16_Top", False,
               True, ["Gangfang", "Polaria", "Octomommy", "Snowbae", "Deardeer", "Slithereen"], [27, 28],  # SAME AS trail16
               False, None, None,
               [
                   "Trail 16 Top: Chest South of Cave Entrence",  # 60a5df17-adb0-46ba-ae67-e4df1e45718f ["fallen star", "Golden Seed of life"]
               ],
               None, None, ["Right2", "Cave"], ["Right2", "Cave"]),

    Map_Region("Trail16_Cave", False,
               True, ["Valkyrie_Normal"], [29, 32],  # REQUIRES FISHY SCENT
               False, None, None, None, None, None,
               ["Bottom"],
               ["Bottom"]),

    Map_Region("AbandonedMine", True,
               True, ["Gangfang", "Polaria", "Slithereen", "Deardeer", "Slushie"], [28, 30],
               True, ["Jawsy", "Jellybish"], [28, 30],
               [
                   "Abandoned Mine: Chest North of Trail 16 Entrence",  # 46cf0856-3d1c-440b-a065-b357d399964b ["Swift Plug +1", "2x XP boosters"]
                   "Abandoned Mine: Chest South-West of House",  # 575941ce-96f2-477f-b0bc-facec059184c ["3x greater healing potion", "50x coins"]
               ],
               None,
               [
               ],
               ["Right", "House1"],
               ["Right", "House1"]),

    Map_Region("AbandonedMine_House1", False, False, None, None, False, None, None, None, None,
               [
                   "Complete Main Quest: Demand for Dynamite",
                   "Complete Main Quest: Suit In Hand",
                   "Complete Main Quest: Fishing For Treasure",
               ],
               ["Bottom"], ["Bottom"]),

    Map_Region("Trail17", False,
               True, ["Slithereen", "Deardeer", "Slushie", "Queenbee", "Boobarella"], [29, 32],
               True, ["Jellybish", "Jawsy"], [29, 32],
               [
                   "Trail 17: Chest North of Clara",  # db51e404-218c-4288-8860-b5ecf2b25059 ["2x Spirit crystal +2"]
                   "Trail 17: Chest South-East of Liv",  # 2d01eaea-aecd-4b90-9029-6498f03c3558 ["greater rejuvination potion", "greater healing potion"]
                   "Trail 17: Chest North-East of Karly",  # cef39514-d07c-4531-8fa5-52ebd56df4c9 ["2x candy cane", "2x strawberry cake"]
               ],
               [
                   "Trail 17: Defeat Clara",  # 5d964c9f-f399-4a24-98f6-def8af276d4c [{"Slithereen":27}, {"Arachna":28}]
                   "Trail 17: Defeat Liv",  # 38419b1d-9908-4ef4-a962-1406aa2a4352 [{"Jellybish":29}, {"Jawsy":27}, {"Harpie":23}]
                   "Trail 17: Defeat Karly",  # d09da17a-d5b6-415f-986f-9dc216400385 [{"Slushie":25}, {"Gangfang":30}]
               ],
               [
                   "Complete Side Quest: Legend of the Valkyrie part 1.",
                   "Complete Side Quest: Legend of the Valkyrie part 2."
               ],
               ["Bottom", "Right"],
               ["Bottom", "Right"]),

    Map_Region("Trail18", True,
               True, ["Slushie", "Slithereen", "Queenbee", "Boobarella", "Panthera"], [30, 33],
               True, ["Jellybish", "Jawsy"], [30, 33],
               [
                   "Trail 18: Chest South of Anabelle",  # 1f7ba32d-3992-42c2-ab0c-f5b7d382af55 ["2x infinity charm", "2x cleansing tonic"]
                   "Trail 18: Chest in North Part of Map",  # 72243934-12c9-440a-a226-e9de780f25fd ["icey dildo", "55x gold"]
                   "Trail 18: Chest North of Ingrid",  # 02d71004-c006-4b9a-a467-48396c815865 ["fallen star", "greater rejuvination potion"]
               ],
               [
                   "Trail 18: Defeat Stacy",  # 0a2fe22c-e43e-457f-85af-29ed94e9f57d [{"Polaria":30}, {"Harpie":28}]
                   "Trail 18: Defeat Anabelle",  # 4492eac4-575d-46c8-8d4f-4418e4ab1065 [{"Jellybish":31}, {"Slithereen":29}]
                   "Trail 18: Defeat Ingrid",  # 5676a70d-5a1c-4868-906f-a269dffc5f2f [{"Slithereen":28}, {"Queenbee":31}, {"Slushie":25}]
               ],
               [
                   "Complete Main Quest: Crimson Chase",
                   "Complete Main Quest: Through the Portal"
               ],
               ["Left", "TempleIn"],#, "TempleOut"
               ["Left", "TempleIn"]),#, "TempleOut"

    Map_Region("ArcticTemple1", False,
               False, None, None,
               False, None, None,
               [
                   "Artic Temple: Chest in South-East",  # f5c25d35-2be7-445d-8432-f31b58d29f81 ["Vibrating willy+1", "evolution charm"]
                   "Artic Temple: Chest in West",  # c1b51d5f-663e-4ca5-94a2-1611880789d7 ["300x coin", "2x antidote"]
                   "Artic Temple: Chest in North-West",  # c790f2f6-78ae-4e26-b46b-82d0823a6118 ["golden seed of life", "2x greater healing potion"]
               ],
               [
                   "Artic Temple 1: Defeat 1st Crimson Cloak",  # 23aa2df5-197e-45cb-af67-dfc97e83dd3b [{"Octomommy":32}, {"Harpie":26}, {"Mamaoak":27}]
                   "Artic Temple 1: Defeat 2nd Crimson Cloak",  # 1452eb18-e64d-4fb6-93b3-84574ee29396 [{"Arachna":28}, {"Boobarella":31}]
                   "Artic Temple 1: Defeat 3rd Crimson Cloak",  # 4bd72a1d-cdf9-49b4-ba2b-245dabf60035 [{"Jellybish":30}, {"Polaria":29}]
                   "Artic Temple 1: Defeat 4th Crimson Cloak",  # 60f3aad3-3f2d-4ce1-ab4a-f6833957b8ab [{"Slithereen":31}, {"Deardeer":32}]
                   "Artic Temple 1: Defeat 5th Crimson Cloak",  # 5272d410-ae2d-42b5-93a8-b06b4ba20fe2 [{"Gangfang":27}, {"Queenbee":31}]
               ],
               None,
               ["Top", "Bottom"],
               ["Top", "Bottom"]),

    Map_Region("ArcticTemple2", False,
               False, None, None,
               False, None, None,
               None,
               [
                   "Artic Temple 2: Defeat Crimson Countess",  # NPC SEQUENCE [{"Queenbee":32}, {"Chocostar":28}, {"Octomommy":30}, {"Archna":31}, {"Jawsy":33}]
               ],
               ["Complete Main Quest: Arctic Harmony"],
               ["Top", "Bottom"],
               ["Top", "Bottom"]),

    Map_Region("Trail19", True,
               True, ["Queenbee", "Deardeer", "Panthera", "Unihorn", "Fungie"], [33, 35],
               False, None, None,
               [
                   "Trail 19: Chest Near Start",  # c1df6726-ecd8-4863-b1ae-d2d995d6cdf4 ["100 Coin","2x spirit crystal +2"]
                   "Trail 19: Chest South of 1st Crimson Cloak",  # e8bbd1c5-3777-4a13-bcf2-b58e2d6d5d2c ["2x greater healing potion"]
                   "Trail 19: Chest East of 2nd Crimson Cloak",  # 5a746032-358e-4ace-aa5e-bd614f610742 ["2x Cleansing tonic"]
               ],
               [
                   "Trail 19: Defeat 1st Crimson Cloak",  # 97fab556-a752-489c-8de5-04d3449afeca [{"Harpie":34},{"Slithereen":32},]
                   "Trail 19: Defeat 2nd Crimson Cloak",  # ce0b7e57-6bbd-4034-9f2b-2785f6b6f07d [{"Fungie":33},]
                   "Trail 19: Defeat 3rd Crimson Cloak",  # bbb2a608-b9f8-4701-a978-549f98628a70 [{"Arachna":32},{"Jellybish":33},]
               ],
               None,
               ["Top"],
               ["Top"]),

    Map_Region("Trail20", False,
               True, ["Queenbee", "Unihorn", "Fungie", "Juggsie", "Serphina"], [33, 36],
               False, None, None,
               [
                   "Trail 20: Chest Near 1st Crimson Cloak",  # ac4251e7-b377-4124-814a-95601ac2e10f ["Unicorn Dildo"]
                   "Trail 20: Chest Near 2nd Crimson Cloak",  # b8d3a32e-2b9a-45a9-8496-07d98d24ebe3 ["150x coin","2x greater rejuvination potion"]
               ],
               [
                   "Trail 20: Defeat 1st Crimson Cloak",  # 4d8163f6-3e75-4112-9824-7e0247d4118f [{"Chocostar":34},{"Fungie":32},]
                   "Trail 20: Defeat 2nd Crimson Cloak",  # 72d37c80-d416-48b0-8e1f-ab6c9f49e40c [{"Polaria":35},]
               ],
               [
                   "Complete Main Quest: Sanctuary Shakedown",
                   "Complete Main Quest: Breezie Runs Free",
               ],
               ["Bottom", "Left"],
               ["Bottom", "Left"]),

    Map_Region("Trail20_Right", False,
               True, ["Queenbee", "Unihorn", "Fungie", "Juggsie", "Serphina"], [33, 36], #SAME AS Trail20
               False, None, None,
               [
                   "Trail 20 Right: Chest Near Cave Entrance",  # affeeef4-519b-4b7c-8bea-f6011e35c2fe ["Golden seed of life","2x Spirit Repelent"]
               ],
               [
                   "Trail 20 Right: Defeat Crimson Cloak",  # 149cf1b9-7344-4037-88b8-42fe6f471e64 [{"Mamaoak":32},{"Jawsy":34},]
               ],
               None,
               ["Right"],
               ["Right"]),

    Map_Region("Trail21", False,
               True, ["Queenbee", "Fungie", "Juggsie", "Serphina"], [34, 37],
               True, ["Jellybish", "Lizzie"], [34, 37],
               [
                   "Trail 21: Chest Near Pushable Bolder",  # c9bccc23-9abc-412b-a969-be4b38fe8c07 ["fallen star","2x evolution charm"]
                   "Trail 21: Chest North of Pond",  # a0ea4f50-253d-41c3-a01e-4b2c0de0c846 ["2x candy cane"]
                   "Trail 21: Chest South area of map",  # 0c7e4c71-2b16-4171-a256-55820b5f41c5 ["Diamond Butt Plug"]
               ],
               [
                   "Trail 21: Defeat 1st Crimson Cloak",  # ff372848-9064-45a9-9e2c-dd98e3fd1313 [{"Juggsie":36},]
                   "Trail 21: Defeat 2nd Crimson Cloak",  # 24e2596a-4820-46e2-a06a-59a5333d1e4b [{"Unihorn":34},{"Octomommy":30},]
                   "Trail 21: Defeat Kinley",  # 0ea61b92-8dcd-4adf-a070-4bc5870b2698 [{"Queenbee":32},{"Snowbae":30},{"Pinchie":35},{"Boobarella":34},]
               ],
               ["Complete Main Quest: Hostage Situation"],
               ["Right"],
               ["Right"]),

    Map_Region("SpiritPassage", False,
               True, ["Slithereen", "Octomommy", "Fungie", "Dominatrix"], [35, 38],
               False, None, None,
               [
                   "Trail Spirit Passage: Chest north of first fork in path",  # 35f79fc2-e0ce-4b1a-90a5-fc87436b8c51 ["Spiked Collar +3"]
                   "Trail Spirit Passage: Chest in first loop area",  # 1ae0306c-1da3-4248-b1a2-b4ecb14d40c5 ["150x coin","2x cleansing tonic"]
                   "Trail Spirit Passage: Chest north of first loop area",  # dec67487-358b-43b6-a97e-ca892aa95d89 ["2x antidote","2x infinity charm"]
                   "Trail Spirit Passage: Chest near 5th Crimson Cloak",  # ee7e2616-1b0d-4c92-9014-53c9fa72f424 ["200x coin"]
               ],
               [
                   "Trail Spirit Passage: Defeat 1st Crimson Cloak",  # 9eeac2b8-20b3-4d35-a7b9-bb01169dc72d [{"Chocostar ":35},{"Harpie":32},]
                   "Trail Spirit Passage: Defeat 2nd Crimson Cloak",  # 70e65def-a84b-4df5-873c-77d2f02fc30b [{"Slushie":35},]
                   "Trail Spirit Passage: Defeat 3rd Crimson Cloak",  # b8863596-1a75-481f-94ca-4178785f0554 [{"Amazona":37},]
                   "Trail Spirit Passage: Defeat 4th Crimson Cloak",  # 97835a52-0d7b-4d9d-9184-8eb813faf909 [{"Seraphina":38},{"Marinel":36},]
                   "Trail Spirit Passage: Defeat 5th Crimson Cloak",  # a2557c2e-85f8-4511-8d14-da72a962943c [{"Twerqueen":36},{"Faerie":37},]

               ],
               None,
               ["Left", "Right"],
               ["Left", "Right"]),

    Map_Region("Trail22", True,
               True, ["Unihorn", "Juggsie", "Seraphina", "Dominatrix"], [37, 40],
               False, None, None,
               [
                   "Trail 22: Chest north west of pond",  # 22527dc8-b6b1-4af2-974d-2e56b8fc96b6 ["Butt plug of life +2"]
                   "Trail 22: Chest north path before large grass patch",  # a3f235a1-bc10-4012-8203-37be87ecf06c ["2x golden seed of life"]
                   "Trail 22: Chest north of large grass patch",  # e88b6c20-4e22-459e-b229-50bd0edc835d ["250x coin"]
                   "Trail 22: Chest west side of lake near waypoint",  # f533f7ee-5852-4dc8-87c4-73e434942e3d ["3x spirit crystal +2"]
               ],
               [
                   "Trail 22: Defeat 1st Crimson Cloak",  # 7f45394d-44a9-466e-b9a5-7a169ae47754 [{"Deardeer":36},{"Dominatrix":35},{"Octocunt":35},]
                   "Trail 22: Defeat 2nd Crimson Cloak",  # 95124723-8456-47a9-91fa-1576ef841d84 [{"Seraphina":39},{"Unihorn":33},]
                   "Trail 22: Defeat 3rd Crimson Cloak",  # c618afc1-47b2-4de3-b09d-483d57333482 [{"Jawsy":39},]
               ],
               [
                   "Complete Main Quest: Desperate Dash",
                   "Complete Side Quest: Hunt for the Centiboob part 1.",
                   "Complete Side Quest: Hunt for the Centiboob part 2.",
                   "Complete Side Quest: Hunt for the Centiboob part 3.",
               ],
               ["Left", "Top", "Cave"],
               ["Left", "Top", "Cave"]),

    Map_Region("Trail22_Cave", False,
               True, ["Centiboob_Normal"], [37, 40],
               False, None, None,
               [
                   "Trail 22 Cave: Chest In Cave",  # afe7ac71-80d5-45c2-b6c0-683732d1fdf4 ["500x coin"]
               ],
               None,
               None,
               ["Bottom"],
               ["Bottom"]),

    Map_Region("InnerGrove", False,
               False, None, None,
               False, None, None,
               [],
               [
                   "Inner Grove: Defeat Spirit Mother",  # [{"SpiritMother":43},]
               ],
               [
                   "Complete Main Quest: Battle for Spirit Valley"
               ],
               ["Bottom"],
               ["Bottom"]),

]

transition_areas = [
    transititon("OakwoodVillage", "Top", "Trail1", "Bottom", False),
    #transititon("OakwoodVillage", "ClinicOut", "OakwoodVillage_Clinic", "Bottom", False),
    transititon("OakwoodVillage", "FarmHouseOut", "OakwoodVillage_FarmHouse", "Bottom", False),
    transititon("OakwoodVillage", "HqOut", "OakwoodVillage_Hq", "Bottom", False),

    transititon("Trail1", "Top", "EvergreenOutpost", "Bottom", False),

    transititon("EvergreenOutpost", "Left", "Trail2", "Right", False),
    transititon("EvergreenOutpost_East", "Right", "Trail5", "Left", False),

    transititon("Trail2", "Left", "Greensvale", "Right", False),

    transititon("Greensvale", "Top", "Trail3", "Bottom", False),
    transititon("Greensvale", "Bottom", "MillysFarm", "Top", False),
    transititon("Greensvale", "ClinicOut", "Greensvale_Clinic", "Bottom", False),
    transititon("Greensvale", "MerchantOut", "Greensvale_Merchant", "Bottom", False),
    transititon("Greensvale", "SexShopOut", "Greensvale_SexShop", "Bottom", False),
    transititon("Greensvale", "SmallHouseOut", "Greensvale_SmallHouse", "Bottom", False),

    transititon("Trail3", "Cave", "EvergreenCaverns", "Bottom", False),

    transititon("EvergreenCaverns", "Top", "Trail4", "Cave", False),

    transititon("Trail4", "Temple", "AncientTemple1", "Bottom", False),

    transititon("AncientTemple1", "Top", "AncientTemple2", "Bottom", False),

    transititon("AncientTemple2", "Top", "AncientTemple3", "Bottom", False),

    transititon("AncientTemple3", "Top", "Trail4", "TempleBackDoor", True),

    transititon("Trail5", "TunnelsOut", "SandyTunnels", "Bottom", False),

    transititon("SandyTunnels", "Top", "Trail6", "TunnelsOut", False),

    transititon("Trail6", "Right", "DairyFarm", "Left", False),

    transititon("DairyFarm", "Right", "Trail7", "Left", False),

    transititon("Trail7", "Right", "TumbleweedTown", "Left", False),

    transititon("TumbleweedTown", "Bottom", "Trail8", "Top", False),
    transititon("TumbleweedTown", "Top", "Trail9", "Bottom", False),
    transititon("TumbleweedTown", "ClinicOut", "TumbleweedTown_Clinic", "Bottom", False),
    transititon("TumbleweedTown", "KingsSaloonOut", "TumbleweedTown_KingsSaloon1", "Bottom", False),
    transititon("TumbleweedTown", "MerchantOut", "TumbleweedTown_Merchant", "Bottom", False),
    transititon("TumbleweedTown", "SmallHouseOut", "TumbleweedTown_SmallHouse1", "Bottom", False),

    transititon("Trail8", "Tunnel", "DustyGrotto", "Top", False),

    transititon("DustyGrotto", "Bottom", "OldMastersHut", "Tunnel", False),

    transititon("OldMastersHut", "HutOut", "OldMastersHut_Upstairs", "Bottom", False),
    transititon("OldMastersHut", "Cave", "CaveOfTorment", "Bottom", False),

    transititon("OldMastersHut_Upstairs", "Basement", "OldMastersHut_Basement", "Bottom", False),

    transititon("Trail9", "Temple", "DesertTemple1", "Bottom", False),

    transititon("DesertTemple1", "Top", "DesertTemple2", "Bottom", False),

    transititon("DesertTemple2", "Top", "Trail9", "TempleBackdoor", True),

    transititon("CrashSite", "Bottom", "Trail10", "Top", False),

    transititon("Trail10", "Left", "CoconutVillage", "Right", False),

    transititon("CoconutVillage", "Left", "Trail11", "Right", False),
    transititon("CoconutVillage", "ClinicOut", "CoconutVillage_Clinic", "Bottom", False),
    transititon("CoconutVillage", "MerchantOut", "CoconutVillage_Merchant", "Bottom", False),
    transititon("CoconutVillage", "TempleOut", "CoconutVillage_Temple", "Bottom", False),
    transititon("CoconutVillage", "House1Out", "CoconutVillage_House1", "Bottom", False),
    transititon("CoconutVillage", "House2Out", "CoconutVillage_House2", "Bottom", False),

    transititon("Trail11", "Bottom", "Trail12", "Top", False),
    transititon("Trail11", "pier", "Trail13", "pier", False),

    transititon("Trail12", "Bottom", "FishingHut", "Top", False),

    transititon("Trail13", "Left", "Trail14", "Right", False),

    transititon("Trail14", "CaveIn", "IslandCave", "Bottom", False),

    transititon("IslandCave", "Top", "IslandCave2", "Bottom", False),

    transititon("IslandCave2", "Top", "Trail14", "CaveOut", True),

    transititon("ColdHarbor", "Top", "Frostville1", "Bottom", False),

    transititon("Frostville1", "Top", "Trail17", "Bottom", False),
    transititon("Frostville1", "Left", "Trail15", "Right", False),
    transititon("Frostville1", "ClinicOut", "Frostville1_Clinic", "Bottom", False),
    transititon("Frostville1", "MerchantOut", "Frostville1_Merchant", "Bottom", False),
    transititon("Frostville1", "Church", "Frostville1_Church", "Bottom", False),
    transititon("Frostville1", "House1", "Frostville1_House1", "Bottom", False),

    transititon("Trail15", "Left", "Trail16", "Right", False),
    transititon("Trail15", "Left2", "Trail16_Top", "Right2", False),


    transititon("Trail16", "Left", "AbandonedMine", "Right", False),
    transititon("Trail16_Top", "Cave", "Trail16_Cave", "Bottom", False),

    transititon("AbandonedMine", "House1", "AbandonedMine_House1", "Bottom", False),

    transititon("Trail17", "Right", "Trail18", "Left", False),

    transititon("Trail18", "TempleIn", "ArcticTemple1", "Bottom", False),

    transititon("ArcticTemple1", "Top", "ArcticTemple2", "Bottom", False),

    transititon("ArcticTemple2", "Top", "Trail18", "TempleOut", True),

    transititon("Trail19", "Top", "Trail20", "Bottom", False),

    transititon("Trail20", "Left", "Trail21", "Right", False),
    transititon("Trail20_Right", "Right", "SpiritPassage", "Left", False),

    transititon("SpiritPassage", "Right", "Trail22", "Left", False),

    transititon("Trail22", "Top", "InnerGrove", "Bottom", False),
    transititon("Trail22", "Cave", "Trail22_Cave", "Bottom", False),

]

specical_transition_areas = [
    #transititon("Menu",None,"OakwoodVillage",None,True),
    transititon("EvergreenOutpost",  "EVENT_bridge", "EvergreenOutpost_East", "EVENT_bridge", False),  # REQUIRES "Complete Main Quest: Bridge crossing" TO ACCESS

    transititon("Trail16_Top", "EVENT_bridge", "Trail16", "EVENT_bridge", False),  # MUST BE UNLOCKED BY PUSHING A BOLDER FROM Trail16_Top

    transititon("Trail20", "EVENT_bridge", "Trail20_Right", "EVENT_bridge", False),  # REQUIRES COMPLETION OF "Complete Main Quest: Breezie Runs Free"

    transititon("TumbleweedTown",None,"CrashSite",None,True),
    transititon("CoconutVillage_Temple",None,"ColdHarbor",None,True),
    transititon("Trail18",None,"Trail19",None,True),
]

mapid_to_text = {
    "OakwoodVillage":"Oakwood Village",
    "OakwoodVillage_Clinic":"Oakwood Village Clinic",
    "OakwoodVillage_FarmHouse":"Oakwood Village FarmHouse",
    "OakwoodVillage_Hq":"Oakwood Village Hq",
    "Trail1":"Trail 1",
    "EvergreenOutpost":"Evergreen Outpost",
    "EvergreenOutpost_East":"Evergreen Outpost East",
    "Trail2":"Trail 2",
    "Greensvale":"Greensvale",
    "Greensvale_Clinic":"Greensvale Clinic",
    "Greensvale_Merchant":"Greensvale Merchant",
    "Greensvale_SexShop":"Greensvale Sex Shop",
    "Greensvale_SmallHouse":"Greensvale Small House",
    "MillysFarm":"Millys Farm",
    "Trail3":"Trail 3",
    "EvergreenCaverns":"Evergreen Caverns",
    "Trail4":"Trail 4",
    "AncientTemple1":"Ancient Temple 1",
    "AncientTemple2":"Ancient Temple 2",
    "AncientTemple3":"Ancient Temple 3",
    "Trail5":"Trail 5",
    "SandyTunnels":"Sandy Tunnels",
    "Trail6":"Trail 6",
    "DairyFarm":"Dairy Farm",
    "Trail7":"Trail 7",
    "TumbleweedTown":"Tumbleweed Town",
    "TumbleweedTown_Clinic":"Tumbleweed Town Clinic",
    "TumbleweedTown_KingsSaloon1":"Tumbleweed Town Kings Saloon",
    "TumbleweedTown_Merchant":"Tumbleweed Town Merchant",
    "TumbleweedTown_SmallHouse1":"Tumbleweed Town Small House",
    "Trail8":"Trail 8",
    "DustyGrotto":"Dusty Grotto",
    "OldMastersHut":"Old Masters Hut",
    "OldMastersHut_Upstairs":"Old Masters Hut Upstairs",
    "OldMastersHut_Basement":"Old Masters Hut Basement",
    "CaveOfTorment":"Cave Of Torment",
    "Trail9":"Trail 9",
    "DesertTemple1":"Desert Temple 1",
    "DesertTemple2":"Desert Temple 2",
    "CrashSite":"Crash Site",
    "Trail10":"Trail 10",
    "CoconutVillage":"Coconut Village",
    "CoconutVillage_Clinic":"Coconut Village Clinic",
    "CoconutVillage_Merchant":"Coconut Village Merchant",
    "CoconutVillage_Temple":"Coconut Village Temple",
    "CoconutVillage_House1":"Coconut Village House 1",
    "CoconutVillage_House2":"Coconut Village House 2",
    "Trail11":"Trail 11",
    "Trail12":"Trail 12",
    "FishingHut":"Fishing Hut",
    "Trail13":"Trail 13",
    "Trail14":"Trail 14",
    "IslandCave":"Island Cave 1",
    "IslandCave2":"Island Cave 2",
    "ColdHarbor":"Cold Harbor",
    "Frostville1":"Frostville",
    "Frostville1_Clinic":"Frostville Clinic",
    "Frostville1_Merchant":"Frostville Merchant",
    "Frostville1_Church":"Frostville Church",
    "Frostville1_House1":"Frostville House",
    "Trail15":"Trail 15",
    "Trail16":"Trail 16",
    "Trail16_Top":"Trail 16 Top",
    "Trail16_Cave":"Trail 16 Cave",
    "AbandonedMine":"Abandoned Mine",
    "AbandonedMine_House1":"Abandoned Mine House",
    "Trail17":"Trail 17",
    "Trail18":"Trail 18",
    "ArcticTemple1":"Arctic Temple 1",
    "ArcticTemple2":"Arctic Temple 2",
    "Trail19":"Trail 19",
    "Trail20":"Trail 20",
    "Trail20_Right":"Trail 20 Right",
    "Trail21":"Trail 21",
    "SpiritPassage":"Spirit Passage",
    "Trail22":"Trail 22",
    "Trail22_Cave":"Trail 22 Cave",
    "InnerGrove":"Inner Grove",
}

grass_loc = [
"Trail1",
"EvergreenOutpost",
"Trail2",
"MillysFarm",
"Trail3",
"EvergreenCaverns",
"Trail4",
"Trail5",
"SandyTunnels",
"Trail6",
"DairyFarm",
"Trail7",
"Trail8",
"DustyGrotto",
"OldMastersHut",
"CaveOfTorment",
"Trail9",
"CrashSite",
"Trail10",
"Trail11",
"Trail12",
"FishingHut",
"Trail13",
"Trail14",
"IslandCave",
"ColdHarbor",
"Trail15",
"Trail16",
"Trail16_Cave",
"AbandonedMine",
"Trail17",
"Trail18",
"Trail19",
"Trail20",
"Trail21",
"SpiritPassage",
"Trail22",
"Trail22_Cave",
]

water_loc = [
"Trail10",
"Trail11",
"Trail12",
"Trail13",
"Trail14",
"ColdHarbor",
"Trail16",
"AbandonedMine",
"Trail17",
"Trail18",
"Trail21",
]

default_grass_loc = {
    "Trail1": ["Petunia", "Beebee","Slimee"],
    "EvergreenOutpost": ["Petunia", "Beebee", "Slimee", "Bunni", "Wolfy", ],
    "Trail2": ["Petunia", "Beebee", "Slimee", "Wolfy", "Bunni", "Ursie", "Gloria"],
    "MillysFarm": ["Serpentia"],
    "Trail3": ["Beebee", "Gloria", "Ursie", "Wolfy", "Belle", "Oakie", "trissy", ],
    "EvergreenCaverns": ["Slimee", "Serpentia", "Spinnie", "Octopussy"],
    "Trail4": ["Ursie", "Gloria", "Belle", "Oakie", "Trissy", "Serpentia", "Chubbie", "Pusseen"],
    "Trail5": ["Oakie", "Trissy", "Chubbie", "Pusseen", "Boobae", "Tinky"],
    "SandyTunnels": ["Spinnie", "Octopussy", "Chubbie", "Rawry", "Serpentax"],
    "Trail6": ["Serpentax", "Boobae", "Rawry", "Birdy", "Cactee", "Twerky"],
    "DairyFarm": ["Serpentax", "Birdy", "Cactee", "Twerky", "Bovina", "lacteena", "Flora"],
    "Trail7": ["Bovina", "Lacteena", "Flora", "Birdy", "Hornie", "Buzzeena", "Bellend"],
    "Trail8": ["Cactee", "Birdy", "Buzzeena", "Bellend", "Flora", "Gloreen", "Triboobe", "Kittypus"],
    "DustyGrotto": ["Serpentax", "Twerky", "Hornie", "Dripsy", "Octocunt", "Bearboo"],
    "OldMastersHut": ["Dripsy", "Cactee", "Triboobe", "Lacteena", "Harlie", "Growleen"],
    "CaveOfTorment": ["Hornie", "Octocunt", "Domina", "Dracoomer"],
    "Trail9": ["Lacteena", "Growleen", "Harlie", "Dracoomer", "Triboobe", "Thiccsie", "Megaboob"],
    "CrashSite": ["Thiccsie", "Megaboob", "Kittypus", "Sexybun", "Mamaoak"],
    "Trail10": ["Megaboob", "Growleen", "Sexybun", "Mamaoak", "Pinchie"],
    "Trail11": ["Octocunt", "Pinchie", "Sexybun", "Mamaoak", "Udderella"],
    "Trail12": ["Octocunt", "Pinchie", "Dracoomer", "Udderella", "Faerie"],
    "FishingHut": ["Pinchie", "Thiccsie", "Faerie", "Twerqueen"],
    "Trail13": ["Twerqueen", "Faerie", "Sexybun", "Amazona"],
    "Trail14": ["Faerie", "Amazona", "Mamaoak", "Harpie"],
    "IslandCave":["Amazona", "Harpie", "Twerqueen", "Arachna", "Succubae"],
    "ColdHarbor": ["Harpie", "Pinchie", "Gangfang", "Octomommy", "Snowbae"],
    "Trail15": ["Archna", "Gangfang", "Octomommy", "Snowbae", "Polaria", "Deardeer"],
    "Trail16": ["Gangfang", "Polaria", "Octomommy", "Snowbae", "Deardeer", "Slithereen"],
    "Trail16_Cave": ["Valkyrie_Normal"],
    "AbandonedMine": ["Gangfang", "Polaria", "Slithereen", "Deardeer", "Slushie"],
    "Trail17": ["Slithereen", "Deardeer", "Slushie", "Queenbee", "Boobarella"],
    "Trail18": ["Slushie", "Slithereen", "Queenbee", "Boobarella", "Panthera"],
    "Trail19": ["Queenbee","Deardeer","Panthera","Unihorn","Fungie"],
    "Trail20": ["Queenbee","Unihorn","Fungie","Juggsie","Serphina"],
    "Trail21": ["Queenbee","Fungie","Juggsie","Serphina"],
    "SpiritPassage": ["Slithereen","Octomommy","Fungie","Dominatrix"],
    "Trail22": ["Unihorn","Juggsie","Seraphina","Dominatrix"],
    "Trail22_Cave": ["Centiboob_Normal"],
}

default_water_loc = {
    "Trail10":["Marinel", "Pinchie"],
    "Trail11":["Sharky", "Marinel"],
    "Trail12":["Marinel", "Pinchie", "Chocostar", "Octocunt"],
    "Trail13":["Jellygal", "Sharky", "Chocostar"],
    "Trail14":["Marinel", "Jellygal", "Sharky"],
    "ColdHarbor":["Chocostar", "Pinchie"],
    "Trail16":["Jawsy"],
    "AbandonedMine":["Jawsy", "Jellybish"],
    "Trail17":["Jellybish", "Jawsy"],
    "Trail18":["Jellybish", "Jawsy"],
    "Trail21":["Jellybish","Lizzie"],
}
