def flip_flip_and_flip(N: int, M: int) -> int:
    if N == 1 and M == 1:
        return 1
    if N == 1:
        return M - 2
    if M == 1:
        return N - 2
    return (N-2)*(M-2)


if __name__ == "__main__":
    N, M = map(int, input().split())
    ans = flip_flip_and_flip(N, M)
    print(ans)
