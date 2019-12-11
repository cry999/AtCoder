def balanced_path(H: int, W: int, A: list, B: list)->int:
    # M = max(
    #     abs(A[i][j] - B[i][j])
    #     for i in range(H) for j in range(W)
    # ) * (H+W-1)

    # dp = [[[False] * (M+1) for _ in range(W)] for _ in range(H)]
    dp = [[set() for _ in range(W)] for _ in range(H)]
    # dp[0][0][abs(A[0][0] - B[0][0])] = True
    dp[0][0] = set([abs(A[0][0] - B[0][0])])

    for h in range(H):
        for w in range(W):
            # for k in range(M+1):
            for k in dp[h][w]:
                # if not dp[h][w][k]:
                #     continue
                if h+1 < H:
                    s0 = abs(A[h+1][w]-B[h+1][w])

                    s1 = k+s0
                    dp[h+1][w].add(s1)
                    # if s1 < M+1:
                    #     dp[h+1][w][s1] = True

                    s2 = abs(k-s0)
                    dp[h+1][w].add(s2)
                    # if s2 < M+1:
                    #     dp[h+1][w][s2] = True

                if w+1 < W:
                    s0 = abs(A[h][w+1]-B[h][w+1])

                    s1 = k+s0
                    dp[h][w+1].add(s1)
                    # if s1 < M+1:
                    #     dp[h][w+1][s1] = True

                    s2 = abs(k-s0)
                    dp[h][w+1].add(s2)
                    # if s2 < M+1:
                    #     dp[h][w+1][s2] = True

    # for k in range(M+1):
    #     if dp[H-1][W-1][k]:
    #         return k
    # for k in dp[H-1][W-1]:

    # return None
    return min(dp[H-1][W-1])


if __name__ == "__main__":
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]

    ans = balanced_path(H, W, A, B)
    print(ans)
