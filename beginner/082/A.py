def round_up_the_mean(a: int, b: int) -> int:
    return (a + b) // 2 if (a + b) % 2 == 0 else (a + b) // 2 + 1


if __name__ == "__main__":
    a, b = map(int, input().split())
    ans = round_up_the_mean(a, b)
    print(ans)
