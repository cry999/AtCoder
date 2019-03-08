from math import sqrt


def divisors(n: int) -> list:
    sq = int(sqrt(n))
    l, m, r = [], [], []
    if sq * sq == n:
        m = [sq]
    else:
        sq += 1

    for i in range(1, sq):
        if n % i == 0:
            l.append(i)
            r = [n // i] + r

    return l + m + r


def one_hundred_and_five(N: int) -> int:
    count = 0
    for n in range(105, N + 1, 2):
        if len(divisors(n)) == 8:
            count += 1
    return count


if __name__ == "__main__":
    N = int(input())
    ans = one_hundred_and_five(N)
    print(ans)
