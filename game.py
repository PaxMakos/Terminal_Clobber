from inputOutput import *

def possibleMoves(board, player):
    moves = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player:
                if i > 0 and board[i-1][j] == -player:
                    moves.append((i, j, i-1, j))
                if i < len(board)-1 and board[i+1][j] == -player:
                    moves.append((i, j, i+1, j))
                if j > 0 and board[i][j-1] == -player:
                    moves.append((i, j, i, j-1))
                if j < len(board[0])-1 and board[i][j+1] == -player:
                    moves.append((i, j, i, j+1))

    return moves

def makeMove(board, move):
    new_board = [row[:] for row in board]
    i1, j1, i2, j2 = move
    new_board[i1][j1] = 0
    new_board[i2][j2] = -new_board[i2][j2]
    return new_board

