def is_acgt(s: str)->int:
    AGCT = 'AGCT'
    for c in s:
        if c not in AGCT:
            return False
    return True


def atcoder(S: str)->int:
    n = len(S)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            if is_acgt(S[i:j+1]):
                max_len = max(max_len, j - i + 1)
    return max_len


if __name__ == "__main__":
    S = input()
    ans = atcoder(S)
    print(ans)
