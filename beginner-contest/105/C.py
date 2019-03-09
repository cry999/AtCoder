def div_minus2(n: int)->tuple:
    """n を -2 で割ったときの商とあまりを計算する。
    """
    d = n // (-2)
    r = n % (-2)
    if r == -1:
        return d+1, 1
    return d, r


def base_2number(N: int) -> int:
    if N == 0:
        return '0'
    # N > 0
    s = ''
    while N != 0:
        d, r = div_minus2(N)
        N = d
        s = str(r) + s

    return s


if __name__ == "__main__":
    N = int(input())
    ans = base_2number(N)
    print(ans)
