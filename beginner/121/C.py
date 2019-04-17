from math import ceil


def energy_drink_collector(N: int, M: int, AB: list)->int:
    total_price = 0
    total_num = 0
    for price, stock in sorted(AB, key=lambda x: x[0]):
        if total_num + stock >= M:
            total_price += price * (M - total_num)
            break
        else:
            total_price += price * stock
            total_num += stock
    return total_price


if __name__ == "__main__":
    N = 0
    N, M = map(int, input().split())
    AB = [tuple(int(s) for s in input().split()) for _ in range(N)]
    ans = energy_drink_collector(N, M, AB)
    print(ans)
