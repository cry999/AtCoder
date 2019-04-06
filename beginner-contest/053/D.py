def card_eater(N: int, A: list)->int:
    d = {}
    for a in A:
        d.setdefault(a, -1)
        d[a] += 1

    exceeds = sum(v for v in d.values())

    return N - exceeds - exceeds % 2


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = card_eater(N, A)
    print(ans)
