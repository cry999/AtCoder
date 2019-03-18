def recording(N: int, C: int, info: list) -> int:
    recorders = []
    info.sort(key=lambda x: x[1])
    for s, t, c in info:
        recorded = False
        for i, (rt, rc) in enumerate(recorders):
            if c == rc and rt <= s:
                recorders[i] = (t, c)
                recorded = True
            elif c != rc and rt < s:
                recorders[i] = (t, c)
                recorded = True
        if not recorded:
            recorders.append((t, c))
    return len(recorders)


if __name__ == "__main__":
    N = 0
    N, C = map(int, input().split())
    info = [tuple(map(int, input().split())) for _ in range(N)]
    ans = recording(N, C, info)
    print(ans)
