def between_two_integers(A: int, B: int, C: int)->bool:
    return A <= C and C <= B


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    yes = between_two_integers(A, B, C)
    print('Yes' if yes else 'No')
