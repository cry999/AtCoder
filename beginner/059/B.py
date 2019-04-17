def comparison(A: int, B: int) -> str:
    if A < B:
        return 'LESS'
    if B < A:
        return 'GREATER'
    return 'EQUAL'


if __name__ == "__main__":
    A, B = int(input()), int(input())
    ans = comparison(A, B)
    print(ans)
