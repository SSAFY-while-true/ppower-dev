import sys
input = sys.stdin.readline
from collections import deque


def main():
	city_num, road_num = map(int, input().split())
	
	# 정비 전 도시를 인접 리스트 그래프로 구현
	initial_graph = [[] for _ in range(city_num + 1)]
	for _ in range(road_num):
		city1, city2 = map(int, input().split())
		initial_graph[city1].append(city2)
		initial_graph[city2].append(city1)
	
	# 정비 계획 중인 길 정보를 튜플 타입으로 큐에 추가
	scheduled_road_num = int(input())
	scheduled_road = deque()
	for _ in range(scheduled_road_num):
		scheduled_road.append(tuple(map(int, input().split())))
	
	for _ in range(scheduled_road_num):
		repair_road(initial_graph, scheduled_road)
		output_list = []
		for i in range(1, city_num + 1):
			shortest_dist = find_shortest_dist(initial_graph, i)
			output_list.append(shortest_dist)
		print(" ".join(map(str, output_list)))


# 정비할 길을 순서대로 꺼내어 그래프에 추가하는 함수
def repair_road(initial_graph, scheduled_road):
	node1, node2 = scheduled_road.popleft()
	initial_graph[node1].append(node2)
	initial_graph[node2].append(node1)
	

# 목적지로 향하는 최단거리를 BFS로 계산하는 함수
def find_shortest_dist(graph, start, goal=1):
	if start == goal:
		return 0
		
	visited = [False] * len(graph)
	visited[start] = True
	queue = deque([(start, 0)])
	
	while queue:
		cur_node, dist = queue.popleft()
		
		if cur_node == goal:
			return dist
			
		for next_node in graph[cur_node]:
			if not visited[next_node]:
				queue.append((next_node, dist + 1))
				visited[next_node] = True
	
	return -1
		

if __name__ == '__main__':
	main()