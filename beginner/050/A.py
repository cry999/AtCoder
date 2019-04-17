def addition_and_subtraction_easy(A: int, op: str, B: int)->int:
    return A+B if op == '+' else A-B


if __name__ == "__main__":
    A, op, B = input().split()
    ans = addition_and_subtraction_easy(int(A), op, int(B))
    print(ans)
