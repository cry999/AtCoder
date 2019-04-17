def counting_roads(N: int, M: int, roads: list)->list:
    d = {i: 0 for i in range(N)}
    for u, v in roads:
        d[u-1] += 1
        d[v-1] += 1

    return d.values()


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(M)]
    ans = counting_roads(N, M, roads)
    print('\n'.join(map(str, ans)))
