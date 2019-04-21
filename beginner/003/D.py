def winter(R: int, C: int, X: int, Y: int, D: int, L: int)->int:
    MOD = 10**9 + 7

    # (X x Y) の区画の作り方
    res = ((R-X+1) * (C-Y+1)) % MOD

    comb = [[0] * (X*Y+1) for i in range(X*Y + 1)]
    comb[0][0] = 1

    for n in range(X*Y):
        comb[n+1][0] = 1
        for r in range(n+1):
            comb[n+1][r+1] = (comb[n][r] + comb[n][r+1]) % MOD

    if (X-1)*Y < D + L or X*(Y-1) < D + L:
        # 何も考えず配置しても、上下左右の最大値のさがそれぞれ X, Y となるように
        # 取れる。
        res = (res * comb[X*Y][D]) % MOD
        res = (res * comb[X*Y-D][L]) % MOD
    else:
        # (X-i)*(Y-j) (0 <= i, 0 <= j and (i != 0 or j != 0)) に
        # おさまってしまう場合がある。それらの可能性を引く。
        # dp[x][y] を x 行 y 列に収まる場合の配置数とする。
        # この時、dp[X][Y] - dp[X][Y-1] - dp[X-1][Y] + dp[X-1][Y-1]
        # が作る区画が (X x Y) となる。
        dp = [[0] * (Y+1) for _ in range(X+1)]

        for x in range(X+1):
            for y in range(Y+1):
                if D + L <= x*y:
                    dp[x][y] = (comb[x*y][D] * comb[x*y-D][L]) % MOD
        res = (res * (dp[X][Y]-dp[X][Y-1]-dp[X-1][Y]+dp[X-1][Y-1])) % MOD

        for x in range(X+1):
            print(dp[x])

    return res


if __name__ == "__main__":
    R, C = map(int, input().split())
    X, Y = map(int, input().split())
    D, L = map(int, input().split())

    ans = winter(R, C, X, Y, D, L)
    print(ans)
