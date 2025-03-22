if __name__ == '__main__':
    """
    dp[n] = n킬로그램의 설탕을 가져가기 위한 최소 봉지 수
    dp[n] = min(dp[n - 3], dp[n - 5]) + 1
    """
    n = int(input())
    dp = [float('inf')] * 5001
    dp[3] = 1
    dp[5] = 1

    for i in range(6, n + 1):
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
            
    output = dp[n] if dp[n] != float('inf') else -1
    print(output)
