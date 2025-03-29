from collections import deque


def snake_and_ladder(num_ladder: int, num_snake: int, ladders: list, snakes: list) -> int:
    board = {}
    for x, y in ladders:
        board[x] = y
    for u, v in snakes:
        board[u] = v
    
    queue = deque([(1, 0)])
    visited = [False] * 101
    visited[1] = True
    
    while queue:
        pos, dice_count = queue.popleft()
        
        if pos == 100:
            return dice_count
        
        for dice in range(1, 7):
            next_pos = pos + dice
            
            if next_pos > 100:
                continue
            
            if next_pos in board:
                next_pos = board[next_pos]
            
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, dice_count + 1))
    
    return -1


def parse_number_to_coord(num: int) -> tuple[int, int]:
    row = (num - 1) // 10
    col = (num - 1) % 10
    return row, col


if __name__ == "__main__":
    N, M = map(int, input().split())
    
    ladders = []
    for _ in range(N):
        x, y = map(int, input().split())
        ladders.append((x, y))
    
    snakes = []
    for _ in range(M):
        u, v = map(int, input().split())
        snakes.append((u, v))
    
    result = snake_and_ladder(N, M, ladders, snakes)
    print(result)
