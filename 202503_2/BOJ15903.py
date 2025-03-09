import heapq

def combine_two_min_val(heap: list, n: int):
    for _ in range(n):
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        combined = min1 + min2

        heapq.heappush(heap, combined)
        heapq.heappush(heap, combined)

    return heap 
    

if __name__ == '__main__':
    card_num, combine_num = map(int, input().split())
    cards = list(map(int, input().split()))
    heapq.heapify(cards)
     
    output = sum(combine_two_min_val(cards, combine_num))
    print(output)
