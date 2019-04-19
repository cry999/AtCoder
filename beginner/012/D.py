def bus_and_inevitable_fate(N: int, M: int, edges: list)->int:
    INF = float('inf')

    d = [[0 if i == j else INF for j in range(N)] for i in range(N)]

    for u, v, t in edges:
        d[u-1][v-1] = t
        d[v-1][u-1] = t

    # warshal-floyd
    for k in range(N):
        for u in range(N):
            for v in range(N):
                d[u][v] = min(d[u][v], d[u][k]+d[k][v])

    # 各駅からもっとも遠い駅のうち、一番遠くないものを出力
    return min(max(row) for row in d)


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    edges = [tuple(int(s) for s in input().split()) for _ in range(M)]

    ans = bus_and_inevitable_fate(N, M, edges)
    print(ans)
