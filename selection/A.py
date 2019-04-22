def welcome_to_atcoder(a: int, b: int, c: int, s: str) -> tuple:
    return a + b + c, s


if __name__ == "__main__":
    a = int(input())
    b, c = [int(s) for s in input().split()]
    s = input()

    n, s = welcome_to_atcoder(a, b, c, s)

    print(n, s)
