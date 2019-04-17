# AtCoder Beginner Contest 109

## A

:o:

条件分岐。O(1)

## B

:o:

`list` 使いながら問題文通り実直に実装するだけ。O(N log(N)) (`in` による探索がおそらく log(N))

## C

:o:

位置をソートして、隣の点との距離を取る。それらの GCD を取っておしまい。O(N log(N)) (GCD が log(N)、ソートが N log(N))

## D

:x:

マスの選択が一度しかできないことを見落としていた。一筆書きを実装して AC。O(HW)
