def sandglass2(X: int, t: int)->int:
    return max(0, X-t)


if __name__ == "__main__":
    X, t = map(int, input().split())
    ans = sandglass2(X, t)
    print(ans)
