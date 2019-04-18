# AtCoder Beginner Contest 022

## A

:o:

愚直にシミュレーション。`O(N)`

## B

:o:

`A` を前から順番に見て行って、出現した数を `set` などで管理する。`O(N logN)`

## C

:x:

わからなかった。最短閉路は、始点の隣の 2 頂点間の最小経路を求めれば良い。あとは、その 2 頂点への距離を含めて最小なものを探す。`O(N(N + M)logM)`

## D

平行移動、回転に関係ないものを探すという考えができなかった。`O(N)`