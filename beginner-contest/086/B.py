from math import sqrt


def one_twoone(a: int, b: int)->bool:
    c = int(str(a) + str(b))
    sq = int(sqrt(c))
    return c == sq * sq


if __name__ == "__main__":
    a, b = map(int, input().split())
    yes = one_twoone(a, b)
    print('Yes' if yes else 'No')
