from math import sqrt, ceil


def digit_num(n: int)->int:
    ret = 0
    while n > 0:
        ret += 1
        n //= 10
    return ret


def F(A: int, B: int)->int:
    return digit_num(max(A, B))


def digits_in_multiplication(N: int)->int:
    sq = ceil(sqrt(N))

    for n in range(sq, 0, -1):
        if N % n == 0:
            return F(N//n, n)
    return F(N, 1)


if __name__ == "__main__":
    N = int(input())
    ans = digits_in_multiplication(N)
    print(ans)
