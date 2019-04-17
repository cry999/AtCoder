if __name__ == "__main__":
    n = input()

    t = ''
    for c in n:
        if c == '1':
            t += '9'
        elif c == '9':
            t += '1'

    print(t)
