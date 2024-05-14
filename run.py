from random import randint

# Initialize scores for computer and player
scores = {"computer": 0, "player": 0}

class Board:
    """
    Main board class. Sets size, number of ships, players name and board type (player or computer)
    Can add ships and guesses aswell as print board
    """

    def __init__(self, size, num_ships, name, type):

        """
        Initialize the board with specified size, number of ships, player's name, and board type.

        Parameters:
            size (int): Size of the board.
            num_ships (int): Number of ships to be placed on the board.
            name (str): Name of the player.
            type (str): Type of the board (player or computer).
        """
        self.size = size
        self.num_ships = num_ships
        self.type = type
        self.name = name
        self.board = [['.' for x in range(size)] for y in range(size)]
        self.guesses = []
        self.ships = []

        def place_ships(self):
            """
            Randomily place ships on board. col is colum, 
            """
            for _ in range(self.num_ships):
                ship_row = randint(0, self.size -1)
                ship_col = randint(0, self.size -1)