def q754(S: str) -> int:
    ans = float('inf')
    for i in range(len(S)):
        d = int(S[i:i+3])
        if abs(753 - d) < ans:
            ans = abs(753-d)
    return ans


if __name__ == "__main__":
    S = input()
    ans = q754(S)
    print(ans)
