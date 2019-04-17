import heapq


class UnionFind:
    def __init__(self, size: int):
        self.__size = size
        self.__root = [-1] * size

    def find(self, x: int)->int:
        if self.__root[x] < 0:
            return x

        root = self.find(self.__root[x])
        self.__root[x] = root

        return root

    def same(self, x: int, y: int)->bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)

        if rx == ry:
            return

        if self.__root[ry] < self.__root[rx]:
            rx, ry = ry, rx

        self.__root[rx] += self.__root[ry]
        self.__root[ry] = rx


class PriorityQueue:
    def __init__(self):
        self.__heap = []
        self.__count = 0

    def empty(self) -> bool:
        return self.__count == 0

    def dequeue(self):
        if self.empty():
            raise Exception('empty')
        self.__count -= 1
        return heapq.heappop(self.__heap)

    def enqueue(self, v):
        self.__count += 1
        heapq.heappush(self.__heap, v)

    def __len__(self):
        return self.__count


def kruskal(edges: list, size: int)->list:
    q = PriorityQueue()
    for c, u, v in edges:
        q.enqueue((c, u, v))
    uf = UnionFind(size)

    min_tree = []
    while not q.empty():
        c, u, v = q.dequeue()

        if not uf.same(u, v):
            uf.union(u, v)
            min_tree.append((c, u, v))

    return min_tree


def built(N: int, points: list)->int:
    edges = []
    points = [(i, x, y) for i, (x, y) in enumerate(points)]
    sorted_x = sorted(points, key=lambda p: p[1])
    sorted_y = sorted(points, key=lambda p: p[2])

    for i in range(N-1):
        u, ux, _ = sorted_x[i]
        v, vx, _ = sorted_x[i+1]
        edges.append((vx-ux, u, v))

        u, _, uy = sorted_y[i]
        v, _, vy = sorted_y[i+1]
        edges.append((vy-uy, u, v))

    tree = kruskal(edges, 2*(N-1))

    return sum(c for c, _, _ in tree)


if __name__ == "__main__":
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    ans = built(N, points)
    print(ans)
