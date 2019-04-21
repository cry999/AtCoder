def trump_insert_sort(N: int, C: list)->int:
    INF = float('inf')
    # dp[k] = 長さ k の部分列の最後の数字で最小のもの
    dp = [INF] * (N+1)
    dp[0] = -INF

    for c in C:
        # 自分より小さい値で終わっている最長の部分列を探す
        l, r = 0, N
        while r-l > 1:
            m = (r+l)//2
            # print(m)
            if dp[m] < c:
                l = m
            else:
                r = m
        dp[l+1] = min(dp[l+1], c)

    max_len = 0
    for k, v in enumerate(dp):
        if v < INF:
            max_len = k

    # print(dp)

    return N - max_len


if __name__ == "__main__":
    N = int(input())
    C = [int(input()) for _ in range(N)]

    ans = trump_insert_sort(N, C)
    print(ans)
