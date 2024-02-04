import tkinter as tk
from itertools import cycle
from typing import NamedTuple

class Player(NamedTuple):
    label: str
    color: str

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green")
)

class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, ...):
        # Your game initialization code here

    # Other methods for the game logic

# Create an instance of the game and run it
game = TicTacToeGame()