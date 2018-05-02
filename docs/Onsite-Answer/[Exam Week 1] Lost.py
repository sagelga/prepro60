"""
Sample Answer from P' Kumamon
This program will calculate the ticket price for all customer count
"""
def main():
    """Main calculation of the program"""
    angle = direction_to_angle(input())
    angle += int(input()) + int(input()) + int(input()) + int(input())
    print(angle_to_direction(angle%360))

def direction_to_angle(direction):
    """Converts direction to angle"""
    if direction == "N":
        return 0
    elif direction == "E":
        return 90
    elif direction == "S":
        return 180
    elif direction == "W":
        return 270

def angle_to_direction(angle):
    """Converts angle to direction"""
    if angle == 0:
        return "N"
    elif angle == 90:
        return "E"
    elif angle == 180:
        return "S"
    elif angle == 270:
        return "W"
    else:
        return "Error"

main()
