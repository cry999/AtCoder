def isu(X: int, Y: int, Z: int) -> int:
    return (X-Z) // (Y+Z)


if __name__ == "__main__":
    X, Y, Z = map(int, input().split())
    ans = isu(X, Y, Z)
    print(ans)
