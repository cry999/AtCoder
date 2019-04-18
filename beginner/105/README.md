# AtCoder Beginner Contest 105

## A

:o:

剰余問題。O(1)

## B

:o:

候補全探索。O(N)

## C

:o:

あまりが 0 以上の数になる様に割り算を設計すれば、あとは普通の n 進数の求め方と同じ。O(log N)

## D

:x:

i までの累積和を S{i} とすると、A{l} + ... + A{r} = S{r} - S{l-1} である。さらに、これが M の倍数となるのは、S{r} と S{l-1} の M で割ったあまりが等しい時。したがって、あまりの出現数 r を記録し、各 r に対して rC2 の総和を取れば良い。O(N)