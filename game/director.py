

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.
    
    Attributes:
    is_playing (boolean): whether or not the game is being played."""

    def _init_(self):
        """Constructs a new director.
        
        """

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