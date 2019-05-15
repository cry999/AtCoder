def gcd(a: int, b: int)->int:
    if a < b:
        a, b = b, a
    return a if b == 0 else gcd(a % b, b)


def lcm(a: int, b: int)->int:
    return (a * b) // gcd(a, b)


def decrescend()->list:
    N = 1000
    a = 1
    for b in range(2, N+1):
        a = lcm(a, b)

    return [a-i-1 for i in range(N)]


if __name__ == "__main__":
    for ans in decrescend():
        print(ans)
