def regular_triangle(A: int, B: int, C: int)->bool:
    return A == B and B == C


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    yes = regular_triangle(A, B, C)
    print('Yes' if yes else 'No')
