def get_choice(lower_bound, upper_bound):
    """Return a valid choice within the bounds or keep repeating."""

    valid_choice = False

    while not valid_choice:
        try:
            choice = int(input("Enter choice: "))   # get user entry
            if choice < lower_bound or choice > upper_bound:
                print(f"Invalid entry - Input must be between {lower_bound} and {upper_bound}")
            else:
                valid_choice = True
        except ValueError:
            print("Choice must be an integer")


    return choice    # return a valid choice


def print_title(text):
    """Print title in a nice format."""
    horizontal_rule = "=" * 40
    print(horizontal_rule)
    print(f"| {text:^36} |")
    print(horizontal_rule)
