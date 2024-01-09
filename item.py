from typing import Iterable

Item = tuple[str, bytes, bytes, bytes, bytes]
""" Name, Visible, Chozo, Hidden, AmmoQty """

class Items:
    MagicBolt = ("Magic Bolt",
               b"\xdb\xee",
               b"\x2f\xef",
               b"\x83\xef",
               b"\x00")
    Baseball = ("Baseball",
             b"\xdf\xee",
             b"\x33\xef",
             b"\x87\xef",
             b"\x00")
    Sparksuit = ("Sparksuit",
                 b"\xe3\xee",
                 b"\x37\xef",
                 b"\x8b\xef",
                 b"\x00")
    RatCloak = ("Rat Cloak",
             b"\x23\xef",
             b"\x77\xef",
             b"\xcb\xef",
             b"\x00")
    WaveBangle = ("Wave Bangle",
                 b"\x03\xef",
                 b"\x57\xef",
                 b"\xab\xef",
                 b"\x00")
    RatBurst = ("Rat Burst",
             b"\xe7\xee",
             b"\x3b\xef",
             b"\x8f\xef",
             b"\x00")
    Feather = ("Feather",
              b"\xf3\xee",
              b"\x47\xef",
              b"\x9b\xef",
              b"\x00")
    PurpleLocket = ("Purple Locket",
             b"\x07\xef",
             b"\x5b\xef",
             b"\xaf\xef",
             b"\x00")
    SanguineFin = ("Sanguine Fin",
                   b"\x0b\xef",
                   b"\x5f\xef",
                   b"\xb3\xef",
                   b"\x00")
    BloodGem = ("Gem Of Blood",
            b"\xfb\xee",
            b"\x4f\xef",
            b"\xa3\xef",
            b"\x00")
    RatDasher = ("Rat Dasher",
                    b"\xf7\xee",
                    b"\x4b\xef",
                    b"\x9f\xef",
                    b"\x00")
    # Spazer = ("Spazer",
    #           b"\xff\xee",
    #           b"\x53\xef",
    #           b"\xa7\xef",
    #           b"\x00")
    IceGem = ("Gem Of Ice",
           b"\xef\xee",
           b"\x43\xef",
           b"\x97\xef",
           b"\x00")
    DreamersCrown  = ("Dreamer's Crown",
               b"\x17\xef",
               b"\x6b\xef",
               b"\xbf\xef",
               b"\x00")
    StormsGem = ("Gem Of Storms",
              b"\x13\xef",
              b"\x13\xef",
              b"\xbb\xef",
              b"\x00")
    Wallkicks = ("Wallkicks",
             b"\x1f\xef",
             b"\x73\xef",
             b"\xc7\xef",
             b"\x00")
    DeathGem = ("Gem Of Death",
              b"\xeb\xee",
              b"\x3f\xef",
              b"\x93\xef",
              b"\x00")
    MagicBroom = ("Magic Broom",
                 b"\x1b\xef",
                 b"\x6f\xef",
                 b"\xc3\xef",
                 b"\x00")
    Heart = ("Heart",
              b"\xd7\xee",
              b"\x2b\xef",
              b"\x7f\xef",
              b"\x00")
    LuckyFrog = ("Lucky Frog",
              b"\x27\xef",
              b"\x7b\xef",
              b"\xcf\xef",
              b"\x00")
    MagicSoap = ("Magic Soap",
            b"\x0f\xef",
            b"\x63\xef",
            b"\xb7\xef",
            b"\x00")
    BigLeaugeGlove = ("Big Leauge Glove",
                      b"\xa0\xf4",
                      b"\xa0\xf4",
                      b"\xa0\xf4",
                      b"\x00")
    
items_unpackable: Iterable[Item] = (
    Items.MagicBolt, Items.Baseball, Items.Sparksuit, Items.RatCloak, Items.WaveBangle, Items.RatBurst, Items.Feather, Items.PurpleLocket, Items.SanguineFin, Items.BloodGem, Items.RatDasher, Items.IceGem, Items.DreamersCrown, 
    Items.StormsGem, Items.Wallkicks, Items.DeathGem, Items.MagicBroom, Items.Heart, Items.LuckyFrog, Items.MagicSoap, Items.BigLeaugeGlove
)

all_items: dict[str, Item] = {
    item[0]: item
    for item in items_unpackable
}