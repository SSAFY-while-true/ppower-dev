num_soldiers = int(input())
soldiers = list(map(int, input().split()))

dp = [1] * num_soldiers

for i in range(1, num_soldiers):
    for j in range(i):
        if soldiers[j] > soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

max_soldiers = max(dp)
min_removed = num_soldiers - max_soldiers
print(min_removed)
