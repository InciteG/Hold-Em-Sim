import card
import deal
import deck
import roommanage
import profile
import round
import pokerengine as pke
import table

pke.setuserdb()
pke.settabledb()

while True:
    joinorcreate = input("Join or Create Game")
    if joinorcreate == "Join Game" or joinorcreate == "Join":
        break
    elif joinorcreate == "Create Game" or joinorcreate == "Create":
        roommanage.gamesetup()
        break
    else:
        print("Error. Input in incorrect format. Please try again.")