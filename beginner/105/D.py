def candy_distribution(N: int, M: int, A: list)->int:
    # 累積和 % M を保持
    S = 0
    # 累積和を M で割ったあまりを保持
    remainders = {0: 1}
    for a in A:
        S = (S + a) % M
        if S not in remainders:
            remainders[S] = 0
        remainders[S] += 1

    # i までの累積和を Si とすると Al + ... + Ar = Sr - S{l-1} である。
    # これが M の倍数となるのは、Sl % M == Sr % M となる時である。
    # したがって、Si の累積和のあまりの出現をカウントし、あまりの出現数 r に対して、
    # r(r-1)/2 の総和を求めれば良い。
    return sum(r*(r-1)//2 for r in remainders.values())


if __name__ == "__main__":
    N, M = map(int, input().split())
    A = [int(s) for s in input().split()]
    ans = candy_distribution(N, M, A)
    print(ans)
