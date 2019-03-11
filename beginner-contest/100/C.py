def num2(n: int) -> int:
    """n を素因数分解した時の 2 の指数
    """
    s = 0
    while n % 2 == 0:
        s += 1
        n //= 2
    return s


def multiple3_or_divide2(N: int, A: list) -> int:
    return sum(num2(a) for a in A)


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = multiple3_or_divide2(N, A)
    print(ans)
