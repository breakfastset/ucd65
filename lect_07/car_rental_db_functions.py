import csv

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