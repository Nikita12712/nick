def split_list(input_list):

    mid_index = (len(input_list) + 1) // 2


    first_half = input_list[:mid_index]
    second_half = input_list[mid_index:]


    return [first_half, second_half]



print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))  
