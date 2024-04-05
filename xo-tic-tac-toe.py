from random import randrange

board = [[1,2,3],[4,"X",6],[7,8,9]]

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    # Printing board to the console
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |  ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |  ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |  ")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    while True:
        try:
            victory_for(board)
            display_board(board)
            free_num_result = make_list_of_free_fields(board)
            move = int(input("Enter an integer number (1-9): "))
            #print(free_num_result)
            while len(free_num_result) > 0:
                if victory_for(board):
                    break
                if move in free_num_result:
                    # zapisywanie nowego ruch
                    match move:
                        case 1:
                            board[0][0] = "O"
                            free_num_result.remove(move)
                            computer_move_gen(board)
                        case 2:
                            board[0][1] = "O"
                            free_num_result.remove(move)
                            computer_move_gen(board)
                        case 3:
                            board[0][2] = "O"
                            free_num_result.remove(move)
                            computer_move_gen(board)
                        case 4:
                            board[1][0] = "O"
                            free_num_result.remove(move)
                            computer_move_gen(board)
                        case 6:
                            board[1][2] = "O"
                            free_num_result.remove(move)
                            computer_move_gen(board)
                        case 7:
                            board[2][0] = "O"
                            free_num_result.remove(move)
                            computer_move_gen(board)
                        case 8:
                            board[2][1] = "O"
                            free_num_result.remove(move)
                            computer_move_gen(board)
                        case 9:
                            board[2][2] = "O"
                            free_num_result.remove(move)
                            computer_move_gen(board)
                        case _:
                            return "This value move is not possible"
                    # ruch komputera
                else:
                    print("This value isn't properly or is already occupied!")
                    move = int(input("Enter an integer number (1-9): "))
            break
        except:
            print("Warning: the value entered is not a valid number. Try again...")

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares_list = []
    free_num = []
    row_col_tuple = ()
    for elem in board:
        for val in elem:
            if val !="X" and val !="O":
                for row, sublist in enumerate(board):
                    if val in sublist:
                        free_num.append(val) 
                        
    return free_num

def computer_move_gen(board):
    # The function geneate the computer's move.
    victory_for(board)
    display_board(board)
    free_num_result = make_list_of_free_fields(board)
    computer_move = randrange(1, 10, 1)
    while len(free_num_result) > 0:
        if victory_for(board):
            break
        if computer_move in free_num_result:
            # zapisywanie nowego ruch
            match computer_move:
                case 1:
                    board[0][0] = "X"
                    free_num_result.remove(computer_move)
                    enter_move(board)
                case 2:
                    board[0][1] = "X"
                    free_num_result.remove(computer_move)
                    enter_move(board)
                case 3:
                    board[0][2] = "X"
                    free_num_result.remove(computer_move)
                    enter_move(board)
                case 4:
                    board[1][0] = "X"
                    free_num_result.remove(computer_move)
                    enter_move(board)
                case 5:
                    computer_move = randrange(1, 10, 1)
                case 6:
                    board[1][2] = "X"
                    free_num_result.remove(computer_move)
                    enter_move(board)
                case 7:
                    board[2][0] = "X"
                    free_num_result.remove(computer_move)
                    enter_move(board)
                case 8:
                    board[2][1] = "X"
                    free_num_result.remove(computer_move)
                    enter_move(board)
                case 9:
                    board[2][2] = "X"
                    free_num_result.remove(computer_move)
                    enter_move(board)
                case _:
                    return "This value move is not possible"
        else:
                #print("This value isn't properly or is already occupied!")
                computer_move = randrange(1, 10, 1)
                    
def victory_for(board):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pole_1 = board[0][0]
    pole_2 = board[0][1]
    pole_3 = board[0][2]
    pole_4 = board[1][0]
    pole_5 = board[1][1]
    pole_6 = board[1][2]
    pole_7 = board[2][0]
    pole_8 = board[2][1]
    pole_9 = board[2][2]

    if pole_1 == pole_2 == pole_3:
        if pole_1 == "O":
            print("You won!")
            return True
        else:
            print("Computer won!")
            return True
    elif pole_4 == pole_5 == pole_6:
        if pole_4 == "O":
            print("You won!")
            return True
        else:
            print("Computer won!")
            return True
    elif pole_7 == pole_8 == pole_9:
        if pole_7 == "O":
            print("You won!")
            return True
        else:
            print("Computer won!")
            return True
    elif pole_1 == pole_5 == pole_9:
        if pole_1 == "O":
            print("You won!")
            return True
        else:
            print("Computer won!")
            return True
    elif pole_3 == pole_5 == pole_7:
        if pole_3 == "O":
            print("You won!")
            return True
        else:
            print("Computer won!")
            return True
    elif pole_1 == pole_4 == pole_7:
        if pole_1 == "O":
            print("You won!")
            return True
        else:
            print("Computer won!")
            return True
    elif pole_2 == pole_5 == pole_8:
        if pole_2 == "O":
            print("You won!")
            return True
        else:
            print("Computer won!")
            return True
    elif pole_3 == pole_6 == pole_9:
        if pole_3 == "O":
            print("You won!")
            return True
        else:
            print("Computer won!")
            return True
    else:
        return False
    

    
print("Hello, let's start game!")
#display_board(board)
enter_move(board)
