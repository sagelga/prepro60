""" Descendants of the Sun """
import math
def main():
    """ Main Function """
    # Get how many input
    nnn = int(input())
    # Variable Define
    data = list()
    lat = list()
    lng = list()
    dlat = list()
    dlng = list()
    result = list()

    # Input data
    for _ in range(nnn + 1):
        data += [input().split(', ')]

    # Convert data to radian
    for cnt in range(nnn + 1):
        lat += [float(data[cnt][0].replace('(', '')) * 3.1416 / 180]
        dlat += [float(data[cnt][0].replace('(', ''))]
        lng += [float(data[cnt][1].replace(')', '')) * 3.1416 / 180]
        dlng += [float(data[cnt][1].replace(')', ''))]

    for cnt in range(1, nnn + 1):
        result += [2 * 6378.137 * math.asin(math.sqrt(
            (math.sin((lat[cnt] - lat[cnt-1]) / 2) ** 2)
            + (math.cos(lat[cnt-1])
               * math.cos(lat[cnt])
               * math.sin((lng[cnt] - lng[cnt-1]) / 2) ** 2)
            ))]

    for cnt in range(nnn):
        print("#", cnt + 1, " Distance: %.2fkm Direction: " %result[cnt], sep='', end='')
        if dlat[cnt + 1] > dlat[cnt] and dlng[cnt + 1] > dlng[cnt]: # NE
            print("NE")
        elif dlat[cnt + 1] > dlat[cnt] and dlng[cnt + 1] < dlng[cnt]: # NW
            print("NW")
        elif dlat[cnt + 1] > dlat[cnt] and dlng[cnt + 1] == dlng[cnt]: # N
            print("N")
        elif dlat[cnt + 1] < dlat[cnt] and dlng[cnt + 1] > dlng[cnt]: # SE
            print("SE")
        elif dlat[cnt + 1] < dlat[cnt] and dlng[cnt + 1] < dlng[cnt]: # SW
            print("SW")
        elif dlat[cnt + 1] < dlat[cnt] and dlng[cnt + 1] == dlng[cnt]: # S
            print("S")
        elif dlat[cnt + 1] == dlat[cnt] and dlng[cnt + 1] > dlng[cnt]: # E
            print("E")
        elif dlat[cnt + 1] == dlat[cnt] and dlng[cnt + 1] < dlng[cnt]: # W
            print("W")

main()
