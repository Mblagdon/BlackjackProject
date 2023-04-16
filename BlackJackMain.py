# import random and db
import random
import db

# a list of suit, rank, and point value for each card
deck = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
pointValues = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

# the bet min and max
betMin = 5
betMax = 1000


# creating the deck
def deckCreation():
    for suit in suits:
        for rank in ranks:
            deck.append([suit, rank, pointValues[rank]])


# a function to deal the cards
def dealCard(hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)


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
            if (money < 5):
            userBuyBack = input("Would you like to purchase some more chips? (y/n)")
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
    points = sum(card[1] for card in hand)
    """ if hand contains an Ace, check if total points would be greater than 21 with normal
    ace value of 11. If normal ace value of 11 would cause a bust, converts ace value to 1."""
    if card[0].startswith("Ace") and points > 21:
        points -= 10
    return points

# function to operate the blackjack game
def playBlackjack():
    pass



def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    try:
        money = db.readMoney()
    except FileNotFoundError:
        money = 100


if __name__ == '__main__':
    main()

    ERROR TESTING 2.0