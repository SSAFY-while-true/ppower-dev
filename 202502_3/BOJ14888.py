import sys
from itertools import permutations

def main():
    n = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().split()))
    operator_counts = list(map(int, sys.stdin.readline().split()))
    
    max_result, min_result = calculate(n, numbers, operator_counts)
    print(max_result)
    print(min_result)
    

def calculate(n, numbers, operator_counts):
    operators = ('+', '-', '*', '/')
    operator_list = []
    
    for i in range(4):
        operator_list.extend([operators[i]] * operator_counts[i])
    
    max_value = -float('inf')
    min_value = float('inf')
    
    for perm in set(permutations(operator_list)):
        result = numbers[0]
        for i in range(n - 1):
            if perm[i] == '+':
                result += numbers[i + 1]
            elif perm[i] == '-':
                result -= numbers[i + 1]
            elif perm[i] == '*':
                result *= numbers[i + 1]
            elif perm[i] == '/':
                if result < 0:
                    result = -(-result // numbers[i + 1])
                else:
                    result //= numbers[i + 1]
        
        max_value = max(max_value, result)
        min_value = min(min_value, result)
    
    return max_value, min_value


if __name__ == '__main__':
    main()
