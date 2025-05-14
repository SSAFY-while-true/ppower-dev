table_size, num_case = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(table_size)]

sum_table = [[0] * (table_size + 1) for _ in range(table_size + 1)]
for i in range(1, table_size + 1):
    for j in range(1, table_size + 1):
        # dp 점화식
        # 1. 현재 위치의 원본 값(table[i-1][j-1])을 더함
        # 2. 위쪽 누적합(sum_table[i-1][j])을 더함
        # 3. 왼쪽 누적합(sum_table[i][j-1])을 더함
        # 4. 대각선 방향의 누적합(sum_table[i-1][j-1])을 빼줌 (중복 계산 방지)
        sum_table[i][j] = table[i-1][j-1] + sum_table[i-1][j] + sum_table[i][j-1] - sum_table[i-1][j-1]

for _ in range(num_case):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_table[x2][y2] - sum_table[x2][y1-1] - sum_table[x1-1][y2] + sum_table[x1-1][y1-1])
