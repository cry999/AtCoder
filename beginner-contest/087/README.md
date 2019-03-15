# AtCoder Beginner Contest 087

## A

:o:

`(X-A)%B`。`O(1)`

## B

:o:

`A` `B` `C` について全探索で間に合う。`O(ABC)`

## C

:o:

各列に関して、1 列目は前から、2 列目は後ろから累積和をとって、どのインデックスで曲がるのが最適化を調べる。`O(N)`

## D

:x:

dijkstra 法と Union Find を利用して解こうとしたが、「右に」d の位置という方向がついていることを忘れていて `WA`。方向に対応するために左方向の辺には負数の重みをつけたが、dijkstra 法では負数に対応できないので `WA`。負数に対応できる Bellman-ford 法を使おうと思ったが、こちらは計算量が大きすぎて断念。結局 [重み付き Union-Find 木とそれが使える問題のまとめ、および、牛ゲーについて](https://qiita.com/drken/items/cce6fc5c579051e64fab) を参考に重み付き Union Find を使った。
