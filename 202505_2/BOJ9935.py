string = input().strip()
bomb = input().strip()

stack = []

"""
매번 string을 탐색하면 시간복잡도가 너무 크다
한번에 탐색하는 방법으로는 스택 사용이 있다

1. 만약 스택에 문자가 추가되면서 폭발 문자열이 되면 스택에서 제거해야 한다
2. 만약 폭발 문자열이 되지 않으면 스택에 추가한다
3. 만약 폭발 문자열이 되면 스택에서 제거한다
4. 만약 스택에 문자가 남아있으면 출력하고 없으면 FRULA를 출력한다
"""
for char in string:
    stack.append(char)
    if len(stack) >= len(bomb) and stack[len(stack) - len(bomb):] == list(bomb):
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")