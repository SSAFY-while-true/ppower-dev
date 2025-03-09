from collections import deque

def find_min_dist(matrix: list, start: tuple, goal: tuple) -> int:
    row_num = len(matrix)
    col_num = len(matrix[0])
    
    visited = [[[False, False] for _ in range(col_num)] for _ in range(row_num)]
    visited[start[0]][start[1]][0] = True
    queue = deque([(start[0], start[1], 1, 0)])

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue:
        r, c, dist, broke = queue.popleft()
        
        if (r, c) == goal:
            return dist
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < row_num and 0 <= nc < col_num:
                if matrix[nr][nc] == 0 and not visited[nr][nc][broke]:
                    queue.append((nr, nc, dist + 1, broke))
                    visited[nr][nc][broke] = True
                
                elif matrix[nr][nc] == 1 and broke == 0 and not visited[nr][nc][1]:
                    queue.append((nr, nc, dist + 1, 1))
                    visited[nr][nc][1] = True
    
    return -1

if __name__ == '__main__':
    row_num, col_num = map(int, input().split())
    matrix = [list(map(int, list(input().strip()))) for _ in range(row_num)]
    output = find_min_dist(matrix, (0, 0), (row_num - 1, col_num - 1))
    print(output)
