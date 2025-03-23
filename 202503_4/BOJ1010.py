num_case = int(input())
for _ in range(num_case):
    n, m = map(int, input().split())
    # mCn 구하면 됨
    output = 1
    for i in range(m, m - n, -1):
        output *= i
    for i in range(2, n + 1):
        output //= i
    print(output)
