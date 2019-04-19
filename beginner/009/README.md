# AtCoder Beginner Contest 009

## A

:o:

問題文通り。`O(1)`

## B

:o:

ソートして、`bisect_left` などで `max(A)` の一番左(小さい数より)のインデックスを取得すれば良い。`O(N logN)`

## C

:x:

よくわからなかった。`O(N logN)`

## D

:x:

漸化式で行列を表現するのを知らなかった。あと、`M < K` の場合を考えてなくてハマって `WA` 出しまくった。`O(K^3 logM)`
