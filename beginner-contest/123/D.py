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


def cake123(X: int, Y: int, Z: int, K: int, A: list, B: list, C: list)->list:
    ret = [0] * K

    sA = sorted(-a for a in A)
    sB = sorted(-b for b in B)
    sC = sorted(-c for c in C)

    q = PriorityQueue()
    q.enqueue((sA[0] + sB[0] + sC[0], 0, 0, 0))

    used = {}

    k = 0
    while k < K:
        delicious, ai, bi, ci = q.dequeue()
        if -delicious in used and (ai, bi, ci) in used[-delicious]:
            continue

        used.setdefault(-delicious, set())
        used[-delicious].add((ai, bi, ci))

        ret[k] = -delicious
        k += 1

        if ai+1 < X:
            q.enqueue((sA[ai+1] + sB[bi] + sC[ci], ai+1, bi, ci))
        if bi+1 < Y:
            q.enqueue((sA[ai] + sB[bi+1] + sC[ci], ai, bi+1, ci))
        if ci+1 < Z:
            q.enqueue((sA[ai] + sB[bi] + sC[ci+1], ai, bi, ci+1))

    return ret


if __name__ == "__main__":
    X, Y, Z, K = map(int, input().split())
    A = [int(s) for s in input().split()]
    B = [int(s) for s in input().split()]
    C = [int(s) for s in input().split()]
    ans = cake123(X, Y, Z, K, A, B, C)
    for a in ans:
        print(a)
