def one_dimensional_worlds_tale(
        N: int, M: int, X: int, Y: int, x: list, y: list) -> bool:
    border_x = max([X] + x)
    border_y = min([Y] + y)
    return border_x < border_y


if __name__ == "__main__":
    N, M, X, Y = map(int, input().split())
    x = [int(s) for s in input().split()]
    y = [int(s) for s in input().split()]
    ans = one_dimensional_worlds_tale(N, M, X, Y, x, y)
    print('War' if not ans else 'No War')
