from typing import ClassVar

from item import items_unpackable, Items
from loadout import Loadout
from logicInterface import LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

(
    MagicBolt, Baseball, Sparksuit, RatCloak, WaveBangle, RatBurst, Feather, PurpleLocket, SanguineFin, BloodGem, RatDasher, IceGem, DreamersCrown, StormsGem, Wallkicks, DeathGem, MagicBroom, Heart, LuckyFrog, MagicSoap
) = items_unpackable

canRatBurst = LogicShortcut(lambda loadout: (
    (RatCloak in loadout) and (RatBurst in loadout)
))

canRatDash = LogicShortcut(lambda loadout: (
    (RatCloak in loadout) and (RatDasher in loadout)
))

enterLowerOutskirts = LogicShortcut(lambda loadout: (
    ((RatCloak in loadout) and 
    (
        (Feather in loadout) or 
        (Wallkicks in loadout) or
        (MagicBroom in loadout)
    )) or
    ((Baseball in loadout) and
        (lowerIcePalace in loadout)
    )
))

exitLowerOutskirts = LogicShortcut(lambda loadout: (
    (canRatBurst in loadout) or 
    ((Baseball in loadout) and ((Wallkicks in loadout) or (MagicBroom in loadout)))
))

lowerOutskirts = LogicShortcut(lambda loadout: (
    ((enterLowerOutskirts in loadout) and (exitLowerOutskirts in loadout))
))

lowerIcePalace = LogicShortcut(lambda loadout: (
    ((((Feather in loadout) or (Wallkicks in loadout)) and (IceGem in loadout)) or
    (MagicBroom in loadout)) or
    ((canRatBurst in loadout) and
    (
        (Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout)
    ))
))

crocomire = LogicShortcut(lambda loadout: (
    (lowerIcePalace in loadout) and (canRatBurst in loadout) and (loadout.count(MagicBolt) >= 4) and 
    (Baseball in loadout)
))

junkraid = LogicShortcut(lambda loadout: (
    (crocomire in loadout) and (loadout.count(Heart) >= 4)
))

location_logic: LocationLogicType = {
    "Hidden Rat Tunnel Magic Bolt": lambda loadout: (
        (RatCloak in loadout)
    ),
    "Hidden Pipe Heart": lambda loadout: (
        (canRatBurst in loadout)
    ),
    "Pipe Maze Heart": lambda loadout: (
        (RatCloak in loadout)
    ),
    "Ceiling Baseballs": lambda loadout: (
        (lowerOutskirts in loadout) and
        ((Wallkicks in loadout) or (MagicBroom in loadout)) and
        ((BloodGem in loadout) or (IceGem in loadout))
    ),
    "Wall Jump Climb Magic Bolt": lambda loadout: (
        (lowerOutskirts in loadout) and 
        ((Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Outskirts Baseball Alter": lambda loadout: (
        (Baseball in loadout)
    ),
    "Hidden Heart": lambda loadout: (
        (RatCloak in loadout)
    ),
    "Under Spider Magic Bolt": lambda loadout: (
        (canRatBurst in loadout)
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
        (lowerOutskirts in loadout) and
        (canRatBurst in loadout)
    ),
    "Outside Idol Sparksuit": lambda loadout: (
        (lowerOutskirts in loadout) and 
        (Sparksuit in loadout)
    ),
    "Wallkicks": lambda loadout: (
        (lowerOutskirts in loadout) and 
        ((Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Left Shaft Heart": lambda loadout: ( # TODO False Idol logic
        True
    ),
    "Right Shaft Heart": lambda loadout: (
        True
    ),
    "Wave Bangle": lambda loadout: ( # Deep Purple
        ((lowerOutskirts in loadout) or (lowerIcePalace in loadout)) and
        (Baseball in loadout) and
        ((RatCloak in loadout) or (WaveBangle in loadout))
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
    "Upper Deep Purple Baseball": lambda loadout: ( # Start of Deep Purple
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
    "Behind Throne Heart": lambda loadout: ( # Start Of Ice Palace
        (
            (((Feather in loadout) or (Wallkicks in loadout)) and (IceGem in loadout)) or
            (MagicBroom in loadout)
        ) and 
        (canRatBurst in loadout)
    ),
    "Under Shaft Heart": lambda loadout: (
        (canRatBurst in loadout) and ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Freeze Boost Heart": lambda loadout: (
        ((canRatBurst in loadout) and (canRatDash in loadout) and (IceGem in loadout)) and
        ((Feather in loadout) or (Wallkicks in loadout))
    ),
    "Spike Jump Magic Bolt": lambda loadout: (
        (canRatBurst in loadout) or
        ((((Feather in loadout) or (Wallkicks in loadout)) and (IceGem in loadout)) or
        (MagicBroom in loadout))
    ),
    "Right Shaft Magic Bolt": lambda loadout: (
        (Baseball in loadout) and
        (lowerIcePalace in loadout) and
        (RatCloak in loadout) and 
        ((Sparksuit in loadout) or (IceGem in loadout) or (MagicBroom in loadout))
    ),
    "Crystal Cave Sparksuit": lambda loadout: (
        (Sparksuit in loadout) and 
        (lowerIcePalace in loadout) and
        (RatCloak in loadout)
    ),
    "Frozen Cave Baseball": lambda loadout: (
        (lowerIcePalace in loadout) and
        (
            (canRatBurst in loadout) or
            (canRatDash in loadout) and (BloodGem in loadout)
        ) and
        ((Feather in loadout) and (IceGem in loadout)) or (MagicBroom in loadout)
    ),
    "Water Cave Magic Bolt": lambda loadout: (
        (lowerIcePalace in loadout) and
        (
            (canRatBurst in loadout) or
            (canRatDash in loadout) and (BloodGem in loadout)
        ) and
        (Feather in loadout) and
        ((SanguineFin in loadout) or (Wallkicks in loadout))
    ),
    "Snowmen Mini-Boss Heart": lambda loadout: (
        (lowerIcePalace in loadout) and
        (
            (canRatBurst in loadout) or
            (canRatDash in loadout) and (BloodGem in loadout)
        )
    ),
    "Rat Dasher": lambda loadout: (
        ((((Feather in loadout) or (Wallkicks in loadout)) and (IceGem in loadout)) or
        (MagicBroom in loadout)) and (canRatBurst in loadout) and (canRatDash in loadout)
    ),
    "Gem Of Ice": lambda loadout: (
        (crocomire in loadout) and (IceGem in loadout)
    ),
    "Dreamer's Crown": lambda loadout: (
        (lowerIcePalace in loadout) and (Baseball in loadout) and (Sparksuit in loadout) and (canRatBurst in loadout)
    ),
    "Ice Castle Baseball Alter": lambda loadout: (
        (lowerIcePalace in loadout) and (Baseball in loadout)
    ),
    "Junkraid Lucky Frog": lambda loadout: (
        (junkraid in loadout)
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