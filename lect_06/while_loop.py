# while loop
# is used for unknown number of executions

# for loop
# is used for a fixed number of executions

# 1. prime the loop
# while 2. condition is True
#      3. do statement 1
#         do statement 2
#         ....
#      4. update variable for condition checking in 2 (eventually exit)
#
# eg. 1 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> 2 -> exit loop
#
#
age = int(input("Enter your age (0 to 130): "))  # 1.
while age < 0 or age > 130:   # 2.
    print("Wrong age! Must be 0 to 130!")   # 3.
    age = int(input("Enter your age (0 to 130): "))  # 4.

print(f"Wow! You will be {age + 1} next year!")
print()
print()

count = 1
while count <= 10:
    print(count)
    count += 1




