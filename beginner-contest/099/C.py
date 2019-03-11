def strange_bank(N: int) -> int:
    prices = [1] + \
        [9 ** i for i in range(1, 6)] + \
        [6 ** i for i in range(1, 7)]
    dp = [float('inf')] * (N + 1)
    dp[N] = 0

    for n in range(N, 0, -1):
        for p in prices:
            if p <= N:
                dp[n-p] = min(dp[n] + 1, dp[n-p])

    return dp[0]


if __name__ == "__main__":
    N = int(input())
    ans = strange_bank(N)
    print(ans)
