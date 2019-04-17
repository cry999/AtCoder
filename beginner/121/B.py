def can_you_solve_this(
        N: int, M: int, A: list, B: list, C: int)->int:
    AB = [0] * N
    for i in range(N):
        for j in range(M):
            AB[i] += A[i][j] * B[j]
        AB[i] += C
    return sum(1 for ab in AB if ab > 0)


if __name__ == "__main__":
    N = 0
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [[int(s) for s in input().split()] for _ in range(N)]
    ans = can_you_solve_this(N, M, A, B, C)
    print(ans)
