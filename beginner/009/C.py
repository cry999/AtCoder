def dict_seq(N: int, K: int, S: str)->str:
    T = ''
    not_used = sorted(list(S))

    def score(idx: int, T: str)->int:
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        # S に残されている文字
        leftS = {c: 0 for c in ALPHABET}
        for c in S[idx+1:]:
            leftS[c] += 1

        # T に残されている文字
        leftT = {c: 0 for c in ALPHABET}
        for c in S:
            leftT[c] += 1
        for c in T:
            leftT[c] -= 1

        return len(S[idx+1:]) - sum(min(leftS[c], leftT[c]) for c in ALPHABET)

    mismatch = 0
    for i in range(N):
        for c in not_used:
            if S[i] != c:
                mismatch += 1
            if score(i, T+c) + mismatch <= K:
                T = T+c
                break
            if S[i] != c:
                mismatch -= 1
        not_used.remove(c)

    return T


if __name__ == "__main__":
    N, K = map(int, input().split())
    S = input()

    ans = dict_seq(N, K, S)
    print(ans)
