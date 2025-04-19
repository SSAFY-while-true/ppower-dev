n, m = map(int, input().split())

"""
start부터 end까지 곱하는 함수
start가 end보다 크거나 같다
"""
def factorial(start: int, end: int) -> int:
    if start == end:
        return start
    if start < end:
        return 1
    return start * factorial(start - 1, end)

print(factorial(n, n - m + 1) // factorial(m, 1))
