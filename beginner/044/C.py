def tak_and_cards(N: int, A: int, X: list) -> int:
    #  部分点解法
    # :---------:
    # count = 0
    # for b in range(1, 1 << N):
    #     n, s = 0, 0
    #     for i in range(N):
    #         if (b >> i) & 1 == 0:
    #             continue
    #         n += 1
    #         s += X[i]

    #     if s == n * A:
    #         count += 1
    # return count
    max_X = max(X)
    dp = [[0] * (2 * max_X * N + 1) for _ in range(N + 1)]
    dp[0][max_X * N] = 1

    for k, x in enumerate(X):
        for t in range(2 * max_X * N + 1):
            y = x - A

            dp[k + 1][t] = dp[k][t]
            if 0 <= t - y and t - y <= 2 * max_X * N:
                dp[k + 1][t] += dp[k][t - y]

    return dp[N][max_X*N] - 1


if __name__ == "__main__":
    N, A = map(int, input().split())
    x = [int(s) for s in input().split()]
    ans = tak_and_cards(N, A, x)
    print(ans)
