
# Tic-Tac-Toe Game

## Introduction

Welcome to the Tic-Tac-Toe game! This is a classic game of Tic-Tac-Toe where you play against the computer. The game board is a 3x3 grid where you can place your 'O' and the computer will place its 'X'. The first to align three of their symbols horizontally, vertically, or diagonally wins.

## Features

- **Player vs Computer:** Play against a computer opponent that makes random moves.
- **Game Display:** The board is displayed in the console with clear visual representation.
- **Victory Check:** The game automatically detects and announces the winner or if the game is a draw.

## Requirements

- Python 3.x

## Installation

To play the game, you need to have Python 3 installed on your system. No additional libraries are required. You can run the script directly with Python.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/kukvg/tic-tac-toe.git
   ```


2. **Run the Script:**

   ```bash
   python tic_tac_toe.py
   ```

3. **Follow the Prompts:**

   - Enter an integer between 1 and 9 to make your move. Each number corresponds to a position on the board:
     ```
     1 | 2 | 3
     ---------
     4 | 5 | 6
     ---------
     7 | 8 | 9
     ```
   - The computer will make its move automatically after you make yours.
   - The game will display who won or if it's a draw.

## Code Explanation

### Main Functions

- **`display_board(board)`**
  - Displays the current state of the game board in the console.

- **`enter_move(board)`**
  - Handles the player's input and updates the board. Also invokes the computer's move after a valid player move.

- **`make_list_of_free_fields(board)`**
  - Generates a list of free positions on the board where a move can be made.

- **`computer_move_gen(board)`**
  - Generates a random move for the computer and updates the board accordingly.

- **`victory_for(board)`**
  - Checks the board to determine if there's a winner or if the game is still ongoing.

## Example

Here's a brief example of what the game might look like in the console:

```
Hello, let's start game!
Enter an integer number (1-9): 5
+-------+-------+-------+
|       |       |       |
|  1    |  2    |  3    |  
|       |       |       |
+-------+-------+-------+
|       |       |       |
|  4    |  O    |  6    |  
|       |       |       |
+-------+-------+-------+
|       |       |       |
|  7    |  8    |  9    |  
|       |       |       |
+-------+-------+-------+
Computer's move...
```

## Author

- **Dominik Kuka**

## License

This project is licensed under the MIT License.

