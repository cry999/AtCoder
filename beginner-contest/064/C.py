def colorful_leaderboard(N: int, A: list)->tuple:
    rates = {
        '0001-0399': False,
        '0400-0799': False,
        '0800-1199': False,
        '1200-1599': False,
        '1600-1999': False,
        '2000-2399': False,
        '2400-2799': False,
        '2800-3199': False,
    }
    wildcard = 0

    for a in A:
        if a < 400:
            rates['0001-0399'] = True
        elif a < 800:
            rates['0400-0799'] = True
        elif a < 1200:
            rates['0800-1199'] = True
        elif a < 1600:
            rates['1200-1599'] = True
        elif a < 2000:
            rates['1600-1999'] = True
        elif a < 2400:
            rates['2000-2399'] = True
        elif a < 2800:
            rates['2400-2799'] = True
        elif a < 3200:
            rates['2800-3299'] = True
        else:
            wildcard += 1

    rated_colors = sum(rates.values())

    return rated_colors if rated_colors > 0 else 1, rated_colors + wildcard


if __name__ == "__main__":
    N = int(input())
    A = [int(s) for s in input().split()]
    min_c, max_c = colorful_leaderboard(N, A)
    print(min_c, max_c)
