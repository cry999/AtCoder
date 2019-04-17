def num_2pow(n: int) -> int:
    '''素因数分解した際の 2 の指数を求める。
    '''
    count = 0
    while n & 1 == 0:
        count += 1
        n >>= 1
    return count


def shift_only(N: int, A: list) -> int:
    return min(num_2pow(a) for a in A)


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = shift_only(N, A)
    print(ans)
