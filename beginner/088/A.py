def infinite_coins(N: int, A: int) -> bool:
    return N % 500 <= A


if __name__ == "__main__":
    N = int(input())
    A = int(input())
    yes = infinite_coins(N, A)
    print('Yes' if yes else 'No')
