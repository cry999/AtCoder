import queue


def integer_cards(N: int, M: int, A: list, queries: list)->int:
    que = queue.PriorityQueue()

    for a in A:
        que.put(a)

    queries.sort(key=lambda x: -x[1])

    for B, C in queries:
        x = que.get()
        que.put(x)

        if C <= x:
            break

        for _ in range(B):
            x = que.get()

            que.put(max(x, C))

            if C <= x:
                break

    res = 0
    for _ in range(N):
        res += que.get()
    return res


if __name__ == "__main__":
    M = 0

    N, M = map(int, input().split())
    A = [int(s) for s in input().split()]
    queries = [tuple(int(s) for s in input().split()) for _ in range(M)]

    ans = integer_cards(N, M, A, queries)
    print(ans)
