import random as rand

class shuffle():

    def __init__(self, round_status):
        self.round_status = round_status
        self.deckordermt = None
        self.deckordercustom = None


        if self.round_status == 'End' or self.round_status == 0:
            self.shuffle()
        else:
            pass


    def shuffle(self):
        deckorder = list(range(1,53))
        self.deckordermt = rand.sample(deckorder, k=len(deckorder))
        return

def dealtexas(deckorder, playernum):
    deck = deckorder
    num = playernum
    deal1 = []
    deal2 = []

    for num in range(1,playernum+1):
        deal1.append(deck[0])
        deck.pop(0)

    for num in range(1,playernum+1):
        deal2.append(deck[0])
        deck.pop(0)
    return deck, deal1, deal2
