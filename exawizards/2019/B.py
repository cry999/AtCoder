def red_or_blue(N: int, s: str)->bool:
    r = sum(c == 'R' for c in s)
    return r > N-r


if __name__ == "__main__":
    N = int(input())
    s = input()

    yes = red_or_blue(N, s)
    print('Yes' if yes else 'No')
