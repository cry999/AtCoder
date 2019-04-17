def two_anagrams(s: str, t: str) -> bool:
    '''s を並び替えた実現可能な最小の文字列 s' と t を並び替えて
    実現可能な最小の文字列 t' に関して、s' < t' が成り立てば良い。
    '''
    sn, tn = len(s), len(t)
    sd, td = sorted(s), sorted(t, reverse=True)

    idx = 0
    while idx < sn and idx < tn:
        # idx-1 番目の文字までは同じと仮定する。
        if sd[idx] < td[idx]:
            # この場合 sn < tn が成り立つ。
            return True
        if sd[idx] == td[idx]:
            # 次に持ち越し
            idx += 1
            continue
        if sd[idx] > td[idx]:
            # この場合 sn > tn が成り立つ。
            return False

    # min(sn, tn) 番目まで同じ。あとは長いほうが後ろ
    return sn < tn


if __name__ == "__main__":
    s = input()
    t = input()
    yes = two_anagrams(s, t)
    print('Yes' if yes else 'No')
