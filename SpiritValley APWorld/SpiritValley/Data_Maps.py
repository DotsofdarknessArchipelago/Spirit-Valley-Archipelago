

class Area:
    name:str
    connected_areas: {str:[str]} #name : requirements
    encounters_grass: [str] #name
    grass_level_range: [int] #[min, max]
    encounters_fishing: [str] #name
    fishing_level_range: [str] #[min, max]
    loot: {str:str} #loot location: loot obtained
    quests: [str]
    Warpable: bool
    Trainers: {str:[{str:int}]} # trainer name [max 6 mons{mon name: lv}]

    def __init__(self, name, connected_areas, encounters_grass, grass_level_range, encounters_fishing, fishing_level_range, loot, quests, Warpable, Trainers):
        self.name = name
        self.connected_areas = connected_areas
        self.encounters_grass = encounters_grass
        self.grass_level_range =grass_level_range
        self.encounters_fishing = encounters_fishing
        self.fishing_level_range =fishing_level_range
        self.loot = loot
        self.quests = quests
        self.Warpable = Warpable
        self.Trainers = Trainers


playthrough_area_list = [
    Area("Oakwood Village",
         {"Trail 01":None},
         None,
         None,
         None,
         None,
         {
             "Oakwood Village: Chest In Uncles House": ["Chastity belt"]#b9f52b5c-fd8d-43b8-9f5c-85a5b3686a6a
         },
         [
             "Complete Side Quest: Sparring Match",
             "Complete Main Quest: Doctor’s Appointment",
             "Complete Main Quest: Captain Maria",
             "Complete Main Quest: First Mission: Success",
             "Complete Main Quest: Consulting Dolly",
         ],
         True,
         {
             "Oakwood Village: Defeat Robbie": [{"Wolfy":3}]#NPC SCRIPTED   61822611-267a-4366-b99c-fadc5a23ad01
         }),
    Area("Trail 01",
         {"Oakwood Village":None, "Evergreen Outpost":None},
         ["Petunia","Beebee","Slimee"],
         [3,3],
         None,
         None,
         {
             "Trail 01: Chest Near Piper":["2x spirit crystal","25 coins"],#  #33bdf3c7-7b56-4578-b038-3d9f10a7c978
             "Trail 01: Chest North of Piper":["2x Spirit repelent"],#33a2ce7f-9568-4435-ac78-a4e3660948fe
             "Trail 01: Potion From Jane":["Potion"]}, #3019ab50-bd67-4887-9865-cdc2fa604f55
         ["Piper (catch/give petunia)"],
         False,
         None),
    Area("Evergreen Outpost",
         {"Trail 01":None, "Trail 02":None, "Trail 05":["complete main quest(bridge crossing)"]},
         ["Petunia","Beebee","Slimee", "Bunni", "Wolfy",],
         [3,4],
         None,
         None,
         {
             "Evergreen Outpost: Chest Near Medic":["Butt plug of wisdom"], #7c0b0138-7aa6-49ea-a1eb-015e33731f51
             "Evergreen Outpost: Chest Above Grass Patch":["vial of health", "2x antidote"],#49a27369-563a-444d-9112-45ff04198979
             "Evergreen Outpost: Chest Behind Pushable Bolder":["200x coin", "2x spirit crystal +1"], #576ccf5e-ee72-49c4-930c-a3e4acf6c1b7
         },
         [
             "Complete Side Quest: Larry’s Treasure",
             "Complete Main Quest: First Orders",
             "Complete Main Quest: Super Secret Orders",
             "Complete Main Quest: Bridge crossing",
         ],
         False,
         {
             "Evergreen Outpost: Defeat Elise":[{"Beebee":3}]#19c75671-2314-414f-b500-ef28c011d8d2
         }),
    Area("Trail 02",
         {"Evergreen Outpost":None, "Greensvale":["Complete Main quest(first mission success!)"]},
         ["Petunia","Beebee","Slimee", "Wolfy", "Bunni", "Ursie", "Gloria"],#lv3-4
         [3,4],
         None,
         None,
         {
             "Trail 02: Chest Near Billy":["cupcake", "20x coins"], #e129287a-733f-4761-b12d-d4f6265d3e38
             "Trail 02: Chest in Hidden Path Next to Macy":["Ass lovers Extreme issue 12"], #d36a4079-4dc5-4cbf-92ec-fbb4e5e5a674
             "Trail 02: Chest East of Macy":["15x coins", "2x vial of stanima"], #a6673de2-6794-43ee-b1c3-cc7e7468c7f9
             "Trail 02: Chest Near Skyler":["2x potent sent"], #5c0b8d8e-e4fe-4505-871c-d2c3964b75b5
             #"defeat crimson agent":["Super secret orders"], #quest reward technically
         },
         [
             "Complete Main Quest: Crimson Agent",
         ],
         False,
         {
             "Trail 02: Defeat Billy":[{"Gloria":3}, {"Petunia":2}],#0a40a301-741a-4843-8008-799f4ba37287
             "Trail 02: Defeat Macy":[{"Ursie":4}],#bf261ea7-7b93-4c0b-89a8-da7c93550808
             "Trail 02: Defeat Skyler":[{"Slimee":3}, {"Beebee":3}],#a79a0909-43a5-47ff-b990-a1632a224e83
             "Trail 02: Defeat Crimson Agent":[{"Wolfy":4}, {"Petunia":3}]}),#53af4c29-1d1b-4655-a1db-9ed89c32a981
    Area("Greensvale",
         {"Trail 02":None,"Milly's Farm": None,"Trail 03": None},
         None,
         None,
         None,
         None,
         {
             "Greensvale: Chest South of Waystone": ["2x vial of rejuvination"], #e5139fe4-aae0-4c8c-9591-94cd9405a8cb
             "Greensvale: Chest in Red House":["spirit crystal", "25x coins"], #64386704-ba0e-461c-ad5d-36327d902e9b
             "Greensvale: Chest Next To XXX Shop":["lollypop", "15x coins"], #23d8f4fb-7284-483c-a145-ed500c426339
             "Greensvale: Chest Behind Pushable Bolder In the North":["butt plug of life +1"], #c0fa6732-bee2-47c2-9853-1ffa3e6a98e0
         },
         [
             "Complete Main Quest: Onward to Greensvale",
             "Complete Main Quest: Harmonious Disturbance",
             "Complete Main Quest: Becky can fix it",
             "Complete Main Quest: Hunt for the chunk",
         ],
         True,
         None),
    Area("Milly's Farm",
         {"Greensvale": None},
         ["Serpentia"],
         [5,6],
         None,
         None,
         {
             "Milly's Farm: Chest Behind Pushable Bolder": ["seed of life"]#e21093f1-32a4-4e08-ba6c-7090002ccdd9
         },
         ["Complete Side Quest: Slithering Menace"],
         False,
         None),
    Area("Trail 03",
         {"Greensvale": None, "Evergreen Caverns":None},
         ["Beebee", "Gloria", "Ursie", "Wolfy",  "Belle", "Oakie", "trissy",],
         [5,7],
         None,
         None,
         {
             "Trail 03: Chest North of Miriam": ["2x vial of health", "cleansing tonic"], #44683738-a42b-4c9c-b200-e4742152e790
             "Trail 03: Chest South of Miriam": ["25x coin", "candy cane"], #4d2efd45-b043-46de-9a27-e75da0caec9f
             "Trail 03: Chest Chest Before Evergreen Caverns Entrance": ["rejuvination potion"], #0ab8b8d9-28b6-4bfe-9a4c-188297627ed3
         },
         ["Complete Side Quest: Pleasuring Pusseen"],
         False,
         {
             "Trail 03: Defeat Cheese":[{"Oakie":6}, {"Beebee":5}],#b40b0778-da74-4660-b0a1-fba6d1d16bdd
             "Trail 03: Defeat Miriam":[{"Petunia":7}, {"Wolfy":6}],#c029e36a-14ec-4d07-a45b-b7b57f406575
             "Trail 03: Defeat Jenna":[{"Ursie":6}],#6778b3a1-97d4-457d-adc1-c324dbad017e
          }),
    Area("Evergreen Caverns",
         {"Trail 03": None, "Trail 04":None},
         ["Slimee", "Serpentia", "Spinnie", "Octopussy"],
         [6,9],
         None,
         None,
         {
             "Evergreen Caverns: Chest West of Stu": ["2x vial of stamina"], #0b29ff75-0e24-4378-9053-db03ca077e79
             "Evergreen Caverns: Chest South of Nicole": ["15x coin", "vial of health", "antidote"], #9396ff11-ac75-4b7c-8999-286ff2c84f75
             "Evergreen Caverns: Chest 1 Behind Rawry": ["raw crystal chunk"], #f4de6097-3346-4921-849f-b099ee698aa2
             "Evergreen Caverns: Chest 2 Behind Rawry": ["150x coin", "dragon dildo"], #42de807c-00fe-4570-91ee-8ef1a1241777
         },
         None,
         False,
         {
             "Evergreen Caverns: Defeat Stu":[{"Serpentia":7}, {"Gloria":6}],#e6929a89-5dc3-4118-bcf9-ff20df7ed4af
             "Evergreen Caverns: Defeat Nicole":[{"Octopussy":8}, {"Slimee":6}],#364ef3fd-dfe9-41bb-aa8c-9583af54d8f8
             "Evergreen Caverns: Defeat Rawry":[{"Rawry":15}],#72e0b641-b787-46cb-8fe8-eb17f93073fa
         }),
    Area("Trail 04",
         {"Evergreen Caverns": None, "Ancient temple entrense":["ancient temple key"], "Ancient temple room 2":["ONE WAY NOT ACCESSIABLE"]},
         ["Ursie", "Gloria", "Belle", "Oakie", "Trissy", "Serpentia", "Chubbie", "Pusseen"],
         [7,10],
         None,
         None,
         {
             "Trail 04: Chest West of Evergreen Caverns Entrance": ["2x cupcake", "25x coin", "fallen star"],#0471dbe1-259d-4067-a0a3-ef54917278ad
             "Trail 04: Chest West Side of Map": ["small dildo"],#32d13c92-6c2f-4386-8a6c-e3d6849fbcf8
             "Trail 04: Chest Near Waystone": ["2x elusive Sent"],#19a41d7a-cd3b-4e23-b71a-67f28af913e1
         },
         None,
         True,
         None),
    Area("Ancient Temple 1",
         {"Trail 04": None, "Ancient temple room 1":None},
         None,
         None,
         None,
         None,
         {
             "Ancient Temple 1: Chest Near 3rd Crimson Cloak": ["seed of life", "cleansing Tonic"],#84c4ca3f-c75c-404d-a348-fb7969103347
             "Ancient Temple 1: Chest in Path Loop": ["150x coin", "infinity charm"],#d62d3ed0-99f1-4c84-9c89-cdee2fbcda22
             "Ancient Temple 1: Chest Near 6th Crimson Cloak": ["2x rejuvenation potion"],#36739a3e-47ec-4785-a0e7-6c71bc38f964
         },
         None,
         False,
         {
             "Ancient Temple 1: Defeat 1st Crimson Cloak":[{"Spinnie":8}],#5efd2110-61ad-4bea-9551-2bffee802492
             "Ancient Temple 1: Defeat 2nd Crimson Cloak":[{"Trissy":8}, {"chubbie":7}],#27d2018d-9706-4b17-981d-e408d42e1041
             "Ancient Temple 1: Defeat 3rd Crimson Cloak":[{"Serpentia":9}, {"Belle":6}],#cae4d216-6d69-470b-a721-3d83290c0de6
             "Ancient Temple 1: Defeat 4th Crimson Cloak":[{"Wolfy":8}, {"Beebee":7}],#2174dd35-f25f-4d1a-86a3-c1f46f576ff9
             "Ancient Temple 1: Defeat 5th Crimson Cloak":[{"Trissy":9}],#677f47ac-c833-42c8-a19a-4d99d5985fdd
             "Ancient Temple 1: Defeat 6th Crimson Cloak":[{"Ursie":8}, {"Oakie":6}],#7c73c737-4fd5-4266-92ea-caf02f8c9320
         }),
    Area("Ancient Temple 2",
         {"Ancient temple entrense": None, "Ancient temple room 2":None},
         None,
         None,
         None,
         None,
         {
             "Ancient Temple 2: Chest West Side of Room": ["Butt plug of power +1"],#0b46cb8f-5eb2-4a50-8586-07f94fa07c80
             "Ancient Temple 2: Chest East side of Room": ["2x Spirit Crystal"],#c6b0df02-8d68-414d-9a25-8b9dd4c854f6
             "Ancient Temple 2: Chest in Middle Area of Room": ["Healing potion", "25x coin"],#920a56c1-5bda-41ae-8935-c29d33c2c6f1
         },
         None,
         False,
         {
             "Ancient Temple 2: Defeat Crimson Cloak":[{"Octopussy":8}, {"Serpentia":6}, {"Spinnie":7}],#122ab3e7-c278-402b-a741-c83633c93626
         }),
    Area("Ancient Temple 3",
         {"Ancient temple room 1": None, "Trail 04": ["ONE WAY"]},
         None,
         None,
         None,
         None,
         {
             #"defeat Valkrie": ["craked power crystal"]#technically quest reward
         },
         [
             "Complete Main Quest: Temple Investigation",
         ],
         False,
         {
             "Ancient Temple 3: Defeat Valkrie":[{"Valkrie":11}],#NPC SCRIPTED
         }),
    Area("Trail 05",
         {"Evergreen Outpost":["complete main quest(bridge crossing)"],"Sandy tunnels": None},
         ["Oakie", "Trissy", "Chubbie", "Pusseen", "Boobae", "Tinky"],
         [10,12],
         None,
         None,
         {
             "Trail 05: Chest Near Evergreen Outpost Entrance": ["2x elusive sent"],#4c8940eb-e49c-40dc-8a26-d4f60f4bc9c2
             "Trail 05: Chest East of Mila": ["2x strawberry cake", "35x coins"],#816a4058-20a0-4996-9648-145ad9597850
             "Trail 05: Chest West of Roy": ["ball gag"],#653e6c73-99ab-4b7b-93b3-6b94301378db
             "Trail 05: Chest East of Lulu": ["2x spirit crystal +1", "2x rejuvenation potion", "evolution charm"],#854bb842-23cc-4f46-ae38-7be9f17a2a4b
         },
         None,
         False,
         {
             "Trail 05: Defeat Mila":[{"Pusseen":9}, {"Slimee":7}],#83b06037-1fe2-47d9-8887-479a7b0104d6
             "Trail 05: Defeat Roy":[{"Rawry":10}],#e6cda171-22b9-43fb-9ca0-f2411e2e4226
             "Trail 05: Defeat Lulu":[{"Boobae":10}, {"Beebee":7}],#72a096dd-0fe8-4146-9bf0-c7d5e5234b98
         }),
    Area("Sandy Tunnels",
         {"Trail 05": None, "Trail 06":0},
         ["Spinnie","Octopussy","Chubbie","Rawry","Serpentax"],
         [10,13],
         None,
         None,
         {
             "Sandy Tunnels: Chest South of Chad": ["2x healing potion", "50x coin", "fallen star"],#ba7ef7c4-2cbe-48ef-b777-c9c279d3a8f3
             "Sandy Tunnels: Chest North of Chad": ["chastity belt of love"],#323a990d-8933-4c80-839b-1c40a3eeaaf9
             "Sandy Tunnels: Chest West of Destiny": ["2x stamina potion"],#0cceeb16-b7e3-4440-916f-c08d6662a535
             "Sandy Tunnels: Healing Potion From Jessica": ["healing potion"],#c135099c-4730-4f32-a9c8-1c79ac82945b
         },
         None,
         False,
         {
             "Sandy Tunnels: Defeat Chad":[{"Octopussy":10}],#666003ef-c69e-4279-809a-e757e8cb60b2
             "Sandy Tunnels: Defeat Destiny":[{"Oakie":9}, {"Serpentina":7}],#265abaf4-18eb-45fd-8aba-6bc4f8844f81
         }),
    Area("Trail 06",
         {"Sandy tunnels": None, "Dairy Farm":None},
         ["Serpentax","Boobae","Rawry","Birdy","Cactee","Twerky"],
         [11,13],
         None,
         None,
         {
             "Trail 06: Chest West of Sandy Tunnels Entrance": ["2x healing potion", "candy cane"],#002d680f-44a9-4e90-8827-c57cc8f69e65
             "Trail 06: Chest East of Kelsie": ["2x cupcake", "30x coin"],#be999696-f2d3-4379-adf3-7d16693a5e5f
             "Trail 06: Chest South of Hayden": ["red collar"],#2c975ba2-b3a3-4cea-adb9-b66ddf3c42fc
         },
         None,
         False,
         {
             "Trail 06: Defeat Kelsie":[{"Serpentax":10}, {"Wolfy":8}],#acd2e86c-2cdd-48e9-aaed-ba84a84d70a3
             "Trail 06: Defeat Hayden":[{"Beebee":9}],#8cad5228-7db2-49cd-9fcc-e625029e6817
             "Trail 06: Defeat Juliet":[{"Spinnie":10}, {"Tinky":7}],#4cc138d0-8b3d-4ea6-8dd4-e593ae0d9aef
         }),
    Area("Dairy Farm",
         {"Trail 06": None, "Trail 07":None},
         ["Serpentax","Birdy","Cactee","Twerky","Bovina","lacteena","Flora"],
         [11,14],
         None,
         None,
         {
             "Dairy Farm: Chest North of Waystone": ["100x coin"],#303be291-de84-4fae-b055-822959b7cc0a
             "Dairy Farm: Chest South of Waystone": ["rejuvination potion", "infinity charm"],#d27f5dea-d45b-4cb8-9df8-67538b55548d
             "Dairy Farm: Chest Next to House": ["candy cane"],#f54b3d20-a63e-4f8b-ac30-4c6d8875dd61
             "Dairy Farm: Chest North-East of House": ["2x cocolate cake", "cleansing tonic"],#d6f46d56-9a4b-4225-a4ca-a01067840674
         },
         ["Complete Side Quest: Cattle Thieves"],
         True,
         None),
    Area("Trail 07",
         {"Dairy Farm": None,"Tumbleweed Town": None},
         ["Bovina","Lacteena","Flora","Birdy","Hornie","Buzzeena","Bellend"],
         [12,14],
         None,
         None,
         {
             "Trail 07: Chest Near Dairy Farm Entrance": ["2x spirit repelent"],#38122e15-ff3c-4777-be9f-53b2e7c8c73c
             "Trail 07: Chest North of Bella": ["rubber fist"],#add11e84-b206-48ba-b2dd-2ff56262eabc
             "Trail 07: Chest South of Bella": ["2x spirit crystal+1", "25x coin"],#d834c481-c66d-4f5a-a3f3-376b6239c4a0
             "Trail 07: Chest South of Dakota": ["75x coin"],#c22c51bc-6eaf-40ed-9f4b-62a6e1268a88
         },
         None,
         False,
         {
             "Trail 07: Defeat Sally McTits":[{"Dripsy":14}, {"Gloreen":13}, {"Kittypus":13}, {"Boobae":11}],#6db1fd7b-c78b-4de1-967c-ce67e656236e
             "Trail 07: Defeat Bella":[{"Serpentax":13}, {"cactee":10}, {"Bovina":11}],#56c3e787-d36a-4e11-aead-ea47f500e261
             "Trail 07: Defeat Dakota":[{"Birdy":12}, {"Flora":11}],#ab480291-fa67-4ec2-a724-c048b4537914
             "Trail 07: Defeat Cassidy":[{"Twerky":11}, {"Buzzeena":13}, {"Tinky":10}, {"Octopussy":11}],#0f05b20d-99cf-4cee-852e-7e5edac5a456
         }),
    Area("Tumbleweed Town",
         {"Trail 07": None,"Trail 08": None,"Trail 09": None, "Crash Site":["complete main quest(how the dominoes fall) ONE WAY"]},
         None,
         None,
         None,
         None,
         {
             "Tumbleweed Town: Chest South of Town": ["2x rejuvination potion", "fallen star"],#e4d4ae3a-d411-488f-819d-a9624148a5ed
             "Tumbleweed Town: Chest North-West of Town": ["swift plug"],#b0973844-878a-47e9-8ab2-bea68625ace0
             "Tumbleweed Town: Chest in House Next to Shop": ["2x strawberry cake", "30x coin"],#71627b20-173d-4c34-8242-82806333e7b5
         },
         [
             "Complete Main Quest: Dusty Vale awaits",
             "Complete Main Quest: An audience with the King",
             "Complete Main Quest: The Grand Cuckold Challenge",
             "Complete Main Quest: A challenge awaits",
             "Complete Main Quest: A new challenger",
             "Complete Main Quest: Stiff competition",
             "Complete Main Quest: Final Fight",
             "Complete Main Quest: Return of the champion",
             "Complete Main Quest: Breeding season",
             "Complete Main Quest: Mission success",
             "Complete Main Quest: How the Dominoes fall",
             "Complete Main Quest: Big balloon adventure",
          ],
         True,
         {
             "Tumbleweed Town: Defeat Willy Wanker":[{"Bearboo":17}, {"Kittypus":17}, {"Bunni":16}],#MODIFY SASSY NPC ??? 2aefb292-7d0d-4674-a0bd-eb5e487b1272
             "Tumbleweed Town: Defeat Dick Cummings":[{"Lacteena":18}, {"Megaboob":20}, {"Triboobe":17}, {"Bovina":17}],#MODIFY SASSY NPC ??? 2aefb292-7d0d-4674-a0bd-eb5e487b1272
             "Tumbleweed Town: Defeat Dick Louie":[{"Buzzeena":19}, {"Flora":18}, {"Gloreen":19}, {"Thiccsie":18}, {"Spinnie":17}],#MODIFY SASSY NPC ??? 2aefb292-7d0d-4674-a0bd-eb5e487b1272
         }),
    Area("Trail 08",
         {"Tumbleweed Town": None,"Dusty Grotto": None},
         ["Cactee","Birdy","Buzzeena","Bellend","Flora","Gloreen","Triboobe","Kittypus"],
         [13,15],
         None,
         None,
         {
             "Trail 08: Chest West of Tumbleweed Town Entrance": ["healing potion", "25x coin"],#24c5ce52-ec0f-492f-9447-401df4f6c100
             "Trail 08: Chest South of Marisa": ["butt plug of life +1"],#baea8603-5e88-4935-95a9-ef10c47e8bad
             "Trail 08: Chest Near Dusty Grotto Entrance": ["potent scent", "elusive scent"],#54012631-5481-4e97-85b3-835e6f2128ab
         },
         None,
         False,
         {
             "Trail 08: Defeat Marisa":[{"Lacteena":13}, {"Hornie":13}],#e07a91ad-6fd5-4d54-8b05-36c3f9d090c1
             "Trail 08: Defeat Jenni":[{"Gloreen":14}, {"Birdy":12}],#bd2e9de2-30db-42f2-aa44-678cf71649ea
             "Trail 08: Defeat Alanna":[{"Buzzeena":14}, {"Serpentax":13}, {"Flora":13}],#163d96da-8b46-4b1e-baf6-e46708072abe
         }),
    Area("Dusty Grotto",
         {"Trail 08": None,"Old Masters Hut": None},
         ["Serpentax","Twerky","Hornie","Dripsy","Octocunt","Bearboo"],
         [13,16],
         None,
         None,
         {
             "Dusty Grotto: Chest Near Crystal": ["seed of life", "100x coin", "infinity charm"],#25d61715-32da-4887-a04d-381b74e7fd70
             "Dusty Grotto: Chest West of Skye": ["2x spirit crystal+1", "candy cane"],#b859600e-fad1-486c-9879-5d0782077bc3
         },
         None,
         False,
         {
             "Dusty Grotto: Defeat Arnie":[{"Chubbie":14}, {"Bunni":12}, {"Hornie":15}],#af5b25fb-7066-4fca-b1fa-c94fb7e5f330
             "Dusty Grotto: Defeat Crystal":[{"Buzzeena":15}, {"Cactee":12}],#cf1d4fc7-2757-41ea-8198-322dda687398
             "Dusty Grotto: Defeat Skye":[{"Lacteena":13}, {"Serpentax":14}, {"Rawry":13}],#176d7645-f963-47ca-9af5-344d1c2e8dc0
         }),
    Area("Old Masters Hut",
         {"Dusty Grotto": None,"Cave of Torment": None},
         ["Dripsy","Cactee","Triboobe","Lacteena","Harlie","Growleen"],
         [15,17],
         None,
         None,
         {
             "Old Masters Hut: Chest North of House": ["stamina potion", "50x coin"],#33323326-8c5c-448e-acac-2f50cba62286
             "Old Masters Hut: Chest Next to House": ["2x rejuvination potion", "3x spirit crystal+1"],#7410e48c-cf0e-42da-9760-e0d756ec5856
             "Old Masters Hut: Chest in House": ["2x spirit crystal+1"],#bbef9238-1d46-4d89-8f42-3f086d169e35
             "Old Masters Hut: Chest in House Basement": ["video cassette"],#0feafe23-7fc6-4175-b8b1-90d2323095ce
         },
         [
             "Complete Main Quest: License to battle",
             "Complete Main Quest: Box pusher",
             "Complete Main Quest: Total domination",
         ],
         False,
         None),
    Area("Cave of Torment",
         {"Old Masters Hut": None},
         ["Hornie","Octocunt","Domina","Dracoomer"],
         [15,17],
         None,
         None,
         {
             "Cave of Torment: Chest East Side of Cave": ["150x coin", "infinity charm"],#52ca3362-6a85-4eba-9a4e-64d29dca413e
             "Cave of Torment: Chest North Side of Cave": ["golden seed of life"],#f6f9100f-d007-4407-8273-bb8ac9fc98a7
             "Cave of Torment: Chest West Side of Cave": ["spiked collar"],#e44bc915-f705-4b68-8a9d-a3527264dad8
         },
         None,
         False,
         None),
    Area("Trail 09",
         {"Tumbleweed Town": None,"stone temple entrence": ["Stone Key"], "stone temple room 1": ["ONE WAY NO ACCESS"]},
         ["Lacteena","Growleen","Harlie","Dracoomer","Triboobe","Thiccsie","Megaboob"],
         [16,18],
         None,
         None,
         {
             "Trail 09: Chest near Clementine": ["2x chocolate cake"],#369c6ee5-6b6a-4433-ae92-e5f4b9e911e1
             "Trail 09: Chest North of Mike": ["2x spirit crystal +1"],#1457c1a2-8177-4571-b438-f53cb9c6cd34
             "Trail 09: Chest Near Stone Temple Back Entrance Ledge": ["2x candy cane"],#8af95e31-a76f-4004-9ed4-d208fb94efb3
         },
         None,
         False,
         {
             "Trail 09: Defeat Mike": [{"Birdy":16}, {"Buzzeena":15}],#f792e755-6771-4f50-8dca-8d3cf8b6017a
             "Trail 09: Defeat Clementine": [{"Bovina":14}, {"Gloreen":16}],#00c525ca-41d2-40ba-a68e-c40f8990652c
             "Trail 09: Defeat Bonnie": [{"Octocunt":17}, {"Buxzzeena":16}, {"Growleen":16}],#b4d3fec1-9f7f-4b2e-a3de-cf25bc3fe399
         }),
    Area("Stone Temple 1",
         {"Trail 09": None,"stone temple room 1": None},
         None,
         None,
         None,
         None,
         {
             "Stone Temple 1: Chest Near Trail 09 Entrence": ["2x cupcake", "seed of life", "50x coin"],#515e573f-cf67-473f-a241-7177098013c1
             "Stone Temple 1: Chest Near 6th Crimson Cloak": ["turtle chell collar", "fallen star"],#1f27c663-1dce-47e0-821c-8fd1aae55a46
             "Stone Temple 1: Chest Near Stone Temple 2 Entrance": ["2x healing potion", "50x coin"],#57db7ff2-69b0-4c98-a81b-79b30eb2dd88
         },
         None,
         False,
         {
             "Stone Temple 1: Defeat 1st Crimson Cloak": [{"Domina":19}, {"Growleen":18}],#48a6856e-4dbd-4ca9-b6d5-066b5a55d783
             "Stone Temple 1: Defeat 2nd Crimson Cloak": [{"Buzzeena":17}],#7b40e4f2-990b-4a2c-8ccc-aa283653436a
             "Stone Temple 1: Defeat 3rd Crimson Cloak": [{"Kittypus":16}, {"Flora":17}, {"Dripsy":15}],#b3ab8b9c-5260-47a6-befc-d99487a2a53f
             "Stone Temple 1: Defeat 4th Crimson Cloak": [{"Harlie":18}],#bf8484cc-5889-45ce-8b18-c35b96e0d0e7
             "Stone Temple 1: Defeat 5th Crimson Cloak": [{"Lacteena":20}, {"Octocunt":18}],#02067b08-1777-4713-af0d-123bb86102fe
             "Stone Temple 1: Defeat 6th Crimson Cloak": [{"Megaboob":18}],#a0268c7e-1417-41cb-aa2a-109240ff2eac
         }),
    Area("Stone Temple 2",
         {"stone temple entrence": None,"Trail 09": ["ONE WAY"]},
         None,
         None,
         None,
         None,
         None,
         [
             "Complete Main Quest: Quest for the crystal"
          ],
         False,
         {
             "Stone Temple 2: Defeat Domino": [{"Octocunt":18}, {"Serpentax":19}, {"Harlie":18}, {"Hornie":17}, {"Bearboo":17}],
         }),
    Area("Crash Site",
         {"Tumbleweed Town": ["ONE WAY NO ACCESS"],"Trail 10": None},
         ["Thiccsie","Megaboob","Kittypus","Sexybun","Mamaoak"],
         None,
         None,
         None,
         {
             "Crash Site: Chest East of Athena": ["150x coins", "2x healing potion"],#20af0b9d-a48e-4dff-995e-53758e7d61f3
             "Crash Site: Chest West of Janet": ["2x spirit crystal +1"],#c6f2ad98-a787-4805-9c9b-fca34bd7dee3
             "Crash Site: Chest South of Janet": ["candy cane"],#2300e642-581b-43e8-bc83-c78a246fe948
         },
         None,
         True,
         {
             "Crash Site: Defeat Athena": [{"Pinchie":18}, {"Dracoomer":17}, {"Cactee":15}],#ae458556-c336-43a7-a7c3-be76c84f0a48
             "Crash Site: Defeat Janet": [{"Mamaoak":21}, {"Bearboo":16}],#ef863488-65f8-4827-9e80-0e1c6a42b681
         }),
    Area("Trail 10",
         {"Crash Site": None,"Coconut Village": None},
         ["Megaboob","Growleen","Sexybun","Mamaoak","Pinchie"],
         [19,21],
         ["Marinel", "Pinchie"],
         [19,20],
         {
             "Trail 10: Chest West of Crash Site Entrance": ["100x coins", "infinity charm"],#cbbdd4da-69d4-41c2-9165-ea07e647a369
             "Trail 10: Chest Near Eve": ["2x stamina potion"],#545492fc-2eea-4a81-b1db-12825748f4a0
             "Trail 10: Chest South of Bailee": ["ball gag +1", "fallen star"],#5c21066a-081c-4c75-8a0f-1694ccddbe1f
         },
         None,
         False,
         {
             "Trail 10: Defeat Bailee": [{"Amazona":20}, {"Octocunt":17}],#b15889a3-63eb-490f-8f7b-e14555ac9d97
             "Trail 10: Defeat Eve": [{"Domina":17}, {"Sexybun":21}],#6ee5a399-6614-482d-8e07-00abcf34d10e
         }),
    Area("Coconut Village",
         {"Trail 10": None,"Trail 11": None, "Cold Harbor":["ONE WAY complete Main quest(Glimmering Prize)"]},
         None,
         None,
         None,
         None,
         {
             "Coconut Village: Chest North-East in Village": ["Butt Plug of Power +1"],#9b0fd14d-0aec-4790-900f-553f98af0eb1
             "Coconut Village: Chest East of Village": ["50x coin", "red latex mask"],#56fa7c21-327e-4f5f-8fe2-1b1d35da3dc9
             "Coconut Village: Chest in House in the South-East": ["Seed of Life", "50x coins"],#8a4cdd76-b0a6-4256-a9d4-5797167f7ae5
             "Coconut Village: Chest in Temple": ["2x greater healing potion"],#e68357b4-2017-4962-9935-febbb8afa19e
             "Coconut Village: Chest In Temple After Locked Door": ["red harmony crystal"],#11a5f5c0-f303-469e-96f0-d0df45d2e631
         },
         [
             "Complete Side Quest: Professional Pleasurer",
             "Complete Main Quest: Welcome to Paradise",
             "Complete Main Quest: Savior of Coconut Village",
             "Complete Main Quest: Slippery When Wet",
             "Complete Main Quest: Glimmering Prize",
             "Complete Main Quest: Arctic Adventure",
         ],
         True,
         None),
    Area("Trail 11",
         {"Coconut Village": None,"Trail 12": None,"Trail 13": ["complete optional quest(deadly waters)"]},
         ["Octocunt","Pinchie","Sexybun","Mamaoak","Udderella"],
         [21,22],
         ["Sharky", "Marinel"],
         [21,22],
         {
             "Trail 11: Chest Near Alice": ["Strawberry cake"],#7e5e1b32-a395-449e-8524-85100357f829
             "Trail 11: Chest Near Pier": ["2x spirit crystal +1"],#fc2ae356-2928-4f20-b00a-882f8498ebfc
             "Trail 11: Chest East of Emilia": ["2x spirit repellent"],#1eb894db-663f-4ef8-8bec-9eff702f539b
             "Trail 11: Chest South of Sydney": ["2x elusive scent"],#f54d4a60-9550-4505-962d-917242c1853e
         },
         [
             "Complete Side Quest: Fishmaster’s Challenge",
             "Complete Side Quest: Deadly Waters"
         ],
         False,
         {
             "Trail 11: Defeat Alice": [{"Marinel":21}, {"Pinchie":20}, {"Sharky":22}],#NPC
             "Trail 11: Defeat Emilia": [{"Hornie":17}, {"Marinel":19}],#cc69f7aa-a078-448c-ab25-00c8f774926f
             "Trail 11: Defeat Sydney": [{"Octocunt":16}, {"Mamaoak":20}, {"Serpentax":17}],#2bf2f7ed-e375-4747-875c-3bd1b2048e46
         }),
    Area("Trail 12",
         {"Trail 11": None,"Fishing Hut": None},
         ["Octocunt","Pinchie","Dracoomer","Udderella","Faerie"],
         [21,23],
         ["Marinel","Pinchie","Chocostar", "Octocunt"],
         [21,23],
         {
             "Trail 12: Chest North of Sophie": ["2x cleansing tonic", "50x coins"],#e2598159-fb05-4e8f-88a4-cbb55d12546f
             "Trail 12: Chest North of Ciara": ["evolution charm", "50x coins"],#df5ab9f9-17b1-4629-a683-8e1c6ff122e4
         },
         ["Complete Side Quest: Starry Eyed Surprise"],
         False,
         {
             "Trail 12: Defeat Sophie": [{"Harlie":17}, {"Faerie":21}],#ddc0cee9-5a37-431b-baf8-8653a97f13a0
             "Trail 12: Defeat Ciara": [{"Grewleen":17}, {"Dracoomer":17}, {"Sharky":20}],#961a23f5-023b-4d31-ab65-b8d227a52ded
         }),
    Area("Fishing Hut",
         {"Trail 12": None,"": None},
         ["Pinchie","Thiccsie","Faerie","Twerqueen"],
         [21,23],
         None,
         None,
         {
             "Fishing Hut: Chest North-West on the Beach": ["dragon dildo +1"],#ed0b2740-17bd-49bb-b431-8ee30ffee485
             "Fishing Hut: Chest Next to House": ["100x coins", "2x stamina potion"],#570c6d8b-0f44-4611-8c16-676ea4f2dcf7
             "Fishing Hut: Chest East on the Beach": ["2x rejuvenation potion"],#38a94edd-1946-4076-8ddf-c9e9bf6b3358
             "Fishing Hut: Chest Eastern Side of Map": ["greater healing potion"],#8fa902d2-fc53-4502-b2a4-edd4c2fcdbba
         },
         [
             "Complete Side Quest: Fishy Duel",
             "Complete Side Quest: The Art of Fishing"
         ],
         False,
         {
             "Fishing Hut: Defeat Bonnie Baiter": [{"chocostar":21}, {"Mamaoak":20}, {"Marinel":20}],#05ba33a6-2693-49ba-b570-543c25feeeb2 #NPC
         }),
    Area("Trail 13",
         {"Trail 10": ["complete optional quest(deadly waters)"],"Trail 14": None},
         ["Twerqueen","Faerie","Sexybun","Amazona"],
         [22,24],
         ["Jellygal","Sharky","Chocostar"],
         [22,24],
         {
             "Trail 13: Chest South-West of 1st Cultist": ["butt plug of life +1", "infinity charm"],#2432ca26-daf4-4f91-b0f5-65094ef2f236
             "Trail 13: Chest North of 1st Cultist": ["150x coins", "antidote", "fallen star"],#e349a432-ea25-48fa-b78a-4f7e24a1a21e
         },
         [
             "Complete Main Quest: Coconut Conundrum",
          ],
         False,
         {
             "Trail 13: Defeat 1st Cultist": [{"Gloreen":23}, {"Mamaoak":21}, {"Sharky":20}],#a4a13dee-d151-407c-8ed1-8db2d45efdf2
             "Trail 13: Defeat 2nd Cultist": [{"Triboobe":21}, {"Dripsy":23}],#b4a8bd50-ab01-4e3c-8aba-0469ada1c52f
         }),
    Area("Trail 14",
         {"Trail 13": None,"Island Cave": None, "Island Cave lv2":["ONE WAY NO ACCESS"]},
         ["Faerie","Amazona","Mamaoak","Harpie"],
         [23,25],
         ["Marinel","Jellygal","Sharky"],
         [23,25],
         {
             "Trail 14: Chest North-West of 1st Cultist": ["Spiked Collar +1"],#5fb24dfe-bb8f-4e3d-b5d2-f18331df4040
             "Trail 14: Chest East of 1st Cultist": ["chocolate cake", "2x candy cane"],#4e89c1b8-d75b-4dd1-b333-c091f0683bd8
             "Trail 14: Chest East of Waystone": ["2x rejuvenation potion", "2x stamina potion"],#7b172b42-b00c-4e6b-a6d2-3176cac758d3
         },
         None,
         True,
         {
             "Trail 14: Defeat 1st Cultist": [{"Kittypus":18}, {"Thiccsie":20}, {"Jellygal":22}],#38dd508c-5633-47c3-b142-846c3915716d
             "Trail 14: Defeat 2nd Cultist": [{"Buzzeena":18}, {"Sexybun":22}, {"Twerqueen":24}, {"Chocostar":20}],#9b009cf3-5fad-4076-88d2-3e43e004efec
         }),
    Area("Island Cave 1",
         {"Trail 13": None,"Island Cave lv2": None},
         ["Amazona", "Harpie", "Twerqueen", "Arachna", "Succubae"],
         [23,25],
         None,
         None,
         {
             "Island Cave 1: Chest North-West After 1st Cultist": ["Golden Chastity belt"],#be99f6ef-4289-45b9-b8ca-c6432f64c982
             "Island Cave 1: Chest East After 2st Cultist": ["2x greater healing potion"],#1ffad415-a599-4752-a847-c093e51cbcbe
             "Island Cave 1: Chest West After 2nd Cultist": ["evolution charm", "200x coin"],#78734a81-9888-4e7f-97a8-1b68f590ef43
             "Island Cave 1: Chest Near 3rd Cultist": ["seed of life", "the ace of spades"],#9ad68fef-4f77-4490-9ccd-5d779083bddb
         },
         None,
         False,
         {
             "Island Cave 1: Defeat 1st Cultist": [{"Bovina":18}, {"Mamaoak":22}],#5fbd94fe-f5dc-42bb-9f57-dbaec4d8d3c3
             "Island Cave 1: Defeat 2nd Cultist": [{"Harpie":23}, {"Twerqueen":23}, {"Amazona":20}],#1ad60dfe-2454-431e-8f8a-8f512003aa1d
             "Island Cave 1: Defeat 3rd Cultist": [{"Lacteena":22}, {"Jellygal":24}],#46a60f99-3cb9-42cf-860f-9e471707e263
             "Island Cave 1: Defeat 4th Cultist": [{"Succubae":25}, {"Udderella":22}],#5f53e18a-e6b1-473a-8252-f0d68286ca57
         }),
    Area("Island Cave 2",
         {"Island Cave": None,"Trail 13": ["ONE WAY"]},
         None,
         None,
         None,
         None,
         None,
         [
             "Complete Main Quest: Lusty Cultists",
          ],
         False,
         {
             "Island Cave 2: Defeat Centiboob": [{"Centiboob":26}],#NPC SCRIPTED
         }),
    Area("Cold Harbour",
         {"Coconut Village": ["ONE WAY NO ACCESS"],"Frostville": None},
         ["Harpie","Pinchie","Gangfang","Octomommy","Snowbae"],
         [25,27],
         ["Chocostar", "Pinchie"],
         [25,27],
         {
             "Cold Harbour: Chest North-East of Waystone": ["2x spirit crystal +2", "greater rejuvenation potion"],#4f0e46a1-ad29-4472-a6a9-24120c07535c
             "Cold Harbour: Chest East of Iris": ["200x coins", "2x XP Boosters"],#4b5bceb4-7cff-4419-8116-cf5dd4e6dcb8
         },
         ["Complete Main Quest: The Frigid Maiden"],
         True,
         {
             "Cold Harbour: Defeat Vanessa": [{"Harpie":25}, {"Gangfang":26}],#323cbfec-0db2-43c2-a538-e3b4cf02d260
             "Cold Harbour: Defeat Iris": [{"Amazona":22}, {"Polaria":26}, {"Snowbae":23}],#c34254a6-6f54-4643-8319-75636a798542
         }),
    Area("Frostville",
         {"Cold Harbor": None,"Trail 15": None, "Trail 17": ["complete main quest(here comes the boom)"]},
         None,
         None,
         None,
         None,
         {
             "Frostville: Chest North of Waystone": ["2x greater healing potions"],#dd42f2b7-841c-4726-a597-a8e197e384f4
             "Frostville: Chest South of Waystone": ["3x spirit crystal +2", "fallen star"],#d4f07026-13b3-4b49-ae53-57764bed39a6
             "Frostville: Chest West of Town": ["ball gag +2"],#4c13b886-9a90-4896-b235-d013e69c60e6
         },
         [
             "Complete Main Quest: Arctic Isles",
             "Complete Main Quest: Paisley Bones",
             "Complete Main Quest: Stealing From a Dead Man",
             "Complete Main Quest: The Lewd Exorcist",
             "Complete Main Quest: The Proposal",
             "Complete Main Quest: Here Comes the Boom",
          ],
         True,
         {
             "Frostville: Defeat Mother Evilyn": [{"Hornie":29}, {"Arachna":32}, {"Octomommy":31}],#aa1ce20e-a988-48c9-8a4b-e246fb163402
         }),
    Area("Trail 15",
         {"Frostville": None,"Trail 16": None},
         ["Archna","Gangfang","Octomommy","Snowbae","Polaria","Deardeer"],
         None,
         None,
         None,
         {
             "Trail 15: Chest South of Frostville Entrence": ["chocolate cake", "150x coins"],#18ec8ed3-304e-47a1-8311-b53e9e76ceee
             "Trail 15: Chest West of Mia": ["2x greater rejuvenation potion", "2x cleansing tonic"],#c8875e05-570c-4b7c-a3a6-3939a80e373d
             "Trail 15: Chest South-West of Olga": ["Spiked Collar +2"],#334ebd4f-e47e-494a-9010-f0e431e93cd3
          },
         ["Complete Side Quest: Arctic Menace"],
         False,
         {
             "Trail 15: Defeat Mia": [{"Deardeer":25}, {"Chocostar":25}],#705f45eb-9221-4c47-b339-e8d2b2f6d862
             "Trail 15: Defeat Olga": [{"Pinchie":24}, {"Polaria":27}, {"Harpie":26}],#9f573d72-be6e-48dc-9ffd-50044176a86c
         }),
    Area("Trail 16",
         {"Trail 15": None,"Abandoned Mine": None,"Trail 16 Cave": None},
         ["Gangfang","Polaria","Octomommy","Snowbae","Deardeer","Slithereen"],
         [27,28],
         ["Jawsy"],
         [27,28],
         {
             "Trail 16: Chest Near Northern Trail 15 Entrence": ["fallen star", "Golden Seed of life"],#60a5df17-adb0-46ba-ae67-e4df1e45718f
             "Trail 16: Chest North of Karin": ["2x spirit crystal +2"],#f55efa41-a0da-4307-aa3b-584c1238ddaf
             "Trail 16: Chest North-West of Karin": ["2x greater stamina potion"],#97595abc-e511-4733-827e-e6180c716210
             "Trail 16: Chest East of Dahlia": ["2x spirit repellent", "xp boosters"],#e89b33c2-ef03-4abd-b216-81df8d7e0f65
         },
         None,
         False,
         {
             "Trail 16: Defeat Karin": [{"Mamaoak":21}, {"Gangfang":26}],#911604b8-a719-4eb6-af17-42bd8dc35a9b
             "Trail 16: Defeat Dahlia": [{"Snowbae":25}, {"Chocostar":23}, {"Polaria":28}],#1e4eb581-53ee-4f87-b021-ff0ebc931798
         }),
    Area("Trail 16 Cave",
         {"Trail 16": None},
         ["Valkyrie_Normal"],#REQUIRES FISHY SCENT
         [29,32],
         None,
         None,
         None,
         None,
         False,
         None
         ),
    Area("Abandoned Mine",
         {"Trail 16": None,"": None},
         ["Gangfang","Polaria","Slithereen","Deardeer","Slushie"],
         [28,30],
         ["Jawsy", "Jellybish"],
         [28,30],
         {
             "Abandoned Mine: Chest North of Trail 16 Entrence": ["Swift Plug +1", "2x XP boosters"],#46cf0856-3d1c-440b-a065-b357d399964b
             "Abandoned Mine: Chest South-West of House": ["3x greater healing potion", "50x coins"],#575941ce-96f2-477f-b0bc-facec059184c
         },
         [
             "Complete Main Quest: Demand for Dynamite",
             "Complete Main Quest: Suit In Hand",
             "Complete Main Quest: Fishing For Treasure",
         ],
         True,
         None),
    Area("Trail 17",
         {"Frostville": ["complete main quest(here comes the boom)"],"Trail 18": None},
         ["Slithereen","Deardeer","Slushie","Queenbee","Boobarella"],
         [29,32],
         ["Jellybish","Jawsy"],
         [29,32],
         {
             "Trail 17: Chest North of Clara": ["2x Spirit crystal +2"],#db51e404-218c-4288-8860-b5ecf2b25059
             "Trail 17: Chest South-East of Liv": ["greater rejuvination potion", "greater healing potion"],#2d01eaea-aecd-4b90-9029-6498f03c3558
             "Trail 17: Chest North-East of Karly": ["2x candy cane", "2x strawberry cake"],#cef39514-d07c-4531-8fa5-52ebd56df4c9
         },
         [
             "Complete Side Quest: Legend of the Valkyrie part 1.",
             "Complete Side Quest: Legend of the Valkyrie part 2."
         ],
         False,
         {
             "Trail 17: Defeat Clara": [{"Slithereen":27}, {"Arachna":28}],#5d964c9f-f399-4a24-98f6-def8af276d4c
             "Trail 17: Defeat Liv": [{"Jellybish":29}, {"Jawsy":27}, {"Harpie":23}],#38419b1d-9908-4ef4-a962-1406aa2a4352
             "Trail 17: Defeat Karly": [{"Slushie":25}, {"Gangfang":30}],#d09da17a-d5b6-415f-986f-9dc216400385
         }),
    Area("Trail 18",
         {"Trail 17": None,"artic temple entrence": None, "artic temple room1":["ONE WAY NO ACCESS"]},
         ["Slushie","Slithereen","Queenbee","Boobarella","Panthera"],
         [30,33],
         ["Jellybish","Jawsy"],
         [30,33],
         {
             "Trail 18: Chest South of Anabelle": ["2x infinity charm", "2x cleansing tonic"],#1f7ba32d-3992-42c2-ab0c-f5b7d382af55
             "Trail 18: Chest in North Part of Map": ["icey dildo", "55x gold"],#72243934-12c9-440a-a226-e9de780f25fd
             "Trail 18: Chest North of Ingrid": ["fallen star", "greater rejuvination potion"],#02d71004-c006-4b9a-a467-48396c815865
         },
         [
             "Complete Main Quest: Crimson Chase"
         ],
         True,
         {
             "Trail 18: Defeat Stacy": [{"Polaria":30}, {"Harpie":28}],#0a2fe22c-e43e-457f-85af-29ed94e9f57d
             "Trail 18: Defeat Anabelle": [{"Jellybish":31}, {"Slithereen":29}],#4492eac4-575d-46c8-8d4f-4418e4ab1065
             "Trail 18: Defeat Ingrid": [{"Slithereen":28}, {"Queenbee":31}, {"Slushie":25}],#5676a70d-5a1c-4868-906f-a269dffc5f2f
         }),
    Area("Artic Temple 1",
         {"Trail 18": None,"artic temple room 1": None},
         None,
         None,
         None,
         None,
         {
             "Artic Temple: Chest in South-East": ["Vibrating willy+1", "evolution charm"],#f5c25d35-2be7-445d-8432-f31b58d29f81
             "Artic Temple: Chest in West": ["300x coin", "2x antidote"],#c1b51d5f-663e-4ca5-94a2-1611880789d7
             "Artic Temple: Chest in North-West": ["golden seed of life", "2x greater healing potion"],#c790f2f6-78ae-4e26-b46b-82d0823a6118
         },
         None,
         False,
         {
             "Artic Temple 1: Defeat 1st Crimson Cloak": [{"Octomommy":32}, {"Harpie":26}, {"Mamaoak":27}],#23aa2df5-197e-45cb-af67-dfc97e83dd3b
             "Artic Temple 1: Defeat 2nd Crimson Cloak": [{"Arachna":28}, {"Boobarella":31}],#1452eb18-e64d-4fb6-93b3-84574ee29396
             "Artic Temple 1: Defeat 3rd Crimson Cloak": [{"Jellybish":30}, {"Polaria":29}],#4bd72a1d-cdf9-49b4-ba2b-245dabf60035
             "Artic Temple 1: Defeat 4th Crimson Cloak": [{"Slithereen":31}, {"Deardeer":32}],#60f3aad3-3f2d-4ce1-ab4a-f6833957b8ab
             "Artic Temple 1: Defeat 5th Crimson Cloak": [{"Gangfang":27}, {"Queenbee":31}],#5272d410-ae2d-42b5-93a8-b06b4ba20fe2
         }),
    Area("Artic Temple 2",
         {"artic temple entrence": None,"Trail 18": ["ONE WAY"]},
         None,
         None,
         None,
         None,
         None,
         [
             "Complete Main Quest: Arctic Harmony"
         ],
         False,
         {
             "Artic Temple 2: Defeat Crimson Countess": [{"Queenbee":32}, {"Chocostar":28}, {"Octomommy":30}, {"Archna":31}, {"Jawsy":33}],#NPC SEQUENCE
         }),
    #TODO
    Area("Trail 19",
         {"Trail 18": ["ONE WAY NO ACCESS"],"Trail 20": None},
         ["Queenbee","Deardeer","Panthera","Unihorn","Fungie"],
         [33,35],
         None,
         None,
         {
             "Trail 19: Chest Near Start": ["100 Coin","2x spirit crystal +2"],  #c1df6726-ecd8-4863-b1ae-d2d995d6cdf4
             "Trail 19: Chest South of 1st Crimson Cloak": ["2x greater healing potion"],  #e8bbd1c5-3777-4a13-bcf2-b58e2d6d5d2c
             "Trail 19: Chest East of 2nd Crimson Cloak": ["2x Cleansing tonic"],  #5a746032-358e-4ace-aa5e-bd614f610742
         },
         [
             "Complete Main Quest: Through the Portal"
          ],
         True,
         {
             "Trail 19: Defeat 1st Crimson Cloak": [{"Harpie":34},{"Slithereen":32},],#97fab556-a752-489c-8de5-04d3449afeca
             "Trail 19: Defeat 2nd Crimson Cloak": [{"Fungie":33},],#ce0b7e57-6bbd-4034-9f2b-2785f6b6f07d
             "Trail 19: Defeat 3rd Crimson Cloak": [{"Arachna":32},{"Jellybish":33},],#bbb2a608-b9f8-4701-a978-549f98628a70
         }),
    Area("Trail 20",
         {"Trail 19": None,"Trail 21": None,"Spirit Passage": [""]},
         ["Queenbee","Unihorn","Fungie","Juggsie","Serphina"],
         [33,36],
         None,
         None,
         {
             "Trail 20: Chest Near 1st Crimson Cloak": ["Unicorn Dildo"],  #ac4251e7-b377-4124-814a-95601ac2e10f
             "Trail 20: Chest Near 2nd Crimson Cloak": ["150x coin","2x greater rejuvination potion"],  #b8d3a32e-2b9a-45a9-8496-07d98d24ebe3
             "Trail 20: Chest Near Cave Entrance": ["Golden seed of life","2x Spirit Repelent"],  #affeeef4-519b-4b7c-8bea-f6011e35c2fe
         },
         [
             "Complete Main Quest: Sanctuary Shakedown"
             "Complete Main Quest: Breezie Runs Free"
         ],
         False,
         {
             "Trail 20: Defeat 1st Crimson Cloak": [{"Chocostar":34},{"Fungie":32},],#4d8163f6-3e75-4112-9824-7e0247d4118f
             "Trail 20: Defeat 2nd Crimson Cloak": [{"Polaria":35},],#72d37c80-d416-48b0-8e1f-ab6c9f49e40c
             "Trail 20: Defeat 3rd Crimson Cloak": [{"Mamaoak":32},{"Jawsy":34},],#149cf1b9-7344-4037-88b8-42fe6f471e64
         }),
    Area("Trail 21",
         {"Trail 20": None},
         ["Queenbee","Fungie","Juggsie","Serphina"],
         [34,37],
         ["Jellybish","Lizzie"],
         [34,37],
         {
             "Trail 21: Chest Near Pushable Bolder": ["fallen star","2x evolution charm"],  #c9bccc23-9abc-412b-a969-be4b38fe8c07
             "Trail 21: Chest North of Pond": ["2x candy cane"],  #a0ea4f50-253d-41c3-a01e-4b2c0de0c846
             "Trail 21: Chest South area of map": ["Diamond Butt Plug"],  #0c7e4c71-2b16-4171-a256-55820b5f41c5
         },
         [
             "Complete Main Quest: Hostage Situation"
          ],
         False,
         {
             "Trail 21: Defeat 1st Crimson Cloak": [{"Juggsie":36},],#ff372848-9064-45a9-9e2c-dd98e3fd1313
             "Trail 21: Defeat 2nd Crimson Cloak": [{"Unihorn":34},{"Octomommy":30},],#ff372848-9064-45a9-9e2c-dd98e3fd1313
             "Trail 21: Defeat Kinley": [{"Queenbee":32},{"Snowbae":30},{"Pinchie":35},{"Boobarella":34},],#0ea61b92-8dcd-4adf-a070-4bc5870b2698
         }),
    Area("Spirit Passage",
         {"Trail 20": None,"Trail 22": None},
         ["Slithereen","Octomommy","Fungie","Dominatrix"],
         [35,38],
         None,
         None,
         {
             "Trail Spirit Passage: Chest north of first fork in path": ["Spiked Collar +3"],  #35f79fc2-e0ce-4b1a-90a5-fc87436b8c51
             "Trail Spirit Passage: Chest in first loop area": ["150x coin","2x cleansing tonic"],  #1ae0306c-1da3-4248-b1a2-b4ecb14d40c5
             "Trail Spirit Passage: Chest north of first loop area": ["2x antidote","2x infinity charm"],  #dec67487-358b-43b6-a97e-ca892aa95d89
             "Trail Spirit Passage: Chest near 5th Crimson Cloak": ["200x coin"],  #ee7e2616-1b0d-4c92-9014-53c9fa72f424
         },
         None,
         False,
         {
             "Trail Spirit Passage: Defeat 1st Crimson Cloak": [{"Chocostar ":35},{"Harpie":32},],#9eeac2b8-20b3-4d35-a7b9-bb01169dc72d
             "Trail Spirit Passage: Defeat 2nd Crimson Cloak": [{"Slushie":35},],#70e65def-a84b-4df5-873c-77d2f02fc30b
             "Trail Spirit Passage: Defeat 3rd Crimson Cloak": [{"Amazona":37},],#b8863596-1a75-481f-94ca-4178785f0554
             "Trail Spirit Passage: Defeat 4th Crimson Cloak": [{"Seraphina":38},{"Marinel":36},],#97835a52-0d7b-4d9d-9184-8eb813faf909
             "Trail Spirit Passage: Defeat 5th Crimson Cloak": [{"Twerqueen":36},{"Faerie":37},],#a2557c2e-85f8-4511-8d14-da72a962943c

         }),
    Area("Trail 22",
         {"Spirit Passage": None,"Inner Grove": None,"Trail 22 Cave": None},
         ["Unihorn","Juggsie","Seraphina","Dominatrix"],
         [37,40],
         None,
         None,
         {
             "Trail 22: Chest north west of pond": ["Butt plug of life +2"],  #22527dc8-b6b1-4af2-974d-2e56b8fc96b6
             "Trail 22: Chest north path before large grass patch": ["2x golden seed of life"],  #a3f235a1-bc10-4012-8203-37be87ecf06c
             "Trail 22: Chest north of large grass patch": ["250x coin"],  #e88b6c20-4e22-459e-b229-50bd0edc835d
             "Trail 22: Chest west side of lake near waypoint": ["3x spirit crystal +2"],  #f533f7ee-5852-4dc8-87c4-73e434942e3d
         },
         [
             "Complete Main Quest: Desperate Dash",
             "Complete Side Quest: Hunt for the Centiboob part 1.",
             "Complete Side Quest: Hunt for the Centiboob part 2.",
             "Complete Side Quest: Hunt for the Centiboob part 3.",
         ],
         True,
         {
             "Trail 22: Defeat 1st Crimson Cloak": [{"Deardeer":36},{"Dominatrix":35},{"Octocunt":35},],#7f45394d-44a9-466e-b9a5-7a169ae47754
             "Trail 22: Defeat 2nd Crimson Cloak": [{"Seraphina":39},{"Unihorn":33},],#95124723-8456-47a9-91fa-1576ef841d84
             "Trail 22: Defeat 3rd Crimson Cloak": [{"Jawsy":39},],#c618afc1-47b2-4de3-b09d-483d57333482
         }),
    Area("Trail 22 Cave",
         {"Spirit Passage": None, "Inner Grove": None},
         ["Centiboob_Normal"],#REQUIRES SENT MIXTURE ITEM
         [37,40],
         None,
         None,
         {
             "Trail 22 Cave: Chest ": ["500x coin"],  #afe7ac71-80d5-45c2-b6c0-683732d1fdf4
         },
         None,
         True,
         {
         }),
    Area("Inner Grove",
         {"Spirit Passage": None},
         None,#{"":0},
         None,
         None,
         None,
         None,
         [
             "Complete Main Quest: Battle for Spirit Valley",
         ],
         False,
         {
             "Inner Grove: Defeat Spirit Mother": [{"SpiritMother":43},],#

         }),
    #Area("", {"": None,"": None}, {"":0}, None, {"": [""]}, [""], False, {}),
]

grass_location_list = [
"Trail 01",
"Evergreen Outpost",
"Trail 02",
"Milly's Farm",
"Trail 03",
"Evergreen Caverns",
"Trail 04",
"Trail 05",
"Sandy Tunnels",
"Trail 06",
"Dairy Farm",
"Trail 07",
"Trail 08",
"Dusty Grotto",
"Old Masters Hut",
"Cave of Torment",
"Trail 09",
"Crash Site",
"Trail 10",
"Trail 11",
"Trail 12",
"Fishing Hut",
"Trail 13",
"Trail 14",
"Cold Harbour",
"Trail 15",
"Trail 16",
"Trail 16 Cave", #TODO make cave work
"Abandoned Mine",
"Trail 17",
"Trail 18",
"Trail 19",
"Trail 20",
"Trail 21",
"Spirit Passage",
"Trail 22",
"Trail 22 Cave", #TODO make cave work
]

water_location_list = [
"Trail 10",
"Trail 11",
"Trail 12",
"Trail 13",
"Trail 14",
"Cold Harbour",
"Trail 16",
"Abandoned Mine",
"Trail 17",
"Trail 18",
"Trail 21",
]

default_grass_locations = {
"Trail 01": ["Petunia", "Beebee","Slimee"],
"Evergreen Outpost": ["Petunia", "Beebee", "Slimee", "Bunni", "Wolfy", ],
"Trail 02": ["Petunia", "Beebee", "Slimee", "Wolfy", "Bunni", "Ursie", "Gloria"],
"Milly's Farm": ["Serpentia"],
"Trail 03": ["Beebee", "Gloria", "Ursie", "Wolfy", "Belle", "Oakie", "trissy", ],
"Evergreen Caverns": ["Slimee", "Serpentia", "Spinnie", "Octopussy"],
"Trail 04": ["Ursie", "Gloria", "Belle", "Oakie", "Trissy", "Serpentia", "Chubbie", "Pusseen"],
"Trail 05": ["Oakie", "Trissy", "Chubbie", "Pusseen", "Boobae", "Tinky"],
"Sandy Tunnels": ["Spinnie", "Octopussy", "Chubbie", "Rawry", "Serpentax"],
"Trail 06": ["Serpentax", "Boobae", "Rawry", "Birdy", "Cactee", "Twerky"],
"Dairy Farm": ["Serpentax", "Birdy", "Cactee", "Twerky", "Bovina", "lacteena", "Flora"],
"Trail 07": ["Bovina", "Lacteena", "Flora", "Birdy", "Hornie", "Buzzeena", "Bellend"],
"Trail 08": ["Cactee", "Birdy", "Buzzeena", "Bellend", "Flora", "Gloreen", "Triboobe", "Kittypus"],
"Dusty Grotto": ["Serpentax", "Twerky", "Hornie", "Dripsy", "Octocunt", "Bearboo"],
"Old Masters Hut": ["Dripsy", "Cactee", "Triboobe", "Lacteena", "Harlie", "Growleen"],
"Cave of Torment": ["Hornie", "Octocunt", "Domina", "Dracoomer"],
"Trail 09": ["Lacteena", "Growleen", "Harlie", "Dracoomer", "Triboobe", "Thiccsie", "Megaboob"],
"Crash Site": ["Thiccsie", "Megaboob", "Kittypus", "Sexybun", "Mamaoak"],
"Trail 10": ["Megaboob", "Growleen", "Sexybun", "Mamaoak", "Pinchie"],
"Trail 11": ["Octocunt", "Pinchie", "Sexybun", "Mamaoak", "Udderella"],
"Trail 12": ["Octocunt", "Pinchie", "Dracoomer", "Udderella", "Faerie"],
"Fishing Hut": ["Pinchie", "Thiccsie", "Faerie", "Twerqueen"],
"Trail 13": ["Twerqueen", "Faerie", "Sexybun", "Amazona"],
"Trail 14": ["Faerie", "Amazona", "Mamaoak", "Harpie"],
"Cold Harbour": ["Harpie", "Pinchie", "Gangfang", "Octomommy", "Snowbae"],
"Trail 15": ["Archna", "Gangfang", "Octomommy", "Snowbae", "Polaria", "Deardeer"],
"Trail 16": ["Gangfang", "Polaria", "Octomommy", "Snowbae", "Deardeer", "Slithereen"],
#"Trail 16 Cave": ["Valkyrie_Normal"], TODO add cave
"Abandoned Mine": ["Gangfang", "Polaria", "Slithereen", "Deardeer", "Slushie"],
"Trail 17": ["Slithereen", "Deardeer", "Slushie", "Queenbee", "Boobarella"],
"Trail 18": ["Slushie", "Slithereen", "Queenbee", "Boobarella", "Panthera"],
"Trail 19": ["Queenbee","Deardeer","Panthera","Unihorn","Fungie"],
"Trail 20": ["Queenbee","Unihorn","Fungie","Juggsie","Serphina"],
"Trail 21": ["Queenbee","Fungie","Juggsie","Serphina"],
"Spirit Passage": ["Slithereen","Octomommy","Fungie","Dominatrix"],
"Trail 22": ["Unihorn","Juggsie","Seraphina","Dominatrix"],
#"Trail 22 Cave": ["Centiboob_Normal"], TODO add cave
}

default_water_locations = {
"Trail 10":["Marinel", "Pinchie"],
"Trail 11":["Sharky", "Marinel"],
"Trail 12":["Marinel", "Pinchie", "Chocostar", "Octocunt"],
"Trail 13":["Jellygal", "Sharky", "Chocostar"],
"Trail 14":["Marinel", "Jellygal", "Sharky"],
"Cold Harbour":["Chocostar", "Pinchie"],
"Trail 16":["Jawsy"],
"Abandoned Mine":["Jawsy", "Jellybish"],
"Trail 17":["Jellybish", "Jawsy"],
"Trail 18":["Jellybish", "Jawsy"],
"Trail 21":["Jellybish","Lizzie"],
}


