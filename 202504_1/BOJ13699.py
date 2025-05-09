"""
dp[0] = 1
dp[n] = dp[0] * dp[n-1] + dp[1] * dp[n-2] + ... + dp[n-1] * dp[0]
"""

n = int(input())
dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n + 1):
    for j in range(i):
        dp[i] += dp[j] * dp[i - j - 1]

print(dp[n])