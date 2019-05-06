def head_of_the_dragon(N: int, K: int)->list:
    if 30 < K:
        # 作れる数列は最長でも 2 が 30 個並んだ数列
        # したがって、K が 30 より大きいものは無理。
        return [-1]

    res = [1] * K
    p = 2
    # 素因数を小さい順に突っ込んでいく
    while N > 1 and K > 1 and p * p <= N:
        if N % p == 0:
            res[-K] = p
            N //= p
            K -= 1
        else:
            p += 1
    if K > 1 or N == 1:
        # 素因数の数が足りない。
        return [-1]

    # 余ったものは最後の要素
    res[-1] = N

    return res


if __name__ == "__main__":
    N, K = map(int, input().split())

    ans = head_of_the_dragon(N, K)
    print(' '.join(map(str, ans)))
