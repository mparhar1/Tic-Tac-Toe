#Game: TIC-TAC-TOE

#Imports
from IPython.display import clear_output
import random

#Function's Purpose: Prints a 3x3 Tic-Tac-Toe Board
def display_board(board):
    #Clears the Previous Board
    clear_output()
    
    #Prints the Updated Board
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("---|---|---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("---|---|---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")


#Function's Purpose: Assigns Input Marker to Each Player
def player_input():
    #Variable Declaration
    marker = ""

    #Ask Player 1 to Choose Their Marker 
    while marker != "X" and marker != "O":
        marker = input("\nPlayer 1, please choose your marker (X or O): ")

        if marker != "X" and marker != "O":
            print("\nInvalid marker selected...\n")

    #Assign Selected Marker to Player 1
    player1 = marker
    
    #Assign the Other Marker to Player 2
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    #Return the Player's Marker
    return (player1, player2)


#Function's Purpose: Place the Player's Marker on the Board
def place_marker(board, marker, square):
    
    board[square] = marker


#Function's Purpose: Checks to See if a Player Has Won
def win_check(board, mark):
    
    return (
    #Checks Horizontally if a Player Won
    (board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or

    #Checks Vertically if a Player Won
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or

    #Checks Diagonally if a Player Won
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark) )


#Function's Purpose: Randomly Decide Who Goes First
def choose_first():
    
    #Randomly Pick: 0 or 1 
    flip = random.randint(0, 1)

    #Player 1 Goes First if 0; Player 2 Goes First if 1
    if flip == 0:
        return "\nPlayer 1"
    else:
        return "\nPlayer 2"


#Function's Purpose: Checks to See if the Chosen Square is Available
def space_check(board, square):
    
    #Return True if Square is Empty
    return board[square] == " "


#Function's Purpose: Checks to See if the Board is Full (Results in Tie Game)
def full_board_check(board):
    
    #Return False if Board is NOT Full
    for i in range(1, 10):
        if space_check(board, i):
            return False
    
    #Return True if Board is FULL
    return True


#Function's Purpose: Validates and Returns the square of the Selected Square
def player_choice(board):
    
    #Variable Declaration
    square = 0

    #Validates Square Until an Available Square is Selected
    while square not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, square):
        square = int(input("Please select a square (1-9): "))

    #Resturns Square
    return square


#Function's Purpose: Ask Players to Play Again; Create New Game or Terminate Accordingly
def replay():

    choice = ""
    
    while choice.lower() != "yes" and choice.lower() != "no":
        choice = input("\nWould you like to play again? Please enter Yes or No: ")

        if choice.lower() != "yes" and choice.lower() != "no":
            print("Invalid entry...")

    return choice.lower() == "yes"


#MAIN FUNCTION: Play Tic-Tac-Toe!
#Welcome Message
print('Welcome to TIC-TAC-TOE!')

#Game Logic
while True:
    #Set-Up the Game
    #Create the Board
    the_board = [" "] * 10
    #Let Players Choose Marker
    player1, player2 = player_input()
    #Determine Whos First
    turn = choose_first()
    print(turn + " gets the first turn")
    
    #Check if Players are Ready
    play_game = input("\nReady to play (Yes or No)? ")
    if play_game.lower() == "yes":
        game_on = True
    else:
        game_on = False

    #Game Play Logic
    while game_on:
        #Player 1's Turn
        if turn == "Player 1":
            #Show the Board
            display_board(the_board)

            #Choose a Square
            square = player_choice(the_board)

            #Plase the Marker on the Square
            place_marker(the_board, player1, square)

            #Check if Player 1 Won
            if win_check(the_board, player1):
                display_board(the_board)
                print("\nPLAYER 1 HAS WON!!!")
                game_on = False
            #Else If: Check if the Players Tied
            elif full_board_check(the_board):
                display_board(the_board)
                print("\nTie Game!")
                break
            #Else: Game Continues - Next Player's Turn
            else:
                turn = "Player 2"

        #Player 2's Turn
        else:
            #Show the Board
            display_board(the_board)

            #Choose a Square
            square = player_choice(the_board)

            #Plase the Marker on the Square
            place_marker(the_board, player2, square)

            #Check if Player 2 Won
            if win_check(the_board, player2):
                display_board(the_board)
                print("\nPLAYER 2 HAS WON!!!")
                game_on = False
            #Else If: Check if the Players Tied
            elif full_board_check(the_board):
                display_board(the_board)
                print("\nTie Game!")
                break
            #Else: Game Continues - Next Player's Turn
            else:
                turn = "Player 1"

    #Play Again?
    if not replay():
        break

#Closing Message
print("\nThanks for Playing!")
