"""This is a sample answer from P' Kumamon"""
def main():
    """This is a sample answer from P' Kumamon"""

    # Specification
    listings = [
    [30, 25, "R"],  # Instant Rice
    [25, 40, "S"],  # Sandwitch
    [20, 70, "P"],  # Salapao
    [15, 100, "W"], # Drinks
    [10, 250, "K"]  # Snacks
    ]

    # Initiate State
    name = input() # Seller name
    total = 0
    achievement = ""

    # Calculate State
    for i in range(len(listings)): # Caculate the item listing using the settings in specification
        item = int(input())
        local_total, success = calculate(item, listings[i][0], listings[i][1])
        if success: # If item >= goal
            achievement += listings[i][2] + " "

        total += local_total # Top-up the calculations

    # Ending State
    print("""Employee : %s
Payday : %d Baht.
Archivement : %s
You did great!, %s."""%(name, total, achievement, name))

def calculate(items, price, goal):
    """This is a sample answer from P' Kumamon"""
    success = (items >= goal)

    if success: # Reaching the goal gives 2x the normal price, else is 1x
        price *= 2

    total = items * price

    return total, success

main()
