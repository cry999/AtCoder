def pyramid(N: int, info: list) -> tuple:
    """
    """
    _info = sorted(info, key=lambda x: x[2], reverse=True)
    x, y, h = _info[0]
    candidtes = [
        (cx, cy, h + abs(cx - x) + abs(cy - y))
        for cx in range(100+1)
        for cy in range(100+1)]

    for x, y, h in _info[1:]:
        temp = []
        for cx, cy, H in candidtes:
            th = max(H - abs(cx - x)-abs(cy - y), 0)
            if th == h:
                temp.append((cx, cy, H))

        candidtes = temp

    return candidtes[0]

if __name__ == "__main__":
    N = int(input())
    info = [
        tuple(int(s) for s in input().split())
        for _ in range(N)]
    cx, cy, h = pyramid(N, info)
    print(cx, cy, h)
