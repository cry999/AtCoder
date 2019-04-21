def mask_word(N: int, S: str, K: int)->str:
    return ''.join(c if c == S[K-1] else '*' for c in S)


if __name__ == "__main__":
    N = int(input())
    S = input()
    K = int(input())

    ans = mask_word(N, S, K)
    print(ans)
