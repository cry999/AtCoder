import queue


def megalomania(N: int, tasks: list)->bool:
    que = queue.PriorityQueue()

    for a, b in tasks:
        que.put((b, a))

    time = 0
    while not que.empty():
        b, a = que.get()
        time += a
        if time > b:
            return False

    return True


if __name__ == "__main__":
    N = int(input())
    tasks = [tuple(int(s) for s in input().split()) for _ in range(N)]

    yes = megalomania(N, tasks)
    print('Yes' if yes else 'No')
