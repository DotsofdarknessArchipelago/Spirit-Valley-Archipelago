class SpiritData:
    moves: {str: int}  # move name: lv obtained
    evolution: {str: int}  # evolution name: lv evolved
    type: str
    base_stats = {"HP": 0, "STA": 0, "ATT": 0, "DEF": 0, "SPE": 0}

    def __init__(self, moves, evo, t, base_stats):
        self.moves = moves
        self.evolution = evo
        self.type = t
        self.base_stats = base_stats

    def __str__(self):
        return f"""moves:{self.moves}, evolution:{'null' if self.evolution is None else self.evolution}, type:'{self.type}', stats:{self.base_stats}"""


types = ["Furry", "Lust", "Plant", "Demon", "Scalie", "Slime", "Oppai", "Avian", "Aquatic"]

default_type_effective = {
    # attack:{defending:(1=effective, 0=neutral, -1=resit)}
    # TODO aquatic
    "Furry": {"Furry": 0, "Lust": 0, "Plant": 0, "Demon": 0, "Scalie": 0, "Slime": -1, "Oppai": 0, "Avian": 1, "Aquatic": 1},
    "Lust": {"Furry": 0, "Lust": 0, "Plant": 0, "Demon": -1, "Scalie": 0, "Slime": 1, "Oppai": 1, "Avian": -1, "Aquatic": 0},
    "Plant": {"Furry": 0, "Lust": 0, "Plant": 0, "Demon": 0, "Scalie": -1, "Slime": 1, "Oppai": 0, "Avian": 0, "Aquatic": -1},
    "Demon": {"Furry": -1, "Lust": 0, "Plant": 1, "Demon": 0, "Scalie": 0, "Slime": 0, "Oppai": 0, "Avian": 0, "Aquatic": 0},
    "Scalie": {"Furry": 1, "Lust": 0, "Plant": 0, "Demon": 0, "Scalie": 0, "Slime": 0, "Oppai": -1, "Avian": 0, "Aquatic": 0},
    "Slime": {"Furry": 0, "Lust": -1, "Plant": 0, "Demon": 1, "Scalie": 0, "Slime": 0, "Oppai": 0, "Avian": 0, "Aquatic": 0},
    "Oppai": {"Furry": 0, "Lust": 1, "Plant": -1, "Demon": 0, "Scalie": 0, "Slime": 0, "Oppai": 0, "Avian": 0, "Aquatic": 0},
    "Avian": {"Furry": 0, "Lust": 0, "Plant": 1, "Demon": -1, "Scalie": 1, "Slime": -1, "Oppai": 0, "Avian": 0, "Aquatic": 0},
    "Aquatic": {"Furry": 0, "Lust": 0, "Plant": 0, "Demon": 1, "Scalie": 0, "Slime": -1, "Oppai": 0, "Avian": 0, "Aquatic": 0},
}

spirit_list = ["Amazona", "Arachna", "Bearboo", "Beebee", "Belle", "Bellend", "Birdy", "Boobae", "Boobarella", "Bovina", "Bunni", "Buzzeena", "Cactee", "Centiboob_Boss", "Centiboob", "Chocostar", "Chubbie", "Deardeer", "Domina", "Dominatrix", "Dracoomer", "Dripsy", "EV-3", "Faerie", "Flora", "Fungie", "Gangfang", "Gloreen", "Gloria", "Growleen", "Harlie", "Harpie", "Hornie", "Jawsy", "Jellybish", "Jellygal", "Juggsie", "Kittypus", "Lacteena", "Lizzie", "Mamaoak", "Marinel", "Megaboob", "Oakie", "Octocunt", "Octomommy", "Octopussy", "Panthera", "Petunia", "Pinchie", "Polaria", "Pusseen", "Queenbee", "Rawry", "Seraphina", "Serpentax", "Serpentina", "Sexybun", "Sharky", "Slimee", "Slithereen", "Slushie", "Snowbae", "Spinnie", "Succubae", "Thiccsie", "Tinky", "Triboobe", "Trissy", "Twerky", "Twerqueen", "Udderella", "Unihorn", "Ursie", "Valkyrie_Boss", "Valkyrie", "Wolfy", "SpiritMother", ]
boss_list = ["Centiboob_Boss", "Valkyrie_Boss", "SpiritMother"]
obtainable_spirit_list = ["Amazona", "Arachna", "Bearboo", "Beebee", "Belle", "Bellend", "Birdy", "Boobae", "Boobarella", "Bovina", "Bunni", "Buzzeena", "Cactee", "Centiboob", "Chocostar", "Chubbie", "Deardeer", "Domina", "Dominatrix", "Dracoomer", "Dripsy", "EV-3", "Faerie", "Flora", "Fungie", "Gangfang", "Gloreen", "Gloria", "Growleen", "Harlie", "Harpie", "Hornie", "Jawsy", "Jellybish", "Jellygal", "Juggsie", "Kittypus", "Lacteena", "Lizzie", "Mamaoak", "Marinel", "Megaboob", "Oakie", "Octocunt", "Octomommy", "Octopussy", "Panthera", "Petunia", "Pinchie", "Polaria", "Pusseen", "Queenbee", "Rawry", "Seraphina", "Serpentax", "Serpentina", "Sexybun", "Sharky", "Slimee", "Slithereen", "Slushie", "Snowbae", "Spinnie", "Succubae", "Thiccsie", "Tinky", "Triboobe", "Trissy", "Twerky", "Twerqueen", "Udderella", "Unihorn", "Ursie", "Valkyrie", "Wolfy", ]

spirit_data = {
    "Amazona": SpiritData({"BitchSlap": 1, "MostMuscular": 3, "WarCry": 10, "PowerPunch": 16, "NippleClamp": 23, "Domination": 28, "ToeStrike": 33, "DonkeyPunch": 38, }, None, "Lust", {"HP": 120, "STA": 100, "ATT": 135, "DEF": 110, "SPE": 95}),
    "Arachna": SpiritData({"Bite": 1, "BindingWeb": 3, "Meditate": 7, "Curse": 10, "Fisting": 13, "Hypnosis": 15, "PoisonBite": 20, "LitanyOfCurses": 25, "NippleClamp": 30, }, None, "Demon", {"HP": 115, "STA": 100, "ATT": 140, "DEF": 105, "SPE": 115}),
    "Bearboo": SpiritData({"BitchSlap": 1, "SexyPose": 3, "Lacerate": 7, "Growl": 10, "BearHug": 14, "BoobPounding": 17, "SharpenClaws": 22, "ExtremeFisting": 26, "CleansingSlap": 30, "PowerPunch": 36, }, {"Polaria": 26}, "Furry", {"HP": 135, "STA": 100, "ATT": 120, "DEF": 125, "SPE": 105}),
    "Beebee": SpiritData({"Sting": 1, "Buzz": 3, "HappyThoughts": 6, "Fisting": 9, "BlowKiss": 14, "BeeSwarm": 18, "LethalSting": 28, "PoisonBlitz": 34, "EyePoke": 38, "Domination": 42, }, {"Buzzeena": 10}, "Avian", {"HP": 100, "STA": 100, "ATT": 125, "DEF": 100, "SPE": 110}),
    "Belle": SpiritData({"LeafBlast": 1, "Seduce": 3, "Photosynthesis": 6, "TeamChant": 10, "PoisonSquirt": 13, "FlowerPower": 17, "HappyThoughts": 20, "SeedOfLife": 24, "NaturesMight": 29, }, {"Bellend": 11}, "Plant", {"HP": 110, "STA": 100, "ATT": 115, "DEF": 100, "SPE": 130}),
    "Bellend": SpiritData({"LeafBlast": 1, "Seduce": 3, "Photosynthesis": 6, "TeamChant": 10, "PoisonSquirt": 13, "FlowerPower": 17, "HappyThoughts": 20, "SeedOfLife": 24, "NaturesMight": 29, }, None, "Plant", {"HP": 115, "STA": 100, "ATT": 120, "DEF": 102, "SPE": 135}),
    "Birdy": SpiritData({"Meditate": 1, "Swoop": 3, "BitchSlap": 6, "Hypnosis": 10, "Stretch": 14, "Rimjob": 18, "Yoga": 22, "ExtremeFisting": 27, "GoldenRain": 32, }, {"Harpie": 22}, "Avian", {"HP": 100, "STA": 100, "ATT": 105, "DEF": 100, "SPE": 115}),
    "Boobae": SpiritData({"Slam": 1, "BoobJiggle": 3, "BreastMassage": 5, "BoobPounding": 7, "FreshMilk": 13, "MilkStorm": 18, "Flirt": 22, "BoobSlam": 26, "MassSeduction": 31, "CleansingSlap": 37, }, {"Megaboob": 14}, "Oppai", {"HP": 145, "STA": 100, "ATT": 120, "DEF": 135, "SPE": 100}),
    "Boobarella": SpiritData({"Slam": 1, "BoobJiggle": 3, "BreastMassage": 5, "BoobPounding": 7, "FreshMilk": 13, "MilkStorm": 18, "Flirt": 22, "BoobSlam": 26, "MassSeduction": 31, "CleansingSlap": 37, }, None, "Oppai", {"HP": 155, "STA": 100, "ATT": 125, "DEF": 145, "SPE": 105}),
    "Bovina": SpiritData({"FreshMilk": 1, "Bite": 3, "BoobSlam": 6, "BlowKiss": 10, "BreastMassage": 13, "HappyThoughts": 15, "Smother": 20, "MilkStorm": 24, "CurePoison": 29, }, {"Udderella": 21}, "Oppai", {"HP": 120, "STA": 100, "ATT": 100, "DEF": 120, "SPE": 100}),
    "Bunni": SpiritData({"Scratch": 1, "SwiftPaws": 3, "Pounce": 6, "Flirt": 9, "Bite": 14, "Stretch": 18, "PawStrike": 21, "ScentSpray": 25, "NaturesMight": 31, }, {"Sexybun": 19}, "Furry", {"HP": 90, "STA": 100, "ATT": 110, "DEF": 95, "SPE": 145}),
    "Buzzeena": SpiritData({"Sting": 1, "Buzz": 3, "HappyThoughts": 6, "Fisting": 9, "BlowKiss": 14, "BeeSwarm": 18, "LethalSting": 28, "PoisonBlitz": 34, "EyePoke": 38, "Domination": 42, }, {"Queenbee": 29}, "Avian", {"HP": 105, "STA": 100, "ATT": 130, "DEF": 105, "SPE": 115}),
    "Cactee": SpiritData({"Slam": 1, "ThornStrike": 3, "FlowerPower": 7, "Fisting": 11, "CoatOfSpikes": 14, "Strangle": 17, "Photosynthesis": 21, "SeedOfLife": 25, "EyePoke": 29, }, None, "Plant", {"HP": 110, "STA": 100, "ATT": 105, "DEF": 110, "SPE": 100}),
    "Centiboob_Boss": SpiritData({"KillerInstinct": 1, "PoisonBite": 1, "BoobSlam": 1, "Lactate": 1, "Hypnosis": 1, "LitanyOfCurses": 1, }, None, "Oppai", {"HP": 420, "STA": 100, "ATT": 145, "DEF": 160, "SPE": 145}),
    "Centiboob": SpiritData({"KillerInstinct": 1, "PoisonBite": 3, "BoobSlam": 6, "Lactate": 16, "Hypnosis": 22, "LitanyOfCurses": 28, "BreastMassage": 36, }, None, "Oppai", {"HP": 140, "STA": 100, "ATT": 135, "DEF": 135, "SPE": 135}),
    "Chocostar": SpiritData({"BlowBubbles": 1, "Twerk": 3, "Starfall": 10, "TeamChant": 17, "NastyBubbles": 22, "MiracleCure": 25, "FishyBusiness": 30, "SexyPose": 36, }, None, "Aquatic", {"HP": 110, "STA": 100, "ATT": 110, "DEF": 125, "SPE": 110}),
    "Chubbie": SpiritData({"Slam": 1, "PoisonSlime": 3, "Yoga": 8, "SlimeRain": 12, "BoobJiggle": 15, "BoobPounding": 20, "SlimeArmor": 27, "Lubrication": 32, "Smother": 37, }, {"Thiccsie": 16}, "Slime", {"HP": 120, "STA": 100, "ATT": 100, "DEF": 125, "SPE": 90}),
    "Deardeer": SpiritData({"Snowballing": 1, "NaturesMight": 3, "Stretch": 6, "ScentSpray": 14, "YellowSnow": 19, "MiracleCure": 26, "AntlerAssault": 30, "SeedOfLife": 37, }, None, "Furry", {"HP": 110, "STA": 100, "ATT": 120, "DEF": 110, "SPE": 120}),
    "Domina": SpiritData({"Bite": 1, "BitchSlap": 3, "SexyPose": 8, "Strangle": 11, "Domination": 15, "GoldenShower": 18, "MassSeduction": 23, "ExtremeFisting": 27, "GoldenRain": 32, }, {"Dominatrix": 35}, "Lust", {"HP": 100, "STA": 100, "ATT": 125, "DEF": 100, "SPE": 110}),
    "Dominatrix": SpiritData({"Bite": 1, "BitchSlap": 3, "SexyPose": 8, "Strangle": 11, "Domination": 15, "GoldenShower": 18, "MassSeduction": 23, "ExtremeFisting": 27, "GoldenRain": 32, }, None, "Lust", {"HP": 105, "STA": 100, "ATT": 130, "DEF": 105, "SPE": 115}),
    "Dracoomer": SpiritData({"PoisonBite": 1, "Scratch": 3, "HardenScales": 7, "Yoga": 11, "Lacerate": 16, "SerpentsTongue": 19, "TeamChant": 23, "PoisonSpit": 27, "AcidSquirt": 33, }, None, "Scalie", {"HP": 105, "STA": 100, "ATT": 115, "DEF": 115, "SPE": 115}),
    "Dripsy": SpiritData({"Slam": 1, "SlimeRain": 3, "SlimeArmor": 8, "Yoga": 12, "Lubrication": 15, "SlimeSquirt": 19, "TeamChant": 31, "SlimeTentacle": 36, "BitchSlap": 40, }, None, "Slime", {"HP": 100, "STA": 100, "ATT": 115, "DEF": 100, "SPE": 105}),
    "EV-3": SpiritData({"Suck": 1, "BreastMassage": 3, "NaughtyTentacles": 9, "BeeSwarm": 14, "SlimeSquirt": 17, "Strangle": 24, "PawStrike": 32, "BlowBubbles": 36, "SerpentsTongue": 40, }, None, "Lust", {"HP": 130, "STA": 100, "ATT": 130, "DEF": 130, "SPE": 130}),
    "Faerie": SpiritData({"Swoop": 1, "Flirt": 3, "CockFlurry": 8, "Suck": 12, "TeamChant": 15, "CumRain": 20, "PoisonBlitz": 25, "BlowKiss": 31, "AirStrike": 38, }, None, "Avian", {"HP": 105, "STA": 100, "ATT": 105, "DEF": 110, "SPE": 110}),
    "Flora": SpiritData({"Lash": 1, "LeafBlast": 3, "SeedOfLife": 7, "Meditate": 11, "FlowerPower": 15, "Flirt": 19, "BoobPounding": 31, "ThornStrike": 35, "CurePoison": 39, }, None, "Plant", {"HP": 90, "STA": 100, "ATT": 115, "DEF": 95, "SPE": 115}),
    "Fungie": SpiritData({"Lash": 1, "PoisonSquirt": 3, "Shrooms": 8, "Strangle": 14, "RootBondage": 20, "EyePoke": 31, "VaginalFungus": 38, }, None, "Plant", {"HP": 95, "STA": 100, "ATT": 115, "DEF": 110, "SPE": 105}),
    "Gangfang": SpiritData({"Pounce": 1, "Bite": 3, "Growl": 6, "DoggyStyle": 12, "Howl": 16, "Stretch": 20, "ScentSpray": 25, "PawStrike": 31, "PawStorm": 38, }, None, "Furry", {"HP": 120, "STA": 100, "ATT": 125, "DEF": 120, "SPE": 110}),
    "Gloreen": SpiritData({"Suck": 1, "Slam": 3, "Rimjob": 7, "HappyThoughts": 11, "BlowKiss": 15, "Lubrication": 20, "Meditate": 25, "MassSeduction": 31, "SirenSong": 38, }, None, "Lust", {"HP": 115, "STA": 100, "ATT": 105, "DEF": 125, "SPE": 105}),
    "Gloria": SpiritData({"Suck": 1, "Slam": 3, "Rimjob": 7, "HappyThoughts": 11, "BlowKiss": 15, "Lubrication": 20, "Meditate": 25, "MassSeduction": 31, "SirenSong": 38, }, {"Gloreen": 11}, "Lust", {"HP": 110, "STA": 100, "ATT": 115, "DEF": 115, "SPE": 105}),
    "Growleen": SpiritData({"Pounce": 1, "Bite": 3, "Growl": 6, "DoggyStyle": 12, "Howl": 16, "Stretch": 20, "ScentSpray": 25, "PawStrike": 31, "PawStorm": 38, }, {"Gangfang": 25}, "Furry", {"HP": 115, "STA": 100, "ATT": 120, "DEF": 120, "SPE": 110}),
    "Harlie": SpiritData({"CockBlast": 1, "HappyThoughts": 3, "CockFlurry": 7, "Stretch": 13, "Fisting": 16, "SexyPose": 20, "Rimjob": 25, "CumRain": 29, "ToeStrike": 34, }, None, "Lust", {"HP": 110, "STA": 100, "ATT": 110, "DEF": 115, "SPE": 110}),
    "Harpie": SpiritData({"Meditate": 1, "Swoop": 3, "BitchSlap": 6, "Hypnosis": 10, "Stretch": 14, "Rimjob": 18, "Yoga": 22, "ExtremeFisting": 27, "GoldenRain": 32, }, None, "Avian", {"HP": 105, "STA": 100, "ATT": 110, "DEF": 105, "SPE": 120}),
    "Hornie": SpiritData({"Fisting": 1, "Hypnosis": 3, "Curse": 8, "Rimjob": 12, "LitanyOfCurses": 15, "GoldenShower": 18, "ExtremeFisting": 29, "MassSeduction": 34, "DonkeyPunch": 40, }, {"Succubae": 23}, "Demon", {"HP": 105, "STA": 100, "ATT": 125, "DEF": 100, "SPE": 115}),
    "Jawsy": SpiritData({"Chomp": 1, "KillerInstinct": 3, "Slam": 10, "TailSwipe": 19, "MostMuscular": 22, "FishyBusiness": 26, "Domination": 30, "NippleClamp": 36, }, None, "Aquatic", {"HP": 120, "STA": 100, "ATT": 155, "DEF": 100, "SPE": 135}),
    "Jellybish": SpiritData({"StingingTentacles": 1, "WaterSpray": 3, "CurePoison": 10, "SlimeArmor": 15, "SlimeSquirt": 20, "JellyfishSwarm": 26, "TentacleDrain": 31, "NaughtyTentacles": 37, }, None, "Aquatic", {"HP": 100, "STA": 100, "ATT": 120, "DEF": 115, "SPE": 100}),
    "Jellygal": SpiritData({"StingingTentacles": 1, "WaterSpray": 3, "CurePoison": 10, "SlimeArmor": 15, "SlimeSquirt": 20, "JellyfishSwarm": 26, "TentacleDrain": 31, "NaughtyTentacles": 37, }, {"Jellybish": 28}, "Aquatic", {"HP": 100, "STA": 100, "ATT": 115, "DEF": 110, "SPE": 100}),
    "Juggsie": SpiritData({"BitchSlap": 1, "Lactate": 3, "FreshMilk": 5, "BoobPounding": 9, "TeamChant": 12, "Smother": 17, "MilkStorm": 22, "Titillate": 28, "Starfall": 33, }, None, "Oppai", {"HP": 115, "STA": 100, "ATT": 120, "DEF": 115, "SPE": 105}),
    "Kittypus": SpiritData({"Scratch": 1, "ScentSpray": 3, "PawStrike": 5, "Purr": 10, "Lacerate": 14, "SharpenClaws": 17, "BlowKiss": 21, "TailSwipe": 25, "PawStorm": 30, "KillerInstinct": 36, }, {"Panthera": 30}, "Furry", {"HP": 115, "STA": 100, "ATT": 155, "DEF": 105, "SPE": 140}),
    "Lacteena": SpiritData({"BitchSlap": 1, "Lactate": 3, "FreshMilk": 5, "BoobPounding": 9, "TeamChant": 12, "Smother": 17, "MilkStorm": 22, "Titillate": 28, "Starfall": 33, }, {"Juggsie": 36}, "Oppai", {"HP": 110, "STA": 100, "ATT": 115, "DEF": 110, "SPE": 100}),
    "Lizzie": SpiritData({"WaterSpray": 1, "HardenScales": 3, "FishyBusiness": 12, "SerpentsTongue": 16, "CleansingWaters": 22, "NastyBubbles": 28, "PoisonBite": 36, }, None, "Scalie", {"HP": 100, "STA": 100, "ATT": 130, "DEF": 110, "SPE": 130}),
    "Mamaoak": SpiritData({"Lash": 1, "Strangle": 3, "SeedOfLife": 9, "BitchSlap": 12, "Photosynthesis": 16, "Meditate": 21, "RootBondage": 26, "BoobPounding": 32, "MiracleCure": 39, }, None, "Plant", {"HP": 135, "STA": 100, "ATT": 100, "DEF": 115, "SPE": 100}),
    "Marinel": SpiritData({"WaterSpray": 1, "Seduce": 3, "SeedOfLife": 10, "SirenSong": 17, "FishyBusiness": 21, "CleansingWaters": 26, "Starfall": 31, "CleansingSlap": 37, }, None, "Aquatic", {"HP": 130, "STA": 100, "ATT": 110, "DEF": 115, "SPE": 120}),
    "Megaboob": SpiritData({"Slam": 1, "BoobJiggle": 3, "BreastMassage": 5, "BoobPounding": 7, "FreshMilk": 13, "MilkStorm": 18, "Flirt": 22, "BoobSlam": 26, "MassSeduction": 31, "CleansingSlap": 37, }, {"Boobarella": 29}, "Oppai", {"HP": 150, "STA": 100, "ATT": 125, "DEF": 140, "SPE": 105}),
    "Oakie": SpiritData({"Lash": 1, "Strangle": 3, "SeedOfLife": 9, "BitchSlap": 12, "Photosynthesis": 16, "Meditate": 21, "RootBondage": 26, "BoobPounding": 32, "MiracleCure": 39, }, {"Mamaoak": 19}, "Plant", {"HP": 130, "STA": 100, "ATT": 95, "DEF": 110, "SPE": 95}),
    "Octocunt": SpiritData({"Curse": 1, "Lash": 3, "Suck": 5, "TentacleTrash": 9, "Meditate": 12, "NaughtyTentacles": 16, "TeamChant": 20, "Hypnosis": 24, "TentacleDrain": 29, "NastyBubbles": 34, }, {"Octomommy": 25}, "Demon", {"HP": 130, "STA": 100, "ATT": 135, "DEF": 125, "SPE": 125}),
    "Octomommy": SpiritData({"Curse": 1, "Lash": 3, "Suck": 5, "TentacleTrash": 9, "Meditate": 12, "NaughtyTentacles": 16, "TeamChant": 20, "Hypnosis": 24, "TentacleDrain": 29, "NastyBubbles": 34, }, None, "Demon", {"HP": 135, "STA": 100, "ATT": 140, "DEF": 125, "SPE": 125}),
    "Octopussy": SpiritData({"Curse": 1, "Lash": 3, "Suck": 5, "TentacleTrash": 9, "Meditate": 12, "NaughtyTentacles": 16, "TeamChant": 20, "Hypnosis": 24, "TentacleDrain": 29, "NastyBubbles": 34, }, {"Octocunt": 12}, "Demon", {"HP": 125, "STA": 100, "ATT": 130, "DEF": 120, "SPE": 120}),
    "Panthera": SpiritData({"Scratch": 1, "ScentSpray": 3, "PawStrike": 5, "Purr": 10, "Lacerate": 14, "SharpenClaws": 17, "BlowKiss": 21, "TailSwipe": 25, "PawStorm": 30, "KillerInstinct": 36, }, None, "Furry", {"HP": 120, "STA": 100, "ATT": 160, "DEF": 105, "SPE": 140}),
    "Petunia": SpiritData({"Lash": 1, "LeafBlast": 3, "SeedOfLife": 7, "Meditate": 11, "FlowerPower": 15, "Flirt": 19, "BoobPounding": 31, "ThornStrike": 35, "CurePoison": 39, }, {"Flora": 8}, "Plant", {"HP": 85, "STA": 100, "ATT": 110, "DEF": 90, "SPE": 110}),
    "Pinchie": SpiritData({"NippleClamp": 1, "Slam": 3, "Crabs": 10, "WaterSpray": 18, "ClawFlurry": 23, "TeamChant": 28, "KillerInstinct": 33, "NastyBubbles": 39, }, None, "Aquatic", {"HP": 120, "STA": 100, "ATT": 120, "DEF": 125, "SPE": 100}),
    "Polaria": SpiritData({"BitchSlap": 1, "SexyPose": 3, "Lacerate": 7, "Growl": 10, "BearHug": 14, "BoobPounding": 17, "SharpenClaws": 22, "ExtremeFisting": 26, "CleansingSlap": 30, "PowerPunch": 36, }, None, "Furry", {"HP": 140, "STA": 100, "ATT": 120, "DEF": 130, "SPE": 105}),
    "Pusseen": SpiritData({"Scratch": 1, "ScentSpray": 3, "PawStrike": 5, "Purr": 10, "Lacerate": 14, "SharpenClaws": 17, "BlowKiss": 21, "TailSwipe": 25, "PawStorm": 30, "KillerInstinct": 36, }, {"Kittypus": 12}, "Furry", {"HP": 110, "STA": 100, "ATT": 150, "DEF": 100, "SPE": 135}),
    "Queenbee": SpiritData({"Sting": 1, "Buzz": 3, "HappyThoughts": 6, "Fisting": 9, "BlowKiss": 14, "BeeSwarm": 18, "LethalSting": 28, "PoisonBlitz": 34, "EyePoke": 38, "Domination": 42, }, None, "Avian", {"HP": 105, "STA": 100, "ATT": 135, "DEF": 105, "SPE": 130}),
    "Rawry": SpiritData({"PoisonBite": 1, "Scratch": 3, "HardenScales": 7, "Yoga": 11, "Lacerate": 16, "SerpentsTongue": 19, "TeamChant": 23, "PoisonSpit": 27, "AcidSquirt": 33, }, {"Dracoomer": 14}, "Scalie", {"HP": 100, "STA": 100, "ATT": 110, "DEF": 110, "SPE": 110}),
    "Seraphina": SpiritData({"Slam": 1, "Swoop": 3, "Yoga": 9, "GoldenRain": 15, "AirStrike": 20, "Starfall": 24, "MiracleCure": 35, }, None, "Avian", {"HP": 105, "STA": 100, "ATT": 110, "DEF": 120, "SPE": 125}),
    "Serpentax": SpiritData({"Bite": 1, "PoisonSpit": 3, "SerpentsTongue": 5, "Slither": 9, "Stretch": 14, "PoisonBite": 18, "TailSwipe": 21, "Hypnosis": 25, "AcidSquirt": 30, "LitanyOfCurses": 37, }, {"Slithereen": 27}, "Scalie", {"HP": 120, "STA": 100, "ATT": 135, "DEF": 115, "SPE": 125}),
    "Serpentina": SpiritData({"Bite": 1, "PoisonSpit": 3, "SerpentsTongue": 5, "Slither": 9, "Stretch": 14, "PoisonBite": 18, "TailSwipe": 21, "Hypnosis": 25, "AcidSquirt": 30, "LitanyOfCurses": 37, }, {"Serpentax": 10}, "Scalie", {"HP": 115, "STA": 100, "ATT": 130, "DEF": 110, "SPE": 120}),
    "Sexybun": SpiritData({"Scratch": 1, "SwiftPaws": 3, "Pounce": 6, "Flirt": 9, "Bite": 14, "Stretch": 18, "PawStrike": 21, "ScentSpray": 25, "NaturesMight": 31, }, None, "Furry", {"HP": 95, "STA": 100, "ATT": 115, "DEF": 100, "SPE": 155}),
    "Sharky": SpiritData({"Chomp": 1, "KillerInstinct": 3, "Slam": 10, "TailSwipe": 19, "MostMuscular": 22, "FishyBusiness": 26, "Domination": 30, "NippleClamp": 36, }, {"Jawsy": 27}, "Aquatic", {"HP": 120, "STA": 100, "ATT": 150, "DEF": 100, "SPE": 130}),
    "Slimee": SpiritData({"Slam": 1, "SlimeRain": 3, "SlimeArmor": 8, "Yoga": 12, "Lubrication": 15, "SlimeSquirt": 19, "TeamChant": 31, "SlimeTentacle": 36, "BitchSlap": 40, }, {"Dripsy": 10}, "Slime", {"HP": 95, "STA": 100, "ATT": 110, "DEF": 95, "SPE": 100}),
    "Slithereen": SpiritData({"Bite": 1, "PoisonSpit": 3, "SerpentsTongue": 5, "Slither": 9, "Stretch": 14, "PoisonBite": 18, "TailSwipe": 21, "Hypnosis": 25, "AcidSquirt": 30, "LitanyOfCurses": 37, }, None, "Scalie", {"HP": 120, "STA": 100, "ATT": 140, "DEF": 115, "SPE": 130}),
    "Slushie": SpiritData({"Lash": 1, "SlimeSquirt": 3, "SlimeArmor": 7, "HailStorm": 15, "CleansingWaters": 20, "TeamChant": 25, "FrostArmor": 31, "Snowballing": 37, }, None, "Slime", {"HP": 105, "STA": 100, "ATT": 115, "DEF": 110, "SPE": 115}),
    "Snowbae": SpiritData({"FrostArmor": 1, "Snowballing": 3, "MilkStorm": 8, "BoobSlam": 15, "BitchSlap": 20, "YellowSnow": 25, "BreastMassage": 31, "TeamChant": 37, }, None, "Oppai", {"HP": 125, "STA": 100, "ATT": 105, "DEF": 120, "SPE": 100}),
    "Spinnie": SpiritData({"Bite": 1, "BindingWeb": 3, "Meditate": 7, "Curse": 10, "Fisting": 13, "Hypnosis": 15, "PoisonBite": 20, "LitanyOfCurses": 25, "NippleClamp": 30, }, {"Arachna": 23}, "Demon", {"HP": 110, "STA": 100, "ATT": 135, "DEF": 100, "SPE": 115}),
    "Succubae": SpiritData({"Fisting": 1, "Hypnosis": 3, "Curse": 8, "Rimjob": 12, "LitanyOfCurses": 15, "GoldenShower": 18, "ExtremeFisting": 29, "MassSeduction": 34, "DonkeyPunch": 40, }, None, "Demon", {"HP": 110, "STA": 100, "ATT": 130, "DEF": 105, "SPE": 120}),
    "Thiccsie": SpiritData({"Slam": 1, "PoisonSlime": 3, "Yoga": 8, "SlimeRain": 12, "BoobJiggle": 15, "BoobPounding": 20, "SlimeArmor": 27, "Lubrication": 32, "Smother": 37, }, None, "Slime", {"HP": 125, "STA": 100, "ATT": 105, "DEF": 130, "SPE": 95}),
    "Tinky": SpiritData({"Swoop": 1, "Flirt": 3, "CockFlurry": 8, "Suck": 12, "TeamChant": 15, "CumRain": 20, "PoisonBlitz": 25, "BlowKiss": 31, "AirStrike": 38, }, {"Faerie": 21}, "Avian", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 105, "SPE": 105}),
    "Triboobe": SpiritData({"BitchSlap": 1, "Lactate": 3, "Titillate": 7, "Squirt": 11, "BoobJiggle": 14, "Smother": 18, "ExtremeFisting": 27, "TeamChant": 33, "ToeStrike": 40, }, None, "Oppai", {"HP": 105, "STA": 100, "ATT": 115, "DEF": 115, "SPE": 115}),
    "Trissy": SpiritData({"BitchSlap": 1, "Lactate": 3, "Titillate": 7, "Squirt": 11, "BoobJiggle": 14, "Smother": 18, "ExtremeFisting": 27, "TeamChant": 33, "ToeStrike": 40, }, {"Triboobe": 13}, "Oppai", {"HP": 100, "STA": 100, "ATT": 110, "DEF": 110, "SPE": 110}),
    "Twerky": SpiritData({"Suck": 1, "Scratch": 3, "Squirt": 8, "Stretch": 12, "Twerk": 16, "Rimjob": 20, "GoldenShower": 24, "MassSeduction": 28, "Scissoring": 33, }, {"Twerqueen": 21}, "Lust", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 110, "SPE": 115}),
    "Twerqueen": SpiritData({"Suck": 1, "Scratch": 3, "Squirt": 8, "Stretch": 12, "Twerk": 16, "Rimjob": 20, "GoldenShower": 24, "MassSeduction": 28, "Scissoring": 33, }, None, "Lust", {"HP": 105, "STA": 100, "ATT": 105, "DEF": 115, "SPE": 120}),
    "Udderella": SpiritData({"FreshMilk": 1, "Bite": 3, "BoobSlam": 6, "BlowKiss": 10, "BreastMassage": 13, "HappyThoughts": 15, "Smother": 20, "MilkStorm": 24, "CurePoison": 29, }, None, "Oppai", {"HP": 105, "STA": 100, "ATT": 105, "DEF": 115, "SPE": 120}),
    "Unihorn": SpiritData({"Bite": 1, "TailSwipe": 3, "ScentSpray": 9, "NaturesMight": 15, "CleansingSlap": 25, "TeamChant": 30, "DonkeyPunch": 37, }, None, "Furry", {"HP": 105, "STA": 100, "ATT": 120, "DEF": 100, "SPE": 130}),
    "Ursie": SpiritData({"BitchSlap": 1, "SexyPose": 3, "Lacerate": 7, "Growl": 10, "BearHug": 14, "BoobPounding": 17, "SharpenClaws": 22, "ExtremeFisting": 26, "CleansingSlap": 30, "PowerPunch": 36, }, {"Bearboo": 12}, "Furry", {"HP": 130, "STA": 100, "ATT": 115, "DEF": 120, "SPE": 100}),
    "Valkyrie_Boss": SpiritData({"CockFlurry": 1, "CockBlast": 1, "CumRain": 1, "BoobSlam": 1, "BreastMassage": 1, }, None, "Lust", {"HP": 300, "STA": 100, "ATT": 170, "DEF": 170, "SPE": 115}),
    "Valkyrie": SpiritData({"CockFlurry": 1, "CockBlast": 3, "CumRain": 10, "BoobSlam": 15, "BreastMassage": 22, "CleansingSlap": 27, "MilkStorm": 33, "DonkeyPunch": 38, }, None, "Lust", {"HP": 145, "STA": 100, "ATT": 125, "DEF": 145, "SPE": 115}),
    "Wolfy": SpiritData({"Pounce": 1, "Bite": 3, "Growl": 6, "DoggyStyle": 12, "Howl": 16, "Stretch": 20, "ScentSpray": 25, "PawStrike": 31, "PawStorm": 38, }, {"Growleen": 15}, "Furry", {"HP": 110, "STA": 100, "ATT": 115, "DEF": 115, "SPE": 105}),
    "SpiritMother": SpiritData({"Strangle": 1, "PoisonSquirt": 1, "NaturesMight": 1, "CleansingSlap": 1, "DonkeyPunch": 1, "MassSeduction": 1, }, None, "Plant", {"HP": 460, "STA": 100, "ATT": 155, "DEF": 160, "SPE": 130}),
}

attacking_moves = ["BitchSlap", "PowerPunch", "NippleClamp", "ToeStrike", "DonkeyPunch", "Bite", "Fisting", "PoisonBite", "Lacerate", "BearHug", "BoobPounding", "ExtremeFisting", "CleansingSlap", "Sting", "BeeSwarm", "LethalSting", "EyePoke", "LeafBlast", "Swoop", "Rimjob", "Slam", "BreastMassage", "BoobSlam", "Smother", "Scratch", "Pounce", "PawStrike", "ThornStrike", "Strangle", "BlowBubbles", "Starfall", "NastyBubbles", "SlimeRain", "Snowballing", "YellowSnow", "AntlerAssault", "GoldenShower", "AcidSquirt", "SlimeSquirt", "SlimeTentacle", "Suck", "NaughtyTentacles", "CockFlurry", "AirStrike", "Lash", "DoggyStyle", "PawStorm", "CockBlast", "Chomp", "TailSwipe", "WaterSpray", "JellyfishSwarm", "TentacleDrain", "TentacleTrash", "ClawFlurry", "HailStorm", "Squirt", "Scissoring", ]
non_attack_moves = ["MostMuscular", "WarCry", "Domination", "BindingWeb", "Meditate", "Curse", "Hypnosis", "LitanyOfCurses", "SexyPose", "Growl", "SharpenClaws", "Buzz", "HappyThoughts", "BlowKiss", "PoisonBlitz", "Seduce", "Photosynthesis", "TeamChant", "PoisonSquirt", "FlowerPower", "SeedOfLife", "NaturesMight", "Stretch", "Yoga", "GoldenRain", "BoobJiggle", "FreshMilk", "MilkStorm", "Flirt", "MassSeduction", "CurePoison", "SwiftPaws", "ScentSpray", "CoatOfSpikes", "KillerInstinct", "Lactate", "Twerk", "MiracleCure", "FishyBusiness", "PoisonSlime", "SlimeArmor", "Lubrication", "HardenScales", "SerpentsTongue", "PoisonSpit", "CumRain", "Shrooms", "RootBondage", "VaginalFungus", "Howl", "SirenSong", "StingingTentacles", "Titillate", "Purr", "CleansingWaters", "Crabs", "Slither", "FrostArmor", ]
all_moves = [*non_attack_moves, *attacking_moves]
move_data = {
    # ATTACKING MOVES
    "BitchSlap": {"Power": 40, "Accuracy": 95, "Stamina": 7, "Type": None, "Priority": 1},
    "PowerPunch": {"Power": 60, "Accuracy": 95, "Stamina": 9, "Type": None, "Priority": 2},
    "NippleClamp": {"Power": 45, "Accuracy": 100, "Stamina": 8, "Type": "Lust", "Priority": 1},
    "ToeStrike": {"Power": 60, "Accuracy": 100, "Stamina": 9, "Type": "Lust", "Priority": 1},
    "DonkeyPunch": {"Power": 55, "Accuracy": 100, "Stamina": 9, "Type": None, "Priority": 2},
    "Bite": {"Power": 30, "Accuracy": 95, "Stamina": 6, "Type": None, "Priority": 2},
    "Fisting": {"Power": 40, "Accuracy": 95, "Stamina": 8, "Type": None, "Priority": 1},
    "PoisonBite": {"Power": 50, "Accuracy": 100, "Stamina": 8, "Type": "Scalie", "Priority": 2},
    "Lacerate": {"Power": 55, "Accuracy": 95, "Stamina": 9, "Type": None, "Priority": 2},
    "BearHug": {"Power": 50, "Accuracy": 95, "Stamina": 9, "Type": None, "Priority": 3},
    "BoobPounding": {"Power": 50, "Accuracy": 95, "Stamina": 9, "Type": None, "Priority": 3},
    "ExtremeFisting": {"Power": 50, "Accuracy": 95, "Stamina": 10, "Type": None, "Priority": 2},
    "CleansingSlap": {"Power": 35, "Accuracy": 95, "Stamina": 7, "Type": None, "Priority": 2},
    "Sting": {"Power": 45, "Accuracy": 95, "Stamina": 7, "Type": "Avian", "Priority": 1},
    "BeeSwarm": {"Power": 35, "Accuracy": 95, "Stamina": 8, "Type": "Avian", "Priority": 1},
    "LethalSting": {"Power": 55, "Accuracy": 100, "Stamina": 10, "Type": "Avian", "Priority": 1},
    "EyePoke": {"Power": 45, "Accuracy": 100, "Stamina": 8, "Type": None, "Priority": 2},
    "LeafBlast": {"Power": 45, "Accuracy": 100, "Stamina": 6, "Type": "Plant", "Priority": 2},
    "Swoop": {"Power": 40, "Accuracy": 95, "Stamina": 7, "Type": "Avian", "Priority": 2},
    "Rimjob": {"Power": 35, "Accuracy": 100, "Stamina": 7, "Type": "Lust", "Priority": 1},
    "Slam": {"Power": 40, "Accuracy": 95, "Stamina": 6, "Type": None, "Priority": 3},
    "BreastMassage": {"Power": 25, "Accuracy": 100, "Stamina": 9, "Type": "Oppai", "Priority": 2},
    "BoobSlam": {"Power": 55, "Accuracy": 95, "Stamina": 10, "Type": "Oppai", "Priority": 3},
    "Smother": {"Power": 35, "Accuracy": 90, "Stamina": 7, "Type": "Oppai", "Priority": 2},
    "Scratch": {"Power": 30, "Accuracy": 95, "Stamina": 5, "Type": None, "Priority": 2},
    "Pounce": {"Power": 40, "Accuracy": 95, "Stamina": 6, "Type": "Furry", "Priority": 2},
    "PawStrike": {"Power": 50, "Accuracy": 100, "Stamina": 8, "Type": "Furry", "Priority": 1},
    "ThornStrike": {"Power": 40, "Accuracy": 95, "Stamina": 7, "Type": "Plant", "Priority": 1},
    "Strangle": {"Power": 50, "Accuracy": 100, "Stamina": 8, "Type": "Plant", "Priority": 2},
    "BlowBubbles": {"Power": 40, "Accuracy": 95, "Stamina": 7, "Type": "Aquatic", "Priority": 2},
    "Starfall": {"Power": 45, "Accuracy": 100, "Stamina": 8, "Type": None, "Priority": 1},
    "NastyBubbles": {"Power": 30, "Accuracy": 100, "Stamina": 10, "Type": "Aquatic", "Priority": 2},
    "SlimeRain": {"Power": 50, "Accuracy": 95, "Stamina": 7, "Type": "Slime", "Priority": 2},
    "Snowballing": {"Power": 50, "Accuracy": 95, "Stamina": 5, "Type": None, "Priority": 2},
    "YellowSnow": {"Power": 40, "Accuracy": 95, "Stamina": 9, "Type": None, "Priority": 2},
    "AntlerAssault": {"Power": 55, "Accuracy": 100, "Stamina": 7, "Type": "Furry", "Priority": 2},
    "GoldenShower": {"Power": 30, "Accuracy": 100, "Stamina": 6, "Type": None, "Priority": 2},
    "AcidSquirt": {"Power": 50, "Accuracy": 95, "Stamina": 9, "Type": None, "Priority": 2},
    "SlimeSquirt": {"Power": 35, "Accuracy": 100, "Stamina": 6, "Type": "Slime", "Priority": 1},
    "SlimeTentacle": {"Power": 40, "Accuracy": 95, "Stamina": 8, "Type": "Slime", "Priority": 2},
    "Suck": {"Power": 40, "Accuracy": 95, "Stamina": 9, "Type": "Lust", "Priority": 2},
    "NaughtyTentacles": {"Power": 40, "Accuracy": 100, "Stamina": 5, "Type": "Demon", "Priority": 2},
    "CockFlurry": {"Power": 35, "Accuracy": 95, "Stamina": 5, "Type": None, "Priority": 2},
    "AirStrike": {"Power": 60, "Accuracy": 95, "Stamina": 9, "Type": "Avian", "Priority": 2},
    "Lash": {"Power": 30, "Accuracy": 95, "Stamina": 5, "Type": None, "Priority": 2},
    "DoggyStyle": {"Power": 45, "Accuracy": 90, "Stamina": 7, "Type": "Furry", "Priority": 1},
    "PawStorm": {"Power": 65, "Accuracy": 100, "Stamina": 10, "Type": "Furry", "Priority": 1},
    "CockBlast": {"Power": 40, "Accuracy": 95, "Stamina": 7, "Type": "Lust", "Priority": 1},
    "Chomp": {"Power": 50, "Accuracy": 95, "Stamina": 7, "Type": "Aquatic", "Priority": 2},
    "TailSwipe": {"Power": 30, "Accuracy": 95, "Stamina": 4, "Type": "Furry", "Priority": 1},
    "WaterSpray": {"Power": 35, "Accuracy": 95, "Stamina": 5, "Type": "Aquatic", "Priority": 2},
    "JellyfishSwarm": {"Power": 40, "Accuracy": 100, "Stamina": 6, "Type": "Aquatic", "Priority": 2},
    "TentacleDrain": {"Power": 50, "Accuracy": 100, "Stamina": 10, "Type": "Demon", "Priority": 2},
    "TentacleTrash": {"Power": 45, "Accuracy": 95, "Stamina": 7, "Type": "Demon", "Priority": 2},
    "ClawFlurry": {"Power": 55, "Accuracy": 100, "Stamina": 8, "Type": "Aquatic", "Priority": 1},
    "HailStorm": {"Power": 60, "Accuracy": 100, "Stamina": 9, "Type": "Slime", "Priority": 1},
    "Squirt": {"Power": 40, "Accuracy": 95, "Stamina": 8, "Type": "Lust", "Priority": 2},
    "Scissoring": {"Power": 60, "Accuracy": 95, "Stamina": 8, "Type": "Lust", "Priority": 2},
    # NON ATTACKING MOVES,
    "MostMuscular": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "WarCry": {"Power": 0, "Accuracy": 100, "Stamina": 8, "Type": None, "Priority": 2},
    "Domination": {"Power": 0, "Accuracy": 100, "Stamina": 6, "Type": None, "Priority": 2},
    "BindingWeb": {"Power": 0, "Accuracy": 95, "Stamina": 4, "Type": None, "Priority": 2},
    "Meditate": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "Curse": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "Hypnosis": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "LitanyOfCurses": {"Power": 0, "Accuracy": 100, "Stamina": 6, "Type": None, "Priority": 2},
    "SexyPose": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": None, "Priority": 2},
    "Growl": {"Power": 0, "Accuracy": 100, "Stamina": 6, "Type": None, "Priority": 1},
    "SharpenClaws": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": "Furry", "Priority": 2},
    "Buzz": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "HappyThoughts": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "BlowKiss": {"Power": 0, "Accuracy": 95, "Stamina": 4, "Type": None, "Priority": 2},
    "PoisonBlitz": {"Power": 0, "Accuracy": 100, "Stamina": 7, "Type": None, "Priority": 2},
    "Seduce": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "Photosynthesis": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": None, "Priority": 1},
    "TeamChant": {"Power": 0, "Accuracy": 100, "Stamina": 7, "Type": None, "Priority": 2},
    "PoisonSquirt": {"Power": 0, "Accuracy": 100, "Stamina": 6, "Type": None, "Priority": 2},
    "FlowerPower": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "SeedOfLife": {"Power": 0, "Accuracy": 100, "Stamina": 10, "Type": None, "Priority": 2},
    "NaturesMight": {"Power": 0, "Accuracy": 100, "Stamina": 10, "Type": None, "Priority": 2},
    "Stretch": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "Yoga": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": None, "Priority": 2},
    "GoldenRain": {"Power": 0, "Accuracy": 100, "Stamina": 12, "Type": None, "Priority": 2},
    "BoobJiggle": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "FreshMilk": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": "Oppai", "Priority": 2},
    "MilkStorm": {"Power": 0, "Accuracy": 100, "Stamina": 14, "Type": None, "Priority": 3},
    "Flirt": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "MassSeduction": {"Power": 0, "Accuracy": 100, "Stamina": 6, "Type": None, "Priority": 2},
    "CurePoison": {"Power": 0, "Accuracy": 100, "Stamina": 3, "Type": None, "Priority": 1},
    "SwiftPaws": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": None, "Priority": 1},
    "ScentSpray": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "CoatOfSpikes": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": None, "Priority": 2},
    "KillerInstinct": {"Power": 0, "Accuracy": 100, "Stamina": 3, "Type": None, "Priority": 1},
    "Lactate": {"Power": 0, "Accuracy": 95, "Stamina": 4, "Type": "Oppai", "Priority": 2},
    "Twerk": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": None, "Priority": 2},
    "MiracleCure": {"Power": 0, "Accuracy": 100, "Stamina": 6, "Type": None, "Priority": 2},
    "FishyBusiness": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": "Aquatic", "Priority": 2},
    "PoisonSlime": {"Power": 0, "Accuracy": 100, "Stamina": 8, "Type": None, "Priority": 2},
    "SlimeArmor": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": None, "Priority": 1},
    "Lubrication": {"Power": 0, "Accuracy": 95, "Stamina": 4, "Type": None, "Priority": 2},
    "HardenScales": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": None, "Priority": 1},
    "SerpentsTongue": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 2},
    "PoisonSpit": {"Power": 0, "Accuracy": 95, "Stamina": 6, "Type": "Scalie", "Priority": 2},
    "CumRain": {"Power": 0, "Accuracy": 100, "Stamina": 7, "Type": None, "Priority": 2},
    "Shrooms": {"Power": 0, "Accuracy": 100, "Stamina": 8, "Type": None, "Priority": 2},
    "RootBondage": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": None, "Priority": 2},
    "VaginalFungus": {"Power": 0, "Accuracy": 100, "Stamina": 9, "Type": None, "Priority": 2},
    "Howl": {"Power": 0, "Accuracy": 100, "Stamina": 7, "Type": None, "Priority": 2},
    "SirenSong": {"Power": 0, "Accuracy": 100, "Stamina": 5, "Type": None, "Priority": 2},
    "StingingTentacles": {"Power": 0, "Accuracy": 100, "Stamina": 7, "Type": None, "Priority": 2},
    "Titillate": {"Power": 0, "Accuracy": 95, "Stamina": 4, "Type": None, "Priority": 2},
    "Purr": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 1},
    "CleansingWaters": {"Power": 0, "Accuracy": 100, "Stamina": 10, "Type": None, "Priority": 1},
    "Crabs": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": "Aquatic", "Priority": 2},
    "Slither": {"Power": 0, "Accuracy": 100, "Stamina": 4, "Type": None, "Priority": 1},
    "FrostArmor": {"Power": 0, "Accuracy": 100, "Stamina": 8, "Type": None, "Priority": 2},
}

grass_loc = ["Trail1", "EvergreenOutpost", "Trail2", "MillysFarm", "Trail3", "EvergreenCaverns", "Trail4", "Trail5", "SandyTunnels", "Trail6", "DairyFarm", "Trail7", "Trail8", "DustyGrotto", "OldMastersHut", "CaveOfTorment", "Trail9", "CrashSite", "Trail10", "Trail11", "Trail12", "FishingHut", "Trail13", "Trail14", "IslandCave", "ColdHarbor", "Trail15", "Trail16", "Trail16_Cave", "AbandonedMine", "Trail17", "Trail18", "Trail19", "Trail20", "Trail21", "SpiritPassage", "Trail22", "Trail22_Cave", ]

water_loc = ["Trail10", "Trail11", "Trail12", "Trail13", "Trail14", "ColdHarbor", "Trail16", "AbandonedMine", "Trail17", "Trail18", "Trail21", ]

default_grass_loc = {
    "Trail1": ["Petunia", "Beebee", "Slimee"],
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
    "IslandCave": ["Amazona", "Harpie", "Twerqueen", "Arachna", "Succubae"],
    "ColdHarbor": ["Harpie", "Pinchie", "Gangfang", "Octomommy", "Snowbae"],
    "Trail15": ["Archna", "Gangfang", "Octomommy", "Snowbae", "Polaria", "Deardeer"],
    "Trail16": ["Gangfang", "Polaria", "Octomommy", "Snowbae", "Deardeer", "Slithereen"],
    "Trail16_Cave": ["Valkyrie_Normal"],
    "AbandonedMine": ["Gangfang", "Polaria", "Slithereen", "Deardeer", "Slushie"],
    "Trail17": ["Slithereen", "Deardeer", "Slushie", "Queenbee", "Boobarella"],
    "Trail18": ["Slushie", "Slithereen", "Queenbee", "Boobarella", "Panthera"],
    "Trail19": ["Queenbee", "Deardeer", "Panthera", "Unihorn", "Fungie"],
    "Trail20": ["Queenbee", "Unihorn", "Fungie", "Juggsie", "Serphina"],
    "Trail21": ["Queenbee", "Fungie", "Juggsie", "Serphina"],
    "SpiritPassage": ["Slithereen", "Octomommy", "Fungie", "Dominatrix"],
    "Trail22": ["Unihorn", "Juggsie", "Seraphina", "Dominatrix"],
    "Trail22_Cave": ["Centiboob_Normal"],
}

default_water_loc = {
    "Trail10": ["Marinel", "Pinchie"],
    "Trail11": ["Sharky", "Marinel"],
    "Trail12": ["Marinel", "Pinchie", "Chocostar", "Octocunt"],
    "Trail13": ["Jellygal", "Sharky", "Chocostar"],
    "Trail14": ["Marinel", "Jellygal", "Sharky"],
    "ColdHarbor": ["Chocostar", "Pinchie"],
    "Trail16": ["Jawsy"],
    "AbandonedMine": ["Jawsy", "Jellybish"],
    "Trail17": ["Jellybish", "Jawsy"],
    "Trail18": ["Jellybish", "Jawsy"],
    "Trail21": ["Jellybish", "Lizzie"],
}


def rand_spirit_list(moves, nummoves, evo, stype, base, random) -> list[str]:
    outlist = {}
    for s in obtainable_spirit_list:
        if moves:
            m = {}
            first = random.choice(attacking_moves)  # make sure all spirits have an attacking move
            moves = all_moves.copy()
            moves.remove(first)
            rest = random.sample(moves, (nummoves - 1))

            levelgap = 45 // nummoves
            lv = 1 + levelgap

            m[first] = 1
            for mov in rest:
                m[mov] = lv
                lv = lv + levelgap
        else:
            m = spirit_data[s].moves

        if evo:
            if random.choice(range(0, 100)) < 50:
                e = None
            else:
                tmpspirits = obtainable_spirit_list.copy()
                tmpspirits.remove(s)
                e = {random.choice(tmpspirits): random.choice(range(10, 40))}
        else:
            e = spirit_data[s].evolution

        if stype:
            t = random.choice(types)
        else:
            t = spirit_data[s].type

        if base:
            b = {"HP": random.choice(range(80, 200)), "STA": random.choice(range(80, 200)), "ATT": random.choice(range(80, 200)), "DEF": random.choice(range(80, 200)), "SPE": random.choice(range(80, 200))}
        else:
            b = spirit_data[s].base_stats

        outlist[s] = SpiritData(m, e, t, b)

    for boss in boss_list:
        outlist[boss] = spirit_data[boss]

    return [f"{{name:'{s}',{outlist[s]}}}" for s in outlist]


def rand_type_chart(random) -> dict[str, dict[str, int]]:
    chart = {}

    for t in types:
        c = {}
        for t2 in types:
            c[t2] = random.choice(range(-1, 2))
        chart[t] = c

    return chart


def rand_grass_spawn(slots, random) -> dict[str, list[str]]:
    grassout = {}
    for g in grass_loc:
        grassout[g] = []
    tmp_loc = grass_loc.copy()
    for s in obtainable_spirit_list:
        m = random.choice(tmp_loc)
        grassout[m].append(s)
        if len(grassout[m]) == slots:
            tmp_loc.remove(m)

    for t in tmp_loc:
        tmp_spirit = [s for s in obtainable_spirit_list if s not in grassout[t]]
        for i in random.sample(tmp_spirit, slots - len(grassout[t])):
            grassout[t].append(i)

    return grassout


def rand_water_spawn(slots, random) -> dict[str, list[str]]:
    waterout = {}

    for w in water_loc:
        waterout[w] = random.sample(obtainable_spirit_list, slots)

    return waterout

def rand_move_data(random) -> dict[str, dict]:
    output = move_data.copy()
    for move in all_moves:
        if move in attacking_moves:
            pow = random.choice(range(70))
        else:
            if random.choice([0,1,1,1,1,1,1,1]) == 0:
                pow = random.choice(range(70))
            else:
                pow = 0

        acc = min(random.choice(range(79,131)),100)
        sta = random.choice(range(2,16))
        typ = random.choice([*types, None])
        pri = random.choice([1,2,3])
        output[move] = {"Power": pow, "Accuracy": acc, "Stamina": sta, "Type": typ, "Priority": pri}
    return output