def f(x: int) -> int:
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


def harshad_number(N: int) -> bool:
    return N % f(N) == 0


if __name__ == "__main__":
    N = int(input())
    yes = harshad_number(N)
    print('Yes' if yes else 'No')
