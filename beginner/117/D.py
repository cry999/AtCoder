def xxor(N: int, K: int, A: list) -> int:
    opt = 0
    num_digit_2 = 0  # binary 表示での桁数
    while 2 ** num_digit_2 < K:
        num_digit_2 += 1

    # 範囲関係なく最適解(opt)を計算する
    mask = 1
    for _ in range(num_digit_2):
        count_0, count_1 = 0, 0
        for a in A:
            if a & mask > 0:
                count_1 += 1
            else:
                count_0 += 1

        if count_0 > count_1:
            opt = opt | mask

        mask <<= 1

    # 上で求めた最適解を範囲内に落とし込む
    max_ret = 0
    x = opt
    # 以下、X = (X40 X39 ... X0)2, K+1 = (K40 K39 ... K0)2 として考える。
    for i in range(40):
        mask = 1 << (40 - i - 1)

        if x < K + 1:
            temp = sum(a ^ x for a in A)
            max_ret = max(temp, max_ret)

        x2 = (x & ~mask)  # Xi = 0 とする
        if x2 < K + 1:
            temp = sum(a ^ x2 for a in A)
            max_ret = max(temp, max_ret)

        x = ((K + 1) & ~(mask - 1)) | (opt & (mask - 1))

    return max_ret


if __name__ == "__main__":
    N, K = [int(s) for s in input().split()]
    A = [int(s) for s in input().split()]

    ans = xxor(N, K, A)
    print(ans)
