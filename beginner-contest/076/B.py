def addition_and_multiplication(N: int, K: int)->int:
    min_d = float('inf')
    for i in range(1 << N):
        d = 1
        # i のビットが立っているところでは 2 倍にする。
        # それ以外では K をたす。
        for _ in range(N):
            if i & 1:
                d = d * 2
            else:
                d = d + K
            i >>= 1
        min_d = min(d, min_d)
    return min_d


if __name__ == "__main__":
    N = int(input())
    K = int(input())
    ans = addition_and_multiplication(N, K)
    print(ans)
