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

def main(argv: list[str]) -> None:
    rom_path = Path("roms/Super Junkoid 1.3.sfc")

    if(not rom_path.is_file()):
        patch_rom_with_ips("Super Junkoid 1.3.ips","roms/Super Metroid (JU).sfc", rom_path)

    rom_writer = RomWriter.fromFilePath(rom_path)

    location_data = pullCSV()
    for name, loc in location_data.items():
        address = loc["locationid"]
        expected_item_data = plmidFromHiddenness(all_items[loc["vanillaitemname"]], loc["hiddenness"])
        item_data = rom_writer.rom_data[address:address+2]
        if(expected_item_data == item_data):
            print(f"Index: {loc['index']} has the expected item of {loc['vanillaitemname']}")
        else:
            print(f"Index: {loc['index']} has an unepected item (Expected: {expected_item_data} Got: {item_data})")
        if(loc["altlocationids"][0] != 0):
            for address in loc["altlocationids"]:
                expected_item_data = plmidFromHiddenness(all_items[loc["vanillaitemname"]], loc["hiddenness"])
                item_data = rom_writer.rom_data[address:address+2]
                if(expected_item_data == item_data):
                    print(f"Index: {loc['index']} has the expected item of {loc['vanillaitemname']}")
                else:
                    print(f"Index: {loc['index']} has an unepected item (Expected: {expected_item_data}" 
                          f"Got: {item_data})")


    # change item into magic bolt in the room with a heart hidden behind a wall underwater
    rom_writer.writeItem(0x7d2dc,plmidFromHiddenness(all_items["Magic Bolt"],'open'))

    # change item into magic bolt(eye) in the rat cloak room
    rom_writer.writeItem(0x7d2a4,plmidFromHiddenness(all_items["Magic Bolt"],'eye'))

    # change item with plm index 1 (plm loc + (index*6))
    rom_writer.writeItem(0x7cd44, plmidFromHiddenness(all_items["Magic Bolt"],'open'))

    # change item with alt locations
    rom_writer.writeItem(0x79330,plmidFromHiddenness(all_items["Magic Bolt"],'open'))
    rom_writer.writeItem(0x7ce08,plmidFromHiddenness(all_items["Magic Bolt"],'open'))

    rom_writer.finalizeRom("roms/Super Junkoid 1.3(mod).sfc")

if __name__ == "__main__":
    import time
    t0 = time.perf_counter()
    main(sys.argv)
    t1 = time.perf_counter()
    print(f"Time taken: {t1-t0}")