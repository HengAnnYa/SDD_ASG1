
import random, json

# game variables

game_vars = {
    "turn" : 1,             # Current turn
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
    "shortform" : "0",
    "name" : "Park",
    "price" : 1
    }

road = {
    "shortform" : "*",
    "name" : "Road",
    "price" : 1
    }

scores = {
    1: {"name": "Annya", "score": 10},
    2: {"name": "Denise", "score": 10},
    3: {"name": "Harishma", "score": 10},
    4: {"name": "Eudora", "score": 10}
    }
with open('scores.json', 'w') as json_file:
        json.dump(scores, json_file)

position = 0
building = 0

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

#global boolean to end game
end_game = False

#global boolean to not end turn for :don't buy or invalid inputs
dont_end_turn = False

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
            else:
                first_line += "{:^5}|".format(space[0])
                second_line += "{:^5}|".format(space[1])
                
        print(letters[row], first_line)
        print(" ", second_line)
        print(connectline)

# option 5 function to display rules of game: 
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
    print("The scoring system is documented as follows:")
    print()
    print("Residential (R): If it is next to an industry (I), then it scores 1 point only.")
    print("                 Otherwise, it scores 1 point for each adjacent residential (R) or commercial (C),")
    print("                 and 2 points for each adjacent park (O).")
    print("Industry    (I): Scores 1 point per industry in the city.")
    print("                 Each industry generates 1 coin per residential building adjacent to it.")
    print("Commercial  (C): Scores 1 point per commercial adjacent to it.")
    print("                 Each commercial generates 1 coin per residential adjacent to it. ")
    print("Park (O): Scores 1 point per park adjacent to it.")
    print("Road (*): Scores 1 point per connected road (*) in the same row.")
    print("--------------------------------------------------")
    print()
    

#function to display_high_scores
def display_high_scores():
    ##scores = {i: f"Name{i}" for i in range(1, 11)}
    ##with open('scores.json', 'w') as json_file:
    ##    json.dump(scores, json_file)
    ##with open('scores.json', 'r') as json_file:
    ##        scores = json.load(json_file)
    ##        print("High Scores: ")
    ##        print(f"{'Rank':<2}  Name\tScore")
    ##        scores = {int(key): value for key, value in scores.items()}
    ##        sorted_scores = sorted(scores.keys(), reverse=True)
    ##        for rank, (key, value) in enumerate(scores.items(),start=1):
    ##            if value.startswith("Name"):
    ##                print(f"{rank:<2})   Empty\t0")
    ##            else:
    ##                for rank, key in enumerate(sorted_scores, start=1):
    ##                    print(f"{rank:<2})   {scores[key]}\t{key}")
    print("High Scores:")
    print("    Name      Score")
    print("1.  Annya     10")
    print("2.  Denise    10")
    print("3.  Harishma  10")
    print("4.  Eudora    10")
    print("5.  -----     --")
    print("6.  -----     --")
    print("7.  -----     --")
    print("8.  -----     --")
    print("9.  -----     --")
    print("10. -----     --")



# initialize game 
def initialize_game():
    game_vars["name"] = ""
    game_vars["turn"] = 1
    game_vars["buildings"] = 0
    game_vars["coins"] = 16
    game_vars["score"] = 0
    
# show in game menu while playing game
def show_game_menu(game_vars):
    print('Turn: {}     Score: {}'.format(game_vars["turn"], game_vars["score"]))
    print('Coins = {}     Buildings = {}/400'.format(game_vars["coins"],game_vars['buildings']))
    print("")
    print("1: Place a Building   2: Quit to menu")
    print("3: Save Game          4: View Rules")
    

###############################################################
#function to calculate score
def calculate_score(board):
    score = 0

    for row in range(20):
        for col in range(20):
            if board[row][col] == ['Resi', 'R']:
                adjacent_industry = count_adjacent_building(board, row, col, 'I')
                adjacent_residential = count_adjacent_building(board, row, col, 'R')
                adjacent_commercial = count_adjacent_building(board, row, col, 'C')
                adjacent_park = count_adjacent_building(board, row, col, '0')

                if adjacent_industry > 0 or adjacent_commercial > 0:
                    score += 1
                elif adjacent_park > 0:
                    score += 2
                else:
                    score += adjacent_residential

            elif board[row][col] == ['Ind', 'I']:
                score += 1

            elif board[row][col] == ['Comm', 'C']:
                score += count_adjacent_building(board, row, col, 'C')

            elif board[row][col] == ['Park', '0']:
                score += count_adjacent_building(board, row, col, '0')

            elif board[row][col] == ['Road', '*']:
                # Assuming all connected roads in the same row count as 1 point each
                score += 1
                
    return score

##############################################################3
# function
def count_adjacent_building(board, row, col, building_type):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if (dr != 0 or dc != 0) and 0 <= row + dr < 20 and 0 <= col + dc < 20:
                if board[row + dr][col + dc] == [building_type, None]:
                    count += 1
    #print(count);
    return count


# function to place building
# check if square is valid
# returns true if placement is successful

def place_building(board, position, building):
    global dont_end_turn
    able_to_place = False

    row = ord(position[0].upper()) - ord("A")
    column = int(position[1:]) - 1

    if building == "Residential" :
        longerName = "Resi"
        shorterName = "R"

    elif building == "Commercial" :
        longerName = "Comm"
        shorterName = "C"
            
    elif building == "Industry" :
        longerName = "Ind"
        shorterName = "I"
    
    elif building == "Park" :
        longerName = "Park"
        shorterName = "0"

    elif building == "Road" :
        longerName = "Road"
        shorterName = "*"

    if game_vars["turn"] > 1:
        able_to_place = False
        for y in range(-1, 2):
            for x in range(-1, 2):
                new_row = row + y
                new_column = column + x
                if 0 <= new_row < 20 and 0 <= new_column < 20 and board[new_row][new_column] != None:
                    able_to_place = True
                    # print(able_to_place)
                    
        if able_to_place:
            board[row][column] = [longerName, shorterName]
            game_vars["turn"] += 1
            ####################################testing
            game_vars["score"] = calculate_score(board)  # Update score here
            game_vars["buildings"] += 1
            #print("Current Score:", game_vars["score"])
        else:
            print("Invalid Position")
            dont_end_turn = True

    else:
        board[row][column] = [longerName, shorterName]
        game_vars["turn"] += 1
        game_vars["buildings"] += 1
        #######################################testing
        game_vars["score"] = calculate_score(board)  # Update score here
        #print("Current Score:", game_vars["score"])
    
# code to randomly select 2 building types for player to choose
buildings = ['Residential', 'Industry', 'Commercial', 'Park', 'Road']
def select_buildings():
    building1 = random.choice(buildings)
    building2 = random.choice(buildings)

    while building1 == building2:  # code to prevent duplicate options 
        building2 = random.choice(buildings) 
    
    return building1, building2

# function to buy building
def buy_building(board, game_vars):
    global dont_end_turn

    # randomly select 2 buildings for this turn
    building1, building2 = select_buildings()
    if building1 == "Residential":
        opt1 = residential["shortform"]
    elif building1 == "Industry":
        opt1 = industry["shortform"]
    elif building1 == "Commercial":
        opt1 = commercial["shortform"]
    elif building1 == "Park":
        opt1 = park["shortform"]
    elif building1 == "Road":
        opt1 = road["shortform"]
            
    if building2 == "Residential":
        opt2 = residential["shortform"]
    elif building2 == "Industry":
        opt2 = industry["shortform"]
    elif building2 == "Commercial":
        opt2 = commercial["shortform"]
    elif building2 == "Park":
        opt2 = park["shortform"]
    elif building2 == "Road":
        opt2 = road["shortform"]

    print("")
    print("Choose your building type: ({}) {} or ({}) {}. Cost: 1 coin".format(opt1, building1, opt2, building2))
    print("The unselected building will be discarded.")
    print("")
    building_choice = str(input("Your Choice? "))
    if building_choice == opt1:
        position = input("Place where?")
        if building_choice.upper() == residential["shortform"] and game_vars["coins"] >= 1:
            building = "Residential"
            if (place_building(board, position, building) == False): #check if there square is unoccupied
                dont_end_turn = True
                end_turn()
            else:
                #since place_unit function already called, no need to call again
                game_vars["coins"] = int(game_vars["coins"]) - 1
                dont_end_turn = False
        elif building_choice.upper() == industry["shortform"] and game_vars["coins"] >= 1:
            building = "Industry"
            if (place_building(board, position, building) == False): #check if there square is unoccupied
                dont_end_turn = True
            else:
                #since place_unit function already called, no need to call again
                game_vars["coins"] = int(game_vars["coins"]) - 1
                dont_end_turn = False
        elif building_choice.upper() == commercial["shortform"] and game_vars["coins"] >= 1:
            building = "Commercial"
            if (place_building(board, position, building) == False): #check if there square is unoccupied
                dont_end_turn = True
            else:
                #since place_unit function already called, no need to call again
                game_vars["coins"] = int(game_vars["coins"]) - 1
                dont_end_turn = False
        elif building_choice == park["shortform"] and game_vars["coins"] >= 1:
            building = "Park"
            if (place_building(board, position, building) == False): #check if there square is unoccupied
                dont_end_turn = True
            else:
                #since place_unit function already called, no need to call again
                game_vars["coins"] = int(game_vars["coins"]) - 1
                dont_end_turn = False
        elif building_choice == road["shortform"] and game_vars["coins"] >= 1:
            building = "Road"
            if (place_building(board, position, building) == False): #check if there square is unoccupied
                dont_end_turn = True
            else:
                #since place_unit function already called, no need to call again
                game_vars["coins"] = int(game_vars["coins"]) - 1
                dont_end_turn = False
        else:
            print("You do not have enough coins to buy this building. Game over")
            

    elif building_choice == opt2:
        position = input("Place where?")
        if building_choice.upper() == residential["shortform"] and game_vars["coins"] >= 1:
            building = "Residential"
            if (place_building(board, position, building) == False): #check if there square is unoccupied
                dont_end_turn = True
            else:
                #since place_unit function already called, no need to call again
                game_vars["coins"] = int(game_vars["coins"]) - 1
                dont_end_turn = False
        elif building_choice.upper() == industry["shortform"] and game_vars["coins"] >= 1:
            building = "Industry"
            if (place_building(board, position, building) == False): #check if there square is unoccupied
                dont_end_turn = True
            else:
                #since place_unit function already called, no need to call again
                game_vars["coins"] = int(game_vars["coins"]) - 1
                dont_end_turn = False
        elif building_choice.upper() == commercial["shortform"] and game_vars["coins"] >= 1:
            building = "Commercial"
            if (place_building(board, position, building) == False): #check if there square is unoccupied
                dont_end_turn = True
            else:
                #since place_unit function already called, no need to call again
                game_vars["coins"] = int(game_vars["coins"]) - 1
                dont_end_turn = False
        elif building_choice == park["shortform"] and game_vars["coins"] >= 1:
            building = "Park"
            if (place_building(board, position, building) == False): #check if there square is unoccupied
                dont_end_turn = True
            else:
                #since place_unit function already called, no need to call again
                game_vars["coins"] = int(game_vars["coins"]) - 1
                dont_end_turn = False
        elif building_choice == road["shortform"] and game_vars["coins"] >= 1:
            building = "Road"
            if (place_building(board, position, building) == False): #check if there square is unoccupied
                dont_end_turn = True
            else:
                #since place_unit function already called, no need to call again
                game_vars["coins"] = int(game_vars["coins"]) - 1
                dont_end_turn = False
        else:
            print("You do not have enough coins to buy this building. Game over")
            
    
    else:
        print("Invalid action.")
        dont_end_turn = True


#display game summary when game over - displays score, how many buildings you have
def game_summary():
    print("")
    print("-------- GAME SUMMARY --------")
    print("")
    print("Final Score: {}".format(game_vars["score"]))
    print("Buildings Placed: {}".format(game_vars["buildings"]))
    print("No. of Turns: {}".format(game_vars["turn"]))
    print("")
    print("------------------------------")

# save game 
def save_game(game_vars):
    data = open("save.txt", "w")
    data.write(str(board) + "\n" + str(game_vars))
    data.close()
    print("Game saved!")

#load saved game
def load_game(game_vars):
    data = open("save.txt", "r")
    line_count = 1
    for i in data:
        i = i.strip("\n")
        if line_count == 1:
            board = eval(i)
            line_count += 1
        elif line_count > 1:
            game_vars = eval(i)
    return game_vars, board

# end_turn()
# when turn ends -after buying and placing unit

def end_turn():

    if dont_end_turn == True: #for don't buy and any other invalid options (turn will not end)
        show_game_menu(game_vars)
    else:
        game_vars["turn"] += 1              

# MAIN CODE: START NEW GAME SESSION

option = 0
gamecontinue = False

while True:
    if (not(gamecontinue)):
        display_main_menu()
        option = int(input('Your choice? '))
        print("---------------------------------------")
        print("")
        scores = {i: f"Name{i}" for i in range(1, 11)}
        with open('scores.json', 'w') as json_file:
            json.dump(scores, json_file)
    elif gamecontinue:
        option = 1
    if option == 1:
        # method for initialise new game
        ended = False
        if (not(gamecontinue)):
            initialize_game()
        while not ended:
            display_game_board()
            ########################current_score = calculate_score(board)        
            show_game_menu(game_vars)
            game_vars['advance_time'] = False
            if game_vars["buildings"] == 400 or game_vars["coins"] == 0:
                print("Game Over!")
                game_summary()
                sorted_scores = sorted(scores.keys(), reverse=True)
                if game_vars["score"] > sorted_scores[-1]:
                    print("Congratulations, you're in the top 10!")
                    name = input("What's your name: ")
                    sorted_scores.append(game_vars["score"])
                    for key, value in list(scores.items()):
                        if value == sorted_scores[-1]:
                            del scores[key]                    
                with open('scores.json', 'w') as json_file:
                    json.dump(scores, json_file)
                print("Select an Option to Continue...")
                print("1: Exit to Menu       2: View Highscores")
                print("3: Quit Game")
                end_choice = int(input("Your Choice: "))
                # add function to display options to view summary and highscore etc
                if end_choice == 1:
                    ended = True
                    print("Returning to Main Menu...")
                    option = 0
                elif end_choice == 2:
                    with open('scores.json', 'r') as json_file:
                        scores = json.load(json_file)
                        #print("High Scores: ")
                        #print(f"{'Rank':<2}  Name\tScore")
                        display_high_scores()
                        scores = {int(key): value for key, value in scores.items()}
                        sorted_scores = sorted(scores.keys(), reverse=True)
                        #for rank, (key, value) in enumerate(scores.items(),start=1):
                        #    if value.startswith("Name"):
                        #        print(f"{rank:<2})   Empty\t0")
                        #    else:
                        #        for rank, key in enumerate(sorted_scores, start=1):
                        #            print(f"{rank:<2})   {scores[key]}\t{key}")
                        #            print("Returning to main menu...")
                    print("Returning to Main Menu...")
                    option = 0
                elif end_choice == 3:
                    ended = True
                    print("See you next time! Goodbye!")
                    break
                    
            
            if ended == True:
                break

            choice = int(input("Your choice? "))
            if choice == 1:  # Place building
                # function to buy and place building 
                # time passes
                
                if buy_building(board, game_vars) == True:
                    game_vars['advance_time'] = True
                    game_vars["turn"] += 1
            elif choice == 2: # Quit game
                selection = 0
                print("Are you sure you want to quit? Your game will not be saved.")
                print("1: Yes 2: No")
                selection = int(input('Your choice? '))
                if selection == 1:
                    ended = True
                    option = 0
                elif selection == 2:
                    continue
                
            elif choice == 3: # function to save game files
                save_game(game_vars)
                break
                
            elif choice == 4: # Display game rules
                display_game_rules()
                print("Returning to game...")
                continue

    elif option == 2:
    # method for load save game
        game_vars, board = load_game(game_vars)
        gamecontinue = True
        continue
    elif option == 3:
    # method for view highscore
        with open('scores.json', 'r') as json_file:
            scores = json.load(json_file)
        #print("High Scores: ")
        #print(f"{'Rank':<2}  Name\tScore")
        display_high_scores()
        scores = {int(key): value for key, value in scores.items()}
        sorted_scores = sorted(scores.keys(), reverse=True)
        #for rank, (key, value) in enumerate(scores.items(),start=1):
        #    if value.startswith("Name"):
        #        print(f"{rank:<2})   Empty\t0")
        #    else:
        #        for rank, key in enumerate(sorted_scores, start=1):
        #            print(f"{rank:<2})   {scores[key]}\t{key}")
        print("Returning to main menu...")

    elif option == 5:
        display_game_rules()
        print("Returning to main menu...")
    elif option == 4:
        selection = 0
        print("Are you sure you want to exit?")
        print("1: Yes 2: No")
        selection = int(input('Your choice? '))
        if selection == 2:
            print("Returning to main menu...")
        elif selection == 1:
            print("See you next time! Goodbye!")
            break
