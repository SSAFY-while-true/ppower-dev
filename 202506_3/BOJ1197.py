# BOJ1197: 최소 스패닝 트리
import heapq


def prim_mst(adj_list: set, num_nodes: int, start: int):
    """
    :param adj_list: {노드: [(가중치, 인접노드), ...]} 형식의 인접 리스트
    :param num_vertices: 노드 개수
    :param start: 시작 노드
    """
    visited = [False] * (num_nodes + 1)
    priority_queue = []
    
    visited[start] = True
    for cost, next_node in adj_list[start]:
        heapq.heappush(priority_queue, (cost, next_node))
    
    mst_cost = 0
    edge_used = 0
    
    while priority_queue and edge_used < num_nodes - 1:
        cost, next_node = heapq.heappop(priority_queue)
        if visited[next_node]:
            continue
        
        visited[next_node] = True
        mst_cost += cost
        edge_used += 1
        
        for next_cost, adj_node in adj_list[next_node]:
            if not visited[adj_node]:
                heapq.heappush(priority_queue, (next_cost, adj_node))
    
    return mst_cost


num_nodes, num_edges = map(int, input().split())

adj_list = {}
for i in range(1, num_nodes + 1):
    adj_list[i] = []

for _ in range(num_edges):
    node, next_node, cost = map(int, input().split())
    adj_list[node].append((cost, next_node))
    adj_list[next_node].append((cost, node))

output = prim_mst(adj_list, num_nodes, 1)
print(output)
