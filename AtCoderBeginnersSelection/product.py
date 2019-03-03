def product(a: int, b: int) -> str:
    p = a * b
    return 'Even' if (p & 1) == 0 else 'Odd'


if __name__ == "__main__":
    a, b = [int(s) for s in input().split()]
    ans = product(a, b)
    print(ans)
