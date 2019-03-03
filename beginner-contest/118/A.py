if __name__ == "__main__":
    A, B = [int(s) for s in input().split()]

    if B % A == 0:
        print(A + B)
    else:
        print(B - A)
