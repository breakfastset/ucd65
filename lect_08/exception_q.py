# suppose the program asks for an input of height
# for a typical adult.
# height must be between 1 to 3.5m
# use exception handling to ensure that the input
# is correct

# Sample run:
# Enter height between 1 to 3.5 : 0.5
# Height must be from 1 to 3.5, try again!
# Enter height between 1 to 3.5 : 4
# Height must be from 1 to 3.5, try again!
# Enter height between 1 to 3.5 : xyz
# Invalid input, must be a float! Try again!
# Enter height between 1 to 3.5 : 5
# Height must be from 1 to 3.5, try again!
# Enter height between 1 to 3.5 : 2
# Wow, you are 2m tall!

valid_input = False
while not valid_input:
    try:
        height = float(input("Enter height between 1 to 3.5: "))
        if 1 <= height <= 3.5:
            valid_input = True
        else:
            print("Height must be from 1 to 3.5, try again!")
    except ValueError:
        print("Invalid input, must be a float! Try again!")

print(f"Wow, you are {height:.0f}m tall!")
