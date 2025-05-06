def hanoi(num_circle: int, start: int, to: int, via: int):
    """
    params:
        num_move: 옮길 원판의 개수
        start: 출발지
        to: 도착지
        via: 경유지
    """
    # 기저
    if num_circle == 1:
        print(start, to)
        return
    
    # n-1개의 원판을 start에서 via로 옮긴다.
    hanoi(num_circle - 1, start, via, to)
    # 1개의 원판을 start에서 to로 옮긴다.
    print(start, to)
    # n-1개의 원판을 via에서 to로 옮긴다.
    hanoi(num_circle - 1, via, to, start)


num_circle = int(input())

hanoi(num_circle, 1, 3, 2)