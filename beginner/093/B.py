def small_and_large_integers(A: int, B: int, K: int) -> list:
    l, r = [], []
    for k in range(K):
        if A + k == B - k:
            l = l + [A+k]
            break
        if B - k < A + k:
            break

        l = l + [A+k]

        r = [B-k] + r
    return l + r


if __name__ == "__main__":
    A, B, K = map(int, input().split())
    ans = small_and_large_integers(A, B, K)
    for a in ans:
        print(a)
