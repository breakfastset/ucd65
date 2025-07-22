from car_rental_db_functions import *
from car_rental_utilities import *

MENU="""Welcome to the minimal car-rental company.
1. Rent car
2. Return car
3. Read T&C
4. Quit
Please choose an option: """

DATABASE_FILE = "cars_db.csv"

def display_cars(car_fleet):
    """Display each car as an option."""
    headers = "     Make        Model      Cls   Qty"
    print(headers)
    print(len(headers) * "-")

    for i in range(len(car_fleet)):
        car = car_fleet[i]
        make = car[0]
        model = car[1]
        car_class = car[2]
        quantity = car[3]
        print(f"{i:2}) {make:12} {model:10} ({car_class:^3}) {quantity:3}")

def rent_car(car_fleet):
    """Rent car and inform the customer"""
    display_cars(car_fleet)
    choice = get_choice(0, len(car_fleet) - 1)

    car_type = car_fleet[choice]  # Get the car to be rented
    if car_type[-1] > 0:          # if quantity is > 0
        car_type[-1] -= 1
        print("Your car is available at checkout.")
    else:
        print("Sorry, no cars are available at the moment.")

    return car_fleet

def return_car(car_fleet):
    """Return a car and inform the customer."""
    display_cars(car_fleet)
    choice = get_choice(0, len(car_fleet) - 1)   # 0 to 4 if there are 5 cars

    car_type = car_fleet[choice]        # Get the car to be returned
    car_type[-1] += 1                   # Increase its quantity
    print("Car returned. Thank you!")
    return car_fleet

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
    car_fleet = read_availability(DATABASE_FILE)   # read from file
    print_title("Main Menu")
    choice = input(MENU)    # 1. prime the loop

    # --- start of the loop ---- #
    while choice != "4":     # 2. while condition is True
        if choice == "1":          # 3. statements ...
            print_title("1. Rent Car")
            car_fleet = rent_car(car_fleet)
        elif choice == "2":
            print_title("2. Return Car")
            car_fleet = return_car(car_fleet)
        elif choice == "3":
            print_title("3. Read Terms & Conditions")
            display_terms_conditions()
        else:
            print("Invalid choice! 1 to 4 only!")

        print_title("Main Menu")
        choice = input(MENU)  # 4. ask the user again to test condition
    # --- end of the loop --- #

    print("Bye bye! Thank you for using our Service!")
    save_availability(DATABASE_FILE, car_fleet)  # save updated value to file

#-------------------------
# main program
# -----------------------
main()   # Call the main() to start program