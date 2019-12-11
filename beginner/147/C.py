def honest_or_unkind_2(N: int, testimonies: dict)->int:
    ans = 0
    for i in range(1 << N):
        honest_num = 0
        for j in range(N):
            if i & (1 << j) == 0:
                continue
            honest_num += 1

            # 正直者の場合はその人の証言が全て正しいことをチェックする
            for k, is_honest in testimonies[j]:
                if bool(i & (1 << k)) != is_honest:
                    # 証言の矛盾
                    break
            else:
                # 証言に矛盾なし。次の人をチェック
                continue
            # 証言に矛盾があった
            break
        else:
            # 正直者全員の証言に矛盾なし。この組み合わせは成り立つ。
            ans = max(ans, honest_num)
        # i の表す正直者と嘘つきの組み合わせは証言に矛盾がある

    return ans


if __name__ == "__main__":
    N = int(input())
    testimonies = {}

    for i in range(N):
        A = int(input())
        testimonies[i] = [None] * A
        for a in range(A):
            x, y = map(int, input().split())
            testimonies[i][a] = (x-1, bool(y))

    ans = honest_or_unkind_2(N, testimonies)
    print(ans)
