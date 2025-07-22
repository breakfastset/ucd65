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


def display_terms_conditions():
    """Display the terms and conditions of use a number of lines each time."""
    in_file = open("terms.txt", "r", encoding="utf-8")
    count = 1
    for line in in_file:
        print(line.strip())
        if count % 10 == 0:
            dummy = input(" --- Press Enter for More --- ")
        count += 1
    in_file.close()

def main():
    """Start of program."""
    availability = read_availability("cars.txt")   # read from file
    print(f"Cars available: {availability}")
    choice = input(MENU)    # 1. prime the loop

    # --- start of the loop ---- #
    while choice != "4":     # 2. while condition is True
        if choice == "1":          # 3. statements ...
            print("1. Rent Car")
            availability = rent_car(availability)
        elif choice == "2":
            print("2. Return Car")
            availability = return_car(availability)
        elif choice == "3":
            print("3. Read Terms & Conditions")
            display_terms_conditions()
        else:
            print("Invalid choice! 1 to 4 only!")

        choice = input(MENU)  # 4. ask the user again to test condition
    # --- end of the loop --- #

    print("Bye bye! Thank you for using our Service!")
    save_availability("cars.txt", availability)  # save updated value to file

#-------------------------
# main program
# -----------------------
main()   # Call the main() to start program