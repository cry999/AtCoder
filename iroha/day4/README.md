# Iroha Chan Contest day4

## A

:o:

メモ化再起。`O(N^4)`

## B

:x:

~~最終的に電車に乗ってゴールするなら最初から乗ってても到達時間は変わらない。したがって、いろはちゃんが走る時は最後まで走る。なのでいろはちゃんがどの駅から走るかを二分探索で求めれば良い。いろはちゃんが走った方が早い場合は走る駅を増やして調べる、逆の場合は走る駅を減らして調べるを繰り返す。~~

~~いろはちゃんが走り出す駅を決めたら、その駅にたどり着く一番早い電車を決めるために `O(N)` かかるので、全体として `O(N logM)`~~

そもそも乗り換えは生じない。`O(N)`

## C

:x:

2 のべき乗で分解できることに気づけなかった。`O(|S| log|S|)`

## D

:x:

考察が甘かった。二分探索のチェックを高速にやる方法を思いつかなかった。`O(T logA)`

## E

TODO: not implemented

## F

TODO: not implemented

## G

TODO: not implemented

## H

TODO: not implemented

## I

TODO: not implemented

## J

TODO: not implemented

## K

TODO: not implemented

## L

TODO: not implemented
