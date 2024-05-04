import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("From following your footprints in the sand", 0.05),
        ("To walking with you on this island", 0.06),
        ("Guided by the grip of your hand", 0.06),
        ("I can feel you're holding my world", 0.06),
        ("Ano ba itong nadarama, oh shux", 0.07),
        ("Ito ba'y pag-ibig na", 0.08),
        ("Totoo ba ang pinadama,", 0.08),
        ("Cause boy, it feels so good", 0.09),
        ("Bawat araw mas sumasaya", 0.08),
        ("Magmula nang makita ka", 0.10),
        ("Nawawala ang pangangamba pag ika'y kapiling na", 0.08),
        ("Feels like summer when i'm with you", 0.09),
        ("Parang islang pantropiko", 0.07),
        ("Can't wait to go back with you", 0.05),
        ("Sa islang pantropiko", 0.07),
    ]

    delays = [0.3] * len(lines)

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()