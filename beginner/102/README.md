# AtCoder Beginner Contest 102

## A

:o:

偶奇で場合分けするだけ。O(1)

## B

:o:

最大・最小の差をとる。O(N)

## C

:o:

絶対値のグラフをかく。ソートがボトルネック。O(N logN)

## D

:x:

真ん中固定して、左右の区間で探索するのまではわかったが、それぞれの区間内での区切り位置が真ん中のそれに対して単調増加という事に気づけず O(N^2) で実装してしまい WA。実際は単調増加を利用すれば O(N)。