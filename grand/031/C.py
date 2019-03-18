def num_of_1bit(n: int)->int:
    '''n の立っているビットを数えます。
    :param n: number
    :return: number of 1 bit
    '''
    s = 0
    while n > 0:
        s += n & 1
        n >>= 1
    return s


def diff_idx(a: int, b: int)->int:
    '''a と b のビット列を比較してビットの状態が異なる最小の
    インデックスを返します。ここで、インデックスは 2^i の i 
    に対応する。
    :param a: number 1
    :param b: number 2
    :return: index
    '''
    if a == b:
        return -1
    idx = 0
    while a > 0 or b > 0:
        if a & 1 != b & 1:
            break
        idx += 1
        a, b = a >> 1, b >> 1
    return idx


def remove_bit(n: int, idx: int)->int:
    '''n の idx 番目のビットを消去します。idx は 2^idx に対
    応します。
    ex) n = 1011011, idx = 2
    -> 101111

    :param n: number
    :param idx: index
    :return: number removed `idx`th bit
    '''
    upper = (n >> (idx+1)) << idx
    lower = n & ((1 << idx) - 1)
    return upper | lower


def insert_bit(n: int, idx: int, bit: bool)->int:
    '''n の idx 番目にビットを挿入します。
    ex) n = 101111, idx = 2, bit = True
    -> 1011111
    '''
    upper = (n >> idx) << (idx + 1)
    lower = n & ((1 << idx) - 1)
    insert = bit << idx
    return upper | insert | lower


def route(_from: int, to: int, N: int)->list:
    '''_from から to に至る N ビットの数を全て使ったルートを
    計算します。
    :param _from: start
    :param to: end
    :param N: number of bit
    :return: routes
    '''
    if N == 1:
        return [_from, to]

    di = diff_idx(_from, to)

    a = remove_bit(_from, di)
    b = remove_bit(to, di)
    c = a ^ 1

    from_bit = (_from & (1 << di)) != 0
    to_bit = (to & (1 << di)) != 0

    first_half = map(lambda x: insert_bit(x, di, from_bit), route(a, c, N-1))
    second_half = map(lambda x: insert_bit(x, di, to_bit),  route(c, b, N-1))

    return list(first_half) + list(second_half)


def diff_by_1_bit(N: int, A: int, B: int)->list:
    num_A = num_of_1bit(A)
    num_B = num_of_1bit(B)
    if abs(num_A - num_B) % 2 == 0:
        return []

    return route(A, B, N)


if __name__ == "__main__":
    N, A, B = map(int, input().split())
    ans = diff_by_1_bit(N, A, B)
    if len(ans) == 0:
        print('NO')
    else:
        print('YES')
        print(' '.join(map(str, ans)))
