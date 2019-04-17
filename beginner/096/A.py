def day_of_takahashi(a: int, b: int) -> int:
    return (a - 1) + (1 if a <= b else 0)


if __name__ == "__main__":
    a, b = map(int, input().split())
    ans = day_of_takahashi(a, b)
    print(ans)
