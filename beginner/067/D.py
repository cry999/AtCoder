from queue import Queue


def distances(tree: list, size: int, root: int)->list:
    dists = [0] * size

    q = Queue()
    q.put((root, -1, 0))

    while not q.empty():
        v, prev, d2v = q.get()
        dists[v] = d2v

        for u, dv2u in tree[v]:
            if u == prev:
                continue
            q.put((u, v, d2v + dv2u))

    return dists


def fennec_vs_snuke(N: int, edges: list)->str:
    tree = [[] for _ in range(N)]
    for a, b in edges:
        tree[a-1].append((b-1, 1))
        tree[b-1].append((a-1, 1))

    d_from1 = distances(tree, N, 0)
    d_fromN = distances(tree, N, N-1)

    fennec, snuke = 0, 0
    for i in range(N):
        if d_fromN[i] < d_from1[i]:
            snuke += 1
        else:
            fennec += 1
    return 'Fennec' if fennec > snuke else 'Snuke'


if __name__ == "__main__":
    N = int(input())
    edges = [tuple(int(s) for s in input().split()) for _ in range(N-1)]
    ans = fennec_vs_snuke(N, edges)
    print(ans)
