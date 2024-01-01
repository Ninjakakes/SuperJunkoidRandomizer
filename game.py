from dataclasses import dataclass

from location import Location

@dataclass
class Game:
    """ a composition of all the components that make up the generated seed """
    all_locations: dict[str, Location]
    seed: int
