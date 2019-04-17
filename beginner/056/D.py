def no_need(N: int, K: int, A: list) -> int:
    A.sort()

    dp = [[False] * (K) for _ in range(N)]

    def need(i: int) -> bool:
        for n in range(N):
            for k in range(K):
                dp[n][k] = False
        dp[0][0] = True

        card_num, n = 0, 0
        for a in A:
            n += 1
            if n-1 == i:
                continue
            for k in range(K):
                dp[card_num + 1][k] = \
                    dp[card_num][k] or (a <= k and dp[card_num][k - a])
            card_num += 1

        for k in range(max(K - A[i], 0), K):
            if dp[N - 1][k]:
                return True
        return False

    l, r = -1, N
    while l + 1 < r:
        m = (l + r) // 2
        if need(m):
            r = m
        else:
            l = m

    return l+1


if __name__ == "__main__":
    N, K = map(int, input().split())
    A = [int(s) for s in input().split()]
    ans = no_need(N, K, A)
    print(ans)
