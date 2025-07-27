import heapq
import sys

def dijkstra(graph, start, n):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, current = heapq.heappop(heap)
        
        if current_dist > dist[current]:
            continue
            
        for next_node, weight in graph[current]:
            new_dist = current_dist + weight
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
    
    return dist

def party():
    n, m, x = map(int, input().split())
    
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))
        reverse_graph[b].append((a, t))
    
    dist_from_x = dijkstra(graph, x, n)
    
    dist_to_x = dijkstra(reverse_graph, x, n)
    
    max_time = 0
    for i in range(1, n + 1):
        if i != x:
            total_time = dist_to_x[i] + dist_from_x[i]
            max_time = max(max_time, total_time)
    
    print(max_time)

if __name__ == "__main__":
    party()
