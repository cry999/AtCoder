def collector_king(R: int, C: int, K: int, N: int, candies: list) -> int:
    r2n, c2n = [0] * R, [0] * C

    for r, c in candies:
        r2n[r - 1] += 1
        c2n[c - 1] += 1

    # n2r[n] は飴の個数が n この行の個数
    n2r = {i: 0 for i in range(N+1)}
    for n in r2n:
        n2r[n] += 1

    # n2c[n] は飴の個数が n この列の個数
    n2c = {i: 0 for i in range(N+1)}
    for n in c2n:
        n2c[n] += 1

    total_K = 0
    for k in range(K+1):
        total_K += n2r[k] * n2c[K - k]

    for r, c in candies:
        s = r2n[r - 1] + c2n[c - 1]

        if s == K:
            # 余計にカウントしている。
            total_K -= 1
        if s == K + 1:
            # カウントし損ねている
            total_K += 1

    return total_K


if __name__ == "__main__":
    R, C, K = map(int, input().split())
    N = int(input())
    candies = [tuple(int(s) for s in input().split()) for _ in range(N)]

    ans = collector_king(R, C, K, N, candies)
    print(ans)
