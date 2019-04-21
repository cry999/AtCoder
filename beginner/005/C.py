def sell_takoyaki(T: int, N: int, A: list, M: int, B: list)->bool:
    if N < M:
        # たこ焼きが足りない
        return False

    ai, bi = 0, 0

    while ai < N and bi < M:
        a, b = A[ai], B[bi]

        if b <= a + T and a <= b:
            # できて T 秒以内なので売れる
            ai += 1
            bi += 1
        else:
            # できて T 秒より時間が立っているので売れない
            ai += 1

    # たこ焼きがなくなる前に客が捌けたか
    return bi == M


if __name__ == "__main__":
    T = int(input())
    N = int(input())
    A = [int(s) for s in input().split()]
    M = int(input())
    B = [int(s) for s in input().split()]

    yes = sell_takoyaki(T, N, A, M, B)
    print('yes' if yes else 'no')
