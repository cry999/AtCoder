def sum_price(n: int, X: int, A: list)->int:
    k = 0
    price = 0
    while X > 0:
        if X & 1 != 0:
            price += A[k]
        X >>= 1
        k += 1
    return price


if __name__ == "__main__":
    n, X = map(int, input().split())
    A = [int(s) for s in input().split()]
    ans = sum_price(n, X, A)
    print(ans)
