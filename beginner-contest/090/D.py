def remainder_reminder(N: int, K: int) -> int:
    if K == 0:
        return N * N

    count = 0
    for b in range(K + 1, N + 1):
        p, r = N // b, N % b
        count += p * max(0, b - K) + max(0, r - K + 1)
    return count


if __name__ == "__main__":
    N, K = map(int, input().split())
    ans = remainder_reminder(N, K)
    print(ans)
