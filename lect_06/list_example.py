
numbers = [44, 55, 66, 22, 11, 5,  8,  9]
#           0   1   2   3   4   5  6  7
#          -8  -7  -6  -5  -4  -3  -2 -1

# 1st item
print(numbers[0])

# last item
print(numbers[-1])

print(len(numbers))   # 8

numbers[2] = 777   # modify position 2 to 777
print(numbers)

# print(numbers[8])   # cause an error IndexError

numbers.append(345)   # add to the back of the list
numbers.insert(1, 789)   # insert into index 1
print(numbers)

numbers.pop()    # remove from the back
del numbers[2]   # remove item at index 2
numbers.pop(0)   # remove item at index 0
print(numbers)