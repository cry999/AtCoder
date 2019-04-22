def measure_wind(deg: int, dis: int) -> tuple:
    if 112.5 <= deg and deg < 337.5:
        deg = "NNE"
    elif 337.5 <= deg and deg < 562.5:
        deg = "NE"
    elif 562.5 <= deg and deg < 787.5:
        deg = "ENE"
    elif 787.5 <= deg and deg < 1012.5:
        deg = "E"
    elif 1012.5 <= deg and deg < 1237.5:
        deg = "ESE"
    elif 1237.5 <= deg and deg < 1462.5:
        deg = "SE"
    elif 1462.5 <= deg and deg < 1687.5:
        deg = "SSE"
    elif 1687.5 <= deg and deg < 1912.5:
        deg = "S"
    elif 1912.5 <= deg and deg < 2137.5:
        deg = "SSW"
    elif 2137.5 <= deg and deg < 2362.5:
        deg = "SW"
    elif 2362.5 <= deg and deg < 2587.5:
        deg = "WSW"
    elif 2587.5 <= deg and deg < 2812.5:
        deg = "W"
    elif 2812.5 <= deg and deg < 3037.5:
        deg = "WNW"
    elif 3037.5 <= deg and deg < 3262.5:
        deg = "NW"
    elif 3262.5 <= deg and deg < 3487.5:
        deg = "NNW"
    else:
        deg = "N"

    dis = dis * 10 // 6
    if dis % 10 >= 5:
        dis += 10

    dis = round(dis / 10)

    if 0 <= dis and dis <= 2:
        deg, dis = "C", 0
    elif dis <= 15:
        dis = 1
    elif dis <= 33:
        dis = 2
    elif dis <= 54:
        dis = 3
    elif dis <= 79:
        dis = 4
    elif dis <= 107:
        dis = 5
    elif dis <= 138:
        dis = 6
    elif dis <= 171:
        dis = 7
    elif dis <= 207:
        dis = 8
    elif dis <= 244:
        dis = 9
    elif dis <= 284:
        dis = 10
    elif dis <= 326:
        dis = 11
    elif dis >= 327:
        dis = 12

    return deg, dis


if __name__ == "__main__":
    deg, dis = map(int, input().split())

    Dir, W = measure_wind(deg, dis)
    print(Dir, W)
