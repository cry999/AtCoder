def snuke_coloring(H: int, W: int, N: int, queries: list) -> list:
    freq = {}
    for h, w in queries:
        # (h, w) を含む 9 この 3x3 行列に含まれる点の数を
        # 増やす。
        h, w = h-1, w-1
        for dh in range(-1, 1 + 1):
            for dw in range(-1, 1 + 1):
                if h + dh < 1 or H - 1 <= h + dh:
                    continue
                if w + dw < 1 or W - 1 <= w + dw:
                    continue

                freq.setdefault((h + dh, w + dw), 0)
                freq[(h + dh, w + dw)] += 1

    ret = [0] * 10
    # 点が 0 の 3x3 行列は freq に含まれないので、
    # (全ての 3x3 行列) - (点をもつ 3x3 行列) で求める。
    ret[0] = (H-2)*(W-2)
    for v in freq.values():
        ret[0] -= 1
        ret[v] += 1

    return ret


if __name__ == "__main__":
    N = 0
    H, W, N = map(int, input().split())
    queries = [tuple(int(s) for s in input().split()) for _ in range(N)]
    ans = snuke_coloring(H, W, N, queries)
    for a in ans:
        print(a)
