def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, edges):
    parent = [i for i in range(n)]
    
    for turn, (a, b) in enumerate(edges, start=1):
        if find_parent(parent, a) == find_parent(parent, b):
            return turn
        union(parent, a, b)
    
    return 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
    
    result = solution(n, edges)
    print(result)