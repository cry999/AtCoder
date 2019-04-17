def cats_and_dogs(A: int, B: int, X: int) -> bool:
    return A <= X and X <= A+B


if __name__ == "__main__":
    A, B, X = map(int, input().split())
    yes = cats_and_dogs(A, B, X)
    print('YES' if yes else 'NO')
