def restoring_road_network(N: int, A: list)->int:
    total = 0
    for i in range(N):
        for j in range(i+1, N):
            ok = True
            for k in range(N):
                if i == k or k == j:
                    continue
                if A[i][k] + A[k][j] < A[i][j]:
                    return -1
                if A[i][k] + A[k][j] == A[i][j]:
                    ok = False
            if ok:
                total += A[i][j]

    return total


if __name__ == "__main__":
    N = int(input())
    A = [[int(s) for s in input().split()] for _ in range(N)]
    ans = restoring_road_network(N, A)
    print(ans)
