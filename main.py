from inputOutput import *
from gameModes import *
from strategy import *
from heuristics import *
from datetime import datetime

def main():
    mode, n, m, board, start_player, depth, player1_strategy, player2_strategy, alpha, beta = readData()

    if player1_strategy is not None:
        if player1_strategy == 1:
            player1_strategy = strategy_1
            player1_heuristics = heuristic_1
        elif player1_strategy == 2:
            player1_strategy = strategy_2
            player1_heuristics = heuristic_2
        elif player1_strategy == 3:
            player1_strategy = strategy_3
            player1_heuristics = heuristic_3
        elif player1_strategy == 4:
            player1_strategy = strategy_4
            player1_heuristics = heuristic_4
        elif player1_strategy == 5:
            player1_strategy = strategy_5
            player1_heuristics = heuristic_5

    if player2_strategy is not None:
        if player2_strategy == 1:
            player2_strategy = strategy_1
            player2_heuristics = heuristic_1
        elif player2_strategy == 2:
            player2_strategy = strategy_2
            player2_heuristics = heuristic_2
        elif player2_strategy == 3:
            player2_strategy = strategy_3
            player2_heuristics = heuristic_3
        elif player2_strategy == 4:
            player2_strategy = strategy_4
            player2_heuristics = heuristic_4
        elif player2_strategy == 5:
            player2_strategy = strategy_5
            player2_heuristics = heuristic_5

    start_time = datetime.now()
    print("Start time:", start_time.strftime("%Y-%m-%d %H:%M:%S"))

    match mode:
        case 1:
            twoHumans(board, start_player)
        case 2:
            twoAIbasic(board, start_player, player1_strategy, player2_strategy)
        case 3:
            twoAIadvanced(board, start_player, depth, alpha, beta, player1_heuristics)
        case 4:
            twoAIDifferentStrategies(board, start_player, depth, alpha, beta, player1_heuristics, player2_heuristics)
        case 5:
            if player1_strategy is not None:
                humanVsAI(board, True, start_player, depth, alpha, beta, player1_heuristics)
            else:
                humanVsAI(board, False, start_player, depth, alpha, beta, player2_heuristics)

    end_time = datetime.now()
    print("End time:", end_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Execution time:", end_time - start_time)

    
    
if __name__ == "__main__":
    main()
