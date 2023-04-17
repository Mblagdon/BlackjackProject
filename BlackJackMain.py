# import random and db
import random
import db

# a list of suit, rank, and point value for each card
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
pointValues = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

# the bet min and max
betMin = 5
betMax = 1000


# creating the deck as a list of lists
def deckCreation():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append([suit, rank, pointValues[rank]])
    return deck


# a function to deal the cards
def dealCard(hand, deck):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
    return hand, deck


# a function to get the bet amount
def getBetAmount(money):
    while True:
        try:
            bet = float(input(f"Enter the bet amount (minimum bet:{betMin}, maximum bet:{betMax}), current money: {money}: "))
            if bet < betMin:
                print(f"The minimum bet must be {betMin}.Please place a larger bet.")
            elif bet > betMax:
                print(f"The maximum bet must be {betMax}.Please place a smaller bet")
            elif bet > money:
                print("Your bet amount cannot be greater the your current money amount. Please place a smaller bet.")
            else:
                return bet
        except ValueError:
            print("Invalid input, please use a valid bet number.")


# added function to handle user purchasing more chips if their balance is below 0
def buyMoreChips(money):
    while True:
        try:
            if money < 5:
                userBuyBack = input("Would you like to purchase some more chips? (y/n)")
            else:
                userBuyBack = None
            if userBuyBack.lower() == "y":
                while True:
                    try:
                        addChips = int(input("Please enter the number of chips you would like to buy (min 5: "))
                        if addChips < 5:
                            print("The minimum amount of chips you can purchase is 5.")
                        elif addChips > 1000:
                            print("The maximum amount of chips you can purchase is 1000.")
                        else:
                            money += addChips
                            db.writeMoney(money)
                            return money
                    except ValueError:
                        print("Please enter a valid number.")
            elif userBuyBack.lower() == "n":
                return money
            else:
                print("Please enter Y or N.")
        except ValueError:
            print("Please enter Y or N.")


# function to handle point value of cards within hand
def pointsInHand(hand):
    points = 0
    numAces = 0
    """ if hand contains an Ace, check if total points would be greater than 21 with normal
    ace value of 11. If normal ace value of 11 would cause a bust, converts ace value to 1."""
    for card in hand:
        if card[1].startswith("Ace"):
            numAces += 1
        points += pointValues[card[1]]
    while numAces > 0 and points > 21:
        points -= 10
        numAces -= 1
    return points

def printCards(hand):

    for card in hand:
        print(f"\t{card[1]} of {card[0]}")
        print(f"\tTotal points: {pointsInHand(hand)}")


# function to operate the blackjack game
def playBlackjack():
    while True:
    # Read player's money from file
        try:
            money = db.readMoney()
    # if file isn't found, then set money to 1000.00
        except FileNotFoundError:
            money = 1000.0
    # loop to handle blackjack game
        while True:
        # check player balance
            if money < betMin:
                money = buyMoreChips(money)
            else:
                if money > 5:
                    break
        # get player's bet amount
        bet = getBetAmount(money)
        # deal cards to both player and dealer
        playerHand = []
        dealerHand = []
        deck = deckCreation()
        # shuffle deck
        random.shuffle(deck)
        # deal cards to player and dealer
        for i in range(2):
            playerHand, deck = dealCard(playerHand, deck)
            dealerHand, deck = dealCard(dealerHand, deck)
        # print player's hand
        print("Player's hand is:")
        printCards(playerHand)
        # print dealer's hand
        print("Dealer's hand is:")
        printCards([dealerHand[0]])
        print("Hidden Card")
        # check if player was dealt blackjack
        if pointsInHand(playerHand) == 21:
            print(f"Blackjack! You have won {round(bet * 1.5, 2)}")
            money += round(bet * 1.5, 2)
            db.writeMoney(money)
            continue
        # check if dealer was dealt blackjack
        if pointsInHand(dealerHand) == 21:
            print(f"Dealer has Blackjack! You lost your bet!")
            money -= bet
            db.writeMoney(money)
            continue

        # if player doesn't have blackjack, continue with game to hit or stand.
        while pointsInHand(playerHand) < 21:
            choice = input("Would you like to hit or stand? ")
            if choice.lower() == "hit":
                dealCard(playerHand)
                print("Player's hand: ")
                printCards(playerHand)
            elif choice.lower() == "stand":
                break
        # check to see if player busted after hit
        if pointsInHand(playerHand) > 21:
            print("You have busted! You lost your bet!")
            money -= bet
            db.writeMoney(money)
            continue
        # dealer's turn
        print("Dealer's hand: ")
        printCards(dealerHand)

        while pointsInHand(dealerHand) < 17:
            dealCard(dealerHand)
            print("Dealer's hand: ")
            printCards(dealerHand)
        # check to see if dealer busts
        if pointsInHand(dealerHand) > 21:
            print("The dealer has busted! You win!")
            money += bet
            db.writeMoney(money)
            continue
        # check to see if player wins
        if pointsInHand(playerHand) > pointsInHand(dealerHand):
            print("You win!")
            money += bet
            db.writeMoney(money)
        # check to see if dealer wins
        if pointsInHand(playerHand) < pointsInHand(dealerHand):
            print("Dealer wins!")
            money -= bet
            db.writeMoney(money)
        # if no one wins, it is a tie
        else:
            print("It's a tie!")
        # save player's money to file
        db.writeMoney(money)
        print("Your current balance is: ")
        # ask if player would like to play again
        playAgain = input("Play again? (y/n)")
        if playAgain.lower() != "y":
            print("Thank you for playing! See you next time! Goodbye!")
            break

def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    deck = deckCreation()
    hand = []
    hand, deck = dealCard(hand, deck)
    playBlackjack()

if __name__ == '__main__':
    main()

