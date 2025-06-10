from collections import deque
import sys
input = sys.stdin.readline

node_num = int(input())
tree = [[] for _ in range(node_num + 1)]
for _ in range(node_num - 1):
    node1, node2 = map(int, input().rstrip().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

parents = [0] * (node_num + 1)

queue = deque([1]) # Root node인 1을 시작점으로 삼아 BFS 실행
parents[1] = -1
while queue:
    current = queue.popleft()
    for neighbor in tree[current]:
        if parents[neighbor] == 0:
            parents[neighbor] = current
            queue.append(neighbor)

for i in range(2, node_num + 1):
    print(parents[i])