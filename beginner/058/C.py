def dubious_document(N: int, S: list)->str:
    ret = ''
    for c in 'abcdefghijklmnopqrstuvwxyz':
        ret += c * min(s.count(c) for s in S)

    return ret


if __name__ == "__main__":
    N = int(input())
    S = [input() for _ in range(N)]
    ans = dubious_document(N, S)
    print(ans)
