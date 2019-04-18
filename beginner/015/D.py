def distress(W: int, N: int, K: int, screenshots: list)->int:
    dp = [[0] * (W+1) for _ in range(K+1)]

    for width, priority in screenshots:
        for k in range(K, 0, -1):
            for w in range(W, -1, -1):
                if width <= w:
                    dp[k][w] = max(dp[k][w], dp[k-1][w-width]+priority)
    return dp[K][W]


if __name__ == "__main__":
    W = int(input())
    N = 0
    N, K = map(int, input().split())
    screenshots = [tuple(int(s) for s in input().split()) for _ in range(N)]

    ans = distress(W, N, K, screenshots)
    print(ans)
