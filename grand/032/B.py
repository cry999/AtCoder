def balanced_neighbors(N: int) -> list:
    # N が偶数の時、i は N+1-i 以外の頂点と結べば
    # 隣接点の和は (N+1)(N-2)/2 となり、i に依存しない
    # ため全て同じになる。
    # N が奇数の時、N を抜いた N-1 個の頂点に対して偶数
    # の場合の処理をする。このとき、N 以外の頂点はその隣
    # 接点の和は N(N-3)/2 となっている。この状態で N と
    # その他全ての頂点とを結べば、N 以外の頂点の隣接点の
    # 和は
    # N(N-3)/2 + N = N(N-1)/2
    # であり、N のそれは 1 ~ N-1 の和なので
    # N(N-1)/2
    # となり等しくなる。
    if N < 3:  # 2 以下の頂点数では無理
        return []
    if N & 1:  # 奇数
        return balanced_neighbors(N-1) + [(i, N) for i in range(1, N)]

    # 偶数
    return [(i+1, j+1) for i in range(N) for j in range(i+1,N) if i+j != N-1]


if __name__ == "__main__":
    N = int(input())

    ans = balanced_neighbors(N)
    print(len(ans))
    for x, y in ans:
        print(x, y)
