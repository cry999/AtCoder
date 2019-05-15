def cardgame_in_the_dark(N: int, A: list) -> int:
    offset = (N+1)//2

    ans = float('inf')
    for n in range(offset-1):
        ans = min(ans, abs(A[n]-A[offset+n]))

    return ans


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]

    ans = cardgame_in_the_dark(N, A)
    print(ans)
