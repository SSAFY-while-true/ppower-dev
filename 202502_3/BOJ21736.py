"""
문제: 헌내기는 친구가 필요해
출처: BOJ
사용 알고리즘: BFS
"""
from collections import deque
import sys
input = sys.stdin.readline

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

WALL = 'X'
DOYEON = 'I'
PERSON = 'P'


def main():
	row_num, col_num = map(int, input().split())
	matrix = [list(input()) for _ in range(row_num)]
	start_coord = find_doyeon(matrix, row_num, col_num)
	output = count_people(matrix, start_coord, row_num, col_num)
	print(output)


# 도연이의 위치(좌표)를 찾는 함수
def find_doyeon(matrix, row_num, col_num):
	for r in range(row_num):
		for c in range(col_num):
			if matrix[r][c] == DOYEON:
				return r, c
	return None


# BFS를 통해 그래프를 탐색하면서 이미 탐색한 좌표는 WALL로 업데이트, 방문한 PERSON의 개수를 세는 함수
def count_people(matrix, start_coord, row_num, col_num):
	queue = deque([start_coord])
	matrix[start_coord[0]][start_coord[1]] = WALL
	count = 0
	
	while queue:
		r, c = queue.popleft()
		
		for i in range(4):
			nr, nc = r + dr[i], c + dc[i]
			if 0 <= nr < row_num and 0 <= nc < col_num and matrix[nr][nc] != WALL:
				queue.append((nr, nc))
				if matrix[nr][nc] == PERSON:
					count += 1
				matrix[nr][nc] = WALL
	
	return count if count != 0 else 'TT'


if __name__ == '__main__':
	main()
