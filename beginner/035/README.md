# AtCoder Beginner Contest 035

## A

:o:

`GCD` 求めてわる。`O(A logA)`

## B

:o:

`'L'` `'R'` `'U'` `'D'` `'?'` の出現回数を求めて、`dx = 'L' + 'R'` `dy = 'U' + 'D'` とすれば、求める答えは、

```math
最大値: dx + dy + '?'
最小値: dx + dy - '?'
```

ただし、最小値は負の値になる場合の場合分けが必要。

## C

:o:

典型的な区間和。`O(N+Q)`

## D

:o:

街 `1` から各街への往復の最小時間を求める。復路の最小時間は辺を逆に張ったグラフを利用すれば一度の `dijkstra` 法でもとまる。`T` から往復にかかる時間を引いた値に `A` をかけた値を計算してその最大値を出力すれば良い。`O(M + N logN)`