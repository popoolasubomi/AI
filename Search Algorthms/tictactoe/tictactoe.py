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
    x_count, o_count = 0, 0
    for row in board:
        for element in row:
            if element == "X":
                x_count += 1
            elif element == "O":
                o_count += 1
    if x_count > o_count:
        return "O"
    elif x_count == o_count:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [[element for element in row] for row in board]
    
    x, y = action[0], action[1]
    if x < len(board) and y < len(board[0]):
        turn = player(new_board)
        new_board[x][y] = turn
        return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Horizonatlly
    for row in board:
        start = row[0]
        if (start != None) and (start == row[1]) and (start == row[2]):
            return start
        
    #Vertically
    i = 0
    while i < len(board[0]):
        start = board[0][i]
        if (start != None) and (start == board[1][i]) and (start == board[2][i]):
            return start
        i += 1
        
    #Diagonally
    start = board[0][0]
    if (start != None) and (start == board[1][1]) and (start == board[2][2]):
        return start
    start = board[2][0]
    if (start != None) and (start == board[1][1]) and (start == board[0][2]):
        return start
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for row in board: 
        for element in row:
            if element == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == "X":
            return 1
        elif winner(board) == "O":
            return -1
        else:
            return 0

def min_play(board):
    if terminal(board):
        return (utility(board), 0, 0)
    minv = 2
    x, y = None, None
    for action in actions(board):
        new_board = result(board, action)
        (v, px, py) = max_play(new_board)
        if v < minv:
            minv = v
            x, y = action[0], action[1]
    return (minv, x, y)

def max_play(board):
    if terminal(board):
        return (utility(board), 0, 0)
    maxv = -2
    x, y = None, None
    for action in actions(board):
        new_board = result(board, action)
        (v, px, py) = min_play(new_board)
        if v > maxv:
            maxv = v
            x, y = action[0], action[1]
    return (maxv, x, y)
    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == "X":
        action = max_play(board)
    elif player(board) == "O":
        action = min_play(board)
    return (action[1], action[2])
    
    
    
            
        
    
    
