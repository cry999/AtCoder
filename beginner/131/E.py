def friendships(N: int, K: int)->list:
    MAX = (N-1)*(N-2)//2
    if K > MAX:
        return []

    res = []
    for v in range(2, N+1):
        res.append((1, v))

    u = 2
    v = 3
    for _ in range(K, MAX):
        res.append((u, v))
        if v == N:
            u += 1
            v = u + 1
        else:
            v += 1

    return res


if __name__ == "__main__":
    N, K = map(int, input().split())

    ans = friendships(N, K)
    if ans:
        print(len(ans))
        for u, v in ans:
            print(u, v)
    else:
        print(-1)
