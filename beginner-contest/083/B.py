def in_range(x: int, lower: int, upper: int) -> bool:
    return lower <= x and x <= upper


def digit_sum(n: int) -> int:
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def some_sums(N: int, A: int, B: int) -> int:
    return sum(n+1 for n in range(N) if in_range(digit_sum(n+1), A, B))


if __name__ == "__main__":
    N, A, B = map(int, input().split())
    ans = some_sums(N, A, B)
    print(ans)
