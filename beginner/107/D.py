def median_of_medians(N: int, A: int)->int:
    def check(x):
        print('check({})'.format(x))
        offset = N
        S = 0
        r = 0
        y = 0
        D = [0] * (2 * N + 1)
        for i in range(N):
            print('A[{}] = {} ? {}'.format(i, A[i], x))
            D[S + offset] += 1
            if A[i] < x:
                r += D[S + offset]
                S += 1
            else:
                S -= 1
                r -= D[S + offset]
            print(D, r)
            print(('   ' * (S + offset)) + ' ^')
            y += r
        return y

    alpha = sorted(A)
    l, r = 0, N
    c = N * (N + 1) // 2
    while True:
        m = (l + r) // 2
        if check(alpha[m]) <= c // 2:
            if m == N - 1:
                break
            elif check(alpha[m + 1]) > c // 2:
                break
            l = m
        else:
            r = m + 1

    return alpha[m]


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    ans = median_of_medians(N, A)
    print(ans)
