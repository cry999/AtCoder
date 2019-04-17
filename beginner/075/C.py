

def dfs(graph: list,
        v: int,
        _from: int,
        low: list,
        pre: list,
        ret: list,
        count: list)->int:
    pre[v] = count[0]
    low[v] = count[0]

    count[0] += 1

    for to in graph[v]:
        if pre[to] >= 0:
            # already visited
            if _from != to:
                low[v] = min(low[v], low[to])
        else:
            low[v] = min(low[v], dfs(graph, to, v, low, pre, ret, count))
            if low[to] == pre[to]:
                ret.append((v, to))

    return low[v]


def bridge(N: int, M: int, edges: list)->int:
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    low, pre = [-1] * N, [-1] * N
    ret = []
    dfs(graph, 0, -1, low, pre, ret, [0])

    return len(ret)


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    edges = [tuple(int(s) for s in input().split()) for _ in range(M)]
    ans = bridge(N, M, edges)
    print(ans)
