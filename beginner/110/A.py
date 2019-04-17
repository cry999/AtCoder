def maximize_the_formula(A: int, B: int, C: int) -> int:
    x, y, z = sorted([A, B, C], reverse=True)
    return 10 * x + y + z


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    ans = maximize_the_formula(A, B, C)
    print(ans)
