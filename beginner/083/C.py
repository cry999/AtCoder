def multiple_gift(X: int, Y: int) -> int:
    n = X
    count = 0
    while n <= Y:
        n <<= 1
        count += 1
    return count


if __name__ == "__main__":
    X, Y = map(int, input().split())
    ans = multiple_gift(X, Y)
    print(ans)
