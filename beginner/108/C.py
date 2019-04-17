def fact(n: int)->int:
    if n == 1:
        return 1
    return n * fact(n-1)


def triangular_relationship(N: int, K: int)->int:
    res = 0
    if K % 2 == 1:
        odd, even = 0, 0
        for k in range(K, N+1, K):
            if k % 2 == 0:
                even += 1
            else:
                odd += 1

        res = sum(d*d*d for d in [odd, even])

        res += odd*odd*even
        res += odd*even*odd
        res += even*odd*odd

        res += even*even*odd
        res += even*odd*even
        res += odd*even*even
    else:
        leftK, leftK2 = 0, 0
        for k in range(K//2, N+1, K//2):
            if k % K == 0:
                leftK += 1
            else:
                leftK2 += 1

        res = sum(d*d*d for d in [leftK, leftK2])

    return res


if __name__ == "__main__":
    N, K = map(int, input().split())
    ans = triangular_relationship(N, K)
    print(ans)
