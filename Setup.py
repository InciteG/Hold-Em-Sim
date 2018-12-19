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

    # if type =='Texas Holdem':
    #     limit = raw_input('No Limit or Pot Limit')
    #     if limit == 'No Limit':
    #         nltexasholdemsetup()
    #     elif limit == 'Pot Limit':
    #         pltexasholdemsetup()
    # elif type == 'Pot Limit Omaha':
    #     plomahasetup()
    # elif type == 'Five Card Stud':
    #     limit = raw_input('No Limit or Pot Limit')
    #     if limit == 'No Limit':
    #         nl5csetup()
    #     elif limit == 'Pot Limit':
    #         pl5csetup()
