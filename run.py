from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    """
    Main board class. Sets size, number of ships, players name and board type (player or computer)
    Can add ships and guesses aswell as print board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.num_ships = num_ships
        self.type = type
        self.name = name
        self.board = [['O' for _ in range(size)] for _ in range(size)]
        self.guesses = []
        self.ships = []