def discount_fare(X: int, Y: int) -> int:
    return X + (Y//2)


if __name__ == "__main__":
    X, Y = map(int, input().split())
    ans = discount_fare(X, Y)
    print(ans)
