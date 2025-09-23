import random


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
    #attack:{defending:(1=effective, 0=neutral, -1=resit)}
    #TODO aquatic
    "Furry":{"Furry": 0, "Lust": 0, "Plant": 0, "Demon": 0, "Scalie": 0, "Slime": -1, "Oppai": 0, "Avian": 1, "Aquatic": 1},
    "Lust":{"Furry": 0, "Lust": 0, "Plant": 0, "Demon": -1, "Scalie": 0, "Slime": 1, "Oppai": 1, "Avian": -1, "Aquatic": 0},
    "Plant":{"Furry": 0, "Lust": 0, "Plant": 0, "Demon": 0, "Scalie": -1, "Slime": 1, "Oppai": 0, "Avian": 0, "Aquatic": -1},
    "Demon":{"Furry": -1, "Lust": 0, "Plant": 1, "Demon": 0, "Scalie": 0, "Slime": 0, "Oppai": 0, "Avian": 0, "Aquatic": 0},
    "Scalie":{"Furry": 1, "Lust": 0, "Plant": 0, "Demon": 0, "Scalie": 0, "Slime": 0, "Oppai": -1, "Avian": 0, "Aquatic": 0},
    "Slime":{"Furry": 0, "Lust": -1, "Plant": 0, "Demon": 1, "Scalie": 0, "Slime": 0, "Oppai": 0, "Avian": 0, "Aquatic": 0},
    "Oppai":{"Furry": 0, "Lust": 1, "Plant": -1, "Demon": 0, "Scalie": 0, "Slime": 0, "Oppai": 0, "Avian": 0, "Aquatic": 0},
    "Avian":{"Furry": 0, "Lust": 0, "Plant": 1, "Demon": -1, "Scalie": 1, "Slime": -1, "Oppai": 0, "Avian": 0, "Aquatic": 0},
    "Aquatic":{"Furry": 0, "Lust": 0, "Plant": 0, "Demon": 1, "Scalie": 0, "Slime": -1, "Oppai": 0, "Avian": 0, "Aquatic": 0},
}

spirit_list = ["Amazona","Arachna","Bearboo","Beebee","Belle","Bellend","Birdy","Boobae","Boobarella","Bovina","Bunni","Buzzeena","Cactee","Centiboob_Boss","Centiboob","Chocostar","Chubbie","Deardeer","Domina","Dominatrix","Dracoomer","Dripsy","EV-3","Faerie","Flora","Fungie","Gangfang","Gloreen","Gloria","Growleen","Harlie","Harpie","Hornie","Jawsy","Jellybish","Jellygal","Juggsie","Kittypus","Lacteena","Lizzie","Mamaoak","Marinel","Megaboob","Oakie","Octocunt","Octomommy","Octopussy","Panthera","Petunia","Pinchie","Polaria","Pusseen","Queenbee","Rawry","Seraphina","Serpentax","Serpentina","Sexybun","Sharky","Slimee","Slithereen","Slushie","Snowbae","Spinnie","Succubae","Thiccsie","Tinky","Triboobe","Trissy","Twerky","Twerqueen","Udderella","Unihorn","Ursie","Valkyrie_Boss","Valkyrie","Wolfy","SpiritMother",]
boss_list = ["Centiboob_Boss","Valkyrie_Boss","SpiritMother"]
obtainable_spirit_list = ["Amazona","Arachna","Bearboo","Beebee","Belle","Bellend","Birdy","Boobae","Boobarella","Bovina","Bunni","Buzzeena","Cactee","Centiboob","Chocostar","Chubbie","Deardeer","Domina","Dominatrix","Dracoomer","Dripsy","EV-3","Faerie","Flora","Fungie","Gangfang","Gloreen","Gloria","Growleen","Harlie","Harpie","Hornie","Jawsy","Jellybish","Jellygal","Juggsie","Kittypus","Lacteena","Lizzie","Mamaoak","Marinel","Megaboob","Oakie","Octocunt","Octomommy","Octopussy","Panthera","Petunia","Pinchie","Polaria","Pusseen","Queenbee","Rawry","Seraphina","Serpentax","Serpentina","Sexybun","Sharky","Slimee","Slithereen","Slushie","Snowbae","Spinnie","Succubae","Thiccsie","Tinky","Triboobe","Trissy","Twerky","Twerqueen","Udderella","Unihorn","Ursie","Valkyrie","Wolfy",]

spirit_data = {
    "Amazona": SpiritData({"BitchSlap": 1, "MostMuscular": 3, "WarCry": 10, "PowerPunch": 16, "NippleClamp": 23, "Domination": 28, "ToeStrike": 33, "DonkeyPunch": 38, }, None, "Lust", {"HP": 120, "STA": 100, "ATT": 135, "DEF": 110, "SPE": 95}),
    "Arachna": SpiritData({"Bite": 1, "BindingWeb": 3, "Meditate": 7, "Curse": 10, "Fisting": 13, "Hypnosis": 15, "PoisonBite": 20, "LitanyOfCurses": 25, "NippleClamp": 30, }, None, "Demon", {"HP": 115, "STA": 100, "ATT": 140, "DEF": 105, "SPE": 115}),
    "Bearboo": SpiritData({"BitchSlap": 1, "SexyPose": 3, "Lacerate": 7, "Growl": 10, "BearHug": 14, "BoobPounding": 17, "SharpenClaws": 22, "ExtremeFisting": 26, "CleansingSlap": 30, "PowerPunch": 36, }, {"Polaria": 26}, "Furry", {"HP": 135, "STA": 100, "ATT": 120, "DEF": 125, "SPE": 105}),
    "Beebee": SpiritData({"Sting": 1, "Buzz": 3, "HappyThoughts": 6, "Fisting": 9, "BlowKiss": 14, "BeeSwarm": 18, "LethalSting": 28, "PoisonBlitz": 34, "EyePoke": 38, "Domination": 42, }, {"Buzzeena": 10}, "Avian", {"HP": 100, "STA": 100, "ATT": 125, "DEF": 100, "SPE": 110}),
    "Belle": SpiritData({"LeafBlast": 1, "Seduce": 3, "Photosynthesis": 6, "TeamChant": 10, "PoisonSquirt": 13, "FlowerPower": 17, "HappyThoughts": 20, "SeedOfLife": 24, "NaturesMight": 29, }, {"Bellend": 11}, "Plant", {"HP": 110, "STA": 100, "ATT": 115, "DEF": 100, "SPE": 130}),
    "Bellend": SpiritData({"LeafBlast": 1, "Seduce": 3, "Photosynthesis": 6, "TeamChant": 10, "PoisonSquirt": 13, "FlowerPower": 17, "HappyThoughts": 20, "SeedOfLife": 24, "NaturesMight": 29, }, None, "Plant", {"HP": 115, "STA": 100, "ATT": 120, "DEF": 102, "SPE": 135}),
    "Birdy": SpiritData({"Meditate": 1, "Swoop": 3, "BitchSlap": 6, "Hypnosis": 10, "Stretch": 14, "Rimjob": 18, "Yoga": 22, "ExtremeFisting": 27, "GoldenRain": 32, }, {"Harpie": 22}, "Avian", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
    "Boobae": SpiritData({"Slam": 1, "BoobJiggle": 3, "BreastMassage": 5, "BoobPounding": 7, "FreshMilk": 13, "MilkStorm": 18, "Flirt": 22, "BoobSlam": 26, "MassSeduction": 31, "CleansingSlap": 37, }, {"Megaboob": 14}, "Oppai", {"HP": 145, "STA": 100, "ATT": 120, "DEF": 135, "SPE": 100}),
    "Boobarella": SpiritData({"Slam": 1, "BoobJiggle": 3, "BreastMassage": 5, "BoobPounding": 7, "FreshMilk": 13, "MilkStorm": 18, "Flirt": 22, "BoobSlam": 26, "MassSeduction": 31, "CleansingSlap": 37, }, None, "Oppai", {"HP": 155, "STA": 100, "ATT": 125, "DEF": 145, "SPE": 105}),
    "Bovina": SpiritData({"FreshMilk": 1, "Bite": 3, "BoobSlam": 6, "BlowKiss": 10, "BreastMassage": 13, "HappyThoughts": 15, "Smother": 20, "MilkStorm": 24, "CurePoison": 29, }, {"Udderella": 21}, "Oppai", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
    "Bunni": SpiritData({"Scratch": 1, "SwiftPaws": 3, "Pounce": 6, "Flirt": 9, "Bite": 14, "Stretch": 18, "PawStrike": 21, "ScentSpray": 25, "NaturesMight": 31, }, {"Sexybun": 19}, "Furry", {"HP": 90, "STA": 100, "ATT": 110, "DEF": 95, "SPE": 145}),
    "Buzzeena": SpiritData({"Sting": 1, "Buzz": 3, "HappyThoughts": 6, "Fisting": 9, "BlowKiss": 14, "BeeSwarm": 18, "LethalSting": 28, "PoisonBlitz": 34, "EyePoke": 38, "Domination": 42, }, {"Queenbee": 29}, "Avian", {"HP": 105, "STA": 100, "ATT": 130, "DEF": 105, "SPE": 115}),
    "Cactee": SpiritData({"Slam": 1, "ThornStrike": 3, "FlowerPower": 7, "Fisting": 11, "CoatOfSpikes": 14, "Strangle": 17, "Photosynthesis": 21, "SeedOfLife": 25, "EyePoke": 29, }, None, "Plant", {"HP": 110, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
    "Centiboob_Boss": SpiritData({"KillerInstinct": 1, "PoisonBite": 1, "BoobSlam": 1, "Lactate": 1, "Hypnosis": 1, "LitanyOfCurses": 1, }, None, "Oppai", {"HP": 420, "STA": 100, "ATT": 145, "DEF": 160, "SPE": 145}),
    "Centiboob": SpiritData({"KillerInstinct": 1, "PoisonBite": 3, "BoobSlam": 6, "Lactate": 16, "Hypnosis": 22, "LitanyOfCurses": 28, "BreastMassage": 36, }, None, "Oppai", {"HP": 140, "STA": 100, "ATT": 135, "DEF": 135, "SPE": 135}),
    "Chocostar": SpiritData({"BlowBubbles": 1, "Twerk": 3, "Starfall": 10, "TeamChant": 17, "NastyBubbles": 22, "MiracleCure": 25, "FishyBusiness": 30, "SexyPose": 36, }, None, "Aquatic", {"HP": 110, "STA": 100, "ATT": 110, "DEF": 125, "SPE": 110}),
    "Chubbie": SpiritData({"Slam": 1, "PoisonSlime": 3, "Yoga": 8, "SlimeRain": 12, "BoobJiggle": 15, "BoobPounding": 20, "SlimeArmor": 27, "Lubrication": 32, "Smother": 37, }, {"Thiccsie": 16}, "Slime", {"HP": 120, "STA": 100, "ATT": 100, "DEF": 125, "SPE": 90}),
    "Deardeer": SpiritData({"Snowballing": 1, "NaturesMight": 3, "Stretch": 6, "ScentSpray": 14, "YellowSnow": 19, "MiracleCure": 26, "AntlerAssault": 30, "SeedOfLife": 37, }, None, "Furry", {"HP": 110, "STA": 100, "ATT": 120, "DEF": 110, "SPE": 120}),
    "Domina": SpiritData({"Bite": 1, "BitchSlap": 3, "SexyPose": 8, "Strangle": 11, "Domination": 15, "GoldenShower": 18, "MassSeduction": 23, "ExtremeFisting": 27, "GoldenRain": 32, }, {"Dominatrix": 35}, "Lust", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
    "Dominatrix": SpiritData({"Bite": 1, "BitchSlap": 3, "SexyPose": 8, "Strangle": 11, "Domination": 15, "GoldenShower": 18, "MassSeduction": 23, "ExtremeFisting": 27, "GoldenRain": 32, }, None, "Lust", {"HP": 135, "STA": 100, "ATT": 125, "DEF": 100, "SPE": 110}),
    "Dracoomer": SpiritData({"PoisonBite": 1, "Scratch": 3, "HardenScales": 7, "Yoga": 11, "Lacerate": 16, "SerpentsTongue": 19, "TeamChant": 23, "PoisonSpit": 27, "AcidSquirt": 33, }, None, "Scalie", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
    "Dripsy": SpiritData({"Slam": 1, "SlimeRain": 3, "SlimeArmor": 8, "Yoga": 12, "Lubrication": 15, "SlimeSquirt": 19, "TeamChant": 31, "SlimeTentacle": 36, "BitchSlap": 40, }, None, "Slime", {"HP": 100, "STA": 100, "ATT": 115, "DEF": 100, "SPE": 105}),
    "EV-3": SpiritData({"Suck": 1, "BreastMassage": 3, "NaughtyTentacles": 9, "BeeSwarm": 14, "SlimeSquirt": 17, "Strangle": 24, "PawStrike": 32, "BlowBubbles": 36, "SerpentsTongue": 40, }, None, "Lust", {"HP": 130, "STA": 100, "ATT": 130, "DEF": 130, "SPE": 130}),
    "Faerie": SpiritData({"Swoop": 1, "Flirt": 3, "CockFlurry": 8, "Suck": 12, "TeamChant": 15, "CumRain": 20, "PoisonBlitz": 25, "BlowKiss": 31, "AirStrike": 38, }, None, "Avian", {"HP": 105, "STA": 100, "ATT": 105, "DEF": 110, "SPE": 110}),
    "Flora": SpiritData({"Lash": 1, "LeafBlast": 3, "SeedOfLife": 7, "Meditate": 11, "FlowerPower": 15, "Flirt": 19, "BoobPounding": 31, "ThornStrike": 35, "CurePoison": 39, }, None, "Plant", {"HP": 90, "STA": 100, "ATT": 115, "DEF": 95, "SPE": 115}),
    "Fungie": SpiritData({"Lash": 1, "PoisonSquirt": 3, "Shrooms": 8, "Strangle": 14, "RootBondage": 20, "EyePoke": 31, "VaginalFungus": 38, }, None, "Plant", {"HP": 95, "STA": 100, "ATT": 115, "DEF": 110, "SPE": 105}),
    "Gangfang": SpiritData({"Pounce": 1, "Bite": 3, "Growl": 6, "DoggyStyle": 12, "Howl": 16, "Stretch": 20, "ScentSpray": 25, "PawStrike": 31, "PawStorm": 38, }, None, "Furry", {"HP": 120, "STA": 100, "ATT": 125, "DEF": 120, "SPE": 110}),
    "Gloreen": SpiritData({"Suck": 1, "Slam": 3, "Rimjob": 7, "HappyThoughts": 11, "BlowKiss": 15, "Lubrication": 20, "Meditate": 25, "MassSeduction": 31, "SirenSong": 38, }, None, "Lust", {"HP": 115, "STA": 100, "ATT": 105, "DEF": 125, "SPE": 105}),
    "Gloria": SpiritData({"Suck": 1, "Slam": 3, "Rimjob": 7, "HappyThoughts": 11, "BlowKiss": 15, "Lubrication": 20, "Meditate": 25, "MassSeduction": 31, "SirenSong": 38, }, {"Gloreen": 11}, "Lust", {"HP": 110, "STA": 100, "ATT": 115, "DEF": 115, "SPE": 105}),
    "Growleen": SpiritData({"Pounce": 1, "Bite": 3, "Growl": 6, "DoggyStyle": 12, "Howl": 16, "Stretch": 20, "ScentSpray": 25, "PawStrike": 31, "PawStorm": 38, }, {"Gangfang": 25}, "Furry", {"HP": 115, "STA": 100, "ATT": 120, "DEF": 120, "SPE": 110}),
    "Harlie": SpiritData({"CockBlast": 1, "HappyThoughts": 3, "CockFlurry": 7, "Stretch": 13, "Fisting": 16, "SexyPose": 20, "Rimjob": 25, "CumRain": 29, "ToeStrike": 34, }, None, "Lust", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
    "Harpie": SpiritData({"Meditate": 1, "Swoop": 3, "BitchSlap": 6, "Hypnosis": 10, "Stretch": 14, "Rimjob": 18, "Yoga": 22, "ExtremeFisting": 27, "GoldenRain": 32, }, None, "Avian", {"HP": 105, "STA": 100, "ATT": 105, "DEF": 110, "SPE": 105}),
    "Hornie": SpiritData({"Fisting": 1, "Hypnosis": 3, "Curse": 8, "Rimjob": 12, "LitanyOfCurses": 15, "GoldenShower": 18, "ExtremeFisting": 29, "MassSeduction": 34, "DonkeyPunch": 40, }, {"Succubae": 23}, "Demon", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
    "Jawsy": SpiritData({"Chomp": 1, "KillerInstinct": 3, "Slam": 10, "TailSwipe": 19, "MostMuscular": 22, "FishyBusiness": 26, "Domination": 30, "NippleClamp": 36, }, None, "Aquatic", {"HP": 120, "STA": 100, "ATT": 155, "DEF": 100, "SPE": 135}),
    "Jellybish": SpiritData({"StingingTentacles": 1, "WaterSpray": 3, "CurePoison": 10, "SlimeArmor": 15, "SlimeSquirt": 20, "JellyfishSwarm": 26, "TentacleDrain": 31, "NaughtyTentacles": 37, }, None, "Aquatic", {"HP": 100, "STA": 100, "ATT": 120, "DEF": 115, "SPE": 100}),
    "Jellygal": SpiritData({"StingingTentacles": 1, "WaterSpray": 3, "CurePoison": 10, "SlimeArmor": 15, "SlimeSquirt": 20, "JellyfishSwarm": 26, "TentacleDrain": 31, "NaughtyTentacles": 37, }, {"Jellybish": 28}, "Aquatic", {"HP": 100, "STA": 100, "ATT": 115, "DEF": 110, "SPE": 100}),
    "Juggsie": SpiritData({"BitchSlap": 1, "Lactate": 3, "FreshMilk": 5, "BoobPounding": 9, "TeamChant": 12, "Smother": 17, "MilkStorm": 22, "Titillate": 28, "Starfall": 33, }, None, "Oppai", {"HP": 120, "STA": 100, "ATT": 110, "DEF": 120, "SPE": 100}),
    "Kittypus": SpiritData({"Scratch": 1, "ScentSpray": 3, "PawStrike": 5, "Purr": 10, "Lacerate": 14, "SharpenClaws": 17, "BlowKiss": 21, "TailSwipe": 25, "PawStorm": 30, "KillerInstinct": 36, }, {"Panthera": 30}, "Furry", {"HP": 115, "STA": 100, "ATT": 155, "DEF": 105, "SPE": 140}),
    "Lacteena": SpiritData({"BitchSlap": 1, "Lactate": 3, "FreshMilk": 5, "BoobPounding": 9, "TeamChant": 12, "Smother": 17, "MilkStorm": 22, "Titillate": 28, "Starfall": 33, }, {"Juggsie": 36}, "Oppai", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
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
    "Rawry": SpiritData({"PoisonBite": 1, "Scratch": 3, "HardenScales": 7, "Yoga": 11, "Lacerate": 16, "SerpentsTongue": 19, "TeamChant": 23, "PoisonSpit": 27, "AcidSquirt": 33, }, {"Dracoomer": 14}, "Scalie", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
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
    "Succubae": SpiritData({"Fisting": 1, "Hypnosis": 3, "Curse": 8, "Rimjob": 12, "LitanyOfCurses": 15, "GoldenShower": 18, "ExtremeFisting": 29, "MassSeduction": 34, "DonkeyPunch": 40, }, None, "Demon", {"HP": 110, "STA": 100, "ATT": 105, "DEF": 110, "SPE": 105}),
    "Thiccsie": SpiritData({"Slam": 1, "PoisonSlime": 3, "Yoga": 8, "SlimeRain": 12, "BoobJiggle": 15, "BoobPounding": 20, "SlimeArmor": 27, "Lubrication": 32, "Smother": 37, }, None, "Slime", {"HP": 125, "STA": 100, "ATT": 105, "DEF": 130, "SPE": 95}),
    "Tinky": SpiritData({"Swoop": 1, "Flirt": 3, "CockFlurry": 8, "Suck": 12, "TeamChant": 15, "CumRain": 20, "PoisonBlitz": 25, "BlowKiss": 31, "AirStrike": 38, }, {"Faerie": 21}, "Avian", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
    "Triboobe": SpiritData({"BitchSlap": 1, "Lactate": 3, "Titillate": 7, "Squirt": 11, "BoobJiggle": 14, "Smother": 18, "ExtremeFisting": 27, "TeamChant": 33, "ToeStrike": 40, }, None, "Oppai", {"HP": 105, "STA": 100, "ATT": 115, "DEF": 115, "SPE": 115}),
    "Trissy": SpiritData({"BitchSlap": 1, "Lactate": 3, "Titillate": 7, "Squirt": 11, "BoobJiggle": 14, "Smother": 18, "ExtremeFisting": 27, "TeamChant": 33, "ToeStrike": 40, }, {"Triboobe": 13}, "Oppai", {"HP": 100, "STA": 100, "ATT": 110, "DEF": 110, "SPE": 110}),
    "Twerky": SpiritData({"Suck": 1, "Scratch": 3, "Squirt": 8, "Stretch": 12, "Twerk": 16, "Rimjob": 20, "GoldenShower": 24, "MassSeduction": 28, "Scissoring": 33, }, {"Twerqueen": 21}, "Lust", {"HP": 100, "STA": 100, "ATT": 100, "DEF": 100, "SPE": 100}),
    "Twerqueen": SpiritData({"Suck": 1, "Scratch": 3, "Squirt": 8, "Stretch": 12, "Twerk": 16, "Rimjob": 20, "GoldenShower": 24, "MassSeduction": 28, "Scissoring": 33, }, None, "Lust", {"HP": 105, "STA": 100, "ATT": 110, "DEF": 100, "SPE": 105}),
    "Udderella": SpiritData({"FreshMilk": 1, "Bite": 3, "BoobSlam": 6, "BlowKiss": 10, "BreastMassage": 13, "HappyThoughts": 15, "Smother": 20, "MilkStorm": 24, "CurePoison": 29, }, None, "Oppai", {"HP": 110, "STA": 100, "ATT": 105, "DEF": 105, "SPE": 110}),
    "Unihorn": SpiritData({"Bite": 1, "TailSwipe": 3, "ScentSpray": 9, "NaturesMight": 15, "CleansingSlap": 25, "TeamChant": 30, "DonkeyPunch": 37, }, None, "Furry", {"HP": 105, "STA": 100, "ATT": 120, "DEF": 100, "SPE": 130}),
    "Ursie": SpiritData({"BitchSlap": 1, "SexyPose": 3, "Lacerate": 7, "Growl": 10, "BearHug": 14, "BoobPounding": 17, "SharpenClaws": 22, "ExtremeFisting": 26, "CleansingSlap": 30, "PowerPunch": 36, }, {"Bearboo": 12}, "Furry", {"HP": 130, "STA": 100, "ATT": 115, "DEF": 120, "SPE": 100}),
    "Valkyrie_Boss": SpiritData({"CockFlurry": 1, "CockBlast": 1, "CumRain": 1, "BoobSlam": 1, "BreastMassage": 1, }, None, "Lust", {"HP": 300, "STA": 100, "ATT": 170, "DEF": 170, "SPE": 115}),
    "Valkyrie": SpiritData({"CockFlurry": 1, "CockBlast": 3, "CumRain": 10, "BoobSlam": 15, "BreastMassage": 22, "CleansingSlap": 27, "MilkStorm": 33, "DonkeyPunch": 38, }, None, "Lust", {"HP": 145, "STA": 100, "ATT": 125, "DEF": 145, "SPE": 115}),
    "Wolfy": SpiritData({"Pounce": 1, "Bite": 3, "Growl": 6, "DoggyStyle": 12, "Howl": 16, "Stretch": 20, "ScentSpray": 25, "PawStrike": 31, "PawStorm": 38, }, {"Growleen": 15}, "Furry", {"HP": 110, "STA": 100, "ATT": 115, "DEF": 115, "SPE": 105}),
    "SpiritMother": SpiritData({"Strangle": 1, "PoisonSquirt": 1, "NaturesMight": 1, "CleansingSlap": 1, "DonkeyPunch": 1, "MassSeduction": 1, }, None, "Plant", {"HP": 460, "STA": 100, "ATT": 155, "DEF": 160, "SPE": 130}),
}

attacking_moves = ["BitchSlap","PowerPunch","NippleClamp","ToeStrike","DonkeyPunch","Bite","Fisting","PoisonBite","Lacerate","BearHug","BoobPounding","ExtremeFisting","CleansingSlap","Sting","BeeSwarm","LethalSting","EyePoke","LeafBlast","Swoop","Rimjob","Slam","BreastMassage","BoobSlam","Smother","Scratch","Pounce","PawStrike","ThornStrike","Strangle","BlowBubbles","Starfall","NastyBubbles","SlimeRain","Snowballing","YellowSnow","AntlerAssault","GoldenShower","AcidSquirt","SlimeSquirt","SlimeTentacle","Suck","NaughtyTentacles","CockFlurry","AirStrike","Lash","DoggyStyle","PawStorm","CockBlast","Chomp","TailSwipe","WaterSpray","JellyfishSwarm","TentacleDrain","TentacleTrash","ClawFlurry","HailStorm","Squirt","Scissoring",]
non_attack_moves = ["MostMuscular","WarCry","Domination","BindingWeb","Meditate","Curse","Hypnosis","LitanyOfCurses","SexyPose","Growl","SharpenClaws","Buzz","HappyThoughts","BlowKiss","PoisonBlitz","Seduce","Photosynthesis","TeamChant","PoisonSquirt","FlowerPower","SeedOfLife","NaturesMight","Stretch","Yoga","GoldenRain","BoobJiggle","FreshMilk","MilkStorm","Flirt","MassSeduction","CurePoison","SwiftPaws","ScentSpray","CoatOfSpikes","KillerInstinct","Lactate","Twerk","MiracleCure","FishyBusiness","PoisonSlime","SlimeArmor","Lubrication","HardenScales","SerpentsTongue","PoisonSpit","CumRain","Shrooms","RootBondage","VaginalFungus","Howl","SirenSong","StingingTentacles","Titillate","Purr","CleansingWaters","Crabs","Slither","FrostArmor",]
all_moves = [*non_attack_moves, *attacking_moves]

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


def rand_spirit_list(moves, nummoves, evo, stype, base) -> list[str]:
    outlist = {}
    for s in obtainable_spirit_list:
        if moves:
            m={}
            first = random.choice(attacking_moves) #make sure all spirits have an attacking move
            moves = all_moves.copy()
            moves.remove(first)
            rest = random.sample(moves,(nummoves-1))

            levelgap = 45//nummoves
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

        outlist[s] = SpiritData(m,e,t,b)

    for boss in boss_list:
        outlist[boss] = spirit_data[boss]

    return [f"{{name:'{s}',{outlist[s]}}}" for s in outlist]

def rand_type_chart() -> dict[str, dict[str,int]]:
    chart = {}

    for t in types:
        c = {}
        for t2 in types:
            c[t2] = random.choice(range(-1,2))
        chart[t] = c

    return chart

def rand_grass_spawn(slots) -> dict[str, list[str]]:
    grassout = {}
    for g in grass_location_list:
        grassout[g] = []
    tmp_loc = grass_location_list.copy()
    for s in obtainable_spirit_list:
        m = random.choice(tmp_loc)
        grassout[m].append(s)
        if len(grassout[m])==slots:
            tmp_loc.remove(m)

    for t in tmp_loc:
        tmp_spirit = [s for s in obtainable_spirit_list if s not in grassout[t]]
        for i in random.sample(tmp_spirit, slots-len(grassout[t])):
            grassout[t].append(i)

    return grassout

def rand_water_spawn(slots) -> dict[str, list[str]]:
    waterout = {}

    for w in water_location_list:
        waterout[w] = random.sample(obtainable_spirit_list, slots)

    return waterout