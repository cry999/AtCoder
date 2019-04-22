def trap(W: str) -> str:
    return ''.join(c for c in W if c not in 'aiueo')


if __name__ == "__main__":
    W = input()

    ans = trap(W)
    print(ans)
