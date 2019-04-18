def friend_of_friend(N: int, M: int, rel: list) -> list:
    INF = float('inf')

    d = [[0 if i == j else INF for i in range(N)] for j in range(N)]
    for a, b in rel:
        d[a-1][b-1] = 1
        d[b-1][a-1] = 1

    # Warshal-Floyd
    for k in range(N):
        for u in range(N):
            for v in range(N):
                d[u][v] = min(d[u][v], d[u][k]+d[k][v])

    return [sum(dist == 2 for dist in from_u) for from_u in d]


if __name__ == "__main__":
    M = 0
    N, M = map(int, input().split())
    rel = [tuple(int(s) for s in input().split()) for _ in range(M)]

    ans = friend_of_friend(N, M, rel)
    for a in ans:
        print(a)
