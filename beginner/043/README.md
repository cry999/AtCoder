# AtCoder Beginner Contest 043

## A

:o:

総和の公式。`O(1)`

## B

:o:

問題文通りにシミュレートする。`O(|s|)`

## C

:o:

求めるコストは `f(x) = (a1 - x)^2 + ... + (aN - x)^2` であり、これを `x` の関数と見れば下に凸の関数で軸で最小値を取る。軸は `(a1 + ... + aN) / N` でつまりは平均値。よって `f(ave(A))` が答え。`O(N)`

## D

:x:

法則性を見つけるのが苦手。要練習。`O(|s|)`
