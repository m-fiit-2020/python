def is_divisor(num, divisors):
    for digit in divisors:
        if num%digit == 0:
            return True
    else:
        return False

prime_digits = [2]
for i in range(3, 1001, 2):
    if not is_divisor(i, range(2, int(i**0.5) + 1)):
        prime_digits.append(i)
print(prime_digits)
