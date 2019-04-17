# 縦線の数に対する横線の引き方
border_num = [1, 1, 2, 3, 5, 8, 13, 21, 34]


def noborder_both_side(cw: int, W: int) -> int:
    """縦線 cw の両隣に横線が存在しない場合の数
    """
    # (cw より左側の縦線間での横線の引き方) x (右側でのそれ)
    return border_num[cw-1] * border_num[W-cw]


def border_only_leftside(cw: int, W: int) -> int:
    """縦線 cw の左側のみに横線が存在する場合の数
    """
    # 左端にいるなら左側に横線は引けない
    if cw == 1:
        return 0

    # (cw より左側の縦線間での横線の引き方) x (右側でのそれ)
    # cw より左側は、cw と隣、隣とその隣の間の引き方は一意に決まるので、
    # それよりさらに左側の cw-2 本の縦線間での引き方を考える。
    return border_num[cw-2] * border_num[W-cw]


def border_only_rightside(cw: int, W: int) -> int:
    """縦線 cw の右側のみに縦線が存在する場合の数
    """
    # 右端にいるなら右側に横線は引けない
    if cw == W:
        return 0

    # (cw より左側の縦線間での横線の引き方) x (右側でのそれ)
    # cw より右側は、cw と隣、隣とその隣の間の引き方は一意に決まるので、
    # それよりさらに右側の W-cw-1 本の縦線間での引き方を考える。
    return border_num[cw-1] * border_num[W-cw-1]


def number_of_amidakuji(H: int, W: int, K: int) -> int:
    # 場合分けを減らすため、w 方向は余計にとってある。
    # dp[h][w] は (0, 1) から (h, w) へ至る道の数
    dp = [[0 for _ in range(W+2)] for _ in range(H+1)]
    dp[0][1] = 1

    for h in range(H):
        for w in range(1, W+1):
            # (h, w) -> (h+1, w) への行き方は次のように求める
            # ((h, w) への到達方法)
            # x (h+1 の横線の引き方の内 w の両隣に横線がない場合の数)
            dp[h+1][w] += dp[h][w] * noborder_both_side(w, W)

            # (h, w) -> (h+1, w-1) への行き方は次のように求める
            # ((h, w) への到達方法)
            # x (h+1 の横線の引き方の内 w の左にのみ横線がある場合の数)
            dp[h+1][w-1] += dp[h][w] * border_only_leftside(w, W)

            # (h, w) -> (h+1, w+1) への行き方は次のように求める
            # ((h, w) への到達方法)
            # x (h+1 の横線の引き方の内 w の右にのみ横線がある場合の数)
            dp[h+1][w+1] += dp[h][w] * border_only_rightside(w, W)

    return dp[H][K]


if __name__ == "__main__":
    H, W, K = map(int, input().split())
    ans = number_of_amidakuji(H, W, K)
    print(ans % 1000000007)
