def cut_and_count(N: int, S: str) -> int:
    l, r = {}, {}
    for c in S:
        if c not in r:
            r[c] = 1
        else:
            r[c] += 1

    max_len = 0
    for c in S:
        if c not in l:
            l[c] = 1
        else:
            l[c] += 1
        r[c] -= 1

        ls = set(k for k, v in l.items() if v > 0)
        rs = set(k for k, v in r.items() if v > 0)

        temp = len(ls & rs)
        max_len = max(max_len, temp)

    return max_len


if __name__ == "__main__":
    N = int(input())
    S = input()
    ans = cut_and_count(N, S)
    print(ans)
