def typical_stairs(N: int, M: int, A: list)->int:
    MOD = 10**9 + 7

    dp = [0] * (N+1)
    dp[0] = 1

    ai = 0
    for i in range(N):
        if ai < M and A[ai] == i+1:
            dp[i+1] = 0
            ai += 1
        else:
            dp[i+1] = dp[i]
            if i > 0:
                dp[i+1] += dp[i-1]
                dp[i+1] %= MOD

    # print(dp)
    return dp[N]


if __name__ == "__main__":
    M = 0

    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]

    ans = typical_stairs(N, M, A)
    print(ans)
