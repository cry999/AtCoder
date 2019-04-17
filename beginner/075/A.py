def one_out_of_three(A: int, B: int, C: int)->int:
    if A == B:
        return C
    if A == C:
        return B
    return A


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    ans = one_out_of_three(A, B, C)
    print(ans)
