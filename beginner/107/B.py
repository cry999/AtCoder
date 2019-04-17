def grid_compression(H: int, W: int, A: list)->list:
    # 黒を含む行・列の番号を取得する。
    cols = []
    rows = []
    # まずは行番号
    for h in range(H):
        all_white = True
        for w in range(W):
            if A[h][w] == '#':
                all_white = False
                break
        if not all_white:
            rows.append(h)

    # 次に列番号
    for w in range(W):
        all_white = True
        for h in range(H):
            if A[h][w] == '#':
                all_white = False
                break
        if not all_white:
            cols.append(w)

    # rows/cols で示される行列の値を順番に突っ込んでく
    compressed = []
    for r in rows:
        compressed.append([])
        for c in cols:
            compressed[-1].append(A[r][c])

    return compressed


if __name__ == "__main__":
    H = 0
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    ans = grid_compression(H, W, A)
    for row in ans:
        print(''.join(row))
