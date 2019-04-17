def maximum_sum(A: int, B: int, C: int, K: int) -> int:
    A, B, C = sorted([A, B, C])
    return A + B + C * (2 ** K)


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    K = int(input())
    ans = maximum_sum(A, B, C, K)
    print(ans)
