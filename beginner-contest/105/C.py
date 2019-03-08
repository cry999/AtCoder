def inverse(s: str) -> int:
    b = 1
    ret = 0
    for c in reversed(s):
        ret += int(c) * b
        b *= -2
    return ret


def base_2number(N: int) -> int:
    pass
    if N == 0:
        return '0'
    if N < 0:
        return 'not implemented'
    # N > 0
    s = ''
    b = []
    carry = 0
    is_minus = False
    while N > 0:
        v = (N % 2) + (carry % 2)
        if is_minus:
            # if v % 2 == 1:
            pass
        else:
            if v % 2 == 1:
                b.append(1)
            v -= v & 1

        s = str(N % 2) + s
        is_minus = not is_minus
        N >>= 1
    return s


if __name__ == "__main__":
    N = int(input())
    ans = base_2number(N)
    print(ans)
