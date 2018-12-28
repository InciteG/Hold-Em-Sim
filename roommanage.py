import sqlite3 as sql
import checker 

conn = sql.connect('PokerGameRooms.db')
cur = conn.cursor()

""" Settings for Poker Game Type, Max People, Blinds, Buyin"""
# def joingame(user_id):
#     customorgeneral = raw_input("Join Public or Custom Game")
#     if customorgeneral =="Public":
#         showgenerallist()
#     else:
#         customname = raw_input("Please Enter Room Name")
#         check = checkpwexist(customname)
#         if check == True:
#             enterpw = raw_input("Please Enter Room Password")
#             checkpw(enterpw)
#             joinroom(customname)
#         else:
#             joinroom(customname)

# def joinroom(name):  
#     cur.execute('SELECT * FROM ['+ name + ']')
#     table = cur.fetchall()
#     return table

# def checkpwexist(name):
#     cur.execute('SELECT Password FROM [Table List] WHERE [Table Name] = [' + name + ']')
#     pwcond = cur.fetch()



def gamesetup():
    while True:
        choice1 = 'Cash Game'
        choice2 = 'Tournament'
        typein = input('Cash Game or Tournament')
        c1 = checker.inputcheck(typein, choice1)
        if c1 == 0:
            c2 = checker.inputcheck(typein, choice2)
            if c2 == 1:
                type = choice2
                antesa = input('Ante Start Amount')
                antescale = input('Ante Scaling')
                antefreq = input('Ante Frequency')
                break
            else:
                print('The input you have provided is invalid. Please try again.')
        else:
            type = choice1
            break
    while True:
        choice1= 'Texas Holdem'
        choice2 = 'Pot Limit Omaha'
        choice3 = 'Five Card Stud'
        gamein = input('Texas Holdem, Pot Limit Omaha or Five Card Stud')
        c1 = checker.inputcheck(gamein, choice1)
        if c1 == 0:
            c2 = checker.inputcheck(gamein, choice2)
            if c2 ==0:
                c3 = checker.inputcheck(gamein, choice3)
                if c3 == 1:
                    game = choice3
                    break
                else:
                    print('Input is invalid. Please try again.')
            else:
                game = choice2
                break
        else:
            game = choice1
            break
    while True:
        blindin = input("Blinds")
        blind_options = ['.05/.1', '.1/.2', '.2/.4', '.25/.5', '.5/1', '1/2', '1/3', '2/5', '5/10', '10/20']
        ver = checker.checkifoption(blindin, blind_options)
        if ver[0] == 1:
            blinds = ver[1]
            break
        else:
            print('Sorry. The option you have chosen is not supported here. Please try again.')
    
    while True:
        maxseatin = int(input("Max Seating"))
        maxseat_options = list(range(2,11))
        ver = checker.checkifoption(maxseatin, maxseat_options)
        if ver[0] == 1:
            maxseat = ver[1]
            break
        else: 
            print('The input is invalid. Please try again.')
    while True:
        maxbuyininput = int(input("Max Buy-in # of big blinds"))
        maxbuyin_options = [20, 40, 50, 100, 150, 200, 300, 500, 1000, 1500, 2000]
        ver = checker.checkifoption(maxbuyininput, maxbuyin_options)
        if ver[0] == 1:
            maxbuyin = ver[1]
            break
        else: 
            print('The input is invalid. Please try again.')

    # type = 'Cash Game'
    # game = 'Texas Holdem'
    # blinds = '10/20'
    # maxseat = 6
    # maxbuyin = 100
    if game =='Texas Holdem':
        while True:
            choice1 = 'No Limit'
            choice2 = 'Pot Limit'
            limitin = input('No Limit or Pot Limit')
            c1 = checker.inputcheck(limitin, choice1)
            if c1 == 0:
                c2 = checker.inputcheck(limitin, choice2)
                if c2 ==1:
                    limit = choice2
                    break
                else:
                    print('Input invalid. Please try again.')
            else:
                limit = choice1
                break
                
        # limit = 'No Limit'
        if limit == 'No Limit':
            if type == 'Tournament':
                tnltexasholdemsetup(blinds, maxseat, maxbuyin, antesa, antescale, antefreq)
            elif type == 'Cash Game':
                nltexasholdemsetup(blinds, maxseat, maxbuyin)
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
    table = [None]*maxseat
    position = range(1,len(table))
    room_name = input('Room name')
    room_pw = input('Room Password')
    tablehold = []
    seatnum  = []
    position = []
    stack = []
    status = []
    for i in range(1, len(table)+1):
        seatnum.append(i)
        position.append(-1)
        stack.append(0)
        status.append(0)
    
    for a,b,c,d,e in zip(seatnum, table, position, stack, status):
        listhold = [a,b,c,d,e]
        tablehold.append(listhold)
    
    if room_pw == None:
        cur.execute('CREATE TABLE IF NOT EXISTS [' + room_name + '](Seat INTEGER, Player TEXT, Position INTEGER, Stacksize TEXT, Status TEXT)')
        cur.executemany('INSERT INTO ['+ room_name + '](Seat,Player,Position,Stacksize,Status) VALUES (?,?,?,?,?)', (tablehold))
        cur.execute('INSERT INTO [Table List]([Table Name], Password, Blinds, [Poker Type], [Cash Style], Status, [Players Seated], [Max Seats]) VALUES (?,?,?,?,?,?,?,?)', (room_name,None,blinds,"No-limit Texas Hold'em","Cash Game","Public", 0, len(table)))
        conn.commit()
    else:
        cur.execute('CREATE TABLE IF NOT EXISTS [' + room_name + '](Seat INTEGER, Player TEXT, Position INTEGER, Stacksize TEXT, Status TEXT)')
        cur.executemany('INSERT INTO ['+ room_name + '](Seat, Player, Position, Stacksize, Status) VALUES (?,?,?,?,?)', (tablehold))
        cur.execute('INSERT INTO [Table List]([Table Name], Password, Blinds, [Poker Type], [Cash Style], Status, [Players Seated], [Max Seats]) VALUES (?,?,?,?,?,?,?,?)', (room_name,room_pw,blinds,"No-limit Texas Hold'em","Cash Game","Private", 0, len(table)))
        conn.commit()

def tnltexasholdemsetup(blinds, maxseat, maxbuyin, antesa, antescale, antefreq):
    return

def gameplayersetup(username, room_name, blinds, maxbuyin, playerbankroll):
    cur.execute('SELECT Seat FROM [' + room_name + ']')
    seating = cur.fetchall()
    print(seating)
    while True:
        seat_option = input("Choose Seat")
        if seating[seat_option] == None:
            cur.execute('UPDATE ['+ room_name + '] SET Player == ['+ username + '] WHERE Seat ==' + seat_option )
            break
        else:
            print('Sorry. There is someone already seated here. Please choose another seat')
    while True:
        buyin = input("Buyin Amount")
        if buyin <= blinds*maxbuyin and buyin <= playerbankroll:
            newbankroll = playerbankroll - buyin
            cur.execute('UPDATE [Poker User List] SET Bankroll = ' + newbankroll + ' WHERE Username ==' + username)
            cur.execute('UPDATE [' + room_name + '] SET Stack == [' + buyin + '] WHERE Player == [' + username + ']')
            conn.commit()
            break
        else:
            print("Error: Buyin Amount Invalid")
