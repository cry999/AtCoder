def two_switches(A: int, B: int, C: int, D: int) -> int:
    if B <= C or D <= A:
        # 交わらない。
        return 0
    if A <= C and D <= B:
        # Alice が Bob を完全に含む
        return D - C
    if C <= A and B <= D:
        # Bob が Alice を完全に含む
        return B - A
    if A <= C:
        # A-----B
        #   C----D
        # こんな感じ
        return B - C
    # 残りは C <= A
    #    A-------B
    # C----D
    # こんな感じ
    return D - A


if __name__ == "__main__":
    A, B, C, D = map(int, input().split())
    ans = two_switches(A, B, C, D)
    print(ans)
