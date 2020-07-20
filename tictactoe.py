"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_of_X=0
    num_of_O=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==X:
                num_of_X+=1
            elif board[i][j]==O:
                num_of_O+=1
    if num_of_X==num_of_O:
        return X
    else:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    l=[]
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                l.append((i,j))
    return l
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    p=player(board)
    if board[action[0]][action[1]]==EMPTY:
        b1=[[],[],[]]
        for i in range(3):
            for j in range(3):
                if i==action[0] and j==action[1]:
                    b1[i].append(p)
                else:
                    b1[i].append(board[i][j])
        return b1
    else:
        raise Exception("Action is not valid for the board")
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][1]!=EMPTY:
            return board[i][0]
        elif board[0][i]==board[1][i] and board[1][i]==board[2][i] and board[1][i]!=EMPTY:
            return board[0][i]
    if board[1][1]==board[0][0] and board[1][1]==board[2][2] and board[1][1]!=EMPTY:
        return board[0][0]
    elif board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]!=EMPTY:
        return board[1][1]
    else:
        return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    num_of_em=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                num_of_em+=1
    if num_of_em==0 or winner(board)!=None:
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    else:
        return 0
    raise NotImplementedError


def maxvalue(board):
    if terminal(board):
        return (utility(board),None)
    else:
        v=-100
        for action in actions(board):
            v1=max(v,minvalue(result(board,action))[0])
            if v1!=v:
                req_act=action
                v=v1
        return (v,req_act)

def minvalue(board):
    if terminal(board):
        return (utility(board),None)
    else:
        v=100
        for action in actions(board):
            v1=min(v,maxvalue(result(board,action))[0])
            if v1!=v:
                req_act=action
                v=v1
        return (v,req_act)    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board)==X:
            return maxvalue(board)[1]
        elif player(board)==O:
            return minvalue(board)[1]

        

    raise NotImplementedError
