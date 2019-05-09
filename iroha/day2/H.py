def maiden_of_nemuro(N: int, B: list) -> list:
    # B は A と A を比較したときの KMP のテーブルになっている。
    # それを確認する。

    A = [0] * N

    cnt = 1
    for i, b in enumerate(B):
        if b == 0:
            # b == 0 の時は新しい文字を置いて損しない
            A[i] = cnt
            cnt += 1
        else:
            # b > 0 の時は
            A[i] = A[b-1]

    # kmp
    table = [0] * (N+1)
    i, j = 0, -1

    table[0] = j
    while i < N:
        while 0 <= j and A[i] != A[j]:
            j = table[j]

        i, j = i + 1, j + 1
        table[i] = j

    if table[1:] != B:
        return []

    return A


if __name__ == "__main__":
    N = int(input())
    B = [int(s) for s in input().split()]

    ans = maiden_of_nemuro(N, B)
    if ans:
        print('Yes')
        print(' '.join(map(str, ans)))
    else:
        print('No')
