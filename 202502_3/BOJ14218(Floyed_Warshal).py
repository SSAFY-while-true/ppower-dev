import sys
input = sys.stdin.read

def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

def main():
    data = input().split()
    idx = 0

    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2

    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        dist[u][v] = 1
        dist[v][u] = 1
        idx += 2

    floyd_warshall(n, dist)

    q = int(data[idx])
    idx += 1

    results = []

    for _ in range(q):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        idx += 2

        if dist[u][v] > 1:
            dist[u][v] = 1
            dist[v][u] = 1

            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][u] + dist[u][v] + dist[v][j]:
                        dist[i][j] = dist[i][u] + dist[u][v] + dist[v][j]
                    if dist[i][j] > dist[i][v] + dist[v][u] + dist[u][j]:
                        dist[i][j] = dist[i][v] + dist[v][u] + dist[u][j]

        total_distance = 0
        for i in range(n):
            for j in range(i + 1, n):
                total_distance += dist[i][j]

        results.append(total_distance)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()