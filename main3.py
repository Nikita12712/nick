import random

list_length = random.randint(3, 10)

my_list = [random.randint(1, 100) for _ in range(list_length)]

new_list = [my_list[0], my_list[2], my_list[-2]]

print("Оригінальний список:", my_list)
print("Новий список:", new_list)