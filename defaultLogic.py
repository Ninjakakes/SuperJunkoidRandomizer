from typing import ClassVar

from item import items_unpackable, Items
from loadout import Loadout
from logicInterface import LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

(
    MagicBolt, Baseball, Sparksuit, RatCloak, WaveBangle, RatBurst, Feather, PurpleLocket, SanguineFin, BloodGem, RatDasher, IceGem, DreamersCrown, StormsGem, Wallkicks, DeathGem, MagicBroom, Heart, LuckyFrog, MagicSoap
) = items_unpackable

location_logic: LocationLogicType = {
    "Hidden Rat Tunnel Magic Bolt": lambda loadout: (
        True
    ),
    "Hidden Pipe Heart": lambda loadout: (
        True
    ),
    "Pipe Maze Heart": lambda loadout: (
        True
    ),
    "Ceiling Baseballs": lambda loadout: (
        True
    ),
    "Wall Jump Climb Magic Bolt": lambda loadout: (
        True
    ),
    "Outskirts Baseball Alter": lambda loadout: (
        True
    ),
    "Hidden Heart": lambda loadout: (
        True
    ),
    "Under Spider Magic Bolt": lambda loadout: (
        True
    ),
    "Hidden Underwater Heart": lambda loadout: (
        True
    ),
    "Feather": lambda loadout: (
        True
    ),
    "Rat Cloak": lambda loadout: (
        True
    ),
    "Rat Burst": lambda loadout: (
        True
    ),
    "Outside Idol Sparksuit": lambda loadout: (
        True
    ),
    "Wallkicks": lambda loadout: (
        True
    ),
    "Left Shaft Heart": lambda loadout: (
        True
    ),
    "Right Shaft Heart": lambda loadout: (
        True
    ),
    "Wave Bangle": lambda loadout: (
        True
    ),
    "Left Idol Magic Bolt": lambda loadout: (
        True
    ),
    "Hidden Shaft Heart": lambda loadout: (
        True
    ),
    "Lower Idol Ceiling Magic Bolt": lambda loadout: (
        True
    ),
    "Under Alter Magic Bolt": lambda loadout: (
        True
    ),
    "First Sparksuit": lambda loadout: (
        True
    ),
    "False Idol Baseball Alter": lambda loadout: (
        True
    ),
    "Spike Spark Heart": lambda loadout: (
        True
    ),
    "Junkoon Lucky Frog": lambda loadout: (
        True
    ),
    "Purple Locket": lambda loadout: (
        True
    ),
    "Upper Middle Idol Baseball": lambda loadout: (
        True
    ),
    "Upper Deep Purple Baseball": lambda loadout: (
        True
    ),
    "Toxic Heart": lambda loadout: (
        True
    ),
    "Mother Brain Sparksuit": lambda loadout: (
        True
    ),
    "Under Stairs Magic Bolt": lambda loadout: (
        True
    ),
    "Water Climb Heart": lambda loadout: (
        True
    ),
    "Deep Magic Bolt": lambda loadout: (
        True
    ),
    "Fake Map Heart": lambda loadout: (
        True
    ),
    "Crateria Heart": lambda loadout: (
        True
    ),
    "Gem Of Storms": lambda loadout: (
        True
    ),
    "Magic Broom": lambda loadout: (
        True
    ),
    "Deep Purple Baseball Alter": lambda loadout: (
        True
    ),
    "Lava Magic Bolt": lambda loadout: (
        True
    ),
    "Junkly Lucky Frog": lambda loadout: (
        True
    ),
    "Behind Throne Heart": lambda loadout: (
        True
    ),
    "Under Shaft Heart": lambda loadout: (
        True
    ),
    "Freeze Boost Heart": lambda loadout: (
        True
    ),
    "Spike Jump Magic Bolt": lambda loadout: (
        True
    ),
    "Left Shaft Magic Bolt": lambda loadout: (
        True
    ),
    "Crystal Cave Sparksuit": lambda loadout: (
        True
    ),
    "Frozen Cave Baseball": lambda loadout: (
        True
    ),
    "Water Cave Magic Bolt": lambda loadout: (
        True
    ),
    "Snowmen Mini-Boss Heart": lambda loadout: (
        True
    ),
    "Rat Dasher": lambda loadout: (
        True
    ),
    "Gem Of Ice": lambda loadout: (
        True
    ),
    "Dreamer's Crown": lambda loadout: (
        True
    ),
    "Ice Castle Baseball Alter": lambda loadout: (
        True
    ),
    "Junkraid Lucky Frog": lambda loadout: (
        True
    ),
    "Under Corpses Heart": lambda loadout: (
        True
    ),
    "Hidden Magic Bolt": lambda loadout: (
        True
    ),
    "Shaft Heart": lambda loadout: (
        True
    ),
    "Magic Soap": lambda loadout: (
        True
    ),
    "Lower Hidden Magic Bolt": lambda loadout: (
        True
    ),
    "Behind Blocks Baseball": lambda loadout: (
        True
    ),
    "Cave Magic Bolt": lambda loadout: (
        True
    ),
    "Gem Of Blood": lambda loadout: (
        True
    ),
    "Hidden Above Door Sparksuit": lambda loadout: (
        True
    ),
    "Hidden Table Heart": lambda loadout: (
        True
    ),
    "Sanguine Fin": lambda loadout: (
        True
    ),
    "OatsnGoats Heart": lambda loadout: (
        True
    ),
    "Blood Bethel Baseball Alter": lambda loadout: (
        True
    ),
    "Junkgon Lucky Frog": lambda loadout: (
        True
    ),
    "Gem Of Death": lambda loadout: (
        True
    )
}

class Default(LogicInterface):
    location_logic: ClassVar[LocationLogicType] = location_logic