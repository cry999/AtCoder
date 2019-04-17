def collatz(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def collatz_problem(s: int) -> int:
    if s == 1 or s == 2 or s == 4:
        return 1 + 3

    i = 1
    while True:
        i += 1
        s = collatz(s)
        if s == 4:
            return i + 3

    return - 1


if __name__ == "__main__":
    s = int(input())
    ans = collatz_problem(s)
    print(ans)
