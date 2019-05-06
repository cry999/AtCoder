def digit_sum(n: int)->int:
    '''n を 10 進法で表した時の各桁の和を求めます。
    '''
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res


def all9(n: int)->bool:
    '''n を 10 進法で表した時の各桁の値が全て 9 であるかどうかを
    判定します。
    '''
    while n > 0:
        if n % 10 != 9:
            return False
        n //= 10
    return True


def chirashi_sushi(N: int)->int:
    ds = digit_sum(N)

    digit = 10 ** (ds // 9)
    res = (ds % 9)*digit + (digit-1)

    if res == N:
        if N < 10:
            res = 10 + (N-1)
        elif ds % 9 == 0:
            digit = 10 ** ((ds - 9) // 9)
            res = 18*digit + (digit-1)
        else:
            digit = 10 ** ((ds - 9) // 9 + 1)
            res = ((ds % 9) + 1)*digit + 8*(digit//10) + (digit//10 - 1)

    return res


if __name__ == "__main__":
    N = int(input())

    ans = chirashi_sushi(N)
    print(ans)
