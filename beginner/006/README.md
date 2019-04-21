# AtCoder Beginner Contest 006

## A

:o:

`3` が含まれるかどうかは `str` で判定する方が楽。`O(log n)`

## B

:o:

問題文通りに実装。`O(n)`

## C

:o:

大人、老人、赤ン坊の人数をそれぞれ `x` `y` `z` とすると、以下の等式が成り立つ。

```math
x + y + z = N
2x + 3y + 4z = M
```

これから `z` を消去して

```math
2x + y = 4N - M
```

となる。これはベズーの等式。[AtCoder Beginners Selection](../../AtCoderBeginnersSelection/otoshidama.py)でも利用した。

`y` が係数 `1` で探索しやすいので、`y` について探索する。`y` の探索範囲は

```diff
-0 <= 2x = 4N - M - y <= N
-∴ 3N - M <= y <= 4N - M
+0 <= y <= N (上の範囲だと WA だった)
```

となるので、`O(N)`

## D

:x:

最長増加部分列。一番ながいソートされている部分列を残して他をソートするという考え方が浮かばなかった。`O(N logN)`
