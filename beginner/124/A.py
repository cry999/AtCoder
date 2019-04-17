def buttons(A: int, B: int)->int:
    s = 0
    for _ in range(2):
        if A > B:
            s += A
            A -= 1
        else:
            s += B
            B -= 1
    return s


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = buttons(A, B)
    print(ans)
