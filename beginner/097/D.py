class UnionFindTree:
    def __init__(self, size: int):
        self.__size = size
        self.__data = [-1] * (size + 1)

    def unite(self, u: int, v: int):
        x, y = self.find(u), self.find(v)
        if x == y:
            return

        self.__data[x] += self.__data[y]
        self.__data[y] = x

    def find(self, u: int) -> int:
        if self.__data[u] < 0:
            return u
        self.__data[u] = self.find(self.__data[u])
        return self.__data[u]

    def same(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)


def equals(N: int, M: int, P: list, XY: list) -> int:
    """例えば xi <-> xj かつ xj <-> xk の場合、xi、xj、xk は
    どの二つも交換可能である。したがって、交換可能なインデックス
    の集合をつくり、そのインデックスの集合とインデックスに対応し
    た P の部分集合との一致する部分が正しい位置における数値群と
    なる。
    """
    uft = UnionFindTree(N)
    for x, y in XY:
        uft.unite(x, y)

    return sum(1 for i, p in enumerate(P) if uft.same(i+1, p))


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    P = [int(s) for s in input().split()]
    XY = [tuple(int(s) for s in input().split()) for _ in range(M)]
    ans = equals(N, M, P, XY)
    print(ans)
