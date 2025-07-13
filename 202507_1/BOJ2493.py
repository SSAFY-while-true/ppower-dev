# BOJ2493: 탑
import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))
answer = [0] * N
stack = []

for i in range(N):
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1  # 1-based index
    else:
        answer[i] = 0
    stack.append(i)

print(' '.join(map(str, answer)))
