def handicraft_king(N: int, S: str)->int:
    if N % 2 == 0:
        # 偶数長はありえない
        return -1

    center = N // 2

    # 手順 0
    turn = 0
    if S[center] != 'b':
        return -1

    turn += 1
    while 0 <= center - turn:
        if turn % 3 == 1:
            # 手順 3n + 1
            left, right = 'a', 'c'
        elif turn % 3 == 2:
            # 手順 3n + 2
            left, right = 'c', 'a'
        else:
            # 手順 3n
            left, right = 'b', 'b'

        if S[center-turn] != left:
            return -1
        if S[center+turn] != right:
            return -1

        turn += 1

    return turn-1


if __name__ == "__main__":
    N = int(input())
    S = input()
    ans = handicraft_king(N, S)
    print(ans)
