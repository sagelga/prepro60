""" This program will calculate minimum, maximum and average of five numbers """
def main(arg_1, arg_2, arg_3, arg_4, arg_5):
    """ This main function take 5 arguments to find and display minimum, maximum and average """
    minimum = min(arg_1, arg_2, arg_3, arg_4, arg_5)
    maximum = max(arg_1, arg_2, arg_3, arg_4, arg_5)
    average = avg(arg_1, arg_2, arg_3, arg_4, arg_5)
    print("Minimum value:", minimum)
    print("Maximum value:", maximum)
    print("Average:", average)

def avg(num_1, num_2, num_3, num_4, num_5):
    """ This function call avg take 5 arguments to calculate average and return back """
    return (num_1+num_2+num_3+num_4+num_5)/5

main(int(input()), int(input()), int(input()), int(input()), int(input()))
