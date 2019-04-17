def garden(A: int, B: int) -> int:
    return (A - 1) * (B - 1)


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = garden(A, B)
    print(ans)
