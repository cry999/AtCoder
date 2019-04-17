import queue


def honest_takahashi(N: int, a: int, b: int, M: int, edges: list) -> int:
    MOD = 10 ** 9 + 7

    d = [[float('inf') if i != j else 0 for i in range(N)] for j in range(N)]
    adj = [[] for _ in range(N)]

    for u, v in edges:
        d[u - 1][v - 1] = 1
        d[v - 1][u - 1] = 1

        # 隣接点を記録しておく
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)

    # warshal-floyd
    for k in range(N):
        for u in range(N):
            for v in range(N):
                d[u][v] = min(d[u][v], d[u][k] + d[k][v])

    # ある点 x から b への最短経路への行き方を再帰的に計算する
    shortest_paths = [0] * N
    shortest_paths[b - 1] = 1

    def rec(start: int) -> int:
        if shortest_paths[start] > 0:
            return shortest_paths[start]

        for k in range(N):
            if d[start][k] == 1 and d[start][b - 1] == d[start][k] + d[k][b - 1]:
                shortest_paths[start] += rec(k)
                shortest_paths[start] %= MOD
        return shortest_paths[start]

    return rec(a-1)


if __name__ == "__main__":
    N = int(input())
    a, b = map(int, input().split())
    M = int(input())
    edges = [tuple(int(s) for s in input().split()) for _ in range(M)]

    ans = honest_takahashi(N, a, b, M, edges)
    print(ans)
