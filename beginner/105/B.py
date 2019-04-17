def cakes_and_donuts(N: int) -> bool:
    while N > 0:
        if N % 4 == 0:
            return True
        N -= 7

    return N == 0  # <=> N % 7 == 0


if __name__ == "__main__":
    N = int(input())
    yes = cakes_and_donuts(N)
    print('Yes' if yes else 'No')
