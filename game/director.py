

from random import Random


class Player:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
    is_playing (boolean): whether or not the game is being played."""

    def _init_(self):
        """Constructs a new player.
        
        """
        self.name = ""
        self.is_playing = True
        self.score_start = 300



    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()

    def get_inputs(self):
        """Ask the user if they want to keep playing.

        Args:
            self (Director): An instance of Director.
        """
        keep_playing = input("Would you like to keep playing? [y/n] ")
        self.is_playing = (keep_playing == "y")

class deck:

    def __init__(self):
        "construct a new deck of cards"
        self.cards = [1,2,3,4,5,6,7,8,9,10,11,12,13]


    def drawCard(self):
        drawn = Random.randint(1,13)
        #make check to see if card is still in pile
        
        return self.cards[drawn - 1]

