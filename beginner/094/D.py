def binomial_coefficients(n: int, A: list) -> tuple:
    max_A = max(A)
    max_r, max_a = 0, 0
    for a in A:
        if a == max_A:
            continue
        r = min(a, max_A - a)
        if max_r < r:
            max_r = r
            max_a = a

    return max_A, max_a


if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    ai, aj = binomial_coefficients(n, A)
    print(ai, aj)
