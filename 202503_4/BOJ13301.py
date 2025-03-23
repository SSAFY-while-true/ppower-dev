"""
dp[n]: n번째 사분원의 반지름
dp[n] = dp[n - 1] + dp[n - 2]
dp[1] = 1
dp[2] = 1
"""
n = int(input())
if n == 1:
    print(4)
else:
    dp = [1] * (n + 1)
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    """
    전체 둘레 = n번째 사각형 둘레 + n-1번째 사각형 변 * 2
    """
    output = dp[n] * 4 + dp[n - 1] * 2
    print(output)
