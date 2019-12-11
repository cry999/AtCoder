def palindrome_philia(S: str)->int:
    ans = 0
    for i in range(len(S)//2):
        if S[i] != S[-(i+1)]:
            ans += 1
    return ans


if __name__ == "__main__":
    S = input()
    ans = palindrome_philia(S)
    print(ans)
