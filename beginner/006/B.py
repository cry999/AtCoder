def tribonacci(n: int)->int:
    MOD = 10007

    if n == 1:
        return 0
    if n == 2:
        return 0
    if n == 3:
        return 1

    a0, a1, a2 = 0, 0, 1

    while n > 3:
        tmp = a2 + a1 + a0
        a0 = a1
        a1 = a2
        a2 = tmp % MOD

        n -= 1

    return a2


if __name__ == "__main__":
    n = int(input())

    ans = tribonacci(n)
    print(ans)
