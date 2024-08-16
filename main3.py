number = int(input("Введіть 5-ти значне число: "))


n1 = number % 10
n2 = (number // 10) % 10
n3 = (number // 100) % 10
n4 = (number // 1000) % 10
n5 = number // 10000


reversed_number = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5


print("Перевернуте число:", reversed_number)
