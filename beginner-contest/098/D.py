def sigmaN(n: int) -> int:
    """sigma{i=1}{n} i = n * (n+1) / 2
    """
    return n * (n+1) // 2


def xor_sum_2(N: int, A: list) -> int:
    """Al + ... + Ar = Al ^ ... ^ Ar
    が成り立つとき、l <= i <= j <= r を満たす全ての
    (i, j) の組について
    Ai + ... + Aj = Ai ^ ... ^ Aj
    が成り立つ。
    また、
    Al + ... + Ar != Al ^ ... ^ Ar
    のとき、
    A{l-1} + Al + ... + Ar != A{l-1} ^ Al ^ ... ^ Ar
    Al + ... + Ar + A{r+1} != Al ^ ... ^ Ar ^ A{r+1}
    が成り立つ。
    したがって、まず l を固定して等式が成り立たなくなるまで r
    を増やしていき、成り立たなくなったら l を一つ進める、という
    ことを繰り返す尺取り法で O(N) になる。
    """
    r = 0              # 右側の上限
    Sadd, Sxor = 0, 0  # +/^ の累積
    count = 0          # (l, r) の組み合わせ数
    overlapped = 0     # 以前に計算済みの部分列との積集合の大きさ
    for l in range(N):
        al = A[l]
        if Sadd != Sxor:
            # l を進めるときは A[l] の削除と重複部分の削除を行う
            Sadd, Sxor = Sadd - al, Sxor ^ al
            overlapped -= 1
            continue

        # 重複して数えてしまう部分の削除
        count -= sigmaN(overlapped-1)

        # r を限界まで伸ばす。
        while r < N and Sadd == Sxor:
            ar = A[r]
            Sadd, Sxor = Sadd + ar, Sxor ^ ar
            overlapped += 1
            r += 1

        if Sadd == Sxor:
            # r を限界まで伸ばして Sadd == Sxor が保たれるということは
            # r == N であり、ここから l を進めても全部重複部分なので
            # 計算する必要がなく、終了
            count += sigmaN(r - l)
            break
        else:
            # r を伸ばすとき、r は Sadd != Sxor になるまで伸ばされていて
            # 結果的に一つ余計なものを含んでいるので、それを削除する
            overlapped -= 1
            count += sigmaN((r-1) - l)

        # l を進めるにあたり、最左の A[l] は削除する必要がある
        Sadd, Sxor = Sadd - al, Sxor ^ al

    return count


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = xor_sum_2(N, A)
    print(ans)
