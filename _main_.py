from game.objects import Player, Deck, Card
def main():
    print("Hello! Welcome to Hi Lo!")
    print()
    print()

    #ask user for how many players 
    # for loop to get multiple players

    playersName = input("What is your name?: ")
    player1 = Player()
    player1.name = playersName
    cardDeck = Deck()
    
    currCard = cardDeck.drawCard()
    while player1.is_playing == True: 
        print(f"{player1.name} current card is the {currCard.number} of {currCard.suit}")        #add current HP?
        question = input("Do you think the next one is Higher or Lower? (h/l): ")
        #validate that input
        nextCard = cardDeck.drawCard()
        if question == "h":
            result = currCard.cardCompareHigher(nextCard)
        else:
            result = currCard.cardCompareLower(nextCard)
        print(f"The next card is the {nextCard.number} of {nextCard.suit}...")
        player1.changePlayerScore(result)
        player1.checkPlayerPoints()
        cardDeck.checkForShuffle()
        currCard = nextCard
        print()
    print("Thanks for playing the game!")



main()