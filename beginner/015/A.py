def training(A: str, B: str)->int:
    if len(A) > len(B):
        return A
    return B


if __name__ == "__main__":
    A = input()
    B = input()

    ans = training(A, B)
    print(ans)
