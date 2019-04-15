def blue_bird(N: int, M: int, edges: list) -> list:
    d = [[float('inf')] * N for _ in range(N)]
    adj = [float('inf') for _ in range(N)]
    for u, v, l in edges:
        if u == 1:
            # 1 の隣接点は別管理。
            adj[v-1] = min(adj[v-1], l)
        else:
            # 1 を除いたグラフを作成する。
            d[u - 1][v - 1] = d[v - 1][u - 1] = l

    # warshal_floyd
    for k in range(N):
        for u in range(N):
            for v in range(N):
                d[u][v] = min(d[u][v], d[u][k] + d[k][v])

    min_d = float('inf')
    for u, ul in enumerate(adj):
        if ul == float('inf'):
            continue

        for v, vl in enumerate(adj):
            if v == u or vl == float('inf'):
                continue
            min_d = min(min_d, ul + d[u][v] + vl)

    return min_d if min_d < float('inf') else - 1


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    edges = [tuple(int(s) for s in input().split()) for _ in range(M)]

    ans = blue_bird(N, M, edges)
    print(ans)
