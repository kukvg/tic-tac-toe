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
    while True:
        try:
            display_board(board)
            free_num_result = make_list_of_free_fields(board)
            move = input("Enter an integer number (1-9): ").strip()  # Usunięcie białych znaków z początku i końca
            if move and move.isdigit():  # Sprawdzenie, czy wartość nie jest pusta i czy jest liczbą
                move = int(move)
                if move in free_num_result:
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
                        case 5:
                            board[1][1] = "O"
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
                            print("This value move is not possible")
                    break
                else:
                    print("This value isn't properly or is already occupied!")
            else:
                print("Warning: please enter a valid integer number (1-9).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


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
    display_board(board)
    free_num_result = make_list_of_free_fields(board)
    computer_move = randrange(1, 10, 1)
    #print("Free:",free_num_result)
    #print("comp:", computer_move)
    while len(free_num_result) > 0:
        if computer_move in free_num_result:
            # zapisywanie nowego ruch
            #print("w while przed match")
            match computer_move:
                case 1:
                    board[0][0] = "X"
                    free_num_result.remove(computer_move)
                    enter_move(board)
                case 2:
                    board[0][1] = "X"
                    free_num_result.remove(computer_move)
                    #print(free_num_result)
                    enter_move(board)
                case 3:
                    board[0][2] = "X"
                    free_num_result.remove(computer_move)
                    #print(free_num_result)
                    enter_move(board)
                case 4:
                    board[1][0] = "X"
                    free_num_result.remove(computer_move)
                    #print(free_num_result)
                    enter_move(board)
                case 5:
                    computer_move = randrange(1, 10, 1)
                case 6:
                    board[1][2] = "X"
                    free_num_result.remove(computer_move)
                    #print(free_num_result)
                    enter_move(board)
                case 7:
                    board[2][0] = "X"
                    free_num_result.remove(computer_move)
                    #print(free_num_result)
                    enter_move(board)
                case 8:
                    board[2][1] = "X"
                    free_num_result.remove(computer_move)
                    #print(free_num_result)
                    enter_move(board)
                case 9:
                    board[2][2] = "X"
                    free_num_result.remove(computer_move)
                    #print(free_num_result)
                    enter_move(board)
                case _:
                    return "This value move is not possible"
        else:
                #print("This value isn't properly or is already occupied!")
                computer_move = randrange(1, 10, 1)
                    
print("Hello, let's start game!")
#display_board(board)
enter_move(board)

