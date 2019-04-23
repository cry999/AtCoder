def rotation_sort(N: int, A: int, B: int, P: list) -> int:
    # x0[v] = v の P 内での初期位置
    x0 = {v: i for i, v in enumerate(P)}

    # dp[k][x] = k が x0[k] から開区間 (x-1, x) に移動するときの最小コスト
    # k が (x-1, x) に移動する際の最小コストは x0->(x-1, x) の移動コストを
    # C とすると
    # dp[k][x] = min(dp[k-1][0], ..., dp[k-1][x])
    dp = [[float('inf')] * (N+1) for _ in range(N+1)]
    dp[0] = [0] * (N+1)

    for k in range(1, N+1):
        # 要素 k-1 が (-inf, x+1) へ移動するための最小コスト
        min_prev = float('inf')
        for x in range(N+1):
            if x == x0[k]:
                # 移動なし
                cost = 0
            elif x < x0[k]:
                # 左移動
                cost = B
            else:
                # 右移動
                cost = A
            min_prev = min(min_prev, dp[k-1][x])
            dp[k][x] = min_prev + cost

    return min(dp[N])


if __name__ == "__main__":
    N, A, B = map(int, input().split())
    P = [int(s) for s in input().split()]

    ans = rotation_sort(N, A, B, P)
    print(ans)
