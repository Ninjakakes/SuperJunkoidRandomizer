import sys

from ips import patch as ips_patch
from romWriter import RomWriter
from location import Location, pullCSV
from item import all_items

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
    rom_path = Path("roms/Super Junkoid 1.3.sfc")

    if(not rom_path.is_file()):
        patch_rom_with_ips("Super Junkoid 1.3.ips","roms/Super Metroid (JU).sfc", rom_path)

    rom_writer = RomWriter.fromFilePath(rom_path)

    csvdict = pullCSV()
    locArray = list(csvdict.values())

    for location in locArray:
        location["item"] = all_items['Magic Bolt']
        write_location(rom_writer, location)

    rom_writer.finalizeRom("roms/Super Junkoid 1.3(mod).sfc")

if __name__ == "__main__":
    import time
    t0 = time.perf_counter()
    main(sys.argv)
    t1 = time.perf_counter()
    print(f"Time taken: {t1-t0}")