def ok(_to: int, _from: int, S: str)->bool:
    '''_to から _from へ行けるかどうかを判定する
    '''
    for i in range(_to, _from+1):
        if i < _from and S[i] == '#' and S[i+1] == '#':
            return False
    return True


def kenken_race(N: int, A: int, B: int, C: int, D: int, S: str)->bool:
    if not ok(A, C, S) or not ok(B, D, S):
        return False

    if C < D:
        # ふぬけくんの方が右にいることは保障されている。
        # この時、ふぬけくんのゴールがすぬけくんのそれより右なら
        # 先にふぬけくんをゴールさせてしまえばいい。
        return True

    # ふぬけくんのゴールの方が左にある場合はどこかですぬけくんが追い抜かないといけない
    # そのスペースがあるかを確認する。
    # 具体的にはふぬけくんのスタートからゴールまでの間に '.' が 3 つ以上連続する点があれば良い。
    for i in range(B, D+1):
        if S[i-1] == '.' and S[i] == '.' and S[i+1] == '.':
            return True
    return False


if __name__ == "__main__":
    N, A, B, C, D = map(int, input().split())
    S = input()

    yes = kenken_race(N, A-1, B-1, C-1, D-1, S)
    print('Yes' if yes else 'No')
