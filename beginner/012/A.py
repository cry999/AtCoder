def swap(A: int, B: int)->tuple:
    return B, A


if __name__ == "__main__":
    A, B = map(int, input().split())
    A, B = swap(A, B)
    print(A, B)
