# AtCoder Beginner Contest 093

## A

:o:

S が 'a'、'b'、'c' を含む事を確認すれば良い。`O(|S|)`

## B

:o:

`k` を `0 ~ K-1` で変化させながら適切に `A+k`、`B-k` を追加していく。ただし、`A+k == B-k` となる時と `A+k > B-k` となる時の処理に注意が必要。`O(K)`

## C

:o:

`A <= B <= C` が成り立っているとする。A、B、を C に近づけたいので、A, B の両方に 1 を足すか、それぞれに 2 を足すかをするかを行うがどっちも結果的に同じなので、後者を選ぶ。この処理を完了したあとの操作回数を `n` とする。(A, B, C) は以下のいずれかの状態になる。

1. (C, C, C)
    終了。結果は `n`。

2. (C-1, C, C)
    (B, C の両方に 1 を足す操作) + (A に 2 を足す操作) で終了。`n + 2`

3. (C-1, C-1, C)
    (A, B の両方に 1 を足す操作) で終了。`n + 1`

`O(1)`

## D

:x:

解説読まないと場合分けが全く理解できなかった。また、解説通り実装しても `C^2 < A * B` を満たす最大の `C` を求める時に `A` から `B` までひとつずつ確かめてたら、`A` や `B` が馬鹿でかいため `TLE` になった。ここも binary search を用いる。`O(Q log(abs(A-B)))`。`C` を求める binary search が `log(abs(A-B))` かかる。
