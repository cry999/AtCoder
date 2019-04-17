# AtCoder Beginner Contest 054

## A

:o:

最強の `1` に注意。`O(1)`

## B

:o:

小さいので全探索で OK。`O(N^2 M^2)`

## C

:o:

これも DFS で全探索。`O(N!)`

## D

:x:

dp を使う。解説通りの実装だと `python` だと `TLE` だった。[この提出](https://atcoder.jp/contests/abc054/submissions/4823416)を参考に、探索を `100` で打ち切るようにしたら `AC`。`O(N^3 max(A) max(B))`
