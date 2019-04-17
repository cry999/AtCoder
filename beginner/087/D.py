class WeightenedUnionFind:
    def __init__(self, size: int):
        self.__size = size
        self.__root = [-1] * size
        self.__diff_weight = [0] * size

    def find(self, u: int)->int:
        if self.__root[u] < 0:
            return u
        r = self.find(self.__root[u])
        self.__diff_weight[u] += self.__diff_weight[self.__root[u]]
        self.__root[u] = r
        return self.__root[u]

    def same(self, u: int, v: int)->bool:
        return self.find(u) == self.find(v)

    def unite(self, u: int, v: int, w: int):
        w += self.weight(u)
        w -= self.weight(v)

        x, y = self.find(u), self.find(v)

        if x == y:
            return

        if self.__root[y] < self.__root[x]:
            x, y = y, x
            w = -w

        self.__root[x] += self.__root[y]
        self.__root[y] = x

        self.__diff_weight[y] = w

    def weight(self, u: int)->int:
        self.find(u)
        return self.__diff_weight[u]

    def diff_weight(self, u: int, v: int)->int:
        return self.weight(v) - self.weight(u)


def people_on_a_line(N: int, M: int, queries: list)->bool:
    uf = WeightenedUnionFind(N)
    for l, r, d in queries:
        if uf.same(l-1, r-1):
            if d != uf.diff_weight(l-1, r-1):
                return False
        else:
            uf.unite(l-1, r-1, d)

    return True


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    queries = [tuple(int(s) for s in input().split()) for _ in range(M)]
    yes = people_on_a_line(N, M, queries)
    print('Yes' if yes else 'No')
