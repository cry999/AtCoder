def identify(N: int, M: int, PY: list) -> list:
    _PY = [(i, p, y) for i, (p, y) in enumerate(PY)]
    _PY.sort(key=lambda x: x[2])
    _PY.sort(key=lambda x: x[1])

    now_p = 0
    now_o = 1
    ids = []
    for i, p, _ in _PY:
        if p != now_p:
            now_p = p
            now_o = 1
        ids.append((i, '{p:06}{o:06}'.format(p=p, o=now_o)))
        now_o += 1

    return [i for _, i in sorted(ids, key=lambda x: x[0])]


if __name__ == "__main__":
    N, M = map(int, input().split())
    PY = [tuple(int(s) for s in input().split()) for _ in range(M)]
    for ans in identify(N, M, PY):
        print(ans)
