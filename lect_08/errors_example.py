print("Start...")

try:
    num_1 = int(input("1st num? "))
    num_2 = int(input("2nd num? "))
    print(f"Result = {num_1 / num_2}")
except ValueError:
    print("Only integers allowed!")
except ZeroDivisionError:
    print("Cannot divided by ZERO!")


print("End...")

age = 21
if age > 21:
    print("You can vote")
else:
    print("You cannot vote")



