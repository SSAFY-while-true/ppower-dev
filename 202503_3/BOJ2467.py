def find_min_diff_coord(solutions: list) -> tuple:
    solutions.sort()
    min_acid_idx = float('inf')
    min_base_idx = float('-inf')
    found_acid = False
    print(solutions)
    print(found_acid)
    for i in range(len(solutions)):
        if solutions[i] > 0:
            found_acid = True
            if i == 0:
                return solutions[0], solutions[1]
            min_acid_idx = i
            min_base_idx = i - 1
            break
        
        if not found_acid:
            return solutions[-2], solutions[-1]
    elem1 = (abs(solutions[min_acid_idx] + solutions[min_base_idx]), solutions[min_base_idx], solutions[min_acid_idx])
    elem2 = (abs(solutions[min_acid_idx] + solutions[min_acid_idx + 1]), solutions[min_acid_idx], solutions[min_acid_idx + 1])
    elem3 = (abs(solutions[min_base_idx] + solutions[min_base_idx - 1]), solutions[min_base_idx - 1], solutions[min_base_idx])
    elem4 = (abs(solutions[0] + solutions[-1]), solutions[0], solutions[-1])
    
    min_elem = min(elem1, elem2, elem3, elem4, key=lambda x: x[0])
    return min_elem[1], min_elem[2]
    

if __name__ == '__main__':
    solution_num = int(input())
    solutions = list(map(int, input().split()))
    min_diff_coord = find_min_diff_coord(solutions)
    sol1, sol2 = min_diff_coord

    print(f'{sol1} {sol2}')
