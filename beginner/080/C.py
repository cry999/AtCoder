def bit_index(n: int) -> list:
    '''n の立っているビットのインデックスを返します。
    '''
    res = []
    idx = 0
    while n > 0:
        if n & 1:
            res.append(idx)
        n >>= 1
        idx += 1
    return res


def shopping_street(N: int, F: list, P: list) -> int:
    max_profits = -float('inf')
    # 10 ビットのフラグの t 番目が立っている時、
    # t // 2 曜日の時間帯 t % 2 に出店するとする。
    # 少なくとも 1 回は出店しないといけないので、0
    # は除く。
    for i in range(1, 1 << 10):
        open_times = bit_index(i)
        profits = 0
        # 各店舗と出店日がかぶる回数を数える。
        for n in range(N):
            shop_count = sum(F[n][t] for t in open_times)
            profits += P[n][shop_count]
        max_profits = max(max_profits, profits)
    return max_profits


if __name__ == "__main__":
    N = int(input())
    F = [[int(s) for s in input().split()] for _ in range(N)]
    P = [[int(s) for s in input().split()] for _ in range(N)]
    ans = shopping_street(N, F, P)
    print(ans)
