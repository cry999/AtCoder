# AtCoder Beginner Contest 113

## A

:o:

算数

## B

:o:

ただの最小値求める問題

## C

:o:

ソートを駆使するだけ。

## D

:x:

目的地から逆算的に 1 へたどりつく道のりを次の漸化式で求めようとした。

```
F(H, W) = F(H-1, W+1) + F(H-1, W) + F(H-1, W-1)
```

加えて、使わない縦線は自由に横線が引けると考えて、使わない縦線の通り方を

```
T(1, W) = T(1, W - 1) + T(1, W - 2) (W > 2)
T(H, W) = T(H - 1) ** H
```

と求めて、(1~wまでの縦線を使った経路の総数) * (w~Wまでの縦線を使ったあみだくじの総数)を w に関して挿話をとればよいと考えたが、F の計算量が H=100 のときに 3^100 になり、さらには、経路で使う縦線内でも経路に影響がなければ自由に縦線がひけることから正答にたどり着かず。