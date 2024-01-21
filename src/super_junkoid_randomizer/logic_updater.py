from typing import Iterable

from .location import Location
from .loadout import Loadout


def updateLogic(unusedLocations: Iterable[Location], loadout: Loadout) -> Iterable[Location]:
    for thisLoc in unusedLocations:
        thisLoc['inlogic'] = loadout.game.logic.location_logic[thisLoc['roomname']](loadout)

    return unusedLocations
