def flipping_signs(N: int, A: list)->int:
    # 負の数が偶数この場合は全部正にできる。
    # 奇数個の場合は必ず一つ正にできないので絶対値の一番小さいもの
    # を残して他は全部正にする。
    min_abs = float('inf')
    s = 0
    neg_n = 0
    for a in A:
        s += abs(a)
        if a < 0:
            neg_n += 1
        min_abs = min(abs(a), min_abs)

    # print(neg_n, min_abs)
    if neg_n & 1:
        return s - 2*min_abs
    return s


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]

    ans = flipping_signs(N, A)
    print(ans)
