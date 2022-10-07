import random


class Player:
    """A person who directs the game. 
    
    Attributes:
    is_playing (boolean): whether or not the game is being played."""

    def __init__(self):
        """Constructs a new player. """
        self.name = ""
        self.is_playing = True
        self.score_start = 300



    #IDK IF WE USE THIS...
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()

    #IDK IF WE USE THIS...
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
        self.cards = []
        for i in range(1,5):
            for j in range(1,14):
                self.cardSingle = card()
                self.cardSingle.number = j
                if i == 1:
                    self.cardSingle.suit == "hearts"
                elif i == 2:
                    self.cardSingle.suit == "diamonds"
                elif i == 3:
                    self.cardSingle.suit == "spades"
                elif i == 4:
                    self.cardSingle.suit == "clubs"
                self.cards.append(self.cardSingle)
        random.shuffle(self.cards)

    #recreate card pile(deck)
    def shuffleDeck(self):
        if len(self.cards)<12:
            print("Everyday I'm shuffling!")
            self.__init__()
            

    #gives us a card out of the deck
    def drawCard(self):
        lookingForCard = True
        while(lookingForCard):    
            drawn = random.randint(1, 13)
            if drawn in self.cards:
                cardWeDrew = self.cards.pop(self.cards.index(drawn))
                return cardWeDrew
            elif len(self.cards) == 0:
                self.shuffleDeck()

class card:
    def __init__(self):
        "construct a new deck of cards"
        self.number = 0
        self.suit = ""


            
                

       

