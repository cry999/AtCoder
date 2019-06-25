def rounding(X: int, A: int)->int:
    return 0 if X < A else 10


if __name__ == "__main__":
    X, A = map(int, input().split())

    ans = rounding(X, A)
    print(ans)
