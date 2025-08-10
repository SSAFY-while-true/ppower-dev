def is_valid(board, row, col, num):
    # 같은 행에 같은 숫자가 있는지 확인
    for x in range(9):
        if board[row][x] == num:
            return False
    
    # 같은 열에 같은 숫자가 있는지 확인
    for x in range(9):
        if board[x][col] == num:
            return False
    
    # 같은 3x3 박스에 같은 숫자가 있는지 확인
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    
    return True

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # 백트래킹
    empty = find_empty(board)
    if not empty:
        return True
    
    row, col = empty
    
    # 1부터 9까지 시도
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            # 재귀적으로 다음 칸 해결
            if solve_sudoku(board):
                return True
            
            # 백트래킹: 현재 숫자가 해답이 아니면 되돌리기
            board[row][col] = 0
    
    return False

# 입력 받기
board = []
for _ in range(9):
    row = list(map(int, input().strip()))
    board.append(row)

solve_sudoku(board)

for row in board:
    print(''.join(map(str, row)))
