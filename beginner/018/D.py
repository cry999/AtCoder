import itertools


def valentine_day(
        N: int, M: int, P: int, Q: int, R: int, choco: list) -> int:

    choco_belong_to = [[] for _ in range(N)]
    for f, m, happiness in choco:
        choco_belong_to[f-1].append((m-1, happiness))

    max_happiness = 0
    for females in itertools.combinations([f for f in range(N)], P):
        happiness_of = [0] * M

        for f in females:
            for m, happiness in choco_belong_to[f]:
                happiness_of[m] += happiness

        happiness_ranking = sorted(happiness_of, key=lambda x: -x)
        max_happiness = max(max_happiness, sum(happiness_ranking[:Q]))

    return max_happiness


if __name__ == "__main__":
    R = 0
    N, M, P, Q, R = map(int, input().split())
    choco = [tuple(int(s) for s in input().split()) for _ in range(R)]
    ans = valentine_day(N, M, P, Q, R, choco)
    print(ans)
