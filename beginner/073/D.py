def permutation(l: list)->list:
    if len(l) == 1:
        return [l]

    ret = []
    for i, e in enumerate(l):
        for p in permutation(l[:i] + l[i+1:]):
            ret.append([e] + p)
    return ret


def joisinos_travel(
        N: int, M: int, R: int, visits: list, edges: list)->int:
    INF = float('inf')

    A = [[INF] * N for _ in range(N)]
    for i in range(N):
        A[i][i] = 0
    for u, v, c in edges:
        A[u-1][v-1] = c
        A[v-1][u-1] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                A[i][j] = min(A[i][j], A[i][k]+A[k][j])

    min_d = float('inf')
    for perm in permutation(visits):
        d = sum(A[perm[i]-1][perm[i+1]-1] for i in range(R-1))
        min_d = min(min_d, d)

    return min_d


if __name__ == "__main__":
    M = 0
    N, M, R = map(int, input().split())
    visits = [int(s) for s in input().split()]
    edges = [tuple(int(s) for s in input().split()) for _ in range(M)]
    ans = joisinos_travel(N, M, R, visits, edges)
    print(ans)
