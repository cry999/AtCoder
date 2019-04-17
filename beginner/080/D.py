def recording(N: int, C: int, info: list) -> int:
    _, max_time, _ = max(info, key=lambda x: x[1])
    max_time = 2*max_time

    # 各チャンネルでのレコーダーの使用数を累積和として求める。
    # recorders が累積和であり、S-0.5 を配列で表すために
    # 2*(max_time) のサイズにしている。
    recorders = [[0] * C for _ in range(max_time + 1)]

    # スタート時間を +1 、終了時間を -1 とすることで、あとで
    # 累積和をとるときに、録画している時間帯が 1 、していない
    # 時間が 0 になるようにできる。
    for s, t, ch in info:
        recorders[2*s-1][ch-1] += 1
        recorders[2*t][ch-1] -= 1

    # 累積和をとる。
    for t in range(max_time):
        for ch in range(C):
            recorders[t+1][ch] += recorders[t][ch]

    # 各時間帯でのレコーダーの使用台数の最大値をとる。
    return max(
        sum(used > 0 for used in recorders[t])
        for t in range(max_time+1))


if __name__ == "__main__":
    N = 0
    N, C = map(int, input().split())
    info = [tuple(map(int, input().split())) for _ in range(N)]
    ans = recording(N, C, info)
    print(ans)
