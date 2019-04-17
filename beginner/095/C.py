def half_and_half(
        A: int, B: int, C: int, X: int, Y: int) -> int:
    """
    :param A: A ピザの値段
    :param B: B ピザの値段
    :param C: AB ピザの値段
    :param X: A ピザの必要数
    :param Y: B ピザの必要数
    """
    min_price = float('inf')
    for num_ab in range(max(X, Y)+1):
        num_a, num_b = max(0, X-num_ab), max(0, Y-num_ab)
        price = num_a*A + num_b*B + 2*num_ab*C
        min_price = min(min_price, price)

    return min_price


if __name__ == "__main__":
    A, B, C, X, Y = map(int, input().split())
    ans = half_and_half(A, B, C, X, Y)
    print(ans)
