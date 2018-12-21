def texaspre(deckorder, playernum):
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

def texasflop(deck):
    dealtdeck = deck
    dealtdeck.pop(0) #burn
    community = []

    for num in range(1,4):
        community.append(deck[0])
        dealtdeck.pop(0)
    return dealtdeck, community

def texasturn(deck, community):
    dealtdeck = deck
    dealtdeck.pop(0) #burn 2
    community = []
    community.append(deck[0])
    dealtdeck.pop(0)
    return dealtdeck, community

def texasriver(deck, community):
    dealtdeck = deck
    dealtdeck.pop(0) #burn 2
    community = []
    community.append(deck[0])
    dealtdeck.pop(0)
    deal_status = 0
    return dealtdeck, community, deal_status

def omaha(deckorder, playernum):
    deck = deckorder
    num = playernum +1
    deal1 = []
    deal2 = []
    deal3 = []
    deal4 = []

    for num in range(1,num):
        deal1.append(deck[0])
        deck.pop(0)

    for num in range(1,num):
        deal2.append(deck[0])
        deck.pop(0)

    for num in range(1,num):
        deal3.append(deck[0])
        deck.pop(0)

    for num in range(1,num):
        deal4.append(deck[0])
        deck.pop(0)
    return deck, deal1, deal2, deal3, deal4

def fivecard(deckorder, playernum):
    return
