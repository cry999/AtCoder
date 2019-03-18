def colorful_subsequence(N: int, S: str)->int:
    MOD = (10 ** 9) + 7
    cum = {}
    for c in S:
        cum.setdefault(c, 0)
        cum[c] += 1

    values = list(cum.values())
    count = 0
    for i, v in enumerate(values):
        temp = v
        for v in values[i+1:]:
            temp = (temp * (1 + v)) % MOD
        count = (count + temp) % MOD

    return count


if __name__ == "__main__":
    N = int(input())
    S = input()
    ans = colorful_subsequence(N, S)
    print(ans)
