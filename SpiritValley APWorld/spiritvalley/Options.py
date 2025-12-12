from dataclasses import dataclass

from Options import Range, Toggle, PerGameCommonOptions, Visibility, Choice


class Char_Gender(Choice):
    """Sets Character Gender in Game NOTE: you can change this by interacting the wardrobe in the house in oakwood village"""
    display_name = "Char Gender"
    option_male = 0
    option_female = 1
    default = 0

class Char_Skin(Range):
    """Sets Character Skin color in Game NOTE: you can change this by interacting the wardrobe in the house in oakwood village"""
    display_name = "Char Skin"
    range_start = 0
    range_end = 2
    default = 0
class Char_Hairstyle(Range):
    """Sets Character Hairstyle in Game NOTE: you can change this by interacting the wardrobe in the house in oakwood village"""
    display_name = "Char Hairstyle"
    range_start = 0
    range_end = 3
    default = 0
class Char_Haircolor(Range):
    """Sets Character Hair Color in Game NOTE: you can change this by interacting the wardrobe in the house in oakwood village
    NOTE 2: Male Chars only have 3 hair colors so if option 3 is selected it will be changed to option 2"""
    display_name = "Char Hair Color"
    range_start = 0
    range_end = 3
    default = 0
class Char_Outfit(Range):
    """Sets Character Outfit in Game NOTE: you can change this by interacting the wardrobe in the house in oakwood village"""
    display_name = "Char Outfit"
    range_start = 0
    range_end = 3
    default = 0






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

class Enemy_Vision(Toggle):
    """Enable/Disable Enemy Vision"""
    display_name = "Enemy Vision"
    default = True

class Enemy_Spin(Choice):
    """Sets whether Enemy's will stand sill, spin in a circle or randomly rotate"""
    display_name = "Enemy Spin"
    option_still = 0
    option_spin = 1
    option_rotate = 2
    default = 0


class Randomise_Spirit_Moves(Toggle):
    """randomise moves learned by spirits"""
    display_name = "Randomise Spirit Moves"
    default = False

class Randomise_Spirit_Moves_Amount(Range):
    """number of move to randomise on to spirits"""
    display_name = "Random Spirit Moves Amount"
    range_start = 5
    range_end = 40
    default = 10

class Randomise_Spirit_Evo(Toggle):
    """randomise Evolution for spirits"""
    display_name = "Randomise Spirit Evo"
    default = False

class Randomise_Spirit_Type(Toggle):
    """randomise Type for spirits"""
    display_name = "Randomise Spirit Type"
    default = False

class Randomise_Spirit_Stats(Toggle):
    """randomise stats for spirits"""
    display_name = "Randomise Spirit Stats"
    default = False


class Randomise_Move_Data(Toggle):
    """randomise Move Data"""
    display_name = "Randomise Move Data"
    default = False


class Randomise_Type_Effective(Toggle):
    """randomise Type effectiveness"""
    display_name = "Randomise Type Effectiveness"
    default = False


class Spirit_Locations(Toggle):
    """have catch/obtaining spirits as locations"""
    display_name = "Spirits locations"
    default = True

class Spirit_Affection(Toggle):
    """have affection lv for spirits as locations requires spirit locations to be true"""
    display_name = "Spirits Affection"
    default = False

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



class randomise_map(Toggle):
    """randomise map"""
    display_name = "map rando"
    default = False

class randomise_map_option(Choice):
    """sets map rando option
    none (default) = no logic in how the map is connected
    some = exits that lead to dead ends will always lead to dead ends
    """
    display_name = "map rando option"
    option_none = 0
    option_some = 1
    default = 1

class randomise_warps(Toggle):
    """add warp locations/items to the rando pool"""
    display_name = "warp rando"
    default = True



class Minigame_Cheat(Toggle):
    """set to enable cheat so sex minigame cant miss"""
    display_name = "minigame cheat"
    default = False

class Guaranteed_Catch(Toggle):
    """set to make sprit crystals catch guaranteed"""
    display_name = "minigame cheat"
    default = False

class Xp_Modifer(Range):
    """Modifier to XP gained.
    0 -> no XP gained
    50 -> 1/2 XP gained
    100 -> XP not effected
    200 -> 2x XP gained"""
    display_name = "XP Modifier"
    range_start = 0
    range_end = 10000
    default = 100





@dataclass
class SpiritValleyOptions(PerGameCommonOptions):
    Char_Gender:Char_Gender
    Char_Skin:Char_Skin
    Char_Hairstyle:Char_Hairstyle
    Char_Haircolor:Char_Haircolor
    Char_Outfit:Char_Outfit

    Randomise_Spawns: Randomise_Spawns
    Grass_slots: Grass_slots
    Water_slots: Water_slots

    Randomise_Enemies: Randomise_Enemies
    Enemy_Vision:Enemy_Vision
    Enemy_Spin:Enemy_Spin

    Randomise_Spirit_Moves: Randomise_Spirit_Moves
    Randomise_Spirit_Moves_Amount: Randomise_Spirit_Moves_Amount
    Randomise_Spirit_Evo: Randomise_Spirit_Evo
    Randomise_Spirit_Type: Randomise_Spirit_Type
    Randomise_Spirit_Stats: Randomise_Spirit_Stats

    Randomise_Move_Data:Randomise_Move_Data

    Randomise_Type_Effective: Randomise_Type_Effective

    Spirit_Locations: Spirit_Locations
    Spirit_Affection: Spirit_Affection
    Rare_Locations: Rare_Locations
    Spirit_Obtain_progression:Spirit_Obtain_progression
    Rare_Spirit_Obtain_progression:Rare_Spirit_Obtain_progression
    Spirit_Affection_progression:Spirit_Affection_progression

    randomise_map:randomise_map
    randomise_map_option:randomise_map_option
    randomise_warps:randomise_warps

    Minigame_Cheat:Minigame_Cheat
    Guaranteed_Catch:Guaranteed_Catch
    Xp_Modifer:Xp_Modifer
