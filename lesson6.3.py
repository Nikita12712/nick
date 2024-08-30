def multiply_digits_until_single_digit(number): #это смогу обьяснить

    number = abs(number) #это не понял

    while number > 9: #это смогу обьяснить
        result = 1 #это смогу обьяснить
        for digit in str(number): #это не понял
            result *= int(digit) #это не понял
        number = result #это смогу обьяснить

    return number #это смогу обьяснить

user_input = int(input("Enter a number: ")) #это смогу обьяснить
result = multiply_digits_until_single_digit(user_input) #это смогу обьяснить
print(result) #это смогу обьяснить