import heapq
"""
I: 넣어라
D -1: 최솟갑 빼라
D 1: 최댓값 빼라
"""
case_num = int(input())
for _ in range(case_num):
    min_heap = []
    max_heap = []
    heap_remain = {}
    cmd_num = int(input())
    
    for _ in range(cmd_num):
        cmd, number = input().strip().split()
        number = int(number)

        if cmd == 'I':
            heapq.heappush(min_heap, number)
            heapq.heappush(max_heap, -number)
            heap_remain[number] = heap_remain.get(number, 0) + 1
        elif cmd == 'D':
            # 최댓값 빼자
            if number == 1:
                # 최대힙 앞쪽에는 남아있는데 실제로는 없어야할 값이 있을지도 몰?루
                # 최대힙에는 분명히 존재하는데 heap_remain에는 없다? 그럼 이미 최소힙에서 삭제된거심
                # 여기서 바로 heappop 해봤자 의미노노
                while max_heap and heap_remain.get(-max_heap[0], 0) == 0:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    heap_remain[max_val] -= 1
            # 최솟값 빼자
            else:
                # 이하 원리는 같음
                while min_heap and heap_remain.get(min_heap[0], 0) == 0:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    heap_remain[min_val] -= 1
        
    while max_heap and heap_remain.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)
    while min_heap and heap_remain.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)
        
    if not min_heap or not max_heap:
        print('EMPTY')
    else:
        print(f'{-max_heap[0]} {min_heap[0]}')