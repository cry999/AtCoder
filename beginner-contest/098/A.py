def add_sub_mul(A: int, B: int) -> int:
    return max(A+B, A-B, A*B)


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = add_sub_mul(A, B)
    print(ans)
