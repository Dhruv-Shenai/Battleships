def print_board(board): #an alternative way I had to search up. I wanted spaces between my O/X/H/S on the board and so printing just the board wouldn't work. Useful to know for arrays with floats. 
    for row in board:
        print(" ".join(row)) #just prints all 10 columns and rows with a space in between

def is_valid_location(board, row, col): #either true or false and if is_valid_location(...) is true then this can be used
    return 0 <= row < len(board) and 0 <= col < len(board[0]) #has to be in the bounds of 1-10 or 0-9 in index

def does_ship_exist_here(board, row, col): #if ship already exists here then it should already have S in it
    return board[row][col] == "S" #S for ship

def can_place_ship(board, start_row, start_col, size, direction):
    if direction == "horizontal":
        return all(is_valid_location(board, start_row, start_col + i) and not does_ship_exist_here(board, start_row, start_col + i) for i in range(size)) #must be valid and not on top of another ship, returns true if it can be placed horizontally
    elif direction == "vertical":
        return all(is_valid_location(board, start_row + i, start_col) and not does_ship_exist_here(board, start_row + i, start_col) for i in range(size))
    else:
        return False #if false then the code later on will redo the random pick of row,column, vertical/horizontal until it gets one that works

def place_ship(board, size): #size= size of boat e.g. 2 if 2by1 ship
    ship_row = random.randint(0, len(board) - 1) #sets location of ship row
    ship_col = random.randint(0, len(board[0]) - 1) #sets location of ship column
    direction = random.choice(["horizontal", "vertical"]) #sets the direction of the ship

    while not can_place_ship(board, ship_row, ship_col, size, direction): #if you can't place ship then repeat the random pick until you have a location where you can actually place the ship
        ship_row = random.randint(0, len(board) - 1)
        ship_col = random.randint(0, len(board[0]) - 1)
        direction = random.choice(["horizontal", "vertical"])

    for i in range(size): #sets the boat down on the board
        if direction == "horizontal":
            shiplocations[ship_row][ship_col + i] = "S"
        elif direction == "vertical":
            shiplocations[ship_row + i][ship_col] = "S"

def play_battleship(board):
    print("Let's play Battleship!")
    howmanyshipsarehit=0
    difficulty=input('What would you like your difficulty to be? E for easy, M for medium, H for hard. (Caps sensitive) )
    if difficulty='E':
        difficulty=18
    if difficulty='M':
        difficulty=15
    if difficulty='H':
        difficulty=10
    for turn in range(num_large_boats*4+num_medium_boats*3+num_small_boats*2+difficulty):  # Allow enough turns to get each part of the ship, and 10 extra guesses
        print(f"Turn {turn + 1}")
        if howmanyshipsarehit==num_large_boats*4+num_medium_boats*3+num_small_boats*2:
            print("You sunk all the ships!!")
            break
        guess_row = int(input("Guess Row (1-10): ")) - 1 #makes it into python index
        guess_col = int(input("Guess Col (1-10): ")) - 1 #makes it into python index

        if is_valid_location(board, guess_row, guess_col):
            if shiplocations[guess_row][guess_col] == "S":  #if a ship is present here it will show S in the box
                print("Congratulations! You sunk my battleship!")
                board[guess_row][guess_col] = "H" #H for Hit
                howmanyshipsarehit=howmanyshipsarehit+1                  #tried 'ships hit' as a variable but didn't like how it looks ;)'
            else:
                print("Oops! You missed the battleship.")
                board[guess_row][guess_col] = "X"
        else:
            print("Oops! That's not even in the ocean.")

        print_board(board)
    print("Game Over")
    

#Sets up the board
board_size = 10 #10 by 10 board but can adjust
board = [["O"] * board_size for _ in range(board_size)] #makes a board size of 10 by 10
shiplocations = [["O"] * board_size for _ in range(board_size)] #stores the ship locations
#User inputs the number of boats
num_small_boats = int(input("Enter the number of small boats: ")) #when testing feel free to use 1,0,0 as then you only need three guesses to get the game over message...
num_medium_boats = int(input("Enter the number of medium boats: "))
num_large_boats = int(input("Enter the number of large boats: "))
#Places boats on the board using place_ship function
for _ in range(num_small_boats): #places small boats on map
    place_ship(board, size=2)

for _ in range(num_medium_boats): #places medium boats on map
    place_ship(board, size=3)

for _ in range(num_large_boats): #places large boats on map
    place_ship(board, size=4)


# Start the game
play_battleship(board)
