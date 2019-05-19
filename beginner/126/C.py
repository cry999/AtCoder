def dice_and_coin(N: int, K: int)->int:
    ans = 0

    for n in range(1, N+1):
        if n < K:
            c = 0
            while n < K:
                n <<= 1
                c += 1

            ans += 1 / (1 << c)
        else:
            ans += 1

    return ans / N


if __name__ == "__main__":
    N, K = map(int, input().split())

    ans = dice_and_coin(N, K)
    print('{:.10f}'.format(ans))
