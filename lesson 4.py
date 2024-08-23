import random

def generate_random_list():

  list_length = random.randint(3, 10)

  random_list = [random.randint(1, 100) for _ in range(list_length)]

  return random_list

my_random_list = generate_random_list()
print(my_random_list)

print(my_random_list[0], my_random_list[2], my_random_list[-2])