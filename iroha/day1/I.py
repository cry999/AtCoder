import queue


def squirrel_work(N: int, M: int, K: int, edges: list)->int:
    g = [[] for _ in range(N)]

    for a, b, c in edges:
        g[a-1].append((b-1, c))
        g[b-1].append((a-1, c))

    d = [float('inf')] * N
    d[0] = 0
    q = queue.PriorityQueue()
    q.put((d[0], 0, -1))

    while not q.empty():
        _, u, pre_c = q.get()

        for v, vc in g[u]:
            c = 0 if pre_c == vc else 1
            alt = d[u] + c
            if alt < d[v]:
                d[v] = alt
                q.put((d[v], v, vc))

    return d[N-1] * K if d[N-1] < float('inf') else -1


if __name__ == "__main__":
    M = 0
    N, M, K = map(int, input().split())
    edges = [tuple(int(s) for s in input().split()) for _ in range(M)]

    ans = squirrel_work(N, M, K, edges)
    print(ans)
