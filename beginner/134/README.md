# AtCoder Beginner Contest 134

## A

:o:

与えられた計算式を実装するだけ。

`O(1)`

## B

:o:

一人で監視できる木の本数は自分の立っているところと、それより左の `D` 本と右の `D` 本の合計 `2*D + 1` 本。したがって必要な監視員は `ceil(N / (2 * D + 1))` 人。

`O(1)`

## C

:o:

`A` の最大値を `M1` とする。その次に大きい数字を `M2` とする。`A[i]` の値で場合わけ。

1. `A[i] < M1`

   当然 `M1` が最大値

1. `A[i] == M1`

   `M1` が 2 つ以上 `A` に含まれるなら一つ除外しても影響はないので最大値は `M1`。一つしかない場合は `M2` が最大値

`O(N)`

## D

:o:

後ろから見ていく。まず `A[N]` が `1` なら `N` 番目の箱にはボールが入らないといけないし、`0` ならボールを入れてはいけない。`N` 番目の箱にボールを入れなかった場合は `N-1` 番目の箱について考えるが、入れた場合は、`N` の約数番目の箱に入るボールの偶奇を入れ替えないといけない。あとはこれを繰り返すだけ。

`O(N√N)`

## E

:o:

単調増加列の個数を数える。`i` 番目までの整数に色を塗りおわっており、使用した色数が `M` であるとする。このとき、`M` 色のそれぞれの最大値(つまりは最後に塗った整数の値)を保持しているとする。`i+1` 番目の整数はこの最大値の中で `A[i+1]` より小さい物の中で最大の物と同じ色を塗れば良い。それを満たす色がない(どの色の最大値も `A[i+1]` より大きい)場合は新しい色をぬる。以上を繰り返す。色の探索は二分探索を用いれば `O(logN)` で実行でき、また新しい色の追加も `queue` を用いれば `O(1)` で行えるので全体としては `O(N logN)` となる。

`O(N logN)`

## F

:x:

全く分からず。

`O(N^4)`
