# AtCoder Beginner Contest 061

## A

:o:

問題文通り。`O(1)`

## B

:o:

頂点をキーにもつ `dict` を作成して、辺の両端の頂点をインクリメントする。`O(N)`

## C

:o:

`dict` 利用して各数字の出現回数を記録する。あとは `dict` を key でソートしてかぞえあげる。`O(N logN`)`

## D

:x:

`Bellman-Ford` 使うだけ。負閉路の検出を最短経路上のみで行うことに気づかなかった。`O(NM)`
