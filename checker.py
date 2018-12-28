import sqlite3 as sql

conn = sql.connect('PokerGameRooms.db')
cur = conn.cursor()

""" Retrieve room password and check the password is entered correctly. Output 1 if correct, 0 if not correct"""
def roompwcheck(roomname, pwinput):
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
""" Allow input that is not case sensitive and ignores spacing and allows abbreviations to the first letter of each word"""
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
    for value in explowlist:
        if value.isalpha() or value.isnumeric():
            expectstore.append(value)
        elif value == ' ':
            expabbstr.append(explowlist[count+1])
        else:
            pass
        count += 1

    expstr = ''.join(expectstore)
    expabbs = ''.join(expabbstr)

    if inpstr == expstr or inpstr == expabbs:
        output = 1
    return output

""" Check if the input option is within the list of options provided - based on numerical input only (for maxseat and maxbuyin)"""
def checkifoption(input, options):
    output = 0

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
    print(sb)
    print(bb)
blindconvert('10/20')
    

    


    


