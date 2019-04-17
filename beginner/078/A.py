def _hex(X: str, Y: str) -> str:
    if X < Y:
        return '<'
    if X > Y:
        return '>'
    return '='


if __name__ == "__main__":
    X, Y = input().split()
    ans = _hex(X, Y)
    print(ans)
