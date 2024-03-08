from typing import ClassVar

from .item import items_unpackable
from .logicInterface import LocationLogicType, LogicInterface
from .logic_shortcut import LogicShortcut

(
    MagicBolt, Baseball, Sparksuit, RatCloak, WaveBangle, RatBurst, Feather, PurpleLocket, SanguineFin, BloodGem,
    RatDasher, IceGem, DreamersCrown, StormsGem, Wallkicks, DeathGem, MagicBroom, Heart, LuckyFrog, MagicSoap,
    BigLeagueGlove
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
         (lowerIceCastle in loadout)
         )
))

exitLowerOutskirts = LogicShortcut(lambda loadout: (
        (canRatBurst in loadout) or
        ((Baseball in loadout) and ((Wallkicks in loadout) or (MagicBroom in loadout)))
))

lowerOutskirts = LogicShortcut(lambda loadout: (
    ((enterLowerOutskirts in loadout) and (exitLowerOutskirts in loadout))
))

lowerIceCastle = LogicShortcut(lambda loadout: (
        ((((Feather in loadout) or (Wallkicks in loadout)) and (IceGem in loadout)) or
         (MagicBroom in loadout)) or
        ((canRatBurst in loadout) and
         (
                 (Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout)
         ))
))

crocomire = LogicShortcut(lambda loadout: (
        (lowerIceCastle in loadout) and (canRatBurst in loadout) and (loadout.count(MagicBolt) >= 4) and
        (Baseball in loadout) and (IceGem in loadout)
))

junkraid = LogicShortcut(lambda loadout: (
        (crocomire in loadout) and (canRatDash in loadout) and (loadout.count(Heart) >= 4)
))

bloodBethel = LogicShortcut(lambda loadout: (
        ((canRatBurst in loadout) or
         (
                 (lowerOutskirts in loadout) and
                 (Baseball in loadout) and ((Wallkicks in loadout) or (MagicBroom in loadout))
         )) and
        ((Feather in loadout) or ((SanguineFin in loadout) and ((Wallkicks in loadout) or MagicBroom in loadout)))
))

botwoon = LogicShortcut(lambda loadout: (
        (bloodBethel in loadout) and (SanguineFin in loadout) and
        ((Wallkicks in loadout) or (MagicBroom in loadout)) and
        (Baseball in loadout) and (loadout.count(Heart) >= 8)
))

junkgon = LogicShortcut(lambda loadout: (
        (botwoon in loadout) and (BloodGem in loadout) and (loadout.count(MagicBolt) >= 4)
))

enterIdol = LogicShortcut(lambda loadout: (
    ((junkraid in loadout) or (junkgon in loadout)) and (Sparksuit in loadout) and (canRatBurst in loadout)
))

sporeSpawn = LogicShortcut(lambda loadout: (
        (enterIdol in loadout) and
        ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
))

junkoon = LogicShortcut(lambda loadout: (
        (sporeSpawn in loadout) and (SanguineFin in loadout) and (RatDasher in loadout) and (Sparksuit in loadout)
        and (loadout.count(Heart) >= 8)
))

deepPurple = LogicShortcut(lambda loadout: (
        ((lowerOutskirts in loadout) and (Baseball in loadout)) or
        ((lowerIceCastle in loadout) and (Baseball in loadout)) or
        ((bloodBethel in loadout) and (Baseball in loadout))
))

crateria = LogicShortcut(lambda loadout: (
        (deepPurple in loadout) and (canRatBurst in loadout) and (Sparksuit in loadout)
))

junkly = LogicShortcut(lambda loadout: (
        (crateria in loadout) and
        (((Feather in loadout) and Wallkicks in loadout) or (MagicBroom in loadout)) and
        (PurpleLocket in loadout) and
        (loadout.count(Heart) >= 12) and (loadout.count(MagicBolt) >= 9) and (loadout.count(Baseball) >= 5)
))

location_logic: LocationLogicType = {
    "Hidden Rat Tunnel Magic Bolt": lambda loadout: (
            (RatCloak in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Hidden Pipe Heart": lambda loadout: (
        True
    ),
    "Pipe Maze Heart": lambda loadout: (
            (RatCloak in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
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
            (Baseball in loadout) and (RatCloak in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Hidden Heart": lambda loadout: (
            (RatCloak in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Under Spider Magic Bolt": lambda loadout: (
            (Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout)
    ),
    "Hidden Underwater Heart": lambda loadout: (
            (Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout)
    ),
    "Feather": lambda loadout: (
            (Feather in loadout) or
            ((SanguineFin in loadout) and ((Wallkicks in loadout) or (MagicBroom in loadout)))
    ),
    "Rat Cloak": lambda loadout: (
            (Wallkicks in loadout) or (MagicBroom in loadout) or
            ((RatCloak in loadout) and (Feather in loadout))
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
    "Left Shaft Heart": lambda loadout: (
            (enterIdol in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Right Shaft Heart": lambda loadout: (
            (enterIdol in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Wave Bangle": lambda loadout: (  # Deep Purple
            (deepPurple in loadout) and
            (canRatBurst in loadout)
    ),
    "Left Idol Magic Bolt": lambda loadout: (
            (enterIdol in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Hidden Shaft Heart": lambda loadout: (
            (sporeSpawn in loadout) and
            ((RatDasher in loadout) or (Sparksuit in loadout))
    ),
    "Lower Idol Ceiling Magic Bolt": lambda loadout: (
            (sporeSpawn in loadout) and
            (((Feather in loadout) and (Wallkicks in loadout)) or (MagicBroom in loadout))
    ),
    "Under Alter Magic Bolt": lambda loadout: (
        (sporeSpawn in loadout)
    ),
    "First Sparksuit": lambda loadout: (
            (sporeSpawn in loadout) and (Sparksuit in loadout)
    ),
    "False Idol Baseball Alter": lambda loadout: (
        (sporeSpawn in loadout)
    ),
    "Spike Spark Heart": lambda loadout: (
            (sporeSpawn in loadout) and (SanguineFin in loadout) and (RatDasher in loadout) and (Sparksuit in loadout)
    ),
    "Junkoon Lucky Frog": lambda loadout: (
        (junkoon in loadout)
    ),
    "Purple Locket": lambda loadout: (
            (sporeSpawn in loadout) and (SanguineFin in loadout) and (RatDasher in loadout) and (Sparksuit in loadout)
    ),
    "Upper Middle Idol Baseball": lambda loadout: (
        (sporeSpawn in loadout)
    ),
    "Upper Deep Purple Baseball": lambda loadout: (  # Start of Deep Purple
            (deepPurple in loadout) and (canRatBurst in loadout) and (Sparksuit in loadout) and
            ((Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Toxic Heart": lambda loadout: (
            (crateria in loadout) and
            ((MagicBroom in loadout) or ((Feather in loadout) and (IceGem in loadout)))
    ),
    "Mother Brain Sparksuit": lambda loadout: (
            (canRatBurst in loadout) and (Wallkicks in loadout) and (Feather in loadout)
    ),
    "Under Stairs Magic Bolt": lambda loadout: (
            (crateria in loadout) and
            (((Feather in loadout) and Wallkicks in loadout) or (MagicBroom in loadout)) and
            (PurpleLocket in loadout)
    ),
    "Water Climb Heart": lambda loadout: (
            (crateria in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Deep Magic Bolt": lambda loadout: (
            (crateria in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
            and (SanguineFin in loadout) and (canRatDash in loadout)
    ),
    "Fake Map Heart": lambda loadout: (
            (crateria in loadout) and
            ((Feather in loadout) or (SanguineFin in loadout))
    ),
    "Crateria Heart": lambda loadout: (
            (crateria in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Gem Of Storms": lambda loadout: (
            (crateria in loadout) and
            ((Feather in loadout) or (Wallkicks in loadout) or (MagicBroom in loadout)) and
            (StormsGem in loadout) and
            (loadout.count(Heart) >= 8) and (loadout.count(Heart) >= 5)
    ),
    "Magic Broom": lambda loadout: (
            (crateria in loadout) and
            (loadout.count(Heart) >= 8) and (loadout.count(MagicBolt) >= 5)
    ),
    "Deep Purple Baseball Alter": lambda loadout: (
            (crateria in loadout) and
            (((Feather in loadout) and Wallkicks in loadout) or (MagicBroom in loadout)) and
            (PurpleLocket in loadout)
    ),
    "Lava Magic Bolt": lambda loadout: (
            (crateria in loadout) and
            (((Feather in loadout) and Wallkicks in loadout) or (MagicBroom in loadout)) and
            (PurpleLocket in loadout)
    ),
    "Junkly Lucky Frog": lambda loadout: (
        (junkly in loadout)
    ),
    "Behind Throne Heart": lambda loadout: (  # Start Of Ice Castle
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
            (lowerIceCastle in loadout) and
            (RatCloak in loadout) and
            ((Sparksuit in loadout) or ((IceGem in loadout) and (Feather in loadout)) or (MagicBroom in loadout))
    ),
    "Crystal Cave Sparksuit": lambda loadout: (
            (Sparksuit in loadout) and
            (lowerIceCastle in loadout) and
            (RatCloak in loadout) and
            (Feather in loadout)
    ),
    "Frozen Cave Baseball": lambda loadout: (
            (lowerIceCastle in loadout) and (RatCloak in loadout) and
            (
                    (canRatBurst in loadout) or
                    (canRatDash in loadout) and (BloodGem in loadout)
            ) and
            (((Feather in loadout) and (IceGem in loadout)) or (MagicBroom in loadout))
    ),
    "Water Cave Magic Bolt": lambda loadout: (
            (lowerIceCastle in loadout) and (RatCloak in loadout) and
            (
                    (canRatBurst in loadout) or
                    (canRatDash in loadout) and (BloodGem in loadout)
            ) and
            (Feather in loadout) and (SanguineFin in loadout)
    ),
    "Snowmen Mini-Boss Heart": lambda loadout: (
        (lowerIceCastle in loadout)
    ),
    "Rat Dasher": lambda loadout: (
            ((((Feather in loadout) or (Wallkicks in loadout)) and (IceGem in loadout)) or
             (MagicBroom in loadout)) and (canRatBurst in loadout) and (canRatDash in loadout)
    ),
    "Gem Of Ice": lambda loadout: (
            (crocomire in loadout) and (IceGem in loadout)
    ),
    "Dreamer's Crown": lambda loadout: (
            (lowerIceCastle in loadout) and (Baseball in loadout) and (Sparksuit in loadout) and
            (canRatBurst in loadout)
    ),
    "Ice Castle Baseball Alter": lambda loadout: (
            (lowerIceCastle in loadout) and (Baseball in loadout)
    ),
    "Junkraid Lucky Frog": lambda loadout: (
        (junkraid in loadout)
    ),
    "Under Corpses Heart": lambda loadout: (  # Start Of Blood Bethel
        (bloodBethel in loadout) and (canRatBurst in loadout)
    ),
    "Hidden Magic Bolt": lambda loadout: (
        (bloodBethel in loadout)
    ),
    "Shaft Heart": lambda loadout: (
        (bloodBethel in loadout)
    ),
    "Magic Soap": lambda loadout: (
            (bloodBethel in loadout) and (canRatBurst in loadout) and
            ((Wallkicks in loadout) or (MagicBroom in loadout))
    ),
    "Lower Hidden Magic Bolt": lambda loadout: (
        (bloodBethel in loadout)
    ),
    "Behind Blocks Baseball": lambda loadout: (
            (bloodBethel in loadout) and (BloodGem in loadout) and (canRatBurst in loadout)
    ),
    "Cave Magic Bolt": lambda loadout: (
            (bloodBethel in loadout) and
            ((canRatDash in loadout) or (Sparksuit in loadout))
    ),
    "Gem Of Blood": lambda loadout: (
            (botwoon in loadout) and (BloodGem in loadout)
    ),
    "Hidden Above Door Sparksuit": lambda loadout: (
            (bloodBethel in loadout) and (Sparksuit in loadout)
    ),
    "Hidden Table Heart": lambda loadout: (
            (bloodBethel in loadout) and (SanguineFin in loadout) and
            ((Wallkicks in loadout) or (MagicBroom in loadout)) and
            (Baseball in loadout)
    ),
    "Sanguine Fin": lambda loadout: (
        (bloodBethel in loadout)
    ),
    "OatsnGoats Heart": lambda loadout: (
            (bloodBethel in loadout) and (BloodGem in loadout) and
            ((SanguineFin in loadout) or ((Wallkicks in loadout) or (MagicBroom in loadout)))
    ),
    "Blood Bethel Baseball Alter": lambda loadout: (
            (bloodBethel in loadout) and (Baseball in loadout)
    ),
    "Junkgon Lucky Frog": lambda loadout: (
        (junkgon in loadout)
    ),
    "Gem Of Death": lambda loadout: (  # SHEOL
            (junkraid in loadout) and (junkgon in loadout) and (junkoon in loadout) and (junkly in loadout) and
            (loadout.count(MagicBolt) >= 15)
    ),
    "Big League Glove": lambda loadout: (
            (crateria in loadout) and (Feather in loadout)
    )
}


class Default(LogicInterface):
    location_logic: ClassVar[LocationLogicType] = location_logic
