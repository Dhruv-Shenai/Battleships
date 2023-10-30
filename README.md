# Battleships
An Initial Attempt at Battleships, the game (against computer and simple text based)
#the aim of the code is to code battleships. I need to define a certain number of functions in order to do this. Initially i had just one boat in one location and once you get that you win. However this was too quick so i adapted to match the rules of the actual game
#X means you hit a dud (no ship), H means you hit a ship, O means not touched yet. S is where the ships are located
#functions: 
# 1) printing the board (i envision keeping this as a separate function as it is good practice and also may be useful for hiding the boats later)
# 2) Any guess and placing a ship must be on a valid location inside the bounds of the length of the board
# 3) When placing multiple ships, the ships cannot overlap each other, hence need a function for this
# 4) Next i want a function that checks if the boat can be placed on the board in the locaiton and orientation specified. 
# 5) randomly picks a location for the ships and places them all randomly, provided can_place_ship function is satisifed (you can place the ship here without overlaps/going off the edge of board)
# will continue randomly picking if not a valid location
# 6) plays battleships until guesses over or all boats hit. 
# I only recently learned that you can simplify if statements by using boolean... So I tried to utilise this in most of my functions. Also, this is the first code I have done that doesn't require numpy...
# Hardest part was envisioning how to not get them to overlap... I'm very happy to have got such a simple way to do it in the end.
