def xor_sum_4(N: int, A: list)->int:
    MOD = 10**9 + 7
    MAX_POW = 60

    # bit_sum[i] := 2 進表記で i 桁目の値の和
    bit_sum = [sum((a >> i) & 1 for a in A) for i in range(MAX_POW)]

    ans = 0
    for a in A:
        N -= 1
        for i in range(MAX_POW):
            bit_sum[i] -= (a >> i) & 1
            if (a >> i) & 1 == 1:
                ans += ((1 << i) * (N-bit_sum[i])) % MOD
            else:
                ans += ((1 << i) * bit_sum[i]) % MOD
            ans %= MOD
    return ans


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    ans = xor_sum_4(N, A)
    print(ans)
