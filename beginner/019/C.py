def binary_search(haystack: list, needle: int) -> int:
    l, r = -1, len(haystack)
    while r - l > 1:
        m = (l + r) // 2
        if haystack[m] < needle:
            l = m
        elif needle < haystack[m]:
            r = m
        else:
            return m
    # not found
    return -1


def magic(N: int, A: list) -> int:
    for i in range(N):
        a = A[i]
        while a % 2 == 0:
            a >>= 1
        A[i] = a
    # A.sort()

    return len(set(A))

if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = magic(N, A)
    print(ans)
