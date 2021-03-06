# AtCoder Beginner Contest 058

## A

:o:

問題文通り。`O(1)`

## B

:o:

問題文通り。`O(|O| + |E|)`

## C

:o:

各文字列での頻度分布をとって、各文字を全文字列での最小出現回数分プリントする。`O(N |S|)`

## D

:o:

x 軸に平行な辺の取りうる全組み合わせを `lx1, lx2, ..., lxN`、y 軸に平行なそれを `ly1, ly2, ..., lyM` とする。この時、求める面積 `S` は

```math
S = (lx1 + lx2 + ... + lxN)(ly1 + ly2 + ... + lyM)
```

となる。後必要なのは、`lx1 + lx2 + ... + lxN` と `ly1 + ly2 + ... + lyM` である。求め方はどちらも同じなので、x 軸に平行な方で説明する。

`xi` と `x{i+1}` を端点とする辺を `li` とする。この時、`lx1 + lx2 + ... + lxN` に `li` が含まれる回数を考えると、`1 <= j <= i` `i+1 <= k <= n` を満たす `(j, k)` について `xj` と `xk` を端点とする辺全てに含まれるので、`i * (n-i)` となる。これを全ての `i` について行えば良い。
つまり、

```math
lx1 + lx2 + ... + lxN = sum(li * i * (n-i) for i in range(n))
```

となる。y 軸に平行な方も同じことをやる。これで `S` が求まる。

`O(n + m)`
