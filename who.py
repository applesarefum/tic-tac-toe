#!/usr/bin/env python3
from getch import getch
print("Will you play as X or O?\nPress A for X\nPress D for O")
meme=getch()
if meme=="a":
    print("You chose X!")
if meme=="d":
    print("You chose O!")

