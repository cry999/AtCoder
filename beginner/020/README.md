# AtCoder Beginner Contest 020

## A

:o:

問題文通り。`O(1)`

## B

:o:

結合する際は文字列として扱うと楽。`O(1)`

## C

:o:

`x` に関して二分探索。チェック内容は、`x` に対して `T` 以内にゴールできるか。これを判定するために、`S` から `G` までの最小コストを計算 (`O(HW)`) して `T` 以下かを判断する。`O(HW logHW)`

## D

:x:

解説見ても `TLE` を超えられなかった。