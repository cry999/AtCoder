def _1d_reversi(S: str) -> int:
    n = len(S)
    return sum(S[i] != S[i-1] for i in range(1, n))


if __name__ == "__main__":
    S = input()
    ans = _1d_reversi(S)
    print(ans)
