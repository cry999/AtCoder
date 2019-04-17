def three_letter_acronym(s1: str, s2: str, s3: str) -> str:
    return (s1[0] + s2[0] + s3[0]).upper()


if __name__ == "__main__":
    s1, s2, s3 = input().split()
    ans = three_letter_acronym(s1, s2, s3)
    print(ans)
