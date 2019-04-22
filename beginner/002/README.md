# AtCoder Beginner Contest 002

## A

:o:

問題文通り。`O(1)`

## B

:o:

問題文通り。`O(|W|)`

## C

:o:

`ab = A->B` `ac = A->C` とする。このとき、三角形の面積 `S` は

```math
S = 1/2 * |ab| * |ac| * sin∠BAC
  = 1/2 * |ab| * |ac| * √(1 - (cos∠BAC)^2)
  = 1/2 * |ab| * |ac| * √(1 - (ab・ac/(|ab||ac|))^2)
  = 1/2 * √((|ab||ac|)^2 - (ab・ac)^2)
```

と表せる。これを計算すれば良い。`O(1)`

## D

:o:

最大クリーク問題。全探索する。`O(N * 2^N)`
