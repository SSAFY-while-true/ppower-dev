def get_max_joy(n: int) -> int:
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j) + dp[j] + dp[i - j])
    return dp[n]


n = int(input())
print(get_max_joy(n))
