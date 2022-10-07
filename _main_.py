from game.director import Player, deck
import imp
def main():
    print("Hello! Welcome to Hi Lo!")
    print()
    print()

    #ask user for how many players 
    # for loop to get multiple players

    playersName = input("What is your name?: ")
    player1 = Player()
    player1.name = playersName
    cardDeck = deck()
    

    while player1.is_playing == True: 
        cardSelection = cardDeck.drawCard()
        print(f"The current card is {cardSelection}")

        question = input("Do you think the next one is Higher or Lower? (h/l): ")
        #validate that input
        nextCard = cardDeck.drawCard()
        print(f"The next card drawn is {nextCard}. ")
        while question != "h" or question != "l":
            print("Invalid Answer")
            question = input("Do you think the next one is Higher or Lower? (h/l): ")
        else:
            if question == "h":
                result = cardCompareHigher(cardSelection, nextCard)
            elif question == "l":
                result = cardCompareLower(cardSelection, nextCard)
        print(f"The next card drawn is {nextCard}. ")

        changePlayerScore(result, player1)
        checkPlayerPoints(player1)
        print(f"You currently have {player1.score_start} points. ")
        answer = input("Do you want to keep playing? y/n: ")
        keepPlaying(player1, answer)

    print("Thanks for playing the game!")

def cardCompareHigher(firstCard, secondCard):
    if firstCard < secondCard: return True
    else: return False

def cardCompareLower(firstCard, secondCard):
    if firstCard > secondCard: return True
    else: return False

def changePlayerScore(outcome, player):
    if outcome:
        player.score_start += 100
    else:
        player.score_start -= 75

def checkPlayerPoints(player):
    if player.score_start <= 0:
        player.is_playing = False
    else:
        return

def keepPlaying(player, answer):
    if answer == "y":
        return
    elif answer == "n":
        player.is_Playing = False

        

main()