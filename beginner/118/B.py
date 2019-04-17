def foods_loved_by_everyone(N: int, M: int, KA: list) -> int:
    loved = [0] * M

    for ka in KA:
        for a in ka[1:]:
            loved[a-1] += 1

    return sum([1 for l in loved if l == N])


if __name__ == "__main__":
    N = 0
    N, M = [int(s) for s in input().split()]
    KA = [[int(s) for s in input().split()] for _ in range(N)]
    ans = foods_loved_by_everyone(N, M, KA)
    print(ans)
