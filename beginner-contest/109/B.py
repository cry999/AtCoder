def shiritori(N: int, W: list)->bool:
    used = []
    head = W[0][0]

    for w in W:
        if w in used or head != w[0]:
            return False
        used.append(w)
        head = w[-1]

    return True


if __name__ == "__main__":
    N = int(input())
    W = [input() for _ in range(N)]
    yes = shiritori(N, W)
    print('Yes' if yes else 'No')
