def traveling(N: int, travel: list) -> bool:
    ct, cx, cy = 0, 0, 0
    for nt, nx, ny in travel:
        dt, dx, dy = nt - ct, abs(nx - cx), abs(ny - cy)

        if dx + dy <= dt and (dx + dy) % 2 == dt % 2:
            pass
        else:
            return False

        ct, cx, cy = nt, nx, ny

    return True


if __name__ == "__main__":
    N = int(input())
    travel = [map(int, input().split()) for _ in range(N)]
    ans = traveling(N, travel)
    print('Yes' if ans else 'No')
