def wide_flip(S: str) -> int:
    min_k = float('inf')
    N = len(S)
    for i in range(N-1):
        if S[i] != S[i + 1]:
            min_k = min(min_k, max(i + 1, N - (i + 1)))
    return min_k


if __name__ == "__main__":
    S = input()
    ans = wide_flip(S)
    print(ans)
