# AtCoder Beginner Contest 040

## A

:o:

左と右の赤の少ないほうに移動する。`O(1)`

## B

:o:

幅に関して全探索。`O(√N)`

## C

:o:

dp を次の漸化式で定義する。

```math
dp[i] = 0                                                           (if i == 0)
dp[i] = dp[i-1] + abs(A[i]-A[i-1])                                  (if i == 1)
dp[i] = min(dp[i-1] + abs(A[i]-A[i-1]), dp[i-2] + abs(A[i]-A[i-2])) (if i >= 2)
```

計算量は `O(N)`

## D

:o:

辺、クエリを重い順に処理する。`UnionFind`。`O(Q logM)`
