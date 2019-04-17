def sum_of_three_integers(K: int, S: int)->int:
    count = 0
    for x in range(K+1):
        for y in range(x, K+1):
            z = S - (x + y)

            if z < 0 or K < z:
                # out of range
                continue

            if z < y:
                # x <= y <= z の場合だけ考えて計算回数を減らしたい。
                break

            if x == y and y == z:
                # 全文字一緒なら 1 通り
                count += 1
            elif x == y or y == z:
                # 同じ文字が 2 つだけなら 3C1 = 3 通り
                count += 3
            else:
                # 全て違う文字なら 3P3 = 6 通り
                count += 6
    return count


if __name__ == "__main__":
    K, S = map(int, input().split())
    ans = sum_of_three_integers(K, S)
    print(ans)
