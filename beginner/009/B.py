def bisect_left(A: list, x: int)->int:
    l, r = -1, len(A)
    while r - l > 1:
        m = (r + l)//2
        if A[m] < x:
            l = m
        else:
            r = m
    return r


def family_restaurant(N: int, A: list)->int:
    A.sort()
    l = bisect_left(A, max(A))
    return A[l-1]


if __name__ == "__main__":
    N = int(input())
    A = [int(input()) for _ in range(N)]
    ans = family_restaurant(N, A)
    print(ans)
