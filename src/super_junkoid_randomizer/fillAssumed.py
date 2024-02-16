import random
from typing import Optional

from .fillInterface import FillAlgorithm
from .item import Item, Items
from .loadout import Loadout
from .location import Location
from .solver import solve

_minor_items = {
    Items.MagicBolt: 14,
    Items.Baseball: 9,
    Items.Sparksuit: 4,
    Items.Heart: 19,
    Items.LuckyFrog: 3
}


class FillAssumed(FillAlgorithm):
    prog_items: list[Item]
    extra_items: list[Item]
    itemLists: list[list[Item]]

    def __init__(self) -> None:
        self.prog_items = [
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
            Items.MagicSoap,
            Items.BigLeagueGlove
        ]

        self.extra_items = []
        for it, n in _minor_items.items():
            self.extra_items.extend([it for _ in range(n)])

        self.itemLists = [self.prog_items, self.extra_items]

    def _get_accessible_locations(self, loadout: Loadout) -> list[Location]:
        _, _, locs = solve(loadout.game, loadout)
        return locs

    def _get_available_locations(self, loadout: Loadout) -> list[Location]:
        return [loc for loc in self._get_accessible_locations(loadout) if loc["item"] is None]

    def _get_empty_locations(self, all_locations: dict[str, Location]) -> list[Location]:
        return [loc for loc in all_locations.values() if loc["item"] is None]

    @staticmethod
    def _choose_location(locs: list[Location]) -> Location:
        return random.choice(locs)

    def choose_placement(self, availableLocations: list[Location], loadout: Loadout) -> Optional[tuple[Location, Item]]:
        from_items = (
            self.prog_items if len(self.prog_items) else (
                self.extra_items
            )
        )

        assert len(from_items), "tried to place item when placement algorithm has 0 items left in item pool"

        item_to_place = random.choice(from_items)

        from_items.remove(item_to_place)

        if from_items is self.prog_items:
            loadout = Loadout(loadout.game)
            for item in from_items:
                loadout.append(item)
            available_locations = self._get_available_locations(loadout)
        else:  # extra
            available_locations = self._get_empty_locations(loadout.game.all_locations)
        if len(available_locations) == 0:
            return None

        return self._choose_location(available_locations), item_to_place

    def count_items_remaining(self) -> int:
        return sum(len(li) for li in self.itemLists)

    def remove_from_pool(self, item: Item) -> None:
        """ removes this item from the item pool """
        pass  # removed in placement function
