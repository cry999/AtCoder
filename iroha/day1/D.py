def muscle_battle(N: int, X: int, Y: int, A: list)->str:
    sortedA = sorted(A, key=lambda x: -x)

    takahashi = X + sum(sortedA[0::2])
    aoki = Y + sum(sortedA[1::2])

    if aoki < takahashi:
        return 'Takahashi'
    elif takahashi < aoki:
        return 'Aoki'
    else:
        return 'Draw'


if __name__ == "__main__":
    N, X, Y = map(int, input().split())
    A = [int(s) for s in input().split()]

    ans = muscle_battle(N, X, Y, A)
    print(ans)
