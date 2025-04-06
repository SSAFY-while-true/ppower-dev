num_float = int(input())
floats = [float(input()) for _ in range(num_float)]

dp = [0] * (num_float + 1)
dp[0] = floats[0]

for i in range(1, num_float + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] * floats[i], floats[i - 1] * floats[i])
    """
    점화식이 이렇게 세워진 이유:
    1. 이전 값을 포함하는 경우(dp[i - 1])
    2. 이전 값을 포함하지 않는 경우(dp[i - 2] * floats[i])
    3. 이전 값을 포함하지 않는 경우(floats[i - 1] * floats[i])
    클선생이 이렇다고는 하는데 이해가 안됨... 여러분이 설명해주세요 희희
    """
print(f"{dp[num_float]:.3f}")