
def p(i: int) -> int:
    """レベルiバーガーのパティの数
    p[i] = 2*p[i-1] + 1
    p[i] + 1 = 2*(p[i-1] + 1)
    p[i] + 1 = (2**i)*(p[0] + 1)
    p[i] + 1 = (2**i)*2
    p[i] = 2**(i+1) - 1
    """
    return 2**(i+1) - 1


def a(i: int) -> int:
    """レベルiバーガーの層の数(パティとパンの数)
    a[i] = 2*a[i-1] + 3
    a[i] + 3 = 2 * (a[i-1] + 3)
    a[i] + 3 = (2**i) * (a[0] + 3)
    a[i] + 3 = (2**i) * 4
    a[i] = (2**(i+2)) - 3
    """
    return 2**(i+2) - 3


def f(N: int, X: int) -> int:
    """レベルNバーガーの下からX層の中に含まれるパティの数
    :param N: バーガーのレベル
    :param X: パティの数を調べたい層の数
    :return: パティの数
    """
    if N == 0:
        return 1 if X > 0 else 0

    an = a(N)
    if X < an // 2 + 1:
        # レベルN-1バーガーに含まれる。
        return f(N-1, X-1)
    if X == an // 2 + 1:
        # 中央のパティ + レベルN-1バーガーに含まれる全てのパティ
        return 1 + p(N-1)
    # レベルN-1バーガの全てのパティ + 中央のパティ
    # + レベルN-1バーガの下から(X-(ai+2))そうに含まれるパティ
    return 1 + p(N-1) + f(N-1, X-(an // 2 + 1))


if __name__ == "__main__":
    N, X = map(int, input().split())
    ans = f(N, X)
    print(ans)
