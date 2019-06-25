def enough_array(N: int, K: int, A: list)->int:
    res = 0
    s = 0  # 累積和
    l, r = 0, 0  # 累積和の最左のインデックスと最右のインデックス

    while l < N:
        while r < N and s < K:
            s += A[r]
            r += 1
        if K <= s:
            res += N-r+1
        s -= A[l]
        l += 1

    return res


if __name__ == "__main__":
    N, K = map(int, input().split())
    A = [int(s) for s in input().split()]

    ans = enough_array(N, K, A)
    print(ans)
