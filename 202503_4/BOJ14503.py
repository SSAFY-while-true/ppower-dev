def clean_room(matrix: list, cur_r: int, cur_c: int, cur_dir: int) -> int:
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    def next_dir(cur_dir: int, n: int) -> int:
        return (cur_dir + n) % 4

    dirty = 0
    count = 0

    stop_cleaning = False
    while not stop_cleaning:
        # 현재 칸이 더럽다면 청소
        if matrix[cur_r][cur_c] == dirty:
            count += 1
            matrix[cur_r][cur_c] = -1
        # 현재 칸이 깨끗하다면 사방을 둘러보자
        else:
            are_there_dirty = False
            for i in range(4):
                nr, nc = cur_r + dr[next_dir(cur_dir, i)], cur_c + dc[next_dir(cur_dir, i)]
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] == dirty:
                    are_there_dirty = True
                    break
            
            # 만약 사방에 더러운 곳이 없다면
            if not are_there_dirty:
                # 후진할 수 있다면 후진
                dir_back = next_dir(cur_dir, 2)
                nr, nc = cur_r + dr[dir_back], cur_c + dc[dir_back]
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] != 1:
                    cur_r, cur_c = nr, nc
                # 후진할 수 없다면 청소 종료
                else:
                    stop_cleaning = True
            
            # 사방 중 더러운 곳이 있다면
            else:
                # 반시계 방향으로 틀자
                cur_dir = next_dir(cur_dir, 3)
                # 그리고나서 앞쪽 칸이 청소되지 않았다면 전진하자
                nr, nc = cur_r + dr[cur_dir], cur_c + dc[cur_dir]
                if 0 <= nr < len(matrix) and 0 <= nc < len(matrix[0]) and matrix[nr][nc] == dirty:
                    cur_r, cur_c = nr, nc
                
    return count
    

if __name__ == '__main__':
    num_row, num_col = map(int, input().split())
    cur_r, cur_c, direction = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(num_row)]
    print(clean_room(matrix, cur_r, cur_c, direction))
