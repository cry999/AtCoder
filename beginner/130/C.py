def rectangle_cutting(W: int, H: int, x: int, y: int)->tuple:
    area = W*H/2
    exists_some = 2*x == W and 2*y == H

    return area, exists_some


if __name__ == "__main__":
    W, H, x, y = map(int, input().split())

    area, exists_some = rectangle_cutting(W, H, x, y)
    print(area, 1 if exists_some else 0)
