def prison(N: int, M: int, queries: list)->list:
    l, r = 1, N

    for L, R in queries:
        l = max(l, L)
        r = min(r, R)

    return max(0, r-l+1)


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    queries = [tuple(int(s) for s in input().split()) for _ in range(M)]

    ans = prison(N, M, queries)
    print(ans)
