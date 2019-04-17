def candies(N: int, A: list) -> int:
    S = [[0] * (N + 1), [0] * (N + 1)]
    for n in range(N):
        S[0][n + 1] = S[0][n] + A[0][n]
        S[1][N - (n + 1)] = S[1][N - n] + A[1][N - (n + 1)]

    max_candies = 0
    for n in range(N):
        max_candies = max(max_candies, S[0][n+1] + S[1][n])

    return max_candies


if __name__ == "__main__":
    N = int(input())
    A = [[], []]
    for i in range(2):
        A[i] = [int(s) for s in input().split()]

    ans = candies(N, A)
    print(ans)
