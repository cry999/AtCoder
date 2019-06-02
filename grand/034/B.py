def abc(s: str)->int:
    count = 0  # 操作回数
    countA = 0  # 現在連続している 'A' の数

    i, N = 0, len(s)
    while i < N:
        if s[i] == 'A':
            countA += 1
            i += 1
        elif s[i] == 'B':
            if countA > 0 and i+1 < N and s[i+1] == 'C':
                count += countA
                i += 2
            else:
                countA = 0
                i += 1
        else:  # s[i] == 'C'
            countA = 0
            i += 1

    return count


if __name__ == "__main__":
    s = input()

    ans = abc(s)
    print(ans)
