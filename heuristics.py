from game import *

#In this heuristics we try to maximalize the number of moves for the player after the move and minimalize the number of moves for the opponent
def heuristic_1(board, player):
    player_moves = possibleMoves(board, player)

    return len(player_moves)


#In this heuristics we try to maximalize the average number of moves for pawns of the player after the move and minimalize the average number of moves for pawns of the opponent
def heuristic_2(board, player):
    player_moves = possibleMoves(board, player)
    opponent_moves = possibleMoves(board, -player)

    pawns_moves_count = {}

    for move in player_moves:
        i1, j1, i2, j2 = move

        if (i1, j1) not in pawns_moves_count:
            pawns_moves_count[(i1, j1)] = 1
        else:
            pawns_moves_count[(i1, j1)] += 1

    player_score = sum(pawns_moves_count.values())/len(pawns_moves_count) if pawns_moves_count else 0
    
    return player_score


#In this heuristics we try to maximalize average number of ways we can kill opponent's pawns after the move and minimalize average number of ways we can kill player's pawns after the move
def heuristic_3(board, player):
    player_moves = possibleMoves(board, player)
    opponent_moves = possibleMoves(board, -player)

    pawns_possible_kills = {}

    for move in opponent_moves:
        i1, j1, i2, j2 = move
        if (i2, j2) not in pawns_possible_kills:
            pawns_possible_kills[(i2, j2)] = 1
        else:
            pawns_possible_kills[(i2, j2)] += 1

    opponent_score = sum(pawns_possible_kills.values())/len(pawns_possible_kills) if pawns_possible_kills else 0

    pawns_possible_kills = {}

    for move in player_moves:
        i1, j1, i2, j2 = move
        if (i2, j2) not in pawns_possible_kills:
            pawns_possible_kills[(i2, j2)] = 1
        else:
            pawns_possible_kills[(i2, j2)] += 1

    player_score = sum(pawns_possible_kills.values())/len(pawns_possible_kills) if pawns_possible_kills else 0

    return opponent_score - player_score


#We try to maximalize the number of player's pawns in the middle of the board and minimalize the number of opponent's pawns in the middle of the board
def heuristic_4(board, player):
    player_score = 0
    opponent_score = 0

    middle = (len(board) // 2, len(board[0]) // 2)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == player:
                player_score += abs(i - middle[0]) + abs(j - middle[1])
            elif board[i][j] == -player:
                opponent_score += abs(i - middle[0]) + abs(j - middle[1])

    return opponent_score - player_score


#We try to maximalize the number of player's pawns neighbors and minimalize the number of opponent's pawns neighbors
def heuristic_5(board, player):
    player_score = 0
    opponent_score = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if i > 0 and board[i-1][j] != 0:
                if board[i][j] == player:
                    player_score += 1
                elif board[i][j] == -player:
                    opponent_score += 1
            if i < len(board)-1 and board[i+1][j] != 0:
                if board[i][j] == player:
                    player_score += 1
                elif board[i][j] == -player:
                    opponent_score += 1
            if j > 0 and board[i][j-1] != 0:
                if board[i][j] == player:
                    player_score += 1
                elif board[i][j] == -player:
                    opponent_score += 1
            if j < len(board[0])-1 and board[i][j+1] != 0:
                if board[i][j] == player:
                    player_score += 1
                elif board[i][j] == -player:
                    opponent_score += 1
            if i > 0 and j > 0 and board[i-1][j-1] != 0:
                if board[i][j] == player:
                    player_score += 1
                elif board[i][j] == -player:
                    opponent_score += 1
            if i > 0 and j < len(board[0])-1 and board[i-1][j+1] != 0:
                if board[i][j] == player:
                    player_score += 1
                elif board[i][j] == -player:
                    opponent_score += 1
            if i < len(board)-1 and j > 0 and board[i+1][j-1] != 0:
                if board[i][j] == player:
                    player_score += 1
                elif board[i][j] == -player:
                    opponent_score += 1
            if i < len(board)-1 and j < len(board[0])-1 and board[i+1][j+1] != 0:
                if board[i][j] == player:
                    player_score += 1
                elif board[i][j] == -player:
                    opponent_score += 1

    return player_score - opponent_score