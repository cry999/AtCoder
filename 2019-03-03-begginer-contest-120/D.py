class UnionFind:
    def __init__(self, size: int):
        self.__root = [-1 for _ in range(size)]

    def find(self, v: int) -> int:
        if self.__root[v] < 0:
            return v
        self.__root[v] = self.find(self.__root[v])
        return self.__root[v]

    def size(self, v: int) -> int:
        r = self.find(v)
        return -self.__root[r]

    def unite(self, u: int, v: int):
        ur, vr = self.find(u), self.find(v)
        if ur == vr:
            return

        if self.size(ur) < self.size(vr):
            ur, vr = vr, ur

        self.__root[ur] += self.__root[vr]
        self.__root[vr] = ur

    def connected(self, u: int, v: int):
        return self.find(u) == self.find(v)


def decayed_bridges(N: int, M: int, edges: list) -> list:
    ret = [0 for _ in range(M)]
    uf = UnionFind(N)

    current = N*(N-1)//2
    for m in range(M-1, -1, -1):
        ret[m] = current

        u, v = edges[m]
        u, v = u-1, v-1

        if not uf.connected(u, v):
            n1, n2 = uf.size(u), uf.size(v)
            current -= n1 * n2
            uf.unite(u, v)

    return ret


if __name__ == "__main__":
    N, M = [int(s) for s in input().split()]
    edges = []
    for _ in range(M):
        a, b = [int(s) for s in input().split()]
        edges.append((a, b))

    answers = decayed_bridges(N, M, edges)

    for a in answers:
        print(a)
