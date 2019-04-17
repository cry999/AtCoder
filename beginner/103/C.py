def modulo_summation(N: int, A: list)->int:
    """f(n) = (n % a1) + ... + (n % aN) の最大値を求める。
    f(n) の各項の最大値を考えると `ai - 1` である。
    lcm(a1, a2, ..., aN) - 1 = M を考えると、任意の i について
    M = ai x M' - 1 = ai x (M' - 1) + (ai - 1)
    となり、M % ai = ai - 1 となることがわかる。したがって、n = M
    とすることで f(n) の各項は最大となり、当然 f(n) も最大となる。

    以上より、f(n) の最大値は sum(a - 1 for a in A)
    """
    return sum(a - 1 for a in A)


if __name__ == "__main__":
    N = int(input())
    A = map(int, input().split())
    ans = modulo_summation(N, A)
    print(ans)
