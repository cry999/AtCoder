# AtCoder Beginner Contest 114

## A

:o:

ただ比較するだけ。

## B

:o:

前から順番に比較するだけ。

## C

:o:

単純に全ての数字を比較すると 10^9 は間に合わない。なので、以下のような工夫をした。

- スタートは 357。これより小さい数字には七五三数は存在しない。
- インクリメントを最初は +2 することで奇数だけみたが、これでも間に合わなかったので、全桁が 3, 5, 7 だけで含まれるものになるようにインクリメントを決めた。ただし、この段階では 3, 5, 7 のなかで含まれないものもありうる。

## D

:o:

`n = a1^p1 * a2^p2 * ... * aN^pN` と表せる時、

```(nの約数の個数) = (p1 + 1) * (p2 + 2) * ... * (pN + 2)```

が成り立つことを利用する。約数をちょうど75個持つ数 n は以下のように表せるはず。

- n = a^74
- n = a^24 * b^2
- n = a^14 * b^4
- n = a^5 * b^5 * c^2

したがって、N! の素因数を調べ、上の (a, (b, (c))) の組み合わせの総数を数え上げれば良い。
