def good_integer(N: int) -> bool:
    d1 = (N//1) % 10
    d10 = (N//10) % 10
    d100 = (N//100) % 10
    d1000 = (N//1000) % 10

    return d10 == d100 and (d1 == d10 or d100 == d1000)


if __name__ == "__main__":
    N = int(input())
    yes = good_integer(N)
    print('Yes' if yes else 'No')
