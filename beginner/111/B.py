def abc111(N: int) -> int:
    d = N // 100
    n1 = d * 111
    n2 = (d+1) * 111

    if N <= n1:
        return n1
    return n2


if __name__ == "__main__":
    N = int(input())
    ans = abc111(N)
    print(ans)
