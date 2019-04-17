def simple_knapsack(N: int, W: int, items: list) -> int:
    w0 = items[0][0]
    d = {w0+i: [] for i in range(4)}
    for w, v in items:
        d[w].append(v)

    s = {}
    for k, values in d.items():
        s[k] = [0] * (len(values)+1)
        for i, v in enumerate(sorted(values, key=lambda x: -x)):
            s[k][i + 1] = s[k][i] + v

    w0, w1, w2, w3 = w0, w0 + 1, w0 + 2, w0 + 3

    max_value = 0
    for i1 in range(len(s[w0])):
        if W < w0 * i1:
            break
        for i2 in range(len(s[w1])):
            if W < w0 * i1 + w1 * i2:
                break
            for i3 in range(len(s[w2])):
                if W < w0 * i1 + w1 * i2 + w2 * i3:
                    break
                for i4 in range(len(s[w3])):
                    if W < w0 * i1 + w1 * i2 + w2 * i3 + w3 * i4:
                        break
                    max_value = max(
                        max_value, s[w0][i1] + s[w1][i2] + s[w2][i3] + s[w3][i4])

    return max_value


if __name__ == "__main__":
    N = 0
    N, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]
    ans = simple_knapsack(N, W, items)
    print(ans)
