def march(N: int, S: list) -> int:
    d = {'M': 0, 'A': 0, 'R': 0, 'C': 0, 'H': 0}
    for s in S:
        k = ''
        if s.startswith('M'):
            k = 'M'
        elif s.startswith('A'):
            k = 'A'
        elif s.startswith('R'):
            k = 'R'
        elif s.startswith('C'):
            k = 'C'
        elif s.startswith('H'):
            k = 'H'
        else:
            continue
        d[k] += 1

    count = 0
    val = list(d.values())
    for i in range(5):
        for j in range(i + 1, 5):
            for k in range(j + 1, 5):
                count += val[i] * val[j] * val[k]

    return count


if __name__ == "__main__":
    N = int(input())
    S = [input() for _ in range(N)]
    ans = march(N, S)
    print(ans)
