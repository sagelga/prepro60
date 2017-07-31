"""This is a sample answer from P' Kumamon"""
def main():
    """This is a sample answer from P' Kumamon"""
    listing = []
    for _ in range(int(input())):
        listing.append(float(input()))

    listing.sort()

    for i in range(len(listing)):
        if listing[i] == int(listing[i]):
            listing[i] = int(listing[i])

        print(listing[i], end=" ")
main()
