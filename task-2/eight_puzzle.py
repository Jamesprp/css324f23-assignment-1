import copy


def initial_state():
    return ((7, 2, 4, 5, 0, 6, 8, 3, 1), 1, 1)


def is_goal(s):
    return s[0] == (1, 2, 3, 4, 5, 6, 7, 8, 0)


def successors(s):
    _, r, c = s
    new_r, new_c = r-1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r+1, c
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c-1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1
    new_r, new_c = r, c+1
    if is_valid(new_r, new_c):
        yield move_blank(s, new_r, new_c), 1


def is_valid(r, c):
    return 0 <= r <= 2 and 0 <= c <= 2


def move_blank(s, new_r, new_c):
    board, r, c = s
    new_board = list(board)
    new_board[r*3 + c] = new_board[new_r*3 + new_c]
    new_board[new_r*3 + new_c] = 0
    return (tuple(new_board), new_r, new_c)

def h1(s):
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    board, _, _ = s
    res = 0
    # The for loop counts the number of elements that is different from
    # the goal configuration.
    # We start from index 1 to 8 because the blank is excluded.
    for idx in range(1, 9):
        if goal[idx] != board[idx]:
            res += 1
    return res

def h3(s):
    # implement this function
    goal = (1,2,3,4,5,6,7,8,9)
    rows = 0
    column =0
    res3 = 0
    board, _, _ = s
    for idx in range(1,9):
        if goal[idx] == 1 or 4 or 7:
            if idx != 0 or 3 or 7:
                rows +=1
        if goal[idx] == 2 or 5 or 8:
            if idx != 0 or 3 or 7:
                rows +=1       
        if goal[idx] == 3 or 7 or 0:
            if idx != 0 or 3 or 7:
                rows +=1
    
    for idx in range(1,9):
        if goal[idx] == 1 or 2 or 3:
            if idx != 0 or 1 or 2:
                column +=1
        if goal[idx] == 4 or 5 or 6:
            if idx != 3 or 4 or 5:
                column +=1       
        if goal[idx] == 7 or 0 or 8:
            if idx != 6 or 7 or 8:
                column +=1
    
    res3 = rows+column
    return res3 + h1(s)
