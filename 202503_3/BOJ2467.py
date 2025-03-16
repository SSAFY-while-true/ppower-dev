def find_min_diff_coord(solutions: list) -> tuple:
    solutions.sort()
    left, right = 0, len(solutions) - 1
    min_diff = float('inf')
    best_pair = (solutions[left], solutions[right])

    while left < right:
        curr_sum = solutions[left] + solutions[right]

        if abs(curr_sum) < min_diff:
            min_diff = abs(curr_sum)
            best_pair = (solutions[left], solutions[right])

        if curr_sum > 0:
            right -= 1
        else:
            left += 1

    return best_pair

if __name__ == '__main__':
    solution_num = int(input())
    solutions = list(map(int, input().split()))
    sol1, sol2 = find_min_diff_coord(solutions)

    print(f'{sol1} {sol2}')
