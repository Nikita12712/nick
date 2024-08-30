def multiply_digits_until_single_digit(number): #это обьясняет всю суть кода,лично я так понял

    number = abs(number) #я так понял это переводит число в положительную форму

    while number > 9: #если число больше 9
        result = 1 #то результат 1
        for digit in str(number): #это не понял
            result *= int(digit) #это не понял
        number = result #это присваеваем номер к результату

    return number #это возвращает номер

user_input = int(input("Enter a number: ")) #это для ввода числа человеком
result = multiply_digits_until_single_digit(user_input) #это для результата
print(result) #это результат
