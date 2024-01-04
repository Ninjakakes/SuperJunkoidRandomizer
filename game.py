from dataclasses import dataclass
from typing import Type

from location import Location
from logicInterface import LogicInterface

@dataclass
class Game:
    """ a composition of all the components that make up the generated seed """
    logic: Type[LogicInterface]
    all_locations: dict[str, Location]
    seed: int
    item_placement_spoiler: str = ""
