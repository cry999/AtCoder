def snuke_festival(N: int, A: list, B: list, C: list) -> int:
    '''
    '''
    A.sort(), B.sort(), C.sort()
    sa, sb = [0] * (N + 1), [0] * (N + 1)

    a_idx = 0
    for i, b in enumerate(B):
        sa[i + 1] += sa[i]
        while a_idx < N and A[a_idx] < b:
            sa[i + 1] += 1
            a_idx += 1

    b_idx = 0
    for i, c in enumerate(C):
        sb[i + 1] += sb[i]
        while b_idx < N and B[b_idx] < c:
            sb[i + 1] += sa[b_idx+1]
            b_idx += 1

    return sum(sb)


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    B = [int(s) for s in input().split()]
    C = [int(s) for s in input().split()]
    ans = snuke_festival(N, A, B, C)
    print(ans)
