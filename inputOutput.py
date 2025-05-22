def readData():
    print("Welcome to the cobbler!")
    print("Please enter the game mode:")
    print("1. Two humans")
    print("2. Two AI (stupid)")
    print("3. Two AI (the same strategy)")
    print("4. Two AI (different strategies)")
    print("5. Human vs AI")
    
    #Mode selection
    mode = int(input("Enter the mode (1-5): "))

    if mode < 1 or mode > 5:
        print("Invalid mode. Please enter a number between 1 and 5.")
        return readData()
    
    temp = input("Enter the board size, defaulf n = 5, m = 6 (n m): ")
    if temp == "":
        n = 5
        m = 6
    else:
        n, m = temp.split()
        n = int(n)
        m = int(m)


    temp = input("Use default board? (y/n): ")
    if temp == "y":
        board = []
        pawn = 1
        for i in range(n):
            row = []
            for j in range(m):
                row.append(pawn)
                pawn *= -1
            board.append(row)

            pawn *= -1

        start_player = 1
    else:
        print("Enter the board row by row, use B for black, W for white and _ for empty cells:")
        board = []
        for i in range(n):
            tempRow = input()
            row = []
            for j in range(m):
                if tempRow[j] == "B":
                    row.append(1)
                elif tempRow[j] == "W":
                    row.append(-1)
                else:
                    row.append(0)
            board.append(row)

        temp = input("Enter the starting player (B for black, W for white): ")
        if temp == "B":
            start_player = 1
        elif temp == "W":
            start_player = -1

    if mode > 2:
        temp = input("Enter the depth of the search tree (default 4): ")
        if temp == "":
            depth = 4
        else:
            depth = int(temp)

        alpha = -float('inf')
        beta = float('inf')
    else:
        depth = None
        alpha = None
        beta = None


    if mode == 2 or mode == 4:
        temp = input("Enter the strategy for player 1 (1-5): ")
        if temp == "":
            player1_strategy = 1
        else:
            player1_strategy = int(temp)

        temp = input("Enter the strategy for player 2 (1-5): ")
        if temp == "":
            player2_strategy = 1
        else:
            player2_strategy = int(temp)
    elif mode == 1:
        player1_strategy = None
        player2_strategy = None
        
    if mode == 3:
        temp = input("Enter the strategy for both players (1-5): ")
        if temp == "":
            player1_strategy = 1
            player2_strategy = 1
        else:
            player1_strategy = int(temp)
            player2_strategy = int(temp)

    if mode == 5:
        temp = input("Enter color for human player, default black (B - black, W - white): ")
        strategy = input("Enter the strategy for AI (1-5): ")

        if temp == "" or temp == "B":
            player1_strategy = int(strategy)
            player2_strategy = None
        elif temp == "W":
            player1_strategy = None
            player2_strategy = int(strategy)


    return mode, n, m, board, start_player, depth, player1_strategy, player2_strategy, alpha, beta


def readmove():
    #Read the move from user input
    temp = input("Enter the move (i1 j1 i2 j2): ")
    i1, j1, i2, j2 = temp.split()
    i1 = int(i1)
    j1 = int(j1)
    i2 = int(i2)
    j2 = int(j2)

    return i1, j1, i2, j2


def printBoard(board):
    for row in board:
        for cell in row:
            if cell == 1:
                print("B", end=" ")
            elif cell == -1:
                print("W", end=" ")
            else:
                print("_", end=" ")
        print()

    print("")


def printMoves(moves, player):
    if player == 1:
        print("Possible moves for black player:")
    else:
        print("Possible moves for white player:")
    
    for move in moves:
        i1, j1, i2, j2 = move
        print(f"Move from ({i1}, {j1}) to ({i2}, {j2})")
    

if __name__ == "__main__":
    readData()
    