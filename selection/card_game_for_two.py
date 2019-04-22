def card_game_for_two(N: int, A: list) -> int:
    _A = sorted(A)
    alice = sum([a for i, a in enumerate(_A) if i % 2 == 0])
    bob = sum([a for i, a in enumerate(_A) if i % 2 == 1])

    return abs(alice - bob)


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    ans = card_game_for_two(N, A)

    print(ans)
