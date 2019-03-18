def reversi(N: int, C: list)->int:
    MOD = 10**9 + 7
    dp = [0] * (N+1)
    dp[0] = 1
    lefts = {}
    for i, c in enumerate(C):
        if c in lefts and lefts[c] != i:
            dp[i+1] = (dp[i] + dp[lefts[c]]) % MOD
        else:
            dp[i+1] = dp[i]
        lefts[c] = i+1
    return dp[N]


if __name__ == "__main__":
    N = int(input())
    C = [int(input()) for _ in range(N)]
    ans = reversi(N, C)
    print(ans)
