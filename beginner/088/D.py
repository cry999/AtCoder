def grid_repainting(H: int, W: int, S: int) -> int:
    # ルート探索用の行列。
    # R[h][w] は (0, 0) -> (h, w) の最短距離になる。
    INF = float('inf')
    R = [[INF] * W for _ in range(H)]
    R[0][0] = 1
    white_num = 0

    update = True
    while update:
        update = False
        white_num = 0
        for h in range(H):
            for w in range(W):
                if S[h][w] == '#':
                    # 黒いマス目は無視
                    continue
                white_num += 1

                before = R[h][w]
                if w > 0:
                    R[h][w] = min(R[h][w], R[h][w - 1] + 1)
                if h > 0:
                    R[h][w] = min(R[h][w], R[h - 1][w] + 1)
                if w < W - 1:
                    R[h][w] = min(R[h][w], R[h][w + 1] + 1)
                if h < H - 1:
                    R[h][w] = min(R[h][w], R[h + 1][w] + 1)

                if before != R[h][w]:
                    update = True

    if R[H - 1][W - 1] is INF:
        return - 1

    # R[H-1][W-1] は (0, 0) -> (H-1, W-1) に至るために必要な
    # 最小のマス数になっている。これ以外の全部の白ますは黒マスに変
    # えていいので、それが最大スコア。
    return white_num - R[H-1][W-1]


if __name__ == "__main__":
    H = 0
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = grid_repainting(H, W, S)
    print(ans)
