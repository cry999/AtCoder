def sub_123(N: int, NG: list)->bool:
    if N in NG:
        return False

    for _ in range(100):
        # 出来るだけ大きく引いていきたい
        for d in [3, 2, 1]:
            if (N-d) in NG:
                continue
            else:
                N -= d
                break
        else:
            # 操作失敗。
            return False

    return N <= 0


if __name__ == "__main__":
    N = int(input())
    NG = [int(input()) for _ in range(3)]
    yes = sub_123(N, NG)
    print('YES' if yes else 'NO')
