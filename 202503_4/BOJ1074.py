def find_order(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)
    quadrant = half ** 2
    
    if r < half and c < half:
        return find_order(n - 1, r, c)
    if r < half and c >= half:
        return quadrant + find_order(n - 1, r, c - half)
    if r >= half and c < half:
        return quadrant * 2 + find_order(n - 1, r - half, c)
    if r >= half and c >= half:
        return quadrant * 3 + find_order(n - 1, r - half, c - half)

n, r, c = map(int, input().split())
print(find_order(n, r, c))