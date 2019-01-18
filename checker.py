import sqlite3 as sql
import card as c
from operator import itemgetter

conn = sql.connect('PokerGameRooms.db')
cur = conn.cursor()

class Inputcheck():

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def checkifoption(input, options):
        output = 0
        chosen = 0
        for opt in options:
            if input == opt:
                output = 1
                chosen = opt
        return output, chosen


    @staticmethod
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

class HSC():
    """ Hand Strength Check"""

    def __init__(self, cards7):
        self.handstrength = None
        self.bestcomb = []
        self.hc = cards7
        self.checkhandstrength()
        

    def checkhandstrength(self):
        full = self.hc
        output = 0
        bestseq = []
        a = self.checkstf(full) #10, or #7, straight flush or straight
        if a[0] == 10:
            output = a[0]
            bestseq = a[1]
        elif a[0] == 0:
            b = self.checkdup(full)  #9 quad, #8 fullhouse, #5 trips, #4 two pair, #3 pair, 
            if b[0] >= 0 and b[0] < 6:
                c = self.checkstraight(full)
                if c[0] == 0:
                    b=self.checkdup(full)
                    if b[0] == 0:
                        d = self.checkhigh(full) 
                        output = d[0]
                        bestseq = d[1]
                    else:
                        output = b[0]
                        bestseq = b[1]
                elif c[0] == 6:
                    output = c[0]
                    bestseq = c[1]
            elif b[0] > 7:
                output = b[0]
                bestseq = b[1]
        
        elif a[0] == 7:
            b = self.checkdup(full)  #9 quad, #8 fullhouse, #5 trips, #4 two pair, #3 pair, 
            if b[0] > 7:
                output = b[0]
                bestseq = b[1]
            elif b[0] < 7:
                output = a[0]
                bestseq = a[1]
        self.handstrength = output
        self.bestcomb = bestseq
        return output, bestseq

    def checkhigh(self, fullhand):
        combine = fullhand
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
        
        return output, bestseq
            
    def checkdup(self, fullhand):
        output = 0
        numrank = [0]*13
        storecomb = fullhand

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
                            check.append([item[0], item[1]])   #reconvert power,suit to card # for checkhigh input
                    elif count == (len(hold)-1):
                        check.append([item[0], item[1]])
                high = self.checkhigh(check)[2]
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
                high = self.checkhigh(fullhand)[2]
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
                            check.append([item[0], item[1]])
                    elif count == (len(checkhold)-1):
                        check.append([item[0], item[1]])
                high = self.checkhigh(check)[2]
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
                high = self.checkhigh(fullhand)[2]
                besthand.append(high[0])
                besthand.append(high[1])
                besthand.append(high[2])
        besthand = besthand[0:5]

        return output, besthand

    def checkflush(self,fullhand):
        output = 0
        suitcheck = [0]*4
        suit = ['H', 'D', 'C', 'S']
        storecomb = fullhand
        suited = []
        
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
        
    def checkstraight(self,fullhand):
        output = 0
        storehand = fullhand
        besthand = []
        althand = []
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

        return output, besthand

    def checkstf(self,fullhand):
        output = 0
        suitcheck = [0]*4
        suit = ['H', 'D', 'C', 'S']
        storecomb = fullhand
        suited = []
        suitcheckst = []
        besthand = []
        
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
                suitcheckst.append([item[0], item[1]])
            sthold = self.checkstraight(suitcheckst)
            if sthold[0] == 6:
                output = 10
                besthand = sthold[2]
            else:
                suitsort = sorted(suited, key=itemgetter(0), reverse = True)
                for item in suitsort[0:5]:
                    besthand.append(item)
        else: 
            pass
        
        return output, besthand

class Wincheck(HSC):

    def __init__(self, tablename):
        self.winners = []
        self.winninghands = []
        self.tableto = tablename

def checkwin(hands, screenname, community):
    comparelist = []
    highesthands = []
    for hand,name in zip(hands,screenname):
        full = hand+community
        strength = HSC.checkhandstrength(full)
        infohold = {
            'Screenname': name,
            'Hand Strength': strength[0],
            'Readable Hand': strength[1]}
        comparelist.append(infohold)
    sortplayer = sorted(comparelist, key = itemgetter('Hand Strength'), reverse = True)
    for player in sortplayer:
        if player['Hand Strength'] == sortplayer[0]['Hand Strength']:
            highesthands.append(player)
            
    if len(highesthands) == 1:
        win= highesthands[0]
    elif len(highesthands) > 1:
        win = deepcompare(highesthands)
    
    return win

def deepcompare(highesthands):
    compareinput = highesthands[0]['Hand Strength']
    if compareinput == 10 or compareinput== 2 or compareinput== 6 or compareinput== 7:
        win = chigh(highesthands)
    elif compareinput ==9 or compareinput == 8:
        win = cquadorfh(highesthands)
    elif compareinput ==5 or compareinput ==4:
        win = ctriptwo(highesthands)
    elif compareinput ==3:
        win = cpair(highesthands)
    
    return win

def chigh(highesthands):
    comparelist = []
    winners = []
    for item in highesthands:
        hold = []
        hold.append(item['Screenname'])
        hold.append(sorted(item['Readable Hand'], key = itemgetter(0), reverse = True))
        comparelist.append(hold)

    strongest = comparelist[0]
    hold = [strongest]

    for np, count in zip(comparelist[1:], range(0,len(comparelist[1:]))):
        for cards, npcard, nc in zip(strongest[1], np[1], range(0,5)):
            if cards[0] > npcard[0]:
                break
            elif cards[0] == npcard[0] and nc <4:
                pass
            elif cards[0] < npcard[0]:
                strongest = [np]
                hold = [strongest]
                break
            elif cards[0] == npcard[0] and nc ==4:
                hold.append(np)
                break
    for item in hold:
        for player in highesthands:
            if item[0] == player['Screenname']:
                winners.append(player)
            else:
                pass

    return winners

def cquadorfh(highesthands):
    comparelist = []
    winners = []
    for item in highesthands:
        hold = []
        hold.append(item['Screenname'])
        hold.append(item['Readable Hand'])
        comparelist.append(hold)
    strongest = comparelist[0]
    hold = [strongest]
    for np in comparelist[1:]:
        if strongest[1][0][0] > np[1][0][0]:
            pass
        elif strongest[1][0][0] < np[1][0][0]:
            strongest = np
            hold = [strongest]
        elif strongest[1][0][0] == np[1][0][0]:
            if strongest[1][4][0] > np[1][4][0]:
                pass
            elif strongest[1][4][0] < np[1][4][0]:
                strongest = np
                hold = [strongest]
            elif strongest[1][4][0] == np[1][4][0]:
                hold.append(np)
    for item in hold:
        for player in highesthands:
            if item[0] == player['Screenname']:
                winners.append(player)
            else:
                pass

    return winners

def ctriptwo(highesthands):
    comparelist = []
    winners = []
    for item in highesthands:
        hold = []
        hold.append(item['Screenname'])
        hold.append(item['Readable Hand'])
        comparelist.append(hold)
    strongest = comparelist[0]
    hold = [strongest]
    for np in comparelist[1:]:
        if strongest[1][0][0] > np[1][0][0]:
            pass
        elif strongest[1][0][0] < np[1][0][0]:
            strongest = np
            hold = [strongest]
        elif strongest[1][0][0] == np[1][0][0]:
            if strongest[1][3][0] > np[1][3][0]:
                pass
            elif strongest[1][3][0] < np[1][3][0]:
                strongest = np
                hold = [strongest]
            elif strongest[1][3][0] == np[1][3][0]:
                if strongest[1][4][0] > np[1][4][0]:
                    pass
                elif strongest[1][4][0] < np[1][4][0]:
                    strongest = np
                    hold = [strongest]
                elif strongest[1][4][0] == np[1][4][0]:
                    hold.append(np)
                
    for item in hold:
        for player in highesthands:
            if item[0] == player['Screenname']:
                winners.append(player)
            else:
                pass

    return winners

def cpair(highesthands):
    comparelist = []
    winners = []
    for item in highesthands:
        hold = []
        hold.append(item['Screenname'])
        hold.append(item['Readable Hand'])
        comparelist.append(hold)
    strongest = comparelist[0]
    hold = [strongest]
    for np in comparelist[1:]:
        if strongest[1][0][0] > np[1][0][0]:
            pass
        elif strongest[1][0][0] < np[1][0][0]:
            strongest = np
            hold = [strongest]
        elif strongest[1][0][0] == np[1][0][0]:
            if strongest[1][2][0] > np[1][2][0]:
                pass
            elif strongest[1][2][0] < np[1][2][0]:
                strongest = np
                hold = [strongest]
            elif strongest[1][2][0] == np[1][2][0]:
                if strongest[1][3][0] > np[1][3][0]:
                    pass
                elif strongest[1][3][0] < np[1][3][0]:
                    strongest = np
                    hold = [strongest]
                elif strongest[1][4][0] == np[1][4][0]:
                    if strongest[1][4][0] > np[1][4][0]:
                        pass
                    elif strongest[1][4][0] < np[1][4][0]:
                        strongest = np
                        hold = [strongest]
                    elif strongest[1][4][0] == np[1][4][0]:
                        hold.append(np)
                
    for item in hold:
        for player in highesthands:
            if item[0] == player['Screenname']:
                winners.append(player)
            else:
                pass

    return winners


    






    
# hands = [[2, 43], [11,12] , [37, 25], [9,10]]
# read = []
# for item in hands:
#     hold = []
#     for card in item:
#         store = []
#         store.append(c.Card(card).power)
#         store.append(c.Card(card).suit)
#         hold.append(store)
#     read.append(hold)
# print(read)
# screenname = ['Sebastian', 'Qwerty123', 'Donavis', 'Richrich']
# community = [3, 17, 24, 52, 5]
# comread = []
# for item in community:
#     store = []
#     store.append(c.Card(item).power)
#     store.append(c.Card(item).suit)
#     comread.append(store)
# print(comread)

# z = checkwin(hands, screenname, community)
# print(z)


    

        








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

    

    


    


