def white_cells(H: int, W: int, h: int, w: int)->int:
    return (H-h) * (W-w)


if __name__ == "__main__":
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    ans = white_cells(H, W, h, w)
    print(ans)
