# diverta Programing Contest 2019

いろはちゃんコンテストに夢中で出遅れる。

## A

:o:

`N - (K-1)`。`O(1)`

## B

:o:

全探索。`O(N^2/max(RG, GB, BR))` くらい。

## C

:o:

簡単な問題だったがゆえに一度ハマったら何を間違っているのか気づきずらかった。

`A` で終わる文字列、`B` で始まる文字列、`B` で始まり `A` で終わる文字列をカウントする。それぞれのカウント数を `X` `Y` `Z` とする。

まず、`BxxxA` の文字列を全部つなげることで `Z-1` この `AB` が作れる。

次に、`X > 0` なら、`xxxA` を上で作った文字列の頭につなげることで `1` つ `AB` が増やせる。

同様に、`Y > 0` の時に `Bxxx` を上の文字列の後ろにつなげることで `1` つ `AB` が増やせる。

最後に、残った `xxxA` と `Bxxx` を繋げられるだけ繋げれば良い。

`O(N)`

## D

:o:

`N` を `m` で割った時の商と余りが等しいので、これを `a` とする。この時、`N = am + a = (m + 1)a` が成り立つので、`a = 1` から `a * a <= N` を満たす全て `a` について検証すれば良い。`a` が `m` のあまりであることから、`a < m` が成り立つことに注意。

`O(√N)`

## E

:x:

わからなかった。 ~~ 2 進数表記の各桁の偶奇で `dp` するのかな? ~~

`A` の累積 xor を `B` とする。`B` に含まれる任意の数 `X` を選び、`0` と `X` 以外の数字を消して `0 X 0 X 0 ...` の形の数列に落とし込む。

たとえば `B = [0, X, 0, 0, 0, X]` であったとする。このとき、`0` が 3 つ並んでいる区間の xor は xor の性質から `X` になることがわかる。したがって、`0` と `X` を正しく選んでその後ろに仕切りを入れればよく、この例の場合は 1 番目の要素の後と 4 番目の要素の後に仕切りを入れることで xor が `X` になる区間が 3 つ作れる。

どの `0` と `X` の後に仕切りを入れれば良いかを考える。

最初の仕切りを `0` の後に入れたとする。この場合、各区間の xor は `0` でないといけないのでその後も `0` の後にしか仕切りを入れられない。

最初の仕切りを `X` の後に入れたとする。この場合、各区間の xor は `X` でないといけないので `0` と `X` の後に交互に入れていく必要がある。

あとは、`B` の最後の要素で場合分け。

1. `B` が `0` で終わる場合

   この場合はありうる `X` 全てについて考える必要がある。

2. `B` が `0` で終わらない場合

   `X` は `B` の最終要素で決まり。

仕切りの入れ方は `dp` を利用してかぞえあげる。

## F

:x:

全くわからない。高速ゼータ変換について調べる。`O(2^N N)`