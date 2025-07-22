
numbers = [67, 14, -15, -2, 18, 0, -9, 50, 51, 37, -12]

positive_numbers = [num for num in numbers if num >= 0]
print(positive_numbers)

squares = [num ** 2 for num in numbers]
print(squares)

negative_even_numbers = [num for num in numbers if num < 0 and num % 2 == 0]
print(negative_even_numbers)

absolute_numbers = [num if num >= 0 else num * -1 for num in numbers]
print(absolute_numbers)

binaries = [1 if num >= 0 else 0 for num in numbers]
print(binaries)

sorted_big_numbers = sorted([num for num in numbers if num > 20])
print(sorted_big_numbers)

# positive_numbers = []
# for number in numbers:
#     if number >= 0:
#         positive_numbers.append(number)

things = ["mountain", "river", "garden", "bottle", "bat", "glasses", "airport"]

long_strings = [thing for thing in things if len(thing) > 5]
print(long_strings)

things_ending_with_t = [thing for thing in things if thing.endswith('t')]
print(things_ending_with_t)

