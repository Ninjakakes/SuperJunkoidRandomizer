import random
import sys

from ips import patch as ips_patch
from romWriter import RomWriter
from location import Location, pullCSV
from item import all_items
from loadout import Loadout
from game import Game
import fillAssumed

from typing import Union
from pathlib import Path

def plmidFromHiddenness(itemArray, hiddenness) -> bytes:
    if hiddenness == "open":
        plmid = itemArray[1]
    elif hiddenness == "eye":
        plmid = itemArray[2]
    else:
        plmid = itemArray[3]
    return plmid

def ips_patch_from_file(ips_file_name: Union[str, Path], input_bytes: Union[bytes, bytearray]) -> bytearray:
    with open(ips_file_name,"rb") as isp_file:
        isp_data = isp_file.read()
    return ips_patch(input_bytes, isp_data)

def patch_rom_with_ips(ips_file_name: Union[str, Path], base_rom_file_name: Union[str, Path],
                        patched_rom_file_name: Union[str,Path]) -> None:
    with open(base_rom_file_name, "rb") as base_rom:
        base_rom_data = base_rom.read()
    patched_rom_data = ips_patch_from_file(ips_file_name, base_rom_data)

    with open(patched_rom_file_name,"wb") as patched_rom:
        patched_rom.write(patched_rom_data)

def write_location(romWriter: RomWriter, location: Location) -> None:
    """
    provide a location with an ['item'] value
    write all rom locations associated with the item location
    """
    item = location["item"]
    assert item, f"{location['roomname']} didn't get an item"

    plmid = plmidFromHiddenness(item, location["hiddenness"])
    romWriter.writeItem(location["locationid"], plmid, item[4])
    for address in location["altlocationids"]:
        romWriter.writeItem(address, plmid, item[4])

def main(argv: list[str]) -> None:
    game = generate()
    rom_name = write_rom(game)

def generate() -> Game:
    seed = random.randint(0, 9999999)
    # seed = 0
    random.seed(seed)

    csvdict = pullCSV()
    locArray = list(csvdict.values())

    game = Game(csvdict,seed)

    seedComplete = False
    randomizeAttempts = 0
    while not seedComplete:
        randomizeAttempts += 1
        if randomizeAttempts > 10:
            print("Giving up after 10 attempts. Help?")
            break
        print("Starting randomization attempt:", randomizeAttempts)
        game.item_placement_spoiler = ""
        game.item_placement_spoiler += f"Starting randomization attempt: {randomizeAttempts}\n"
        game.item_placement_spoiler += f"Seed: {seed}"
        # now start randomizing
        seedComplete = assumed_fill(game)

    return game

def assumed_fill(game: Game) -> bool:
    for loc in game.all_locations.values():
        loc["item"] = None
    dummy_locations: list[Location] = []
    loadout = Loadout(game)
    fill_algorithm = fillAssumed.FillAssumed()
    n_items_to_place = fill_algorithm.count_items_remaining()
    assert n_items_to_place <= len(game.all_locations), \
        f"{n_items_to_place} items to put in {len(game.all_locations)} locations"
    print(f"{fill_algorithm.count_items_remaining()} items to place")
    while fill_algorithm.count_items_remaining():
        placePair = fill_algorithm.choose_placement(dummy_locations, loadout)
        if placePair is None:
            message = ('Item placement was not successful in assumed. '
                       f'{fill_algorithm.count_items_remaining()} items remaining.')
            print(message)

            break
        placeLocation, placeItem = placePair
        placeLocation["item"] = placeItem
        print(f"Placing {placeItem[0]} at {placeLocation['index']}:" 
              f"{placeLocation['region']} | {placeLocation['roomname']}")

        if fill_algorithm.count_items_remaining() == 0:
            completable = True
            if completable:
                print("Item placements successful.")
            return completable

    return False

def write_rom(game: Game) -> str:
    rom_name = f"SuperJunkoid{game.seed}.sfc"
    rom1_path = f"roms/{rom_name}"
    rom_clean_path = Path("roms/Super Junkoid 1.3.sfc")

    if(not rom_clean_path.is_file()):
        patch_rom_with_ips("Super Junkoid 1.3.ips","roms/Super Metroid (JU).sfc", rom_clean_path)

    romWriter = RomWriter.fromFilePath(rom_clean_path)

    for loc in game.all_locations.values():
        write_location(romWriter, loc)

    romWriter.finalizeRom(rom1_path)


if __name__ == "__main__":
    import time
    t0 = time.perf_counter()
    main(sys.argv)
    t1 = time.perf_counter()
    print(f"Time taken: {t1-t0}")