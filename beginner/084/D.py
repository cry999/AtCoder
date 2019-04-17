from math import sqrt


def _2017_like_number(Q: int, queries: list) -> list:
    N = 10 ** 5
    prime_numbers, prime_count = [], 0

    def is_prime(n: int) -> bool:
        if n < 2:
            return False

        sq = int(sqrt(n)) + 1
        for p in prime_numbers:
            if sq < p:
                break
            if n % p == 0:
                return False

        return True

    def is_prime_use_list(n: int) -> bool:
        l, r = 0, prime_count
        while r - l > 1:
            m = (l + r) // 2

            if prime_numbers[m] <= n:
                l = m
            else:
                r = m

        return prime_numbers[l] == n

    S = [0] * (N + 1)
    for i in range(0, N):
        S[i + 1] = S[i]

        if is_prime(i + 1):
            prime_numbers.append(i + 1)
            prime_count += 1
        else:
            continue

        if is_prime_use_list((i+2)//2):
            S[i + 1] += 1

    return [S[r] - S[l - 1] for l, r in queries]


if __name__ == "__main__":
    Q = int(input())
    queries = [tuple(int(s) for s in input().split()) for _ in range(Q)]
    ans = _2017_like_number(Q, queries)
    for a in ans:
        print(a)
