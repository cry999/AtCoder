def pushpush(N: int, A: list)->list:
    b = []
    for i, a in enumerate(reversed(A)):
        if i % 2 == 0:
            b.append(a)
    for i, a in enumerate(A):
        if i % 2 == N % 2:
            b.append(a)
    return b


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = pushpush(N, A)
    print(' '.join(map(str, ans)))
