def ringring(a: int, b: int, c: int)->int:
    return sum(sorted([a, b, c])[:2])


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    ans = ringring(a, b, c)
    print(ans)
