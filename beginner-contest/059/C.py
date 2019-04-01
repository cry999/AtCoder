def sequence(N: int, A: list) -> int:
    op1, op2 = 0, 0
    s1, s2 = 0, 0

    for i, a in enumerate(A):
        s1, s2 = s1 + a, s2 + a

        if i % 2 > 0:  # odd
            if s1 <= 0:
                op1 += abs(s1) + 1
                s1 += abs(s1) + 1
            if s2 >= 0:
                op2 += abs(s2) + 1
                s2 -= abs(s2) + 1
        else:  # even
            if s1 >= 0:
                op1 += abs(s1) + 1
                s1 -= abs(s1) + 1
            if s2 <= 0:
                op2 += abs(s2) + 1
                s2 += abs(s2) + 1

    return min(op1, op2)


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = sequence(N, A)
    print(ans)
