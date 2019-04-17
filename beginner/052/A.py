def two_rectangles(A: int, B: int, C: int, D: int)->int:
    return max(A*B, C*D)


if __name__ == "__main__":
    A, B, C, D = map(int, input().split())
    ans = two_rectangles(A, B, C, D)
    print(ans)
