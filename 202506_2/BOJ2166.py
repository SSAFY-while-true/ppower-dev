# 다각형의 면적
def get_surface_area(nodes: list[tuple[int, int]]):
    """
    좌표평면에서 각 꼭짓점들의 좌표를 모두 알 때 면적을 구할 수 있다.
    0.5 * |Sigma(xi * yi+1 - xi+1 * yi)|
    """
    node_num = len(nodes)

    # 꼭짓점이 3개 이하일 때 면적은 0
    if node_num < 3:
        return 0
    
    # 가우스 면적 공식 적용
    nodes.append(nodes[0])
    surface_area = 0

    for i in range(node_num):
        surface_area += nodes[i][0] * nodes[i+1][1]
        surface_area -= nodes[i+1][0] * nodes[i][1]
    surface_area *= 0.5
    surface_area = abs(surface_area)

    return surface_area


node_num = int(input())
nodes = []
for i in range(node_num):
    node = tuple(map(int, input().split()))
    nodes.append(node)

output = get_surface_area(nodes)
print(output)
