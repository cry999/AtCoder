import sys


def question(u: int, v: int) -> int:
    '''u と v の距離を訪ねる。
    '''
    print('? {} {}'.format(u, v))
    sys.stdout.flush()
    ans = int(input())
    return ans


def tree_diameter(N: int) -> int:
    # question time
    # 1 からその他のすべての頂点への距離を訪ねる。
    one_to_others = [0] * N
    for i in range(1, N):
        one_to_others[i] = question(1, i+1)

    if N == 2:
        # 頂点二つなら辺は一つで、それをすでに聞き出しているので
        # それが答え。
        return one_to_others[1]

    sorted_one2others = sorted((d, i) for i, d in enumerate(one_to_others))

    # 1 から最も遠い 2 点を選ぶ
    farthest = sorted_one2others[-1]
    # second_farthest = sorted_one2others[-2]

    # # この 2 点間の距離を訪ねる。
    _, i1 = farthest
    # d1, i1 = farthest
    # d2, i2 = second_farthest

    # max_d = question(i1+1, i2+1)
    # if max_d == d1 + d2:
    #     # この場合、farthest と second_farthest は 1 の左右に
    #     # 分かれており、この二つが最遠
    #     return max_d

    # # 上の条件に合致しない場合、1 を挟んで second_farthest のほかに
    # # 最遠点がある可能性があるのでそれを探す。ただし、farthest は必ず
    # # 最遠点の一端点である。
    # for n in range(1, N):
    #     if n == d1 or n == d2:
    #         # すでに探索しているのは聞くだけ無駄なので skip
    #         continue
    #     max_d = max(max_d, question(d1+1, n+1))

    # return max_d
    return max(question(i1+1, i+1) for i in range(N))


if __name__ == "__main__":
    N = int(input())
    ans = tree_diameter(N)
    print('! {}'.format(ans))
