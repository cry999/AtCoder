def biscuit_generator(A: int, B: int, T: int)->int:
    return (T//A) * B


if __name__ == "__main__":
    A, B, T = map(int, input().split())
    ans = biscuit_generator(A, B, T)
    print(ans)
