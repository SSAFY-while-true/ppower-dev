# BOJ10844: 쉬운 계단 수
"""
dp[i][j] = i자리수에서 마지막 자리가 j인 계단수의 개수
"""
MOD = 1000000000
n = int(input())
# 한자리 수
if n == 1:
    print(9)

# 그 외
else:
    dp = [[0] * 10 for _ in range(n + 1)]
    # 1자리수
    for i in range(1, 10):
        dp[1][i] = 1
    
    # 2자리부터 n자리까지 계단수 개수 계산
    for i in range(2, n + 1):
        for j in range(10):
            # 현재 자리가 j 일 때, 이전 자리는 j-1 or j+1 이어야 한다
            if j > 0:
                dp[i][j] += dp[i-1][j-1]
            if j < 9:
                dp[i][j] += dp[i-1][j+1]
    
    output = sum(dp[n]) % MOD
    print(output)
