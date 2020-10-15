def multiplication_input_array(digits=list()):
    digit = int(input('Enter digit (write \'0\' to end): '))
    if digit == 0:
        multi = 1
        for digit in digits:
            multi *= digit
        return multi
    else:
        digits.append(digit)
        return multiplication_input_array(digits)

print(multiplication_input_array())
