def linear_approximation(N: int, A: int)->int:
    """悲しさを f(b) = sum|ai - (b + i)| とする。
    これを少し変形して
    f(b) = sum|b - (ai - i)|
    とする。この形の関数は b = (ai - i) の位置で傾きが代わり、
    詳しくは述べないが、ソートして N/2 番目の点で最小値になる。
    """
    new_A = []  # A の各値から i+1 を引いたものを保持しておく
    for i, a in enumerate(A):
        tmp = a - (i+1)
        new_A.append(tmp)

    b = sorted(new_A)[N//2]

    return sum(abs(a-b) for a in new_A)


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = linear_approximation(N, A)
    print(ans)
