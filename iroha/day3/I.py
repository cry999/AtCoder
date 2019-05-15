def prime_or_not()->tuple:
    return 9 * (10**15), 9 * (10**15) + 2018


if __name__ == "__main__":
    A, B = prime_or_not()
    print(A, B)
