from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 목표 지점 좌표 찾기
start_x = -1
start_y = -1
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            start_x = i
            start_y = j
            break
    if start_x != -1:
        break

result = [[-1] * m for _ in range(n)]

# BFS 함수 정의
def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and matrix[nx][ny] != 0:
                if matrix[nx][ny] == 0:
                    visited[nx][ny] = 0
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                print(0, end=' ')
            else:
                print(visited[i][j], end=' ')
        print()

bfs(start_x, start_y)