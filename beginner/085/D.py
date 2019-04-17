from math import ceil


def katana_thrower(N: int, H: int, AB: int)->int:
    damages = []
    for a, b in AB:
        damages.append((a, False))
        damages.append((b, True))

    count = 0
    for damage, throw in sorted(damages, key=lambda x: -x[0]):
        if H <= 0:
            break
        if throw:
            H -= damage
            count += 1
        else:
            count += ceil(H / damage)
            break
    return count


if __name__ == "__main__":
    N = 0
    N, H = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]
    ans = katana_thrower(N, H, AB)
    print(ans)
