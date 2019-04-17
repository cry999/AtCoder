class Queue:
    def __init__(self):
        self.__count = 0
        self.__data = []

    def count(self) -> int:
        return self.__count

    def empty(self) -> bool:
        return self.__count == 0

    def front(self):
        if self.empty():
            raise Exception('empty')
        return self.__data[0]

    def dequeue(self):
        if self.empty():
            raise Exception('empty')
        res, self.__data = self.__data[0], self.__data[1:]
        self.__count -= 1
        return res

    def enqueue(self, v):
        self.__data.append(v)
        self.__count += 1


class Edge:
    def __init__(self, v: int, cap: int, rev: int):
        """
        :param v: to
        :param cap: capacity
        :param rev: revesed to
        """
        self.v = v
        self.cap = cap
        self.rev = rev

        self.flow = 0


class Graph:
    def __init__(self, num_v: int):
        """
        :param num_v: number of vertex
        """
        self.num_v = num_v
        self.level = [0] * num_v
        self.graph = [[] for _ in range(num_v)]

    def add_edge(self, u: int, v: int, cap: int):
        """add edge
        :param u: from
        :param v: to
        :param cap: capacity
        """
        forward = Edge(v, cap, len(self.graph[v]))
        back = Edge(u, 0, len(self.graph[u]))

        self.graph[u].append(forward)
        self.graph[v].append(back)

    def __bfs(self, s: int, t: int) -> bool:
        """Finds if more flow can be sent from s to t.
        Also assigns level to nodes.
        :param s: source
        :param t: sink
        :return: `True` if finds more flow can be sent from s to t.
        """
        self.level = [-1] * self.num_v
        self.level[s] = 0

        q = Queue()
        q.enqueue(s)
        while not q.empty():
            u = q.dequeue()

            for e in self.graph[u]:
                # not yet visited, and flow can be sent more
                if self.level[e.v] < 0 and e.flow < e.cap:
                    # level of v is level of its parent + 1
                    self.level[e.v] = self.level[u] + 1

                    q.enqueue(e.v)

        return self.level[t] >= 0

    def __send_flow(self,
                    u: int, flow: int, t: int, start: list = None) -> int:
        """send `flow` from `u` to `t`.
        :param u: from
        :param flow: flow
        :param t: to
        :param start: explored vertex
        :return: value of flow can be sent from u to t.
        """
        if u == t:
            return flow

        if start is None:
            start = [0] * (self.num_v + 1)

        while start[u] < len(self.graph[u]):
            e = self.graph[u][start[u]]

            if self.level[e.v] != self.level[u] + 1:
                # skip if level of e.v is not next to
                # u's one.
                start[u] += 1
                continue
            if not (e.flow < e.cap):
                # skip if flow cannot be sent more to
                # v.
                start[u] += 1
                continue

            cur_f = min(flow, e.cap - e.flow)
            tmp_f = self.__send_flow(e.v, cur_f, t, start)

            if tmp_f > 0:
                # add flow to current edge
                e.flow += tmp_f
                # subtract flow from reverse edge of current one.
                self.graph[e.v][e.rev].flow -= tmp_f

                return tmp_f

            start[u] += 1

        return 0

    def maximum_flow(self, s: int, t: int) -> int:
        """maximum flow from s to t.
        :param s: from
        :param t: to
        :return: maximum flow
        """
        if s == t:
            return 0

        max_flow = 0
        while self.__bfs(s, t):
            while True:
                flow = self.__send_flow(s, float('inf'), t)
                if flow == 0:
                    break
                max_flow += flow
        return max_flow


def _2d_plane_2n_points(N: int, reds: list, blues: list) -> int:
    reds = sorted(reds, key=lambda x: x[0])
    blues = sorted(blues, key=lambda x: x[0])

    # bipartite matching
    g = Graph(2*N + 2)
    s, t = 0, 2*N+1

    def blue_idx(i): return i + 1
    def red_idx(i): return N + i + 1

    # add edges from source to blue stars and
    # from red stars to sink
    for i in range(N):
        b, r = blue_idx(i), red_idx(i)
        g.add_edge(s, b, 1)
        g.add_edge(r, t, 1)

    # add edges from blue star to red star
    # when rx < ry and bx < by
    for i, (bx, by) in enumerate(blues):
        bi = blue_idx(i)

        for j, (rx, ry) in enumerate(reds):
            if not (rx < bx):
                break
            if not (ry < by):
                continue

            ri = red_idx(j)
            g.add_edge(bi, ri, 1)

    return g.maximum_flow(s, t)


if __name__ == "__main__":
    N = int(input())
    reds = [tuple(map(int, input().split())) for _ in range(N)]
    blues = [tuple(map(int, input().split())) for _ in range(N)]
    ans = _2d_plane_2n_points(N, reds, blues)
    print(ans)
