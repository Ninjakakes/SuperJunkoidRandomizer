from typing import Optional

from .game import Game
from .item import Items
from .loadout import Loadout
from .location import Location
from .logic_updater import updateLogic

_progression_items = frozenset([
    Items.MagicBolt,
    Items.Baseball,
    Items.Sparksuit,
    Items.RatCloak,
    Items.WaveBangle,
    Items.RatBurst,
    Items.Feather,
    Items.PurpleLocket,
    Items.SanguineFin,
    Items.BloodGem,
    Items.RatDasher,
    Items.IceGem,
    Items.DreamersCrown,
    Items.StormsGem,
    Items.Wallkicks,
    Items.DeathGem,
    Items.MagicBroom,
    Items.Heart,
    Items.LuckyFrog,
    Items.MagicSoap
])


def solve(game: Game, starting_items: Optional[Loadout] = None) -> tuple[bool, list[str], list[Location]]:
    """ returns (completable, spoiler lines, accessible locations) """
    for loc in game.all_locations.values():
        loc["inlogic"] = False

    unused_locations = list(game.all_locations.values())
    used_locations: set[str] = set()

    loadout = Loadout(game, starting_items)

    log_lines = ["- begin -"]

    while "sphere:" in log_lines[-1]:
        log_lines.pop()

    stuck = False
    while not stuck:
        prev_loadout_count = len(loadout)
        updateLogic(unused_locations, loadout)
        log_lines.append("sphere:")
        for loc in unused_locations:
            if loc["inlogic"]:
                loc_name = loc["roomname"]
                item = loc["item"]
                if item:
                    loadout.append(item)
                    if item in _progression_items:
                        log_lines.append(f"    get {item[0]} from {loc_name}")
                used_locations.add(loc_name)
        # remove used locations
        unused_locations = [loc for loc in unused_locations if loc["roomname"] not in used_locations]
        stuck = len(loadout) == prev_loadout_count

    while "sphere:" in log_lines[-1]:
        log_lines.pop()

    # note: the reason for making a new list from all_locations rather than used_locations,
    # is that used_locations is a `set`, so iterating through it is not deterministic, so seeds wouldn't be reproducible
    return (
        len(unused_locations) == 0,
        log_lines,
        [loc for loc in game.all_locations.values() if loc["roomname"] in used_locations]
    )
