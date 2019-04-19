import math


class LCA:
    def __init__(self, edges: list, V: int):
        self.G = [[] for _ in range(V)]
        for u, v in edges:
            self.G[u-1].append(v-1)
            self.G[v-1].append(u-1)

        self.logV = math.ceil(math.log(V, 2))
        self.parent = [[0] * (V) for _ in range(self.logV)]
        self.depth = [0] * V

        self.__build(V)

    def __build(self, V: int):
        self.__dfs(0, -1, 0)

        for k in range(self.logV-1):
            for v in range(V):
                if self.parent[k][v] < 0:
                    self.parent[k+1][v] = -1
                else:
                    self.parent[k+1][v] = self.parent[k][self.parent[k][v]]

    def __dfs(self, v: int, p: int, d: int):
        self.parent[0][v] = p
        self.depth[v] = d
        for u in self.G[v]:
            if u != p:
                self.__dfs(u, v, d+1)

    def lca(self, u: int, v: int)->int:
        if self.depth[u] > self.depth[v]:
            u, v = v, u

        for k in range(self.logV):
            if ((self.depth[v]-self.depth[u]) >> k) & 1:
                v = self.parent[k][v]

        if u == v:
            return u

        for k in range(self.logV-1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]

        return self.parent[0][u]

    def dist(self, u: int, v: int)->int:
        lca = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2*self.depth[lca]


def cycle(N: int, edges: list, Q: int, queries: list)->list:
    lca = LCA(edges, N)

    return [lca.dist(a-1, b-1)+1 for a, b in queries]


if __name__ == "__main__":
    N = int(input())
    edges = [tuple(int(s) for s in input().split()) for _ in range(N-1)]
    Q = int(input())
    queries = [tuple(int(s) for s in input().split()) for _ in range(Q)]

    ans = cycle(N, edges, Q, queries)
    for a in ans:
        print(a)
