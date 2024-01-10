# Super Junkoid Randomizer
## How to Generate

###  Setup / Install
1. Install Python from [https://www.python.org/](https://www.python.org/)
   - Requires Python 3.9 or higher

2. Download the code from this page
   1. Green "Code" button in the top right portion of this page
   2. "Download ZIP"
   3. Unzip it to a folder on your hard drive

3. put your Super Metroid or Super Junkoid 1.3 rom in the `roms` directory with this filename: `Super Metroid (JU).sfc` or `Super Junkoid 1.3.sfc`

### Generate from Command Line
Run `main.py` from the command line

## Logic Notes
All the logic is symmetrical. This means getting out is required to go in.

For example, Gem of Ice cannot be at the vanilla Gem of Ice location, because it requires Gem of Ice to get out.

If you can't get out of a location, you shouldn't go in, because you might be soft-locked.

Using Sparksuits to reach higher locations is not currently in logic