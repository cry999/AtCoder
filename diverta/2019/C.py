def ab_substrings(N: int, S: list)->int:
    res = 0
    endA = 0
    startB = 0
    both = 0

    for s in S:
        res += s.count('AB')
        if s.endswith('A'):
            if s.startswith('B'):
                both += 1
            else:
                endA += 1
        elif s.startswith('B'):
            startB += 1

    if both > 0:
        res += both - 1

        if endA > 0:
            res += 1
            endA -= 1

        if startB > 0:
            res += 1
            startB -= 1

    return res + min(endA, startB)


if __name__ == "__main__":
    N = int(input())
    S = [input() for _ in range(N)]

    ans = ab_substrings(N, S)
    print(ans)
