n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]

# 결과를 저장할 변수 (-1, 0, 1의 개수)
result = [0, 0, 0]

def check_same_number(x, y, size):
    """주어진 영역이 모두 같은 숫자인지 확인"""
    start_value = papers[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if papers[i][j] != start_value:
                return False
    return True

def divide_paper(x, y, size):
    """종이를 9개로 나누어 재귀적으로 처리"""
    # 모두 같은 숫자인 경우
    if check_same_number(x, y, size):
        result[papers[x][y] + 1] += 1
        return
    
    # 같은 숫자가 아니면 9개로 분할
    new_size = size // 3
    for i in range(3):
        for j in range(3):
            divide_paper(x + i * new_size, y + j * new_size, new_size)

divide_paper(0, 0, n)

for count in result:
    print(count)

