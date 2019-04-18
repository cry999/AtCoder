def supplement(N: int, M: int, F: list) -> int:
    MOD = 10**9 + 7

    # dp[i] は i 個目までのサプリメントの摂取方法
    dp = [0] * (N+1)
    dp[0] = 1

    # 現在見ている区間で味 fi を既に使用している場合には
    # fi in using == True
    using = [False] * (M+1)
    l, r = 0, 0  # 現在見ている区間の左右のインデックス
    s = dp[0]    # 現在見ている区間の累積和

    for r in range(N):
        # 新しく入る右端をチェック
        while using[F[r]]:
            # 現在の区間ですでに使っているなら、使わなくなるまで
            # 左端をすすめる。
            using[F[l]] = False
            s -= dp[l]
            s %= MOD
            l += 1
        dp[r+1] = s

        # 右端を進める
        s += dp[r+1]
        s %= MOD
        using[F[r]] = True
        r += 1

    return dp[N]


if __name__ == "__main__":
    N = 0
    N, M = map(int, input().split())
    F = [int(input()) for _ in range(N)]
    ans = supplement(N, M, F)
    print(ans)
