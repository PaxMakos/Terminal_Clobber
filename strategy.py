from game import makeMove, possibleMoves

STRATEGY_1 = "More_moves_after"
STRATEGY_2 = "Less_moves_before"
STRATEGY_3 = "Kill_at_all_cost"
STRATEGY_4 = "To_the_middle"
STRATEGY_5 = "Apes_together_strong"

# all strategies take the board and the player as input, and return the best move
# we try to maximalize the number of moves for the player after the move
def strategy_1(board, player):
    moves = possibleMoves(board, player)
    best_move = None
    best_score = -float('inf')

    for move in moves:
        new_board = makeMove(board, move)
        score = len(possibleMoves(new_board, player))

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def strategy_2(board, player):
    moves = possibleMoves(board, player)
    best_move = None
    best_pawn = None
    best_score = float('inf')

    pawns_moves_count = {}

    for move in moves:
        i1, j1, i2, j2 = move

        if (i1, j1) not in pawns_moves_count:
            pawns_moves_count[(i1, j1)] = 1
        else:
            pawns_moves_count[(i1, j1)] += 1

    for pawn, count in pawns_moves_count.items():
        if count < best_score:
            best_score = count
            best_pawn = pawn

    for move in moves:
        i1, j1, i2, j2 = move
        if (i1, j1) == best_pawn:
            best_move = move
            break

    return best_move


def strategy_3(board, player):
    moves = possibleMoves(board, player)
    best_move = None
    pawn_to_kill = None
    best_score = float('inf')

    pawns_possible_kills = {}
    
    for move in moves:
        i1, j1, i2, j2 = move
        if (i2, j2) not in pawns_possible_kills:
            pawns_possible_kills[(i2, j2)] = 1
        else:
            pawns_possible_kills[(i2, j2)] += 1

    for pawn, count in pawns_possible_kills.items():
        if count < best_score:
            best_score = count
            pawn_to_kill = pawn

    for move in moves:
        i1, j1, i2, j2 = move
        if (i2, j2) == pawn_to_kill:
            best_move = move
            break
        
    return best_move


def strategy_4(board, player):
    moves = possibleMoves(board, player)
    best_move = None
    best_score = float('inf')
    middle = (len(board) // 2, len(board[0]) // 2)

    for move in moves:
        i1, j1, i2, j2 = move
        distance = abs(i2 - middle[0]) + abs(j2 - middle[1])

        if distance < best_score:
            best_score = distance
            best_move = move

    return best_move


def strategy_5(board, player):
    moves = possibleMoves(board, player)
    best_move = None
    best_score = -float('inf')

    for move in moves:
        new_board = makeMove(board, move)
        i1, j1, i2, j2 = move
        score = 0

        if i2 > 0 and new_board[i2-1][j2] != 0:
            score += 1
        if i2 < len(new_board)-1 and new_board[i2+1][j2] != 0:
            score += 1
        if j2 > 0 and new_board[i2][j2-1] != 0:
            score += 1
        if j2 < len(new_board[0])-1 and new_board[i2][j2+1] != 0:
            score += 1
        if i2 > 0 and j2 > 0 and new_board[i2-1][j2-1] != 0:
            score += 1
        if i2 < len(new_board)-1 and j2 < len(new_board[0])-1 and new_board[i2+1][j2+1] != 0:
            score += 1
        if i2 > 0 and j2 < len(new_board[0])-1 and new_board[i2-1][j2+1] != 0:
            score += 1
        if i2 < len(new_board)-1 and j2 > 0 and new_board[i2+1][j2-1] != 0:
            score += 1

        if score > best_score:
            best_score = score
            best_move = move
        
    return best_move