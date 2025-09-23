from dataclasses import dataclass

from Options import Range, Toggle, PerGameCommonOptions


class Randomise_Spawns(Toggle):
    """randomise the spawns in the grass/water"""
    display_name = "Randomise Spawns"
    default = True

class Grass_slots(Range):
    """number of spirit slots in the grass"""
    display_name = "Grass Slots"
    range_start = 3
    range_end = 15
    default = 5

class Water_slots(Range):
    """number of spirit slots in the water"""
    display_name = "Water Slots"
    range_start = 1
    range_end = 15
    default = 5



class Randomise_Enemies(Toggle):
    """randomise the enemies team of spirits"""
    display_name = "Randomise Enemies"
    default = True



class Randomise_Spirit_Moves(Toggle):
    """randomise moves learned by spirits"""
    display_name = "Randomise Spirit Moves"
    default = True

class Randomise_Spirit_Moves_Amount(Range):
    """number of move to randomise on to spirits"""
    display_name = "Random Spirit Moves Amount"
    range_start = 5
    range_end = 40
    default = 10

class Randomise_Spirit_Evo(Toggle):
    """randomise Evolution for spirits"""
    display_name = "Randomise Spirit Evo"
    default = True

class Randomise_Spirit_Type(Toggle):
    """randomise Type for spirits"""
    display_name = "Randomise Spirit Type"
    default = True

class Randomise_Spirit_Stats(Toggle):
    """randomise stats for spirits"""
    display_name = "Randomise Spirit Stats"
    default = True



class Randomise_Type_Effective(Toggle):
    """randomise Type effectiveness"""
    display_name = "Randomise Type Effectiveness"
    default = True


class Spirit_Locations(Toggle):
    """have catch/obtaining/affection lv for spirits as locations"""
    display_name = "Spirits locations"
    default = True

class Rare_Locations(Toggle):
    """have catch/obtaining rare spirits as locations requires spirit locations to be true"""
    display_name = "Rare Spirits"
    default = True

class Spirit_Obtain_progression(Toggle):
    """Stop Progression Items being behind Spirit Obtain Locations"""
    display_name = "Spirit Obtain Progression"
    default = False

class Rare_Spirit_Obtain_progression(Toggle):
    """Stop Progression Items being behind Rare Spirit Obtain Locations"""
    display_name = "Rare Spirit Obtain Progression"
    default = True

class Spirit_Affection_progression(Toggle):
    """Stop Progression Items being behind Spirit Affection Locations"""
    display_name = "Spirit Affection Progression"
    default = True



class randomise_warps(Toggle):
    """add warp locations/items to the rando pool NOTE:CURRENTLY DOES NOTHING"""
    display_name = "warp rando"
    default = False

class Minigame_Cheat(Toggle):
    """set to enable cheat so minigame cant miss"""
    display_name = "minigame cheat"
    default = False

class Guaranteed_Catch(Toggle):
    """set to make sprit crystals catch guaranteed"""
    display_name = "minigame cheat"
    default = False





@dataclass
class SpiritValleyOptions(PerGameCommonOptions):
    Randomise_Spawns: Randomise_Spawns
    Grass_slots: Grass_slots
    Water_slots: Water_slots

    Randomise_Enemies: Randomise_Enemies

    Randomise_Spirit_Moves: Randomise_Spirit_Moves
    Randomise_Spirit_Moves_Amount: Randomise_Spirit_Moves_Amount
    Randomise_Spirit_Evo: Randomise_Spirit_Evo
    Randomise_Spirit_Type: Randomise_Spirit_Type
    Randomise_Spirit_Stats: Randomise_Spirit_Stats

    Randomise_Type_Effective: Randomise_Type_Effective

    Spirit_Locations: Spirit_Locations
    Rare_Locations: Rare_Locations
    Spirit_Obtain_progression:Spirit_Obtain_progression
    Rare_Spirit_Obtain_progression:Rare_Spirit_Obtain_progression
    Spirit_Affection_progression:Spirit_Affection_progression

    randomise_warps:randomise_warps
    Minigame_Cheat:Minigame_Cheat
    Guaranteed_Catch:Guaranteed_Catch
