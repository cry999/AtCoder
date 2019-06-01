# ExaWizards 2019

## A

:o:

`A` `B` `C` が等しいことを確かめる。`O(1)`

## B

:o:

単純に `R` の数を数え上げて、`N-R` と比較する。

## C

:o:

クエリを逆に見ていって、残る範囲を限定していく。`O(Q)`

## D

:x:

確率の問題に読み替えは難しい。問題文通り `dp[i][x] = i 回目の操作で現在の X の値が x の時の最終的な X の期待値` とすると

```math
dp[i][x] = dp[i-1][x] * (N-i) / (N+1-i) + dp[i-1][x] / (N+1-i)
```

と表せる。これを `i` の大きい順に計算する。すると答えは `dp[0][X] * N!` となる。ここで計算途中に少数が入るのを防ぐために `dp[N][x]` の値を `x * N!` に初期化しておくと良い。

`O(NX)`

## E

:x:

2 次元平面に落とすところまでは遷移図を書くことで気づけた。しかしそのあとの combination を利用した式に落とすところが気づけなかった。

`O(B+W)`

## F

:x:

座標圧縮が思いつかなかった。座標圧縮に `O(N)` かかり、座標圧縮後の dijkstra はグラフのサイズは一定で高々 36 頂点ぐらい(6 x 6)なので `O(1)` とみなす。全体で `O(N + Q)`