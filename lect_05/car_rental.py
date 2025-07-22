MENU="""Welcome to the minimal car-rental company.
1. Rent car
2. Return car
3. Read T&C
4. Quit
Please choose an option: """


def read_availability(filename):
    """Read the number of cars from database and return."""
    num_cars = 0
    in_file = open(filename, "r")
    line = in_file.readline()
    num_cars = int(line)
    in_file.close()
    return num_cars


def save_availability(filename, availability):
    """Save updated number of cars to file."""
    out_file = open(filename, "w")
    out_file.write(f"{availability}\n")
    out_file.close()
    print("*** Cars database updated! ***")


def return_car(availability):
    """Return a car and inform the customer."""
    availability += 1
    print("Car returned. Thank you!")
    return availability


def rent_car(availability):
    """Rent car and inform the customer"""
    if availability > 0:
        availability -= 1
        print("Your car is available at checkout.")
    else:
        print("Sorry, no cars are available at the moment.")

    return availability


def main():
    """Start of program."""
    availability = read_availability("cars.txt")   # read from file
    print(f"Cars available: {availability}")
    choice = input(MENU)

    if choice == "1":
        print("1. Rent Car")
        availability = rent_car(availability)
    elif choice == "2":
        print("2. Return Car")
        availability = return_car(availability)
    elif choice == "3":
        print("3. Read Terms & Conditions")
        print("By renting our cars, you agree to ....")
    elif choice == "4":
        print("Bye bye! Thank you for using our Service!")
    else:
        print("Invalid choice! 1 to 4 only!")

    save_availability("cars.txt", availability)  # save updated value to file

main()   # Call the main() to start program