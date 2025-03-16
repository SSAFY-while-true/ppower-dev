from collections import deque

def parse_str_to_list(expression: str) -> list:
    if expression == '[]':
        return []
    expression = expression.strip()[1:len(expression) - 1]
    expression = expression.split(',')
    return expression


def parse_list_to_str(expression: list) -> str:
    return '[' + ','.join(expression) + ']'


def run_AC_function(funcs: str, arr: str) -> list:
    arr = deque(parse_str_to_list(arr))
    
    reversed_flag = False

    for func in funcs:
        if func == 'R':
            if reversed_flag:
                reversed_flag = False
            else:
                reversed_flag = True
        
        elif func == 'D':
            if not arr:
                return 'error'

            arr.popleft() if not reversed_flag else arr.pop()

        else:
            return 'error'
    
    if reversed_flag:
        arr.reverse()
        
    return list(arr)
        

if __name__ == '__main__':
    case_num = int(input())
    for _ in range(case_num):
        funcs = input()
        _ = int(input())
        arr = input() 

        output = run_AC_function(funcs, arr)
        if output != 'error':
            output = parse_list_to_str(output)
        print(output)
