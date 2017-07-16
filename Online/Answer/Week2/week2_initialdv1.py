""" Initial D V1 """
def find(velocity, distance):
    """ Find time """
    time = distance / velocity
    time = round(time * 3600)
    minutes = time // 60
    seconds = time % 60
    print(str(minutes) + " minutes " + str(seconds) + " seconds")

find(float(input()), float(input()))
