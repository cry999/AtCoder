def gen_random(N: int, K: int) -> float:
    res = 0
    # 3 つとも違う数字、(1~(K-1) から一つ)、K、((K+1)~N から一つ)
    # 以下、
    # A = (1~(K-1) から一つ)
    # B = K
    # C = ((K+1)~N から一つ)
    # とする。
    res += (K - 1) * 1 * (N - K) * 6
    # B, B, C
    res += 1 * 1 * (N - K) * 3
    # A, B, B
    res += (K - 1) * 1 * 1 * 3
    # B, B, B
    res += 1 * 1 * 1

    return res / (N * N * N)


if __name__ == "__main__":
    N, K = map(int, input().split())
    ans = gen_random(N, K)
    print(ans)
