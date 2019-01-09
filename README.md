# Poker Matchmaking Emulator

Purpose: Create a poker game simulator and emulate matchmaking environment provided by online services

# Completed Tasks:
  
  Card Classification:
    - Found in the cards.py file, class: Card
    - classifies cards based on number 1-52, presenting value(2 through Ace), suit(Heart, Club, Diamond, Spade) and strength( Ace is strongest, 2 is weakest)
    
   Dealing Texas Holdem:
   - Deals cards for preflop, flop, turn and river. Cards dealt and burnt removed from top of deck-list
   
   Create Room:
   - Based on values input, creates appropiate room (currently only supports texasholdem no limit)
   
   Input Check:
   - Ensures input by user is either recognized in appropiate format or request new input, checker.inputcheck
   - Checks if certain inputs are within desired input-conditions through checker.checkifoption 
   - Room PW Check:
      - obtains room password from database based on room name and assess whether correct password was input to join private room
      
   Winning Assessment:
   - Given a list of hands(list of hands from players who make it to showdown), determines the winning hand(s) to divide pot between individual or multiple winners
    
    

# In Progress Tasks:

  Table class presented to user - table info retrieved from database and placed into class read by user, changes update database
  Table action - call, fold, raise affect stack value and table 
  Join room functionality: - choose available seat, buyin subtract from user bankroll
  Leave room functionality:
  Profile management and user bankroll
  Graphical User Interface:
  
