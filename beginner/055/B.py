def training_camp(N: int) -> int:
    MOD = 10 ** 9 + 7
    ret = 1
    for n in range(N):
        ret = (ret * (n + 1)) % MOD
    return ret


if __name__ == "__main__":
    N = int(input())
    ans = training_camp(N)
    print(ans)
