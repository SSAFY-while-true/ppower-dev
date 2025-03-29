n = int(input())

if n == 1:
    print(-1)

dp = [0] + [float('inf')] * n
coins = (2, 5)

for i in range(1, n + 1):
    for coin in coins:
        if i - coin >= 0 and dp[i - coin] != float('inf'):
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[n] if dp[n] != float('inf') else -1)