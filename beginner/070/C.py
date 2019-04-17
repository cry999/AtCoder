def gcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    return a if b == 0 else gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def multiple_clocks(N: int, T: list) -> int:
    ans = 1
    for t in T:
        ans = lcm(ans, t)
    return ans


if __name__ == "__main__":
    N = int(input())
    T = [int(input()) for _ in range(N)]
    ans = multiple_clocks(N, T)
    print(ans)
