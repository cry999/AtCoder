def various_sushi(N: int, K: int, TD: list) -> int:
    _TD = sorted(TD, key=lambda x: x[1], reverse=True)

    kind = set()
    res = 0
    q = []
    for t, d in _TD[:K]:
        if t not in kind:
            kind.add(t)
        else:
            q.append(d)
        res += d

    max_d = res + len(kind) ** 2
    temp = max_d
    count = len(q)
    for t, d in _TD[K:]:
        if count == 0:
            break
        if t not in kind:
            temp += -q.pop() + d + len(kind) * 2 + 1
            kind.add(t)
            max_d = max(max_d, temp)
            count -= 1

    return max_d


if __name__ == "__main__":
    N, K = [int(s) for s in input().split()]
    TD = [tuple(int(s) for s in input().split()) for _ in range(N)]

    ans = various_sushi(N, K, TD)
    print(ans)
