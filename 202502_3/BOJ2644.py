from collections import deque

def bfs(graph, start, target, visited):
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        v, count = queue.popleft()
        
        if v == target:
            return count
        
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, count + 1))
    
    return -1
        
n = int(input())
person1, person2 = map(int, input().split())
m = int(input())

family_tree = list([] for _ in range(n + 1))
for _ in range(m):
    a, b = map(int, input().split())
    family_tree[a].append(b)
    family_tree[b].append(a)

visited = [False] * (n + 1)

print(bfs(family_tree, person1, person2, visited))