def mod_pow(a: int, n: int, mod: int)->int:
    '''a の n 乗を計算します。
    '''
    res = 1
    while n > 0:
        if n & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        n >>= 1
    return res


def xor_partitioning(N: int, A: list)->int:
    MOD = 10**9 + 7

    # dp[i][0] = i マス目まで処理した時に現在こまが置かれているますに 0 が書かれている
    # dp[i][1] = i マス目まで処理した時に現在こまが置かれているマスに X が書かれている。
    dp = [[0, 1] for _ in range(1 << 20)]
    memo = [0] * (1 << 20)

    b = 0
    num_zero = 0

    for a in A:
        b ^= a

        if b == 0:
            num_zero += 1
        else:
            dp[b][1] += dp[b][0] * (num_zero-memo[b])
            dp[b][1] %= MOD

            dp[b][0] += dp[b][1]
            dp[b][0] %= MOD

            memo[b] = num_zero

    if b > 0:
        return dp[b][1]

    return (sum(_dp[0] for _dp in dp) + mod_pow(2, num_zero-1, MOD)) % MOD


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]

    ans = xor_partitioning(N, A)
    print(ans)
