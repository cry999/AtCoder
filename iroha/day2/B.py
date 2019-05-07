def hentai_by_the_river(X: int, Y: int, A: int, B: int, S: tuple, T: tuple)->bool:
    def f(p: tuple)->int:
        x, y = p
        return (B-A)*x - y*X + A*X

    return f(S) * f(T) <= 0


if __name__ == "__main__":
    X, Y = map(int, input().split())
    A, B = map(int, input().split())
    S = tuple(int(s) for s in input().split())
    T = tuple(int(s) for s in input().split())

    yes = hentai_by_the_river(X, Y, A, B, S, T)
    print('Yes' if yes else 'No')
