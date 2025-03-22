def count_regions(matrix, is_colorblind=False):
    matrix_size = len(matrix)
    visited = [[False] * matrix_size for _ in range(matrix_size)]
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # 같은 색깔인지 확인하는 함수
    def same_color(color1: str, color2: str) -> bool:
        if is_colorblind:
            # 적록색약이면 R과 G를 같은 색으로 취급
            if color1 in ('R', 'G') or color2 in ('R', 'G'):
                return True
            return color1 == color2
        else:
            return color1 == color2
    
    count = 0
    for r in range(matrix_size):
        for c in range(matrix_size):
            if not visited[r][c]:
                count += 1
                val = matrix[r][c]
                
                stack = [(r, c)]
                visited[r][c] = True
                
                while stack:
                    cur_r, cur_c = stack.pop()
                    
                    for i in range(4):
                        nr, nc = cur_r + dr[i], cur_c + dc[i]

                        # 장외거나, 방문한 적이 있거나, 같은 색이 아니라면 패스
                        if nr < 0 or nc < 0 or nr >= matrix_size or nc >= matrix_size or visited[nr][nc] or not same_color(matrix[nr][nc], val):
                            continue
                        
                        visited[nr][nc] = True
                        stack.append((nr, nc))
    
    return count
    
if __name__ == '__main__':
    matrix_size = int(input())
    matrix = [list(input()) for _ in range(matrix_size)]

    rgb_output = count_regions(matrix, is_colorblind=False)
    blind_rgb_output = count_regions(matrix, is_colorblind=True)

    print(f'{rgb_output} {blind_rgb_output}')