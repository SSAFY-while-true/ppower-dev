def find_winner(n: int) -> str:
    """
    자신의 턴에 돌 4개가 남으면 무조건 진다.
    상대에게 무조건 4의 배수 돌을 남기는 것이 중요하다.
    4의 배수가 아닌 돌은 무조건 4의 배수가 되도록 할 수 있긴 함
    """
    if n % 4 == 0:
        return "CY"
    else:
        return "SK"

n = int(input())
print(find_winner(n))
    