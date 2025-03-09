from collections import deque

def boj11403():
    matrix_size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]

    output = [[0] * matrix_size for _ in range(matrix_size)]
    for r in range(matrix_size):
        for c in range(matrix_size):
            if is_possible_to_reach(matrix, r, c):
                output[r][c] = 1

    print_matrix(output)
    

def is_possible_to_reach(matrix, i, j):
    node_num = len(matrix)
    visited = [False] * node_num
    queue = deque([i])

    while queue:
        node = queue.pop()
        if node == j and visited[node]:
            return True
        
        for neighbor in range(node_num):
            if matrix[node][neighbor] and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
    return False


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == '__main__':
    boj11403()

