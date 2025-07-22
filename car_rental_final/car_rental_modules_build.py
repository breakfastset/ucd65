import csv
DATABASE_FILE = "cars_db.csv"

def read_availability(filename):
    """Read the csv file from database and return a list of lists."""
    car_fleet = []
    in_file = open(filename, "r")
    csv_reader = csv.reader(in_file)
    for line in csv_reader:
        line[-1] = int(line[-1])   # convert quantity to int
        car_fleet.append(line)

    in_file.close()
    return car_fleet

def save_availability(filename, car_fleet):
    """Save updated number of cars to file."""
    out_file = open(filename, "w", newline="")
    csv_writer = csv.writer(out_file)
    csv_writer.writerows(car_fleet)
    out_file.close()
    print("*** Cars database updated! ***")

def main():
    car_fleet = read_availability(DATABASE_FILE)
    print(car_fleet)
    car_fleet[1][-1] += 1
    print("Updated quantity for car 2: ")
    print(car_fleet)
    save_availability(DATABASE_FILE, car_fleet)

main()

# This is what availability should contain: List of lists
# [ [ 'BYD', 'Seal', 'B', 7 ],  ['Toyota', 'Camry', 'B', 5],  .... ]


