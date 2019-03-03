def streamline(N: int, M: int, X: list) -> int:
    # 隣の点との距離を大きい順に N-1 こ選ぶ.
    # 選んだ部分で N 区間に分割する。
    # 各部分の和が解答
    # => つまり、総距離から N-1 個の最大距離を引けば良い
    _X = sorted(X)
    dist = [_X[i+1] - _X[i] for i in range(M-1)]
    max_dist = sorted(dist, reverse=True)[:N-1]
    return sum(dist) - sum(max_dist)


if __name__ == "__main__":
    N, M = [int(s) for s in input().split()]
    X = [int(s) for s in input().split()]

    ans = streamline(N, M, X)
    print(ans)
