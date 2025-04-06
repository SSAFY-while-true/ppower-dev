import heapq
import sys
input = sys.stdin.readline


def prim(graph, n):
    visited = [False] * (n + 1)
    mst_edges = []
    start = 1
    visited[start] = True
    
    edges = []
    for neighbor, weight in graph[start]:
        heapq.heappush(edges, (weight, start, neighbor))
        
    while edges:
        weight, u, v = heapq.heappop(edges)
        if visited[v]:
            continue
        visited[v] = True
        mst_edges.append((u, v, weight))
        
        for neighbor, w in graph[v]:
            if not visited[neighbor]:
                heapq.heappush(edges, (w, v, neighbor))
    
    return mst_edges


def find_min_cost(n, m, edges):
    graph = [[] for _ in range(n + 1)]
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    mst_edges = prim(graph, n)
    
    if len(mst_edges) != n - 1:
        return -1
    
    total_weight=  0
    max_edge_weight = 0
    
    for u, v, weight in mst_edges:
        total_weight += weight
        max_edge_weight = max(max_edge_weight, weight)
    
    return total_weight - max_edge_weight


if __name__ == "__main__":
    num_house, num_road = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(num_road)]
    output = find_min_cost(num_house, num_road, roads)
    print(output)
