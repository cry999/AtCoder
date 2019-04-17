def stone_monument(a: int, b: int) -> int:
    n = b - a
    return n * (n + 1) // 2 - b


if __name__ == "__main__":
    a, b = map(int, input().split())
    ans = stone_monument(a, b)
    print(ans)
