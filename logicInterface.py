from typing import Callable, ClassVar

from loadout import Loadout

LocationLogicType = dict[str, Callable[[Loadout], bool]]

class LogicInterface:
    location_logic: ClassVar[LocationLogicType]
    """
    {
        location_name:
            (loadout) -> can_access
    }
    """