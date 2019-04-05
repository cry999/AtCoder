def go_home(X: int) -> int:
    t = 1
    while t * (t + 1) // 2 < X:
        t += 1
    return t


if __name__ == "__main__":
    X = int(input())
    ans = go_home(X)
    print(ans)
