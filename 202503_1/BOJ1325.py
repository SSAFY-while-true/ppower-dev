import sys
input = sys.stdin.readline

def main():
    node_num, edge_num = map(int, input().split())
    graph = [[] * (node_num + 1)]
    for _ in range(edge_num):
        to_node, from_node = map(int, input().split())
        graph[from_node].append(to_node)


if __name__ == '__main__':
    main()