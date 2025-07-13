"""
dp[i] = min(dp[i - tetra] + 1) for all tetrahedral numbers <= i
"""
n = int(input())
tetra = []
for i in range(1, 120):
  tetra.append(i * (i + 1) * (i + 2) // 6)

dp = [1000000000] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
  for t in tetra:
    if i < t:
      break
    dp[i] = min(dp[i], dp[i - t] + 1)
print(dp[n])
