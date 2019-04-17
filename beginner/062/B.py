def picture_frame(H: int, W: int, A: list)->list:
    return ['#' * (W+2)] + ['#' + s + '#' for s in A] + ['#' * (W+2)]


if __name__ == "__main__":
    H = 0
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    ans = picture_frame(H, W, A)
    print('\n'.join(ans))
