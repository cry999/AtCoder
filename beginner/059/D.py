def alice_and_brown(X: int, Y: int)->str:
    return 'Alice' if abs(X-Y) > 1 else 'Brown'


if __name__ == "__main__":
    X, Y = map(int, input().split())
    ans = alice_and_brown(X, Y)
    print(ans)
