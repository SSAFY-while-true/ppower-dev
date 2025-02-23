def main():
    n, d = map(int, input().split())
    pedigree = list(map(int, input().split()))
    output = calculate_min_parent_to_add(n, d, pedigree)
    print(output)

def calculate_min_parent_to_add(n, d, pedigree):
    child_count = [0] * (n + 1)
    result_count = 0

    for ancestor in pedigree:
        child_count[ancestor] += 1

    for child in child_count:
        while child > d:
            result_count += 1
            child = child - d + 1

    return result_count

if __name__ == '__main__':
    main()
