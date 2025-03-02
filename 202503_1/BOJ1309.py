n = int(input())
if n == 1:
    print(3)
elif n == 2:
    print(7)
# 깊이가 3을 넘어가면 DP로 계산
else:
    dp = [0] * (n + 1)
    dp[1] = 3
    dp[2] = 7
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901
    
    print(dp[-1])