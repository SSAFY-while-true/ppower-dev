"""
투포인터가 넘모 어려워용
해시로 풀겠습니다
"""
from collections import defaultdict

fruits_num = int(input())
fruits = list(map(int, input.split()))

max_length = 0

for front in range(fruits_num):
    fruit_count = defaultdict(int)  # 남은 과일들의 개수를 저장할 해시맵
    cur_fruits = 0  # 현재 남은 과일들의 종류 개수
    
    # front부터 시작해서 뒤에서 back 개를 뺄 때까지 탐색
    for i in range(front, fruits_num):
        fruit_count[fruits[i]] += 1
        if fruit_count[fruits[i]] == 1:
            cur_fruits += 1     # 새로운 과일 종류 등장

        # 과일 종류가 2개 이하일 때만 최대 길이 갱신
        if cur_fruits <= 2:
            max_length = max(max_length, i - a + 1)
        else:
            break   # 과일 종류가 3개 이상이면 탐색 종료

print(max_length)