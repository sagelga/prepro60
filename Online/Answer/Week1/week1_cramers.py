""" Cramer's Rule """
def main():
    """ Main function """
    vx1 = float(input()) #a
    vy1 = float(input()) #b
    vz1 = float(input()) #c
    vr1 = float(input()) #j
    vx2 = float(input()) #d
    vy2 = float(input()) #e
    vz2 = float(input()) #f
    vr2 = float(input()) #k
    vx3 = float(input()) #g
    vy3 = float(input()) #h
    vz3 = float(input()) #i
    vr3 = float(input()) #l

    res_x = (vr1 * vy2 * vz3 +
             vy1 * vz2 * vr3 +
             vz1 * vr2 * vy3 -
             vr3 * vy2 * vz1 -
             vy3 * vz2 * vr1 -
             vz3 * vr2 * vy1)/(vx1 * vy2 * vz3 +
                               vy1 * vz2 * vx3 +
                               vz1 * vx2 * vy3 -
                               vx3 * vy2 * vz1 -
                               vy3 * vz2 * vx1 -
                               vz3 * vx2 * vy1)

    res_y = (vx1 * vr2 * vz3 +
             vr1 * vz2 * vx3 +
             vz1 * vx2 * vr3 -
             vx3 * vr2 * vz1 -
             vr3 * vz2 * vx1 -
             vz3 * vx2 * vr1)/(vx1 * vy2 * vz3 +
                               vy1 * vz2 * vx3 +
                               vz1 * vx2 * vy3 -
                               vx3 * vy2 * vz1 -
                               vy3 * vz2 * vx1 -
                               vz3 * vx2 * vy1)
    res_z = (vx1 * vy2 * vr3 +
             vy1 * vr2 * vx3 +
             vr1 * vx2 * vy3 -
             vx3 * vy2 * vr1 -
             vy3 * vr2 * vx1 -
             vr3 * vx2 * vy1)/(vx1 * vy2 * vz3 +
                               vy1 * vz2 * vx3 +
                               vz1 * vx2 * vy3 -
                               vx3 * vy2 * vz1 -
                               vy3 * vz2 * vx1 -
                               vz3 * vx2 * vy1)

    print(round(res_x, 2))
    print(round(res_y, 2))
    print(round(res_z, 2))

main()
