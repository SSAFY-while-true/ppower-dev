if __name__ == '__main__':
    house_num = int(input())
    house_infos = [(0, 0, 0)]
    for _ in range(house_num):
        house_infos.append(tuple(map(int, input().split())))        # (빨강 비용, 초록 비용, 파랑 비용)
    
    """
    dp[i][j]: i번째 집에 j색을 칠했을 때의 최소 비용
    dp[i][j] = min(dp[i-1][(j + 1) % 3], dp[i-1][(j + 2) % 3]) + matrix[i][j]
    """
    dp = [[0, 0, 0] for _ in range(house_num + 1)]
    for i in range(1, len(dp)):
        for j in range(3):
            dp[i][j] = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3]) + house_infos[i][j]
    
    print(min(dp[-1]))
