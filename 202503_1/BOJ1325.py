import sys
input = sys.stdin.readline

def main():
    node_num, edge_num = map(int, input().split())
    graph = [[] for _ in range(node_num + 1)]
    for _ in range(edge_num):
        to_node, from_node = map(int, input().split())
        graph[from_node].append(to_node)
    
    max_count_dict = {}
    max_of_max_count = 0
    for node in range(1, node_num + 1):
        max_count = dfs(graph, node)
        max_of_max_count = max(max_of_max_count, max_count)
        
        if max_count not in max_count_dict:
            max_count_dict[max_count] = [node]
        else:
            max_count_dict[max_count].append(node)
    
    print(" ".join(map(str, sorted(max_count_dict[max_of_max_count]))))
    

def dfs(graph, start):
    visited = [False] * (len(graph) + 1)
    visited[start] = True
    stack = [start]
    max_count = 0
    
    while stack:
        node = stack.pop()
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                max_count += 1
                visited[neighbor] = True
                stack.append((neighbor))
    
    return max_count
        

if __name__ == '__main__':
    main()