def positive_princess_of_monster(N: int, H: list)->list:
    d = {}
    i = 0
    for h in sorted(H):
        if h in d:
            continue
        d[h] = i
        i += 1

    return [d[h]+1 for h in H]


if __name__ == "__main__":
    N = int(input())
    H = [int(input()) for _ in range(N)]

    for ans in positive_princess_of_monster(N, H):
        print(ans)
