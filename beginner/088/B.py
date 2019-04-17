def card_game_for_two(N: int, A: list) -> int:
    sorted_A = sorted(A, key=lambda x: - x)
    alice = sum(a for i, a in enumerate(sorted_A) if i % 2 == 0)
    bob = sum(a for i, a in enumerate(sorted_A) if i % 2 == 1)
    return alice - bob


if __name__ == "__main__":
    N = int(input())
    A = map(int, input().split())
    ans = card_game_for_two(N, A)
    print(ans)
