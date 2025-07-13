# BOJ1174: 줄어드는 수
from itertools import combinations

def count_descending(n):
    descending_numbers = []
    for i in range(1, 11):  # 1자리~10자리까지
        for comb in combinations(range(10), i):
            num = int("".join(map(str, sorted(comb, reverse=True))))
            descending_numbers.append(num)
    descending_numbers.sort()
    return descending_numbers[n - 1] if n <= len(descending_numbers) else -1

n = int(input())
print(count_descending(n))
