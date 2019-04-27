def gcd(a: int, b: int)->int:
    if a < b:
        a, b = b, a
    return a if b == 0 else gcd(b, a % b)


def gcd_on_blackboard(N: int, A: list)->int:
    L, R = [0] * N, [0] * N

    L[0] = A[0]
    for i, a in enumerate(A[1:]):
        L[i+1] = gcd(L[i], a)

    R[-1] = A[-1]
    for i, a in enumerate(reversed(A[:-1])):
        R[N-i-2] = gcd(R[N-i-1], a)

    max_diff = max(R[1], L[-2])
    for i in range(1, N-1):
        max_diff = max(gcd(L[i-1], R[i+1]), max_diff)

    return max_diff


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]

    ans = gcd_on_blackboard(N, A)
    print(ans)
