class Card():
    def __init__(self, numr):
        self.cid = numr
        self.value = None
        self.suit = None
        self.power = None
        self.cdict = None
        self.classify()

    def classify(self):
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

        card_id = {}

        for (n,s) in card_suit.items():
            for (r,d) in card_rank.items():
                num = r + 13*(n-1)
                f = [d,s]
                card_id[num] = f

        self.cdict = card_id
        cardid = self.cid
        for (r,s) in card_id.items():
            if cardid == r:
                self.value = s[0]
                self.suit = s[1]
                for (t,v) in card_rank.items():
                    if s[0] == v:
                        self.power = t


def vsreverse(value, suit):
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
    card_id = {}
    output = 0
    for (n,s) in card_suit.items():
        for (r,d) in card_rank.items():
            num = r + 13*(n-1)
            f = [d,s]
            card_id[num] = f

    for (k,v) in card_id.items():
        if v == [value,suit]:
            output = k
    
    
    return output

def psreverse(power, suit):
    if power == 0:
            power = 13
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
    card_id = {}
    output = 0
    for (n,s) in card_suit.items():
        for (r,d) in card_rank.items():
            num = r + 13*(n-1)
            f = [r,s]
            card_id[num] = f

    for (k,v) in card_id.items():
        if v == [power, suit]:
            output = k
    return output


"""
Input:
x = Card(1)
print(x.value,x.suit, x.power)

Output:
2 H 1

"""

