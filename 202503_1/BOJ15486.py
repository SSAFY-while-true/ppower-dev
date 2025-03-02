date = int(input())
T = [0] * (date + 1)
P = [0] * (date + 1)
dp = [0] * (date + 1)

for i in range(1, date + 1):
    T[i], P[i] = map(int, input().split())
    
for i in range(1, date + 1):
    dp[i] = max(dp[i], dp[i - 1])
    
    end_day = i + T[i] - 1
    if end_day <= date:
        dp[end_day] = max(dp[end_day], dp[i - 1] + P[i])
    
print(max(dp))