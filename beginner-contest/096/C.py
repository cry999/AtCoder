def grid_repeating2(H: int, W: int, S: list) -> bool:
    """マスに塗っていい回数の上限がないので、上下左右に黒ます
    がひとつでもあれば OK。つまり、孤立点の有無で判断すればよ
    い。
    """
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                # 白塗り部分は無視
                continue
            # 上下左右のどれかが黒(#)なら OK
            if w > 0 and S[h][w-1] == '#':
                continue
            if w+1 < W and S[h][w+1] == '#':
                continue
            if h > 0 and S[h-1][w] == '#':
                continue
            if h+1 < H and S[h+1][w] == '#':
                continue

            # 上の条件分岐にすべて失敗したなら孤立点
            return False
    return True


if __name__ == "__main__":
    H = 0
    W = 0
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    yes = grid_repeating2(H, W, S)
    print('Yes' if yes else 'No')
