# import random and db
import random
import db

# a list of suit, rank, and point value for each card
deck = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
point_values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

# the bet min and max
betMin = 5
betMax = 1000


# creating the deck
def deckCreation():
    for suit in suits:
        for rank in ranks:
            deck.append([suit, rank, point_values[rank]])


# a function to deal the cards
def deal_card(hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)


# a function to get the bet amount
def get_bet_amount(money):
    while True:
        try:
            bet = float(input(f"Enter the bet amount (minimum bet:{betMin}, maximum bet:{betMax}, current money: {money}: "))
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



def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    try:
        money = db.readMoney()
    except FileNotFoundError:
        money = 100


if __name__ == '__main__':
    main()

    ERROR TESTING