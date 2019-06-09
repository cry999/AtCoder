def two_piles(A: int, B: int)->bool:
    return A % 2 == 0 or B % 2 == 0


if __name__ == "__main__":
    A, B = map(int, input().split())

    yes = two_piles(A, B)
    print('Yes' if yes else 'No')
