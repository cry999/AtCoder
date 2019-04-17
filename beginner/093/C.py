def same_integers(A: int, B: int, C: int) -> int:
    A, B, C = sorted([A, B, C])
    count = (C-A)//2 + (C-B)//2
    A = A + 2 * ((C-A)//2)
    B = B + 2 * ((C-B)//2)

    A, B, C = sorted([A, B, C])
    # (A,B,C)は以下のいづれか
    # 1.(C, C, C)
    # 終了
    if A == C and B == C:
        return count
    # 2.(C-1, C, C)
    # A に 2 を足して、B, C に 1 を足す。
    if B == C:
        return count + 2
    # 3.(C-1,C-1,C)
    # A, B に 1 を足す。
    return count + 1


if __name__ == "__main__":
    A, B, C = map(int, input().split())
    ans = same_integers(A, B, C)
    print(ans)
