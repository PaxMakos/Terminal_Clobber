from game import *
from inputOutput import *
from strategy import *
from heuristics import *

def twoHumans(board, player):
    while True:
        print("Current board:")
        printBoard(board)
        print("Player", "Black" if player == 1 else "White", "turn")
        moves = possibleMoves(board, player)

        if len(moves) == 0:
            print("No possible moves for player", "Black" if player == 1 else "White")
            print("Player", "White" if player == 1 else "Black", "wins!")
            break

        printMoves(moves, player)

        move = readmove()
        
        if move not in moves:
            print("Invalid move")
            continue

        board = makeMove(board, move)
        player = -player


def twoAIbasic(board, player, player1_strategy, player2_strategy):
    while True:
        print("Current board:")
        printBoard(board)
        print("Player", "Black" if player == 1 else "White", "turn")
        moves = possibleMoves(board, player)

        if len(moves) == 0:
            print("No possible moves for player", "Black" if player == 1 else "White")
            print("Player", "White" if player == 1 else "Black", "wins!")
            break

        if player == 1:
            move = player1_strategy(board, player)
        else:
            move = player2_strategy(board, player)

        if move not in moves:
            print("Invalid move")
            continue

        board = makeMove(board, move)
        player = -player


def minimax(board, depth, player, maximazing, heuristics, alpha, beta):
    if len(possibleMoves(board, player)) == 0:
        if maximazing:
            return -float('inf'), None
        else:
            return float('inf'), None

    elif depth == 0:
        if maximazing:
            return heuristics(board, player), None
        else:
            return heuristics(board, -player), None
    else:
        moves = possibleMoves(board, player)
        best_move = None

        if maximazing:
            best_score = -float('inf')
            
            for move in moves:
                new_board = makeMove(board, move)
                score, _ = minimax(new_board, depth - 1, -player, False, heuristics, alpha, beta)
                
                if score > best_score:
                    best_score = score
                    best_move = move

                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        else:
            best_score = float('inf')
            
            for move in moves:
                new_board = makeMove(board, move)
                score, _ = minimax(new_board, depth - 1, -player, True, heuristics, alpha, beta)
                
                if score < best_score:
                    best_score = score
                    best_move = move

                beta = min(beta, best_score)
                if beta <= alpha:
                    break

        if best_move is None:
            best_move = moves[0]

        return best_score, best_move
    

def twoAIadvanced(board, player, depth, alpha, beta, heuristics):
    while True:
        print("Current board:")
        printBoard(board)
        print("Player", "Black" if player == 1 else "White", "turn")
        moves = possibleMoves(board, player)

        if len(moves) == 0:
            print("No possible moves for player", "Black" if player == 1 else "White")
            print("Player", "White" if player == 1 else "Black", "wins!")
            break

        _, best_move = minimax(board, depth, player, True, heuristics, alpha, beta)
        
        if best_move not in moves:
            print("Invalid move")
            continue

        board = makeMove(board, best_move)
        player = -player


def twoAIDifferentStrategies(board, first_player, depth, alpha, beta, heuristics1, heuristics2):
    player = first_player
    
    while True:
        print("Current board:")
        printBoard(board)
        print("Player", "Black" if player == 1 else "White", "turn")
        moves = possibleMoves(board, player)

        if len(moves) == 0:
            print("\nNo possible moves for player", "Black" if player == 1 else "White")
            print("Player", "White" if player == 1 else "Black", "wins!\n")
            break

        if player == first_player:
            _, best_move = minimax(board, depth, player, True, heuristics1, alpha, beta)
        else:
            _, best_move = minimax(board, depth, player, True, heuristics2, alpha, beta)

        if best_move not in moves:
            print("Invalid move")
            continue

        board = makeMove(board, best_move)
        player = -player


def humanVsAI(board, human_turn, player, depth, alpha, beta, heuristics):
    while True:
        print("Current board:")
        printBoard(board)
        print("Player", "Black" if player == 1 else "White", "turn")
        moves = possibleMoves(board, player)

        if len(moves) == 0:
            print("\n No possible moves for player", "Black" if player == 1 else "White")
            print("Player", "White" if player == 1 else "Black", "wins!")
            break

        if human_turn:
            printMoves(moves, player)
            move = readmove()
            
            if move not in moves:
                print("Invalid move")
                continue
        else:
            _, move = minimax(board, depth, player, True, heuristics, alpha, beta)
            
            if move not in moves:
                print("Invalid move")
                continue

        board = makeMove(board, move)
        player = -player
        human_turn = not human_turn


def testMode():
    n = 10
    m = 10

    board = []
    pawn = 1
    for i in range(n):
        row = []
        for j in range(m):
            row.append(pawn)
            pawn *= -1
        board.append(row)

        pawn *= -1

    first_player = 1
    player = first_player
    depth = 4
    alpha = -float('inf')
    beta = float('inf')
    heuristics1 = heuristic_1
    heuristics2 = heuristic_2
    
    while True:
        print("Current board:")
        printBoard(board)
        print("Player", "Black" if player == 1 else "White", "turn")
        moves = possibleMoves(board, player)

        if len(moves) == 0:
            print("No possible moves for player", "Black" if player == 1 else "White")
            print("Player", "White" if player == 1 else "Black", "wins!")
            break

        if player == first_player:
            _, best_move = testMinimax(board, depth, player, True, heuristics1, alpha, beta)
        else:
            _, best_move = testMinimax(board, depth, player, True, heuristics2, alpha, beta)

        if best_move not in moves:
            print("Invalid move")
            continue

        board = makeMove(board, best_move)
        player = -player


def testMinimax(board, depth, player, maximazing, heuristics, alpha, beta):
    if len(possibleMoves(board, player)) == 0:
        if maximazing:
            return -float('inf'), None
        else:
            return float('inf'), None

    elif depth == 0:
        #print("-----------------------------------------------------")
        #print("Heuristic value:", heuristic_1(board, player))
        #print("Heuristic value:", heuristic_2(board, player))
        #print("Heuristic value:", heuristic_3(board, player))
        #print("Heuristic value:", heuristic_4(board, player))
        #print("Heuristic value:", heuristic_5(board, player))
        #input()

        if(heuristic_1(board, player) != 0):
            print("Heuristic value:", heuristic_1(board, player))
        if(heuristic_2(board, player) != heuristic_3(board, player)):
            print("Heuristic value:", heuristic_2(board, player))
            print("Heuristic value:", heuristic_3(board, player))

        if maximazing:
            return heuristics(board, player), None
        else:
            return heuristics(board, -player), None
    else:
        moves = possibleMoves(board, player)
        best_move = None

        if maximazing:
            best_score = -float('inf')
            
            for move in moves:
                new_board = makeMove(board, move)
                score, _ = testMinimax(new_board, depth - 1, -player, False, heuristics, alpha, beta)
                
                if score > best_score:
                    best_score = score
                    best_move = move

                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        else:
            best_score = float('inf')
            
            for move in moves:
                new_board = makeMove(board, move)
                score, _ = testMinimax(new_board, depth - 1, -player, True, heuristics, alpha, beta)
                
                if score < best_score:
                    best_score = score
                    best_move = move

                beta = min(beta, best_score)
                if beta <= alpha:
                    break

        if best_move is None:
            best_move = moves[0]

        return best_score, best_move
    

if __name__ == "__main__":
    testMode()