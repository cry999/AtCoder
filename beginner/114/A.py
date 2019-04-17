def q753(X: int) -> bool:
    return X == 7 or X == 5 or X == 3


if __name__ == "__main__":
    X = int(input())
    ans = q753(X)
    print('YES' if ans else 'NO')
