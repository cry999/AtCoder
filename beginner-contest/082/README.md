# AtCoder Beginner Contest 082

## A

:o:

`math.ceil` を使うと一発だったがそれだと面白くないので、`(a+b)` の偶奇で場合分け。`O(1)`

## B

:o:

`s` を昇順に、`t` を降順にソートして文字列比較すれば良い。ただ、`s' < t'` としても面白くないので、1文字ずつ見ることにしてみた。`O(min(|s|, |t|))`

## C

:o:

`a` を走査して、各数字の出現頻度を取る。あとは、出現頻度が数字より大きい場合は余剰分を覗き、小さい場合は出現した全てを取り除けば良い。`O(N)`

## D

:o:

[ABC 111 D](../111/D.py) 問題と似たような考え方で解いた。与えられた命令は `T` を区切りにして、奇数番号区間の F の数はその命令により x 軸方向に直進できる距離、偶数番号区間は y 軸方向に直進できる距離。これらの正負は自由に決めていいので、[ABC 111 D](../111/D.py) と同じ方法をここで使う。距離は降順にソートする必要があるのでこれがボトルネックとなり、`O(|S| log|S|)`