def good_grid(N: int, C: int, D: list, c: list) -> int:
    # (i+j) % 3 ごとに色の出現頻度を取る
    freqs = [{}, {}, {}]
    for i, row in enumerate(c):
        for j, e in enumerate(row):
            r = (i + j) % 3
            freq = freqs[r]
            if e not in freq:
                freq[e] = 0
            freq[e] += 1

    # (i+j) % 3 ごとの色の出現頻度から他の色に変更した際の
    # 違和感を全探索
    discomforts = [[(-1, float('inf'))] * 3 for _ in range(3)]

    for freq, discomfort in zip(freqs, discomforts):
        for y in range(C):
            sum_d = sum(D[x - 1][y - 1] * f for x, f in freq.items())
            discomfort.append((y, sum_d))

    # (i+j) % 3 ごとに y の値を被らないように決定して
    # 全体の不快感を最小にする。
    min_dis = float('inf')
    for y1, v1 in discomforts[0]:
        for y2, v2 in discomforts[1]:
            for y3, v3 in discomforts[2]:
                if y1 == y2 or y2 == y3 or y3 == y1:
                    continue
                if v1 + v2 + v3 < min_dis:
                    min_dis = v1 + v2 + v3

    return min_dis


if __name__ == "__main__":
    N = 0
    C = 0
    N, C = map(int, input().split())
    D = [[int(s) for s in input().split()] for _ in range(C)]
    c = [[int(s) for s in input().split()] for _ in range(N)]
    ans = good_grid(N, C, D, c)
    print(ans)
