from math import sqrt


def is_prime(n: int) -> bool:
    sq = int(sqrt(n))
    if sq * sq == n:
        return False

    for i in range(2, sq+1):
        if n % i == 0:
            return False
    return True


def primes(n: int) -> list:
    res = []

    if n < 2:
        return res
    res.append(2)

    if n < 3:
        return res
    res.append(3)

    for i in range(6, n+1, 6):
        if is_prime(i-1):
            res.append(i-1)

        if i + 1 > n:
            break

        if is_prime(i+1):
            res.append(i+1)

    return res


def five_five_everywhere(N: int) -> list:
    res = []
    count = 0
    for p in primes(55555):
        if p % 5 != 1:
            continue

        res.append(p)
        count += 1
        if count == N:
            return res

    return None


if __name__ == "__main__":
    N = int(input())
    ans = five_five_everywhere(N)
    print(' '.join(map(str, ans)))
