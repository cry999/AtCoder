import queue


def even_relation(N: int, edges: list)->list:
    color = [-1] * N
    color[0] = 0

    g = [[] for _ in range(N)]
    for u, v, w in edges:
        g[u-1].append((v-1, w))
        g[v-1].append((u-1, w))

    q = queue.Queue()
    q.put((0, -1))

    while not q.empty():
        u, par = q.get()

        for v, w in g[u]:
            if v == par:
                continue

            if w % 2 == 0:
                color[v] = color[u]
            else:
                color[v] = 1-color[u]

            q.put((v, u))

    return color


if __name__ == "__main__":
    N = int(input())
    edges = [tuple(int(s) for s in input().split()) for _ in range(N-1)]

    for ans in even_relation(N, edges):
        print(ans)
