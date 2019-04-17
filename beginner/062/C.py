def chocolate_bar(H: int, W: int)->int:
    # 縦 3 分割
    h1 = H // 3
    h2 = H // 3 + (H % 3)//2
    h3 = H - h1 - h2

    min_diff = (h3 - h1) * W

    # 横 3 分割
    w1 = W // 3
    w2 = W // 3 + (W % 3)//2
    w3 = W - w1 - w2

    min_diff = min(min_diff, (w3 - w1) * H)

    # 縦に分割した後に一方を横分割　
    #  --------
    # |        |
    # |--------|
    # |    |   |
    #  --------
    h1 = round(H/3)
    h2 = H - h1
    w1 = W // 2
    w2 = W - w1

    S = [h1*W, h2*w1, h2*w2]

    min_diff = min(min_diff, max(S)-min(S))

    # 横に分割した後に一方を縦分割
    #  --------
    # |    |   |
    # |    |---|
    # |    |   |
    #  --------
    h1 = H // 2
    h2 = H - h1
    w1 = round(W/3)
    w2 = W - w1

    S = [H*w1, h1*w2, h2*w2]

    min_diff = min(min_diff, max(S)-min(S))

    return min_diff


if __name__ == "__main__":
    H, W = map(int, input().split())
    ans = chocolate_bar(H, W)
    print(ans)
