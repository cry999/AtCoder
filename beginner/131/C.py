def gcd(a: int, b: int)->int:
    if a < b:
        a, b = b, a
    return a if b == 0 else gcd(b, a % b)


def lcm(a: int, b: int)->int:
    return a * b // gcd(a, b)


def div_num(n: int, a: int)->int:
    '''n 以下の整数で a で割り切れるものの数を計算します。
    '''
    return n // a


def anti_division(A: int, B: int, C: int, D: int)->int:
    A -= 1

    n1 = div_num(A, C)+div_num(A, D)-div_num(A, lcm(C, D))
    n2 = div_num(B, C)+div_num(B, D)-div_num(B, lcm(C, D))

    return (B-A) - (n2-n1)


if __name__ == "__main__":
    A, B, C, D = map(int, input().split())

    ans = anti_division(A, B, C, D)
    print(ans)
