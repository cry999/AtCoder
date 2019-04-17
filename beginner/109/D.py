def make_them_even(H: int, W: int, A: list)->list:
    odds = []
    for h in range(H):
        for w in range(W):
            if h % 2 == 0 and A[h][w] % 2 == 1:
                odds.append((h+1, w+1))
            elif h % 2 == 1 and A[h][W-w-1] % 2 == 1:
                odds.append((h+1, W-w))

    res = []
    for i in range(len(odds) // 2):
        (h1, w1), (h2, w2) = odds[2*i], odds[2*i+1]

        while h1 != h2 or w1 != w2:
            # 目的地に着くまで繰り返す

            # 横方向の目的地をきめる
            if h1 == h2:
                # 縦方向が目標位置なら w2 まで移動する
                target_w = w2
            elif h1 % 2 == 1:
                # 縦方向が目標位置でなく、奇数列なら右端に向かう
                target_w = W
            else:
                # 縦方向が目標位置でなく、偶数列なら左端に向かう
                target_w = 1

            # 横方向の移動を実際に行う。
            step = 1 if w1 < target_w else -1
            while w1 != target_w:
                res.append((h1, w1, h1, w1+step))
                w1 = w1 + step

            # 縦方向の目標位置でないなら、縦方向に一度うごく
            if h1 != h2:
                res.append((h1, w1, h1+1, w1))
                h1 += 1

    return res


if __name__ == "__main__":
    H = 0
    H, W = map(int, input().split())
    A = [[int(s) for s in input().split()] for _ in range(H)]
    ans = make_them_even(H, W, A)
    print(len(ans))
    for a in ans:
        print(' '.join(map(str, a)))
