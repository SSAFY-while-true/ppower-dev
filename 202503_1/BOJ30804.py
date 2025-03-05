from collections import defaultdict

def max_fruit_length(fruits):
    fruits_num = len(fruits)
    max_length = 0

    for front in range(fruits_num):  # 시작점을 하나씩 탐색
        fruit_count = defaultdict(int)  # 현재 바구니 상태 (과일 종류별 개수)
        cur_fruits = 0  # 현재 과일 종류 개수

        for back in range(front, fruits_num):  # front부터 시작해서 끝까지 탐색
            fruit_count[fruits[back]] += 1

            if fruit_count[fruits[back]] == 1:  # 새로운 과일 등장
                cur_fruits += 1

            if cur_fruits > 2:  # 과일이 2종류 초과되면 종료
                break

            max_length = max(max_length, back - front + 1)

    return max_length

fruits_num = int(input())
fruits = list(map(int, input().split()))

print(max_fruit_length(fruits))
