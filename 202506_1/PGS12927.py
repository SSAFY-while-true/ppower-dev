def solution(n, works):
    import heapq
    # 모든 작업을 완료할 수 있는 경우
    if n >= sum(works):
        return 0
    
    # 최대 힙을 구현하기 위해 음수로 변환
    max_heap = [-work for work in works]
    heapq.heapify(max_heap)
    
    # n시간 동안 가장 큰 작업량을 1씩 감소
    for _ in range(n):
        # 가장 큰 작업량 추출
        max_work = -heapq.heappop(max_heap)
        
        # 1만큼 감소시킨 후 다시 힙에 삽입
        if max_work > 0:
            heapq.heappush(max_heap, -(max_work - 1))
        else:
            heapq.heappush(max_heap, 0)
    
    # 남은 작업량들의 제곱의 합 계산
    answer = sum(work * work for work in max_heap)
    return answer
