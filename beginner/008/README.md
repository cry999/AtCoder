# AtCoder Beginner Contest 008

## A

:o:

問題文通り。`O(1)`

## B

:o:

出現頻度をかぞえあげる。`O(N)`

## C

:o:

`全組み合わせでの表の個数 = 各コインの全組み合わせでの表になる回数` が成り立つので、各コインの表になる組み合わせについて計算すれば良い。

`c` の約数が `C` に `n` こあったとする。この時、`c` が表になる組み合わせは

```math
(N この並びから c とその約数を並べるための場所を確保)
x (c の約数の並び)
x (c の約数の並びの間で c が表になるように置ける場所)
x (c とその約数以外の数字の並び)
= N_C_{n+1} x n! x (n//2 + 1) x (N-(n+1))!
```

通りとなる。`c` の約数の並びの間で、`c` が表になるように置ける場所とは `c` の前に偶数個の約数が存在する場所のこと。

約数探しで `O(N^2)`

## D

:x:

いまだに `dp` がパッと思いつかない。もっと練習しないといけない。`O(N^4)`
