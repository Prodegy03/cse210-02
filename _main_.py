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
        print(f"{player1.name} current card is the {currCard.number} of {currCard.suit}")
        nextCard = cardDeck.drawCard()
        validated = False
        while(not validated):
            question = input("Do you think the next one is Higher or Lower? (h/l): ") 
            if question == "h":
                validated = True
                result = currCard.cardCompareHigher(nextCard)
            elif question == "l":
                validated = True
                result = currCard.cardCompareLower(nextCard)
            elif question == "quit":
                validated = True
            else:
                print("If you meant to exit program, please enter \"quit\", otherwise try again... ")
        if question == "quit":
            break
        print(f"The next card is the {nextCard.number} of {nextCard.suit}...")
        player1.changePlayerScore(result)
        player1.checkPlayerPoints()
        cardDeck.checkForShuffle()
        currCard = nextCard
        print()
    print("Thanks for playing the game!")



main()