def big_jump(N: int, D: int, X: int, Y: int)->float:
    if X % D > 0 or Y % D > 0:
        # X, Y 共に D の倍数の位置にしか移動できないので
        # そうでない場合はたどり着けない。
        return 0.0

    # 座標圧縮。D の倍数の位置にしか移動できないので
    # その係数だけ見てれば良い。
        # 上下左右対称なので (X, Y) は第一象限にあるものとして良い
    X, Y = abs(X//D), abs(Y//D)

    if N % 2 != (X+Y) % 2:
        # 例えば 1 回の移動では (1, 0), (0, 1), (-1, 0), (0, -1)
        # にしか移動できないように、この二つの偶奇は一致しないといけない。
        # 一致しない場合はたどり着けない。
        return 0.0

    comb = [[0.0] * (N+1) for _ in range(N+1)]
    comb[0][0] = 1.0

    for n in range(1, N+1):
        comb[n][0] = comb[n-1][0] / 2.0
        for r in range(1, N+1):
            comb[n][r] = (comb[n-1][r]+comb[n-1][r-1])/2.0

    prob = 0.0
    for left_and_right in range(X, N+1):
        if (left_and_right + X) % 2 > 0:
            continue
        right = (left_and_right+X)//2
        # left = left_and_right - right

        up_and_down = N-left_and_right
        if (up_and_down+Y) % 2 > 0:
            continue
        up = (up_and_down+Y)//2
        # down = up_and_down - up

        prob += comb[N][left_and_right] * \
            comb[left_and_right][right] * \
            comb[up_and_down][up]

    return prob


if __name__ == "__main__":
    N, D = map(int, input().split())
    X, Y = map(int, input().split())
    ans = big_jump(N, D, X, Y)
    print(ans)
