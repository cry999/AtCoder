def two_coins(A: int, B: int, C: int) -> bool:
    return C <= A + B


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    yes = two_coins(A, B, C)
    print('Yes' if yes else 'No')
