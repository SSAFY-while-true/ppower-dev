import sys
input = sys.stdin.readline

people_num = int(input())
matrix = [list(input().strip()) for _ in range(people_num)]
friends_count = [0] * people_num

for i in range(people_num):
  for j in range(people_num):
    # 자기 자신은 제외
    if i == j:
      continue
    # 친구 관계인 경우
    elif matrix[i][j] == 'Y':
      friends_count[i] += 1
    # 친구가 아닌 경우
    elif matrix[i][j] == 'N':
      # 친구의 친구인 경우
      for k in range(people_num):
        if matrix[i][k] == 'Y' and matrix[k][j] == 'Y':
          friends_count[i] += 1
          break

print(max(friends_count))