# AtCoder Beginner Contest 034

## A

:o:

`x < y`。`O(1)`

## B

:o:

`N` の偶奇に注目。`O(1)`

## C

:o:

高速に combination を求める。`(n+1)_C_(r+1) = (n+1) * n_C_r / (r+1)` を利用すれば、`(n-r)_C_0 = 1` から初めて `O(r)` で `n_C_r` を求められる。したがって `O(min(H, W))`

## D

:x:

二分法。`O(K + N logN)`
