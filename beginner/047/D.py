def an_invisible_hand(N: int, T: int, A: list) -> int:
    max_profit = 0
    max_profit_pair_num = 0
    min_price = A[0]

    for price in A[1:]:
        # 今まで訪れた街の中で最安値で買えるところで買えるだけ
        # 買って今いる街で全て売ると仮定して利益を算出
        profit = price - min_price

        if max_profit < profit:
            # 利益の最大値を更新できるなら更新する。
            max_profit = profit
            max_profit_pair_num = 1
        elif max_profit == profit:
            # 最大利益を出せる街のペアに対して操作を
            # 行うので、その数を保持する。
            max_profit_pair_num += 1

        min_price = min(min_price, price)

    # 最大利益を出せる街のペアに対して、最高値を 1 下げるか最安値を 1 あげるか
    # すれば利益を 1 円減らせる。ただ、一つのペアを変更してもそのほかのペアが残
    # っていればそのペアを利用して最高利益をあげられるので全ペアに同じ操作が必要
    # 。結局、最大利益をあげるペアの数が最小操作回数で、それらに 1 の変化を与え
    # れば良いので最小コストでもある。
    return max_profit_pair_num


if __name__ == "__main__":
    N, T = map(int, input().split())
    A = [int(s) for s in input().split()]
    ans = an_invisible_hand(N, T, A)
    print(ans)
