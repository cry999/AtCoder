class UnionFind:
    def __init__(self, size: int):
        self.__size = size
        self.__root = [-1] * size

    def root(self, x: int)->int:
        if self.__root[x] < 0:
            return x
        self.__root[x] = self.root(self.__root[x])
        return self.__root[x]

    def size(self, x: int)->int:
        root = self.root(x)
        return self.__root[root]

    def same(self, x: int, y: int)->bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int):
        rx, ry = self.root(x), self.root(y)

        if rx == ry:
            return

        if ry < rx:
            rx, ry = ry, rx

        self.__root[rx] += self.__root[ry]
        self.__root[ry] = rx


def connectivity(N: int, K: int, L: int, roads: list, rails: list)->list:
    road_uf, rail_uf = UnionFind(N), UnionFind(N)

    for p, q in roads:
        road_uf.unite(p-1, q-1)

    for r, s in rails:
        rail_uf.unite(r-1, s-1)

    freq = {}
    for i in range(N):
        p = (road_uf.root(i), rail_uf.root(i))
        freq.setdefault(p, 0)
        freq[p] += 1

    return [freq[(road_uf.root(i), rail_uf.root(i))] for i in range(N)]


if __name__ == "__main__":
    K = 0
    L = 0
    N, K, L = map(int, input().split())
    roads = [tuple(int(s) for s in input().split()) for _ in range(K)]
    rails = [tuple(int(s) for s in input().split()) for _ in range(L)]
    ans = connectivity(N, K, L, roads, rails)
    print(' '.join(map(str, ans)))
