# tictactoe
Using minimax algorithm developed an AI for tictactoe game(single player).
There are two main files in this project: runner.py and tictactoe.py. tictactoe.py contains all of the logic for playing the game, and for making optimal moves. 
runner.py contains all of the code to run the graphical interface for the game. You should run python runner.py to play against your AI!


Let’s open up tictactoe.py to get an understanding for what’s provided. First, we define three variables: X, O, and EMPTY, to represent possible moves of the board.
The function initial_state returns the starting state of the board. For this problem, we’ve chosen to represent the board as a list of three lists (representing the three rows of the board),
where each internal list contains three values that are either X, O, or EMPTY.

DESCRIPTION OF FUNCTIONS IN tictactoe.py:
    
    player : The player takes a board state as input, and return which player’s turn it is (either X or O).
    actions : The actions function return a set of all of the possible actions that can be taken on a given board.
    result : The result function takes a board and an action as input, and should return a new board state, without modifying the original board.
    winner : The winner function accepts a board as input, and return the winner of the board if there is one.
    terminal : The terminal function accepts a board as input, and return a boolean value indicating whether the game is over.
    utility : The utility function accepts a terminal board as input and output the utility of the board.
    minimax : The minimax function takes a board as input, and return the optimal move for the player to move on that board.
    
   
This tictactoe AI which you play against by runner.py will not lose but it maybe tie.
