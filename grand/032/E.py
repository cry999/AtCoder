def modulo_pairing(N: int, M: int, A: list)->int:
    A.sort()

    def check(n: int)->bool:
        '''2*n の位置を区切りとして、右側が全て赤のペアになることを確認する。
        '''
        for i in range(2*n, N+n):
            if A[i] + A[2*N+2*n-i-1] < M:
                return False
        return True

    l, r = -1, N+1
    while r - l > 1:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m

    blue = [A[i]+A[2*r-i-1] for i in range(r)]
    red = [A[i]+A[2*N+2*r-i-1]-M for i in range(2*r, N+r)]

    return max(blue + red)


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = [int(s) for s in input().split()]

    ans = modulo_pairing(N, M, A)
    print(ans)
