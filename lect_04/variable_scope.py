singer = "Lady Yaya"  # global

def shout(name):
    row = f"===={name}!!!===="
    print(row)
    print(row)
    print(row)
    # name and row
    # are local to the shout()


def main():
    shout("Simba")
    print(singer)
    # In programming
    # we want most of the variables to be local
    # NOT Global
    # Only CONSTANTS are GLOBAL

main()
