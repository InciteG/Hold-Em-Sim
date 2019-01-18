import random as rand

class Deck:

    def __init__(self, table):
        self.deckorder = None
        self.cardsout = None
        self.tableserve = table

    @staticmethod
    def shuffle(self):
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
            13: "A",
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
                f = [d,s]
                cardlist.append(f)
        self.deckorder = rand.sample(cardlist, k=len(cardlist))
        return self.deckorder

    @classmethod
    def texaspre(self, deck):
        deck = deck
        cardout = deck[0]
        deck.pop(0)
        self.deckorder = deck
        return deck, cardout

    @classmethod
    def texasflop(self, deck):
        dealtdeck = deck
        dealtdeck.pop(0) #burn
        community = []
        
        for i in range(1,4):
            community.append(dealtdeck[0])
            dealtdeck.pop(0)

        self.cardsout = community
        self.deckorder = dealtdeck
        return dealtdeck, community

    @classmethod
    def texasturn(self, deck):
        dealtdeck = deck
        dealtdeck.pop(0) #burn 2
        community = deck[0]
        dealtdeck.pop(0)
        self.cardsout = community
        self.deckorder = dealtdeck
        return dealtdeck, community

    @classmethod
    def texasriver(self, deck):
        dealtdeck = deck
        dealtdeck.pop(0) #burn 2
        community = deck[0]
        dealtdeck.pop(0)
        deal_status = 0
        self.cardsout = community
        self.deckorder = dealtdeck
        return dealtdeck, community, deal_status
