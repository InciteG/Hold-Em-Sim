class Card():
    def __init__(self):
        card_rank = {
        1 : "2",
        2: "3",
        3: "4",
        4: "5",
        5: "6",
        6: "7",
        7: "8",
        8: "9",
        9: "10",
        10: "J",
        11: "Q",
        12: "K",
        13: "A"
        }
        card_suit = {
        1: "H", #hearts
        2: "D", #diamonds
        3: "C", #clubs
        4: "S", #spades
        }

        cardlist = []

        for (n,s) in card_suit.items():
            for (r,d) in card_rank.items():
                num = r + 13*(n-1)
                f = [d,s]
                cardlist.append(f)

        self.deck = cardlist

print(Card.deck)

