#import random and db
import random
import db


# a list of suit, rank, and point value for each card

deck = []
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
point_values = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}

for suit in suits:
    for rank in ranks:
        deck.append([suit, rank, point_values[rank]])

def deal_card(hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)



def main():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")

    try:
        money = db.readMoney()
    except FileNotFoundError:
        money = 100


if __name__ == '__main__':
    main()
