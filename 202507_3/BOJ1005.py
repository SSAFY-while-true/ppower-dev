from collections import deque

def acm():
    n, k = map(int, input().split())
    
    build_time = [0] + list(map(int, input().split()))
    
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    
    # 목표 건물
    w = int(input())
    
    # 각 건물을 짓는데 걸리는 최소 시간
    dp = [0] * (n + 1)
    
    queue = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = build_time[i]
    
    while queue:
        current = queue.popleft()
        
        for next_building in graph[current]:
            dp[next_building] = max(dp[next_building], dp[current] + build_time[next_building])
            
            indegree[next_building] -= 1
            
            if indegree[next_building] == 0:
                queue.append(next_building)
    
    return dp[w]


t = int(input())
for _ in range(t):
    result = acm()
    print(result)
