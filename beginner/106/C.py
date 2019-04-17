def to_infinity(S: str, K: int) -> str:
    """5000兆 = 5e15 であり、文字 n は 5e15 日後には n^(5e15) の長さになっている。
    これは 2^100 = 10^30 より、K の範囲には確実に収まらない。
    """
    if K == 1:
        return S[0]
    # K > 1
    if len(S) == 1:
        return S[0]
    # K > 1 and |S| > 1
    for k in range(K):
        if k >= len(S):
            return '1'
        if S[k] != '1':
            return S[k]
    return '1'


if __name__ == "__main__":
    S = input()
    K = int(input())
    ans = to_infinity(S, K)
    print(ans)
