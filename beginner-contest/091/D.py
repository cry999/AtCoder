import bisect


def lower_bound(A: list, v: int) -> int:
    l, r = -1, len(A)
    while r - l > 1:
        m = (r + l) // 2
        if A[m] < v:
            l = m
        else:
            r = m
    return r


def count(A: list, a: int, b: int) -> int:
    l = lower_bound(A, a)
    u = lower_bound(A, b)
    return u - l


def two_sequences(N: int, A: list, B: list) -> int:
    BIT_LIM = 40

    res = 0
    for k in range(BIT_LIM):
        T = 1 << (k+1)
        sorted_B = sorted(b & (T-1) for b in B)
        num_kth_bit_is_1 = 0
        for ai in A:
            ai_mod = ai & (T-1)

            T = T >> 1
            num_kth_bit_is_1 += count(sorted_B, T - ai_mod, 2*T - ai_mod)
            num_kth_bit_is_1 += count(sorted_B, 3*T - ai_mod, 4*T - ai_mod)
            T = T << 1

        res = ((num_kth_bit_is_1 & 1) << k) | res

    return res


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    B = [int(s) for s in input().split()]
    ans = two_sequences(N, A, B)
    print(ans)
