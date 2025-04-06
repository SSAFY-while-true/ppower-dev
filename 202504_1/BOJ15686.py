# 폐업시키지 않을 치킨집을 최대 chicken_count개 골랐을 때, 도시의 치킨 거리의 최솟값을 출력하는 함수
def get_chicken_distance(matrix: list, chicken_count: int) -> int:
    chicken_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == CHICKEN:
                chicken_list.append((i, j))

    total_distance = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == HOME:
                min_distance = float('inf')
                for chicken in chicken_list:
                    min_distance = min(min_distance, abs(i - chicken[0]) + abs(j - chicken[1]))
                total_distance += min_distance

    return total_distance


if __name__ == "__main__":
    HOME = 1
    CHICKEN = 2
    matrix_size, chicken_count = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(matrix_size)]

    output = get_chicken_distance(matrix, chicken_count)
    print(output)

