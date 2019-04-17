def is_palindromic(n: int) -> bool:
    s = str(n)
    l = len(s)
    for i in range(l//2):
        if s[i] != s[-(i+1)]:
            return False
    return True


def palindromic_numbers(A: int, B: int) -> int:
    return sum(is_palindromic(n) for n in range(A, B+1, 1))


if __name__ == "__main__":
    A, B = map(int, input().split())
    ans = palindromic_numbers(A, B)
    print(ans)
