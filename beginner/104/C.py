from math import ceil


def all_green(D: int, G: int, PC: int)->int:
    min_coin_num = float('inf')
    for n in range(1 << D):
        # 中途半端に解く問題の(番号, 数)
        not_used = []
        # 完全に解く問題数と、使った時の得点
        used_coin_num, total_point = 0, 0
        for i, (p, c) in enumerate(PC):
            # n = 0b10110 とすると、
            # レベル 1 問題をとかない
            # レベル 2 問題をとく
            # レベル 3 問題をとく
            # レベル 4 問題をとかない
            # レベル 5 問題をとく
            # と考える。
            if n & 1 == 1:
                # 完全に解く問題
                total_point += (100*(i+1)) * p + c
                used_coin_num += p
            else:
                # 完全にとかない問題
                not_used.append((i, p))
            n = n >> 1

        if total_point >= G:
            # 完全に解く問題だけで間に合うならそれで終わり。
            min_coin_num = min(min_coin_num, used_coin_num)
        else:
            # 完全に解く問題だけで間に合わない場合は、いづれか一種類のレベル
            # の問題を中途半端に解いて補填する。
            for i, p in not_used:
                # (中途半端に使う問題数) = ceil((残っている得点) / (注目している問題一つの得点))
                coin_num = ceil((G-total_point)/(100*(i+1)))
                if coin_num < p:
                    # コインの枚数が足りる場合のみ
                    min_coin_num = min(min_coin_num, used_coin_num+coin_num)

    return min_coin_num


if __name__ == "__main__":
    D = 0
    D, G = map(int, input().split())
    PC = [tuple(int(s) for s in input().split()) for _ in range(D)]
    ans = all_green(D, G, PC)
    print(ans)
