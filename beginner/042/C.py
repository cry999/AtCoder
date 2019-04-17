def irohas_obsession(N: int, K: int, D: list) -> int:
    # D に含まれない最小の値
    min_not_d = min(d for d in range(10) if d not in D)
    min_not_d_and_not_zero = min(d for d in range(10) if d not in D and d != 0)

    # 数字を各桁に分解する。
    nums = []
    while N > 0:
        nums = [N % 10] + nums
        N //= 10

    # 上位の桁から見ていって最初に D に含まれる数字を探す。
    convert_idx = -1
    for i, n in enumerate(nums):
        if n not in D:
            # 変換の必要がない
            continue

        convert_idx = i
        break
    # print(convert_idx)
    for i in range(convert_idx, -1, -1):
        n = nums[i]
        if n > 9:
            n %= 10
            if i > 0:
                nums[i - 1] += 1
            else:
                nums = [min_not_d_and_not_zero] + nums

        for d in range(n, 10):
            # 変換先が n 以上 9 以下
            if d in D:
                # NG
                continue

            nums[i] = d
            break
        else:
            # 変換先が n 未満
            for d in range(n, 10):
                if d in D:
                    # NG
                    continue

                nums[i] = d

            # 上位の桁に繰り上がりを伝搬
            if i > 0:
                nums[i - 1] += 1
            else:
                nums = [min_not_d_and_not_zero] + nums

    # 残りの桁は D に含まれない最小の値に変換する。
    nums = [min_not_d if n in D else n for n in nums]

    ret = 0
    digit = 1
    # print(nums)
    for n in reversed(nums):
        ret += n * digit
        digit *= 10

    return ret


if __name__ == "__main__":
    N, K = map(int, input().split())
    D = [int(s) for s in input().split()]
    ans = irohas_obsession(N, K, D)
    print(ans)
