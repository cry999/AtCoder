def UOIAUAI(c: str)->bool:
    return c in 'aeiuo'


if __name__ == "__main__":
    s = input()
    is_vowel = UOIAUAI(s)
    print('vowel' if is_vowel else 'consonant')
