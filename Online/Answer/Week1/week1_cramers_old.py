""" [Hardcore] [Week1] Cramer's Rule """
def main():
    """ Main function """
    inputs_dict = {'a': float(input()),
                   'b': float(input()),
                   'c': float(input()),
                   'j': float(input()),
                   'd': float(input()),
                   'e': float(input()),
                   'f': float(input()),
                   'k': float(input()),
                   'g': float(input()),
                   'h': float(input()),
                   'i': float(input()),
                   'l': float(input())}

    det_coeffs_matrix = (inputs_dict['a'] * inputs_dict['e'] * inputs_dict['i'] +
                         inputs_dict['b'] * inputs_dict['f'] * inputs_dict['g'] +
                         inputs_dict['c'] * inputs_dict['d'] * inputs_dict['h'] -
                         inputs_dict['g'] * inputs_dict['e'] * inputs_dict['c'] -
                         inputs_dict['h'] * inputs_dict['f'] * inputs_dict['a'] -
                         inputs_dict['i'] * inputs_dict['d'] * inputs_dict['b'])

    det_x = (inputs_dict['j'] * inputs_dict['e'] * inputs_dict['i'] +
             inputs_dict['b'] * inputs_dict['f'] * inputs_dict['l'] +
             inputs_dict['c'] * inputs_dict['k'] * inputs_dict['h'] -
             inputs_dict['l'] * inputs_dict['e'] * inputs_dict['c'] -
             inputs_dict['h'] * inputs_dict['f'] * inputs_dict['j'] -
             inputs_dict['i'] * inputs_dict['k'] * inputs_dict['b'])

    det_y = (inputs_dict['a'] * inputs_dict['k'] * inputs_dict['i'] +
             inputs_dict['j'] * inputs_dict['f'] * inputs_dict['g'] +
             inputs_dict['c'] * inputs_dict['d'] * inputs_dict['l'] -
             inputs_dict['g'] * inputs_dict['k'] * inputs_dict['c'] -
             inputs_dict['l'] * inputs_dict['f'] * inputs_dict['a'] -
             inputs_dict['i'] * inputs_dict['d'] * inputs_dict['j'])

    det_z = (inputs_dict['a'] * inputs_dict['e'] * inputs_dict['l'] +
             inputs_dict['b'] * inputs_dict['k'] * inputs_dict['g'] +
             inputs_dict['j'] * inputs_dict['d'] * inputs_dict['h'] -
             inputs_dict['g'] * inputs_dict['e'] * inputs_dict['j'] -
             inputs_dict['h'] * inputs_dict['k'] * inputs_dict['a'] -
             inputs_dict['l'] * inputs_dict['d'] * inputs_dict['b'])

    res_x = det_x/det_coeffs_matrix
    res_y = det_y/det_coeffs_matrix
    res_z = det_z/det_coeffs_matrix

    if res_x % 1 == 0:
        res_x = int(res_x)
    else:
        res_x = round(res_x, 2)
    if res_y % 1 == 0:
        res_y = int(res_y)
    else:
        res_y = round(res_y, 2)
    if res_z % 1 == 0:
        res_z = int(res_z)
    else:
        res_z = round(res_z, 2)

    print(res_x)
    print(res_y)
    print(res_z)

main()
