
import random

# game variables

game_vars = {
    "turn" : 0,             # Current turn
    "coins" : 16,           # Coins for purchasing buildings
    "buildings" : 0,        # No of buildings placed
    "score": 0,             # Amount of points earnt by player
    "advance_time" : False
    }

residential = {
    "shortform" : "R",      
    "name" : "Residential",
    "price" : 1            # Amt of coins needed to build the building
    }

industry = {
    "shortform" : "I",
    "name" : "Industry",
    "price" : 1
    }

commercial = {
    "shortform" : "C",
    "name" : "Commercial",
    "price" : 1
    }

park = {
    "shortform" : 0,
    "name" : "Park",
    "price" : 1
    }

road = {
    "shortform" : "*",
    "name" : "Road",
    "price" : 1
    }

board = [ [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None]]



# function to display main menu
def display_main_menu():
    print()
    print("------ Welcome to Ngee Ann City! ------")
    print("    ")
    print("Select an option to continue:")
    print("---------------------------------------")
    print("1: Start new Game     2: Load save game")
    print("3: View High Scores   4: Exit Game")
    print("5: Rules")
    print("---------------------------------------")

# function to display game board
def display_game_board():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    print("     1     2     3     4     5     6     7     8     9     10    11    12    13    14    15    16    17    18    19    20")
    
    connectline= "  +"
    for row in range (len(board[0])):
        connectline += "-----+"
    print(connectline)
    for row in range (len(board)):
        first_line = "|"
        second_line = "|"
        for space in board[row]:
            if space == None:
                first_line += "     |"
                second_line += "     |"
                
        print(letters[row], first_line)
        print(" ", second_line)
        print(connectline)

# option 5 function: 
def display_game_rules():
    print("------------------- Game Rules -------------------")
    print()
    print("OBJECTIVE:")
    print("The player will play as the mayor of Ngee Ann City.")
    print("Your objective is to place buildings in order to build a city that scores as many points as possible.")
    print()
    print("RULES AND PROGRESSION:")
    print("- The player will start the game with 16 coins.")
    print("- In each turn, the player will construct one of two randomly-selected buildings in the 20x20 city.")
    print("- For the first building, the player can build anywhere in the city.")
    print("- For subsequent constructions, the player can only build on squares that are connected to existing buildings.")
    print("- Each construction will cost 1 coin. The other building that was not built will be discarded.")
    print("- There are 5 types of buildings available to the player, each of which gives the player a different score.")
    print("- The game ends when the player runs out of coins or fills up the board.")
    print()
    print("SCORING SYSTEM:")
    print("The scoring system is documented below as follows:")
    print()
    print("Residential (R): If it is next to an industry (I), then it scores 1 point only.")
    print("                 Otherwise, it scores 1 point for each adjacent residential (R) or commercial (C),")
    print("                 and 2 points for each adjacent park (O).")
    print("Industry (I):    Scores 1 point per industry in the city.")
    print("                 Each industry generates 1 coin per residential building adjacent to it.")
    print("Commercial (C):  Scores 1 point per commercial adjacent to it.")
    print("                 Each commercial generates 1 coin per residential adjacent to it. ")
    print("Park (O): Scores 1 point per park adjacent to it.")
    print("Road (*): Scores 1 point per connected road (*) in the same row.")
    print("--------------------------------------------------")
    print()
    

# initialize game 
def initialize_game():
    game_vars["turn"] = 0
    game_vars["buildings"] = 0
    game_vars["coins"] = 16
    game_vars["score"] = 0
    
# show in game menu while playing game
def show_game_menu(game_vars):
    print('Turn: {}     Score: {}'.format(game_vars["turn"]+1, game_vars["score"]))
    print('Coins = {}     Buildings = {}/400'.format(game_vars["coins"],game_vars['score']))
    print("1: Place a Building   2: Quit to menu")
    print("3: Save Game          4: View Rules")


# MAIN CODE: START NEW GAME SESSION
 
option = 0

while option != 1 and option != 2:
    display_main_menu()
    option = int(input('Your choice? '))
    print("---------------------------------------")
    print("")
    if option == 1:
        # method for initialise new game
        ended = False
        initialize_game()
        while not ended:
            display_game_board()        
            show_game_menu(game_vars)
            game_vars['advance_time'] = False
            if game_vars["buildings"] == 400 or game_vars["coins"] == 0:
                print("Game Over! Select an Option to Continue...")
                # add function to display options to view summary and highscore etc
                ended = True
            
            if ended == True:
                break

            choice = int(input("Your choice?"))
            if choice == 1:  # Place building
                # function to buy and place building 
                # time passes
                #buy_building(board, game_vars)
                #if place_building(board, position, name) == True:
                    #game_vars['advance_time'] = True
                print("Placeholder to prevent error")
                
            elif choice == 2: # Quit game
                selection = 0
                print("Are you sure you want to quit? Your game will not be saved.")
                print("1: Yes 2: No")
                selection = int(input('Your choice?'))
                if selection == 1:
                    ended = True
                    option = 0
                elif selection == 2:
                    continue
                
            elif choice == 3: # function to save game files
                print("Placeholder")
                
            elif choice == 4: # Display game rules
                display_game_rules()
                print("Returning to game...")
                continue

    elif option == 2:
    # method for load save game
        print("This is a placeholder so theres no error")
    elif option == 3:
    # method for view highscore
        print("This is a placeholder so theres no error")
    elif option == 5:
        display_game_rules()
        print("Returning to main menu...")
    elif option == 4:
        selection = 0
        print("Are you sure you want to exit?")
        print("1: Yes 2: No")
        selection = int(input('Your choice?'))
        if selection == 2:
            print("Returning to main menu...")
        elif selection == 1:
            print("See you next time! Goodbye!")
            break



