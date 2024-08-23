def move_zeros_to_end(numbers):

  write_index = 0

  for i in range(len(numbers)):
    if numbers[i] != 0:
      numbers[write_index] = numbers[i]
      write_index += 1

  for i in range(write_index, len(numbers)):
    numbers[i] = 0

  return numbers


my_list = [3, 0, 4, 0, 5, 0, 1]
result = move_zeros_to_end(my_list)
print(result) 