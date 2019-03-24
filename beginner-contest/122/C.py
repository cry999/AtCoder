def get_ac(N: int, Q: int, S: str, queries: list)->list:
    before = ''
    cum = [0] * (N+1)
    for i, c in enumerate(S):
        cum[i+1] = cum[i]
        if before + c == 'AC':
            cum[i+1] += 1
        before = c

    # print(cum)

    res = []
    for l, r in queries:
        res.append(cum[r] - cum[l])

    return res


if __name__ == "__main__":
    Q = 0
    N, Q = map(int, input().split())
    S = input()
    queries = [tuple(int(s) for s in input().split()) for _ in range(Q)]
    ans = get_ac(N, Q, S, queries)

    for a in ans:
        print(a)
