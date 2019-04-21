def make_takoyaki(x: int, y: int)->int:
    return y // x


if __name__ == "__main__":
    x, y = map(int, input().split())

    ans = make_takoyaki(x, y)
    print(ans)
