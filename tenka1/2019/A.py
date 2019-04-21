def on_the_way(A: int, B: int, C: int)->bool:
    if A > B:
        A, B = B, A
    return A < C and C < B


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    yes = on_the_way(A, B, C)
    print('Yes' if yes else 'No')
