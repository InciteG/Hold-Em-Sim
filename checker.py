import sqlite3 as sql
import card as c
from operator import itemgetter

conn = sql.connect('PokerGameRooms.db')
cur = conn.cursor()

def roompwexist(roomname):
    cur.execute('SELECT [Table Name] FROM [Table List]')
    roomex = cur.fetchall()
    roomlist = []
    roomoutput = 0 
    pwoutput = 0
    for n in roomex:
        for x in n:
            roomlist.append(x)
    for x in roomlist:
        if roomname == x:
            roomoutput = 1
    cur.execute('SELECT Password FROM [Table List] WHERE [Table Name] = "' + roomname +'"')
    pwch = cur.fetchone()
    l = list(pwch[0])
    for a in l:
        if l[0].isalpha or l[0].isnumeric:
            pwoutput = 1
    return roomoutput, pwoutput
    
""" Retrieve room password and check the password is entered correctly. Output 1 if correct, 0 if not correct"""
def pwcheck(roomname, pwinput):
    cur.execute('SELECT Password FROM [Table List] WHERE [Table Name] = "' + roomname +'";')
    pwcond = cur.fetchone()
    pwlist = list(pwcond)
    pwstr = '' .join(pwlist)
    output = 0
    if pwstr == pwinput:
        output = 1
    else: 
        pass
    return output
""" Allow input that is not case sensitive and ignores spacing and allows abbreviations to the first letter of each word and the first word of option"""
def inputcheck(input, expected):
    output = 0
    inlower = input.lower()
    inlowlist = list(inlower)
    inputstore = []
    for value in inlowlist:
        if value.isalpha() or value.isnumeric():
            inputstore.append(value)
        else:
            pass
    inpstr = ''.join(inputstore)
    
    expectedlow = expected.lower()
    explowlist = list(expectedlow)
    expectstore = []
    count = 0
    expabbstr = []
    expabbstr.append(explowlist[0])
    fw = []
    for value in explowlist:
        if value.isalpha() or value.isnumeric():
            expectstore.append(value)
        elif value == ' ':
            expabbstr.append(explowlist[count+1])
            fw.append(explowlist[0:count])
        else:
            pass
        count += 1
    fwstr = ''.join(fw[0])
    expstr = ''.join(expectstore)
    expabbs = ''.join(expabbstr)

    if inpstr == expstr or inpstr == expabbs or inpstr == fwstr:
        output = 1
    return output

""" Check if the input option is within the list of options provided - based on numerical input only (for maxseat and maxbuyin)"""
def checkifoption(input, options):
    output = 0
    chosen = 0
    for opt in options:
        if input == opt:
            output = 1
            chosen = opt
    return output, chosen

""" Converts blinds to a usable format. From a string to the variables, small_blind and big_blind"""

def blindconvert(blinds):
    blist = list(blinds)
    count = 0 
    splitnum = None
    for value in blist:
        if value == '/':
            splitnum = count
        else:
            pass
        count += 1
    sbl = blist[0:splitnum]
    sbst = ''.join(sbl)
    sb = float(sbst)
    bbl = blist[splitnum+1:]
    bbst = ''.join(bbl)
    bb = float(bbst)
    return sb, bb

def checkhandstrength(full):
    output = 0
    bestorder = []
    a = checkstf(full) #10, or #7, straight flush or straight
    if a[0] == 10:
        output = a[0]
        bestorder = a[1]

    elif a[0] == 0:
        b = checkdup(full)  #9 quad, #8 fullhouse, #5 trips, #4 two pair, #3 pair, 
        if b[0] >= 0 and b[0] < 6:
            c = checkstraight(full)
            if c[0] == 0:
                b=checkdup(full)
                if b[0] == 0:
                    d = checkhigh(full) 
                    output = d[0]
                    bestorder = d[1]
                else:
                    output = b[0]
                    bestorder = b[1]
            elif c[0] == 6:
                output = c[0]
                bestorder = c[1]
        elif b[0] > 7:
            output = b[0]
            bestorder = b[1]
    
    elif a[0] == 7:
        b = checkdup(full)  #9 quad, #8 fullhouse, #5 trips, #4 two pair, #3 pair, 
        if b[0] > 7:
            output = b[0]
            bestorder = b[1]
        elif b[0] < 7:
            output = a[0]
            bestorder = a[1]
    return output, bestorder

def checkhigh(fullhand):
    combine = []
    for card in fullhand:
        hold = []
        hold.append(c.Card(card).power)
        hold.append(c.Card(card).suit)
        combine.append(hold)
    combine.sort(reverse=True)
    bestseq = []
    for x,y in zip(combine, range(0,len(combine))):
        val = x[0]
        if y == 0:
            if val == combine[y+1][0]:
                pass
            else:
                bestseq.append(x)
        elif y > 0 and y < (len(combine)-1):
            if val == combine[y+1][0] or val == combine[y-1][0]:
                pass
            else:
                bestseq.append(x)
        elif y == len(combine):
            if val == combine[y-1][0]:
                pass
            else:
                bestseq.append(x)
    output = 2
    bestorder = [] #1-52 number, bestseq, power + suit
    for item in bestseq:
        bestorder.append(c.psreverse(item[0], item[1]))
    
    return output, bestorder

""" Checks hand+community for any duplicates and classifies hand strength based on duplicates found. Quads = handstrength of 9, fullhouse =8, etc. 
Outputs strongest sequence in card# format and in power,suit format
"""
def checkdup(fullhand):
    output = 0
    numrank = [0]*13
    storecomb = []
    for card in fullhand:
        hold = []
        hold.append(c.Card(card).power)
        hold.append(c.Card(card).suit)
        storecomb.append(hold)

    for i in range(0, (len(numrank) + 1)):
        for x in storecomb:
            if i == x[0]:
                y = numrank[i-1] + 1
                numrank[i-1] = y
    besthand = []
    pairs = 0
    trips = 0
    quads = 0
    for i,count in zip(numrank, range(1,len(numrank)+1)):
        if i == 4:                                          #quad cond
            quads +=1
            output = 9
            hold = []
            check = []
            for card in storecomb:     
                if card[0] == count:
                    besthand.append(card)
                else:                                   #add rest to check for high card
                    hold.append(card)
            for item, count in zip(hold, range(0, len(hold))): #sort to check for dup - if dup, checkhigh will remove all copies of a duplicate, so must remove duplicates except 1
                if count < (len(hold)-1):
                    if item[0] == hold[count+1][0]:
                        pass
                    else:
                        check.append(c.psreverse(item[0], item[1]))   #reconvert power,suit to card # for checkhigh input
                elif count == (len(hold)-1):
                    check.append(c.psreverse(item[0], item[1]))
            high = checkhigh(check)[2]
            besthand.append(high[0])
            
        elif i ==3: 
            trips +=1
        elif i ==2:
            pairs += 1 
        else:
            pass
    if output == 0 and trips >= 1:                       #trips cond
        if trips > 1 or (trips == 1 and pairs>=1):       #fullhouse cond - consideration for 2 trips
            output = 8
            hold = []
            for i,count in zip(numrank, range(1,len(numrank)+1)):
                if i >=2: 
                    for card in storecomb:
                        if card[0] == count:
                            hold.append(card)
                        else:
                            pass  
                else:
                    pass
            sorting = sorted(hold, key = itemgetter(0), reverse = True)
            print(sorting)
            trunc = sorting[0:5]
            for item in trunc:
                besthand.append(item)
        elif trips ==1 and pairs == 0:                          #single trips cond
            output = 5
            for i,count in zip(numrank, range(1,len(numrank)+1)):
                if i ==3: 
                    for card in storecomb:
                        if card[0] == count:
                            besthand.append(card)
                        else:
                            pass  
                else:
                    pass
            high = checkhigh(fullhand)[2]
            besthand.append(high[0])
            besthand.append(high[1])
    elif output ==0 and pairs >=1:                         #pairs and two pairs cond
        if pairs >= 2:
            output = 4
            hold = []
            checkhold =[]
            check = []
            for i,count in zip(numrank, range(1,len(numrank)+1)):
                if i ==2: 
                    for card in storecomb:
                        if card[0] == count:
                            hold.append(card)
                        else:
                            pass
                if i ==1:
                    for card in storecomb:
                        if card[0] == count:
                            checkhold.append(card)
                        else:
                            pass
                else:
                    pass
            sorting = sorted(hold, key = itemgetter(0), reverse = True)
            if len(sorting) == 4:
                trunc = sorting[0:4]
                for item in trunc:
                    besthand.append(item)
            elif len(sorting) == 6:
                trunc = sorting[0:4]
                for item in trunc:
                    besthand.append(item)
                addtocheck = sorting[4:6]
                for item in addtocheck:
                    checkhold.append(item)
            else:
                pass
            for item, count in zip(checkhold, range(0, len(checkhold))):
                if count < (len(checkhold)-1):
                    if item[0] == checkhold[count+1][0]:
                        pass
                    else:
                        check.append(c.psreverse(item[0], item[1]))
                elif count == (len(checkhold)-1):
                    check.append(c.psreverse(item[0], item[1]))
            high = checkhigh(check)[2]
            besthand.append(high[0])
        elif pairs ==1:
            output = 3
            for i,count in zip(numrank, range(1,len(numrank)+1)):
                if i == 2: 
                    for card in storecomb:
                        if card[0] == count:
                            besthand.append(card)
                        else:
                            pass
                else:
                    pass
            high = checkhigh(fullhand)[2]
            besthand.append(high[0])
            besthand.append(high[1])
            besthand.append(high[2])
    besthand = besthand[0:5]
    bestorder = [] #1-52 number, bestseq, power + suit
    for item in besthand:
        bestorder.append(c.psreverse(item[0], item[1]))

    return output, bestorder

def checkflush(fullhand):
    output = 0
    suitcheck = [0]*4
    suit = ['H', 'D', 'C', 'S']
    storecomb = []
    suited = []
    for card in fullhand:
        hold = []
        hold.append(c.Card(card).power)
        hold.append(c.Card(card).suit)
        storecomb.append(hold)
    
    
    for card in storecomb:
        if card[1] == 'H':
            suitcheck[0] += 1
        if card[1] == 'D':
            suitcheck[1] += 1
        if card[1] == 'C':
            suitcheck[2] += 1
        if card[1] == 'S':
            suitcheck[3] += 1
    for x,y in zip(suitcheck, range(0,len(suitcheck))):
        if x >= 5:
            output = 7
            for item in storecomb:
                if suit[y] == item[1]:
                    suited.append(item)
        else:
            pass
    return output, 
     
def checkstraight(fullhand):
    output = 0
    storehand = []
    bestorder = []
    besthand = []
    althand = []
    for card in fullhand:
        hold = []
        hold.append(c.Card(card).power)
        hold.append(c.Card(card).suit)
        storehand.append(hold)
    for card in storehand:
        store = card
        if store[0] == 13:
            new = [0,card[1]]
            althand.append(new)
        else:
            althand.append(card)
    sorting = sorted(storehand, key = itemgetter(0), reverse = True)
    altsort = sorted(althand, key = itemgetter(0), reverse = True)
    for card, count in zip(sorting[0:3], range(0,len(sorting[0:3]))):
        hold = []
        hold.append(card)
        for next,sub in zip(sorting[count+1:], range(1, (len(sorting)+1))):
            if (card[0] - sub) == next[0]:
                hold.append(next)
            else:
                pass
        sorthold = sorted(hold, key=itemgetter(0), reverse=True)
        if len(sorthold) >=5:
            output = 6
            for card in sorthold[0:5]:
                besthand.append(card)
            break
        else:
            pass
    if output == 0: 
        for card, count in zip(altsort[0:3], range(0,len(altsort[0:3]))):
            hold = []
            hold.append(card)
            for next,sub in zip(altsort[count+1:], range(1, (len(altsort)+1))):
                if (card[0] - sub) == next[0]:
                    hold.append(next)
                else:
                    pass
            sorthold = sorted(hold, key=itemgetter(0), reverse=True)
            if len(sorthold) >=5:
                output = 6
                for card in sorthold[0:5]:
                    besthand.append(card)
            else:
                pass
    else:
        pass

    for item in besthand:
        bestorder.append(c.psreverse(item[0], item[1]))    
    return output, bestorder

def checkstf(fullhand):
    output = 0
    suitcheck = [0]*4
    suit = ['H', 'D', 'C', 'S']
    storecomb = []
    suited = []
    suitcheckst = []
    bestorder = []
    besthand = []
    for card in fullhand:
        hold = []
        hold.append(c.Card(card).power)
        hold.append(c.Card(card).suit)
        storecomb.append(hold)
    
    for card in storecomb:
        if card[1] == 'H':
            suitcheck[0] += 1
        if card[1] == 'D':
            suitcheck[1] += 1
        if card[1] == 'C':
            suitcheck[2] += 1
        if card[1] == 'S':
            suitcheck[3] += 1

    for x,y in zip(suitcheck, range(0,len(suitcheck))):
        if x >= 5:
            output = 7
            for item in storecomb:
                if suit[y] == item[1]:
                    suited.append(item)
        else:
            pass
    if output ==7:
        for item in suited:
            suitcheckst.append(c.psreverse(item[0], item[1]))
        sthold = checkstraight(suitcheckst)
        if sthold[0] == 6:
            output = 10
            besthand = sthold[2]
        else:
            suitsort = sorted(suited, key=itemgetter(0), reverse = True)
            for item in suitsort[0:5]:
                besthand.append(item)
    else: 
        pass
    
    for item in besthand:
        bestorder.append(c.psreverse(item[0], item[1]))
    return output, bestorder

def checkwin(hands, screenname, community):
    comparelist = []
    highesthands = []
    winner = []
    winninghandlist = []
    for hand,name in zip(hands,screenname):
        full = hand+community
        strength = checkhandstrength(full)
        infohold = {
            'Screenname': name,
            'Hand Strength': strength[0],
            'Card Numbers': strength[1],
            'Readable Hand': strength[2]}
        comparelist.append(infohold)
    sortplayer = sorted(comparelist, key = itemgetter('Hand Strength'), reverse = True)
    for player in sortplayer:
        if player['Hand Strength'] == sortplayer[0]['Hand Strength']:
            highesthands.append(player)
            
    if len(highesthands) == 1:
        winner = highesthands[0]['Screenname']
        winninghand = highesthands[0]['Card Numbers']
    elif len(highesthands) > 1:
        win = deepcompare(highesthands)
        winner = win[0]
        winninghand = win[1]

    
    return winner, winninghand

def deepcompare(highesthands):
    compareinput = highesthands[0]['Hand Strength']
    if compareinput == 10:
        win = comparestf(highesthands)
    elif compareinput ==9:
        win = comparestf(highesthands)
    elif compareinput ==8:
        win = comparestf(highesthands)
    elif compareinput ==7:
        win = comparestf(highesthands)
    elif compareinput ==6:
        win = comparestf(highesthands)
    elif compareinput ==5:
        win = comparestf(highesthands)
    elif compareinput ==4:
        win = comparestf(highesthands)
    elif compareinput ==3:
        win = comparestf(highesthands)
    elif compareinput ==2:
        win = chigh(highesthands)
    
    return win

def chigh(highesethands):
    






    
hands = [[2, 1], [3,16] , [14, 23], [9,48]]
screenname = ['Sebastian', 'Qwerty123', 'Donavis', 'Richrich']
community = [29, 43, 36, 22, 13]
checkwin(hands, screenname, community)


    

        








# """ Convert word input of numerics to integer"""
# def strtonum(wordnumber):
#     wordlow = wordnumber.islower()
#     wordlowlist = list(wordlow)
#     for 

#     if wordlow == 'one':
#     elif wordlow =='two':
#     elif wordlow =='three':
#     elif wordlow =='four':
#     elif wordlow =='two':
#     elif wordlow =='two':
#     elif wordlow =='two':
#     elif wordlow =='two':
#     elif wordlow =='two':
#     elif wordlow =='two':
#     elif wordlow =='two':
#     elif wordlow =='two':
#     elif wordlow =='two':
#     elif wordlow =='two':

    

    


    


