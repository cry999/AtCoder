def many_medians(N: int, X: list) -> list:
    """必要なのはXをソート(降順)したとき N/2 番目と
    N/2 + 1 番目(ともに 1-indexed)の値。
    N/2 番目の値を x 、N/2 + 1 番目の値を y とする。
    xi >= x の時は y、xi < x の時は x が答え。
    """
    x, y = sorted(X, key=lambda a: -a)[N//2-1:N//2+1]
    return [x if xi < x else y for xi in X]


if __name__ == "__main__":
    N = int(input())
    X = list(map(int, input().split()))
    ans = many_medians(N, X)
    for b in ans:
        print(b)
