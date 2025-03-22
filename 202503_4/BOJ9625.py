n = int(input())
a = 1
b = 0
for _ in range(n):
    temp_a = b
    temp_b = a + b
    a = temp_a
    b = temp_b

print(a, b)
