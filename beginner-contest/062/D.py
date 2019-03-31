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


def _3N_numbers(N: int, A: list)->int:
    # first half
    q = PriorityQueue()
    first_half = [0] * (N+1)
    for i in range(N):
        q.enqueue(A[i])
        first_half[0] += A[i]

    for k in range(N):
        q.enqueue(A[N+k])
        decrement = q.dequeue()
        first_half[k+1] = first_half[k] - decrement + A[N+k]

    # second half
    q = PriorityQueue()
    second_half = [0] * (N+1)
    for i in range(N):
        q.enqueue(-A[3*N-1-i])
        second_half[N] += A[3*N-1-i]

    for k in range(N):
        q.enqueue(-A[2*N-1-k])
        decrement = -q.dequeue()
        second_half[N-(k+1)] = second_half[N-k] - decrement + A[2*N-1-k]

    return max(f - s for f, s in zip(first_half, second_half))


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = _3N_numbers(N, A)
    print(ans)
