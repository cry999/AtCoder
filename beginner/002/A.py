def honest(X: int, Y: int) -> int:
    return X if X > Y else Y


if __name__ == "__main__":
    X, Y = map(int, input().split())

    ans = honest(X, Y)
    print(ans)
