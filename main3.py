def calculate_sum_product(numbers):

  if not numbers:
    return 0

  sum_of_even_indexed = 0
  for i in range(0, len(numbers), 2):
    sum_of_even_indexed += numbers[i]

  return sum_of_even_indexed * numbers[-1]

list1 = [0, 1, 7, 2, 4, 8]


print(calculate_sum_product(list1)) 

