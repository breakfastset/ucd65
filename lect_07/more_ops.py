numbers = [45, 78, 13, -15, 13, 3, -5, 0, 1, 13, 22, 87, 20, 13, 10, -8]

numbers_1 = numbers[:]
numbers_1.reverse()    # reverse the order

print(numbers)
print(numbers_1)
print("--" * 40)

numbers_1.sort()     # sort() in ascending order modifies orig list
numbers_2 = sorted(numbers_1, reverse=True)  # descending order
print(numbers_1)
print(numbers_2)  # sorted() makes a copy of orig list

print("--" * 40)
target = 13
# while target in numbers:
#     numbers.remove(target)

index = 0
while index < len(numbers):
    if numbers[index] == target:
        numbers.pop(index)
    else:
        index += 1

print(numbers)   # all 13 removed

print("--" * 40)

colours = ["yellow", "blue", "green", "red"]
colours = colours * 3
print(colours)

