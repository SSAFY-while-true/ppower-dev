coins = [1, 2, 5, 7]
n = int(input())

dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[n])
