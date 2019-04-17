def expired(X: int, A: int, B: int)->str:
    if (B-A) <= 0:
        return 'delicious'
    if (B-A) <= X:
        return 'safe'
    return 'dangerous'


if __name__ == "__main__":
    X, A, B = map(int, input().split())
    ans = expired(X, A, B)
    print(ans)
