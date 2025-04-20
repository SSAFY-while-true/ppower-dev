"""
2 ** 32는 2를 32번 곱하는 것. 즉, 연산량이 32번이다.
하지만 (2 ** 16) ** 2 로 계산하면 연산량이 17번이다.
이런 식으로 계산하면 연산량이 줄어든다.
"""

def power(a: int, b: int, c: int) -> int:
    if b == 0:
        return 1
    # 만약 b가 짝수라면
    if b % 2 == 0:
        return power(a, b // 2, c) ** 2 % c
    else:
        return (a * power(a, b // 2, c) ** 2) % c

a, b, c = map(int, input().split())
print(power(a, b, c))
