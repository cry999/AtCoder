def blackjack(A1: int, A2: int, A3: int)->bool:
    return A1+A2+A3 < 22


if __name__ == "__main__":
    A1, A2, A3 = map(int, input().split())
    ans = blackjack(A1, A2, A3)
    print('win' if ans else 'bust')
