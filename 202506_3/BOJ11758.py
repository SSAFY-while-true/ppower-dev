# BOJ11758: CCW
coord1 = tuple(map(int, input().split()))
coord2 = tuple(map(int, input().split()))
coord3 = tuple(map(int, input().split()))

vector1 = (coord2[0] - coord1[0], coord2[1] - coord1[1])
vector2 = (coord3[0] - coord2[0], coord3[1] - coord2[1])

cross_product = vector1[0] * vector2[1] - vector1[1] * vector2[0]

if cross_product > 0:
    print(1)
elif cross_product < 0:
    print(-1)
else:
    print(0)
