from collections import defaultdict

def max_fruit_length(fruits):
    fruit_count = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(fruits)):
        fruit_count[fruits[right]] += 1

        # 과일 종류가 2개를 초과하면 left를 이동하여 범위를 줄임
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


fruits_num = int(input())
fruits = list(map(int, input().split()))

print(max_fruit_length(fruits))
