def a2z_string(s: str)->int:
    a = s.find('A')
    z = s.rfind('Z')
    return z - a + 1


if __name__ == "__main__":
    s = input()
    ans = a2z_string(s)
    print(ans)
