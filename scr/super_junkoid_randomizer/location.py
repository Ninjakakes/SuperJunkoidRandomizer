import csv
import pathlib
from typing import Optional, TypedDict, cast

from .item import Item

class Location(TypedDict):
    index: int
    roomname: str
    region: str
    vanillaitemname: str
    roomid: int
    locationid: int
    hiddenness: str
    altlocationids: list[int]
    item:  Optional[Item]
    inlogic: bool

def pullCSV() -> dict[str, Location]:
    csvdict: dict[str, Location] = {}

    def commentfilter(line: str) -> bool:
        return (line[0] != '#')

    path = pathlib.Path(__file__).parent.resolve()
    with open(path.joinpath("SuperJunkoid.csv"), 'r') as csvfile:
        reader = csv.DictReader(filter(commentfilter, csvfile))
        for row in reader:
            row['altlocationids'] = row['altlocationids'].split(',')
            row["index"] = int(row['index'])
            row["roomid"] = int(row["roomid"], 16)
            row["locationid"] = int(row["locationid"], 16)
            row['altlocationids'] = [
                int(locstr, 16) for locstr in row['altlocationids'] if locstr != '']
            row['item'] = None
            row['inlogic'] = False
            csvdict[row["roomname"]] = cast(Location, row)
    return csvdict