def rot180(C: list)->int:
    N = 4
    for i in range(N//2):
        for j in range(N):
            # print('({}, {}) <-> ({}, {})'.format(i, j, N-1-i, N-1-j))
            C[i][j], C[N-1-i][N-1-j] = C[N-1-i][N-1-j], C[i][j]

    return C


if __name__ == "__main__":
    C = [[s for s in input().split()] for _ in range(4)]

    ans = rot180(C)
    print('\n'.join(map(' '.join, ans)))
