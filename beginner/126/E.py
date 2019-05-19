class UnionFind:
    def __init__(self, size: int):
        self.__size = size
        self.__root = [-1] * size

    def find(self, x: int)->int:
        if self.__root[x] < 0:
            return x
        self.__root[x] = self.find(self.__root[x])
        return self.__root[x]

    def union(self, x: int, y: int)->int:
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return

        if self.__root[ry] < self.__root[rx]:
            rx, ry = ry, rx

        self.__root[rx] += self.__root[ry]
        self.__root[ry] = rx

    def same(self, x: int, y: int)->bool:
        return self.find(x) == self.find(y)


def one_or_two(N: int, M: int, queries: list)->int:
    uf = UnionFind(N)

    for x, y, _ in queries:
        uf.union(x-1, y-1)

    return len(set(uf.find(i) for i in range(N)))


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    queries = [tuple(int(s) for s in input().split()) for _ in range(M)]

    ans = one_or_two(N, M, queries)
    print(ans)
