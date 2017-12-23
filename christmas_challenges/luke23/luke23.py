import numpy as np

with open("moves.txt", "r") as infile:
    moves = infile.read()

def check_if_won(board_state):
    """Checks if X or O has won the game.
    Input board_state is 3x3 matrix with X, O, or emptystring."""
    won = 0
    X_won = np.array([1,1,1])
    O_won = np.array([-1,-1,-1])
    if not 0 in board_state:
        won = 10
    for row in board_state:
        if (row == X_won).all():
            won = 1
        elif (row == O_won).all():
            won = -1
    for column in board_state.T:
        if (column == X_won).all():
            won = 1
        elif (column == O_won).all():
            won = -1
    if (np.diagonal(board_state) == X_won).all():
        won = 1
    elif (np.diagonal(board_state) == O_won).all():
        won = -1
    if (np.diagonal(np.fliplr(board_state)) == X_won).all():
        won = 1
    elif (np.diagonal(np.fliplr(board_state)) == O_won).all():
        won = -1
    return won

def test_check_if_won():
    test_board1 = np.array([[1,1,1],[-1,0,0],[1,0,-1]])
    test_board2 = np.array([[-1,1,1],[1,-1,1],[1,-1,-1]])
    test_board3 = np.array([[0,1,-1],[-1,1,0],[-1,1,0]])
    test_board4 = np.array([[0,-1,1],[-1,0,0],[1,-1,0]])
    test_board5 = np.array([[0,0,-1],[1,-1,-1],[-1,1,1]])
    won1 = check_if_won(test_board1)
    won2 = check_if_won(test_board2)
    won3 = check_if_won(test_board3)
    won4 = check_if_won(test_board4)
    won5 = check_if_won(test_board5)
    assert won1 == 1
    assert won2 == -1
    assert won3 == 1
    assert won4 == 0
    assert won5 == -1
    print("Test passed")
test_check_if_won()


wins = []
default_board_state = np.zeros((3,3))
board_state = default_board_state.copy()
current_move = 1
started_this_time = 1
for move in moves.strip("\n"):
    move = int(move)-1  #Indexes start at 0, not 1.
    board_state[(move//3, move%3)] = current_move
    if check_if_won(board_state) == 10: #Full board
        board_state = default_board_state.copy()
        wins.append(0)
        if wins[-2] == 0 and wins[-3] == 0:
            started_this_time *= -1  #Switching who starts on 3 draws
            current_move = started_this_time
    elif check_if_won(board_state) == 1:  #Checking if anybody won.
        board_state = default_board_state.copy()
        wins.append(1)
        started_this_time *= -1
        current_move = started_this_time
    elif check_if_won(board_state) == -1:
        board_state = default_board_state.copy()
        wins.append(-1)
        started_this_time *= -1
        current_move = started_this_time
    else:  #If not, next players turn
        current_move *= -1
print(wins)
