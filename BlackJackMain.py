# a function that stores a list of suit, rank, and point value for each card
def cardValues():
    deck = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    point_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]

    for suit in suits:
        for i in range(len(ranks)):
            card = [suit, ranks[i], point_values[i]]
            deck.append(card)
    print(deck)



def main():
    print("Blackjack Project")
    cardValues()

if __name__ == '__main__':
    main()
