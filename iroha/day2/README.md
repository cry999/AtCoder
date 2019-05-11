# Iroha Chan Contest day2

## A

:x:

`LCS(最長共通部分列)` という名前をすっかり忘れていた。`O(|S||T|)`

## B

:o:

`S` `T` の 2 点が直線 `(0, A)-(X, B)` の片側にあるか両側にあるかを判定するだけ。`O(1)`

## C

:o:

`H` をソートしてその順番と身長を対応づける。ただし、同じ身長についての処理に気をつける。`O(N logN)`

## D

:o:

`kruskal` 法。`O(M logN)`

## E

:x:

組み合わせの間違いに気づけなかった。`O(N+M)`

## F

:x:

確率苦手。`O(A1xA2xB1xB2xC1xC3)`

## G

:x:

階層化するところまでは実装できたが `TLE` になってしまい、`AC` の実装できず。`O(KM logKN)`

## H

:x:

テキスト `A` から単語 `A` を探すための `KMP` のテーブル `B` から `A` を復元する問題。`KMP` になじみがなく全く分からず。`O(N)`

## I

:o:

`dijkstra` 。方法はすぐに思いつき実装も `O(HW logHW)` くらいでできたつもりだったがなぜか `TLE` 。そのまま嵌まり続ける。結局 `pair` の型引数が `int` だったために `overflow` 起こして無駄な処理が大量発生していた。普段 `python` で型を気にせず実装しているための弊害だった。気をつけたい。`O(HW logHW)`

## J

TODO: not implemented

## K

TODO: not implemented

## L

TODO: not implemented
