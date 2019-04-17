def equal_cut(N: int, A: list) -> int:
    Sa = [0] * (N + 1)  # A の累積和
    for i, a in enumerate(A):
        Sa[i + 1] = Sa[i] + a

    li, ri = 1, 3
    ans = float('inf')
    for mi in range(2, N - 1):
        # 中心の区切り mi を固定して左右の区間内で最適な
        # 区切り位置 li, ri を決めていく
        # B, C, D, E = A[:li], A[li:mi], A[mi:ri], A[ri:]
        if ri <= mi:
            ri = mi + 1

        # 適切な li を決める
        for temp_li in range(li + 1, mi):
            P, Q = Sa[temp_li - 1], Sa[mi] - Sa[temp_li - 1]
            nP, nQ = Sa[temp_li], Sa[mi] - Sa[temp_li]

            if abs(nP - nQ) <= abs(P - Q):
                # nP と nQ が近くなら li を更新する
                li = temp_li
            else:
                # nP と nQ が遠ざかり始めたらこれ以上 li を
                # 右に移動しても差は広がる一方で探索する意味
                # がないので打ち切り
                break

        # 適切な ri を決める
        for temp_ri in range(ri + 1, N):
            R, S = Sa[temp_ri - 1] - Sa[mi], Sa[N] - Sa[temp_ri - 1]
            nR, nS = Sa[temp_ri] - Sa[mi], Sa[N] - Sa[temp_ri]

            if abs(nR - nS) <= abs(R - S):
                ri = temp_ri
            else:
                break

        P = Sa[li]
        Q = Sa[mi] - Sa[li]
        R = Sa[ri] - Sa[mi]
        S = Sa[N] - Sa[ri]
        temp = max(P, Q, R, S) - min(P, Q, R, S)

        if temp < ans:
            ans = temp

    return ans


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = equal_cut(N, A)
    print(ans)
