def plus_minus_problem(A: int, B: int, C: int) -> str:
    if A+B == C and A-B == C:
        return '?'
    if A+B == C:
        return '+'
    if A-B == C:
        return '-'
    return '!'


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    ans = plus_minus_problem(A, B, C)
    print(ans)
