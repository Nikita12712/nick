def multiply_digits_until_single_digit(number):

    number = abs(number)

    while number > 9:
        result = 1
        for digit in str(number):
            result *= int(digit)
        number = result

    return number

user_input = int(input("Enter a number: "))
result = multiply_digits_until_single_digit(user_input)
print(result)