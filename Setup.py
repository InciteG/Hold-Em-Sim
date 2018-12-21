""" Settings for Poker Game Type, Max People, Blinds, Buyin"""

def gamesetup():
    type = raw_input('Cash Game or Tournament')
    if type == 'Tournament':
        antesa = raw_input('Ante Start Amount')
        antescale = raw_input('Ante Scaling')
        antefreq = raw_input('Ante Frequency')
    game = raw_input('Texas Holdem, Pot Limit Omaha or Five Card Stud')
    blinds = raw_input("Blinds")
    blind_options = ['.05/.1', '.1/.2', '.2/.4', '.25/.5', '.5/1', '1/2', '1/3', '2/5', '5/10', '10/20']
    maxseat = raw_input("Max Seating")
    maxseat_options = [2,4,6,9,10]
    maxbuyin = raw_input("Max Buy-in (# of big blinds)")
    maxbuyin_options = [50, 100, 150, 200, 300, 1000, 9999999999]
    if type =='Texas Holdem':
        limit = raw_input('No Limit or Pot Limit')
        if limit == 'No Limit':
            if type == 'Tournament':
                tnltexasholdemsetup(blinds, maxseat, maxbuyin, antesa, antescale, antefreq):
            elif type == 'Cash Game':
                nltexasholdemsetup(blinds, maxseat, maxbuyin):
    #     elif limit == 'Pot Limit':
    #         if type == 'Tournament':
    #             tpltexasholdemsetup(blinds, maxseat, maxbuyin, antesa, antescale, antefreq):
    #         elif type == 'Cash Game':
    #             pltexasholdemsetup(blinds, maxseat, maxbuyin):
    # elif type == 'Pot Limit Omaha':
    #     if type == 'Tournament':
    #         tplomahasetup(blinds, maxseat, maxbuyin, antesa, antescale, antefreq):
    #     elif type == 'Cash Game':
    #         plomahasetup(blinds, maxseat, maxbuyin):
    # elif type == 'Five Card Stud':
    #     limit = raw_input('No Limit or Pot Limit')
    #     if limit == 'No Limit':
    #         nl5csetup()
    #     elif limit == 'Pot Limit':
    #         pl5csetup()

def nltexasholdemsetup(blinds, maxseat, maxbuyin):
    tab = table(maxseat)



    return

def tnltexasholdemsetup(blinds, maxseat, maxbuyin, antesa, antescale, antefreq):
    return

def profilesetup():
    user_id = raw_input("Choose a Screenname")
    bankroll = 0
    return user_id, bankroll

def gameplayersetup(table, blinds, maxbuyin, playerbankroll):
    seat_option = raw_input("Choose Seat")
    seat(seat_option, table)
    while True:
        buyin = raw_input("Buyin Amount")
        if buyin <= blinds*maxbuyin:
            newbankroll = playerbankroll - buyin
            break
        else:
            print("Error: Buyin Amount Invalid")
