def combination(n: int, r: int)->int:
    if r == 0 or n == r:
        return 1
    return combination(n-1, r-1) + combination(n-1, r)


def maximum_average_sets(N: int, A: int, B: int, V: list)->tuple:
    sorted_v = sorted(V, key=lambda v: -v)
    ave = sum(sorted_v[:A]) / A
    num = combination(sorted_v.count(
        sorted_v[A-1]), sorted_v[:A].count(sorted_v[A-1]))
    return ave, num


if __name__ == "__main__":
    N, A, B = map(int, input().split())
    V = [int(s) for s in input().split()]
    ave, num = maximum_average_sets(N, A, B, V)
    print(ave)
    print(num)
