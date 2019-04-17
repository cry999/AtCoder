import heapq


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


def dijkstra(s: int, t: int, V: int, edges: list) -> int:
    '''dijkstra method
    :param s: start
    :param t: finish
    :param V: number of vertexes
    :param edges: collection of edges
    :return: minimum distance from u to v
    '''
    d = [float('inf')] * V
    d[s] = 0

    q = PriorityQueue()
    q.enqueue((d[s], s))

    while not q.empty():
        _, u = q.dequeue()
        for v, cost in edges[u]:
            alt = d[u] + cost

            if alt < d[v]:
                d[v] = alt
                q.enqueue((d[v], v))

    return d[t]


def wall(H: int, W: int, C: list, A: list) -> int:
    # 1 から各数字への最短距離を計算する
    edges = [[(v, C[u][v]) for v in range(10)] for u in range(10)]
    min_dist = [dijkstra(i, 1, 10, edges) for i in range(10)]

    return sum(
        min_dist[a]
        for row in A
        for a in row if a >= 0)


if __name__ == "__main__":
    H = 0
    H, W = map(int, input().split())
    C = [[int(s) for s in input().split()] for _ in range(10)]
    A = [[int(s) for s in input().split()] for _ in range(H)]
    ans = wall(H, W, C, A)
    print(ans)
