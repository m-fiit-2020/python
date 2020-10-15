def reverse_input_array(digits=list()):
    digit = int(input('Enter digit (write \'0\' to end): '))
    if digit == 0:
        for digit in reversed(digits):
            print(digit)
    else:
        digits.append(digit)
        return reverse_input_array(digits)

reverse_input_array()
