"""
점화식
dp[i][j] = 삼각형의 i번째 줄 j번째 숫자까지의 최대합
dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
"""
def max_path_sum(triangle):
    dp = [row[:] for row in triangle]
    
    # 두 번째 줄부터 시작하여 아래로 내려가며 계산
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] += dp[i-1][0]
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    
    return max(dp[-1])

n = int(input())
triangle = []

for i in range(n):
    # 각 줄의 숫자들을 입력받아 정수로 변환하여 리스트에 추가
    row = list(map(int, input().split()))
    triangle.append(row)

result = max_path_sum(triangle)
print(result)