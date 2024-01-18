from copy import deepcopy
from dataclasses import dataclass, asdict
from typing import Type, Any, cast, Optional

from .item import all_items
from .location import Location
from .logicInterface import LogicInterface

@dataclass
class Game:
    """ a composition of all the components that make up the generated seed """
    logic: Type[LogicInterface]
    all_locations: dict[str, Location]
    seed: int
    item_placement_spoiler: str = ""

    def to_jsonable(self) -> dict[str, Any]:
        dct = asdict(self)

        locations_copy = deepcopy(self.all_locations)
        dct["all_locations"] = locations_copy
        for loc in locations_copy.values():
            assert isinstance(loc, dict)
            item = loc["item"]
            if item:
                item_name = item[0]
                assert isinstance(item_name, str)
                non_loc = cast(dict[str, Any], loc)
                non_loc["item"] = item_name

        return dct

    @staticmethod
    def from_jsonable(dct: dict[str, Any]) -> "Game":
        game = Game(**dct)

        for loc in game.all_locations.values():
            item = loc["item"]
            item_name = cast(Optional[str], item)
            if item_name:
                loc["item"] = all_items[item_name]
        return game
