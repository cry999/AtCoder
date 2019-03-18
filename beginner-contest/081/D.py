def non_decreasing(N: int, A: list) -> list:
    res = []

    # まず、A の値を正か負に統一する。
    # なので、A に正と負の値が混在する場合のみ、min(A) と max(A)
    # の絶対値の大きい方を全体に足す。
    min_a, max_a = min(A), max(A)
    min_i, max_i = A.index(min_a), A.index(max_a)

    if min_a * max_a < 0:
        # 正と負の値が混在するのでどちらかに統一する。
        # ここの操作は N-1 回。
        if abs(min_a) < abs(max_a):
            # max_a を全体に加えて正の値のみにし、単調増加
            # するように修正する。
            res = [(max_i + 1, i + 1) for i in range(N) if i != max_i]
            min_a += max_a
        else:
            # min_a を全体に加えて負の値のみにし、絶対値が
            # 単調減少するように修正する。
            res = [(min_i + 1, i + 1) for i in range(N) if i != min_i]
            max_a += min_a

    # この操作が N-1 回。
    if max_a <= 0:
        # 全体が負の値なので、絶対値が単調減少するように N 番目の値から
        # 始めて i 番目の値を i-1 番目の値に足していく。
        res += [(i, i - 1) for i in range(N, 1, -1)]

    else:
        # 全体が正の値なので、単調増加するように 1 番目の値から始めて i
        # 番目の値を i+1 番目の値に足していく。
        res += [(i, i + 1) for i in range(1, N)]

    return res


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = non_decreasing(N, A)
    print(len(ans))
    for x, y in ans:
        print(x, y)
