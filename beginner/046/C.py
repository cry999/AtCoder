import math


def ceil(a: int, b: int) -> int:
    '''a / b の切り上げを求める。
    '''
    n = a // b
    return n if n * b == a else n + 1


def atcodeer_and_election_report(N: int, ratios: list) -> int:
    t, a = ratios[0]

    for nt, na in ratios[1:]:
        # t <= nt * k and a <= na * k
        # を満たす最小の k を求めたい
        k = max(ceil(t, nt), ceil(a, na))
        t, a = nt * k, na * k

    return t + a


if __name__ == "__main__":
    N = int(input())
    ratios = [tuple(int(s) for s in input().split()) for _ in range(N)]
    ans = atcodeer_and_election_report(N, ratios)
    print(ans)
