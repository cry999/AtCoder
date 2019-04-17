def one_card_poker(A: int, B: int) -> str:
    if A == B:
        return 'Draw'
    if A == 1:
        return 'Alice'
    if B == 1:
        return 'Bob'
    if A > B:
        return 'Alice'
    return 'Bob'


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = one_card_poker(A, B)
    print(ans)
