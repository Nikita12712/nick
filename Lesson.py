def move_last_to_first(lst):
    if len(lst) > 1:
        lst.insert(0, lst.pop())
    return lst

print(move_last_to_first([1, 2, 3, 4]))
print(move_last_to_first([7]))
print(move_last_to_first([]))
print(move_last_to_first([3, 4, 2, 5]))