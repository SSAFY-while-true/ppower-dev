"""
dp[n]: n을 제곱수의 합으로 표현할 때 최소 항의 개수

dp[n] = min(dp[n], dp[n - i**2] + 1) for i in range(1, int(n**0.5) + 1)
"""

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = i
    for j in range(1, int(i**0.5) + 1):
        dp[i] = min(dp[i], dp[i - j**2] + 1)

print(dp[n])