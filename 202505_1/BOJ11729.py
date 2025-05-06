def hanoi(num_circle: int, start: int, to: int, via: int, moves: list):
    """
    params:
        num_move: 옮길 원판의 개수
        start: 출발지
        to: 도착지
        via: 경유지
        moves: 이동 경로를 저장할 리스트
    """
    # 기저
    if num_circle == 1:
        moves.append(f"{start} {to}")
        return
    
    # n-1개의 원판을 start에서 via로 옮긴다.
    hanoi(num_circle - 1, start, via, to, moves)
    # 1개의 원판을 start에서 to로 옮긴다.
    moves.append(f"{start} {to}")
    # n-1개의 원판을 via에서 to로 옮긴다.
    hanoi(num_circle - 1, via, to, start, moves)


num_circle = int(input())
moves = []
hanoi(num_circle, 1, 3, 2, moves)
print(len(moves))
print('\n'.join(moves))