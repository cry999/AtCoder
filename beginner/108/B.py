def calc_orthogonal_vect(x1: int, y1: int, x2: int, y2: int)->tuple:
    if x1 == x2:
        return x2 - (y2 - y1), y2

    return x2 - (y2 - y1), y2 + (x2 - x1)


def ruined_square(x1: int, y1: int, x2: int, y2: int)->tuple:
    x3, y3 = calc_orthogonal_vect(x1, y1, x2, y2)
    x4, y4 = calc_orthogonal_vect(x2, y2, x3, y3)

    return x3, y3, x4, y4


if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = ruined_square(x1, y1, x2, y2)
    print(x3, y3, x4, y4)
