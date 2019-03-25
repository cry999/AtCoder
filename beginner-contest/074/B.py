def collecting_balls(N: int, K: int, X: list)->int:
    dist = 0
    for x in X:
        if x < K - x:
            # ボールはロボット A よりなので
            # A を動かす
            dist += 2 * x
        else:
            # ボールはロボット B よりなので
            # B を動かす
            dist += 2 * (K-x)
    return dist


if __name__ == "__main__":
    N = int(input())
    K = int(input())
    X = [int(s) for s in input().split()]
    ans = collecting_balls(N, K, X)
    print(ans)
