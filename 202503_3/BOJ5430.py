from collections import deque

def parse_str_to_list(expression: str) -> list:
    """
    str 타입의 입력을 진짜 list로 파싱하는 함수
    좌우의 '[', ']'를 제외한 나머지 str를 split 메서드를 이용해 list로 변환
    """
    if expression == '[]':
        return []
    expression = expression.strip()[1:len(expression) - 1]
    expression = expression.split(',')
    return expression


def parse_list_to_str(expression: list) -> str:
    """
    결과값 형식에 맞도록 list를 파싱하는 함수
    (결과값 출력에는 공백이 없어야 함)
    """
    return '[' + ','.join(expression) + ']'


def run_AC_function(funcs: str, arr: str) -> list:
    arr = deque(parse_str_to_list(arr))
    
    reversed_flag = False       # flag를 사용하지 않으면 O(n)인 deque.reverse()를 많이 써야함

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
    
    if reversed_flag:       # flag가 True면 결과도 뒤집어야함
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
