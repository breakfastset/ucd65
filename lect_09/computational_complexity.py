
def print_last(items):
    print("==============") # 1 step
    print("| Last index |") # 1 step
    print("==============") # 1 step
    print(items[-1])     #  1 step

    # Total steps = 4 steps
    # O(4) => O(1)
    # 1. Find the largest term
    # 2. Discard the cofficient

def print_all(items):
    print("==============") # 1 step
    print("|  All items |") # 1 step
    print("==============") # 1 step
    for i in range(len(items)): # n times
        print(items[i])         # n times
        print("=-=-=-=-=-=-=-") # n times

    # Total steps = 3n + 3
    # O(3n + 3) = O(3n)     # get the largest term
    #           = O(n)      # discard the coefficient


def print_matrix(items):
    print("---------")   # 1 step
    print("  Matrix ")   # 1 step
    print("---------")   # 1 step
    for row in range(len(items)):   # n times
        for col in range(len(items[row])):  # n * n times
            print(items[row][col])    # n * n times

    # Total steps = 2n^2 + n + 3
    # O(2n^2 + n + 3) = O(2n^2)    # get the largest term
    #                 = O(n^2)     # discard the coeff


def print_half_each_time(number):
    while number > 0:
        print(number)
        number = number // 2

    # The number of executions increase by 1 for each doubling
    # O(log n)

def print_double_each_time(number):
    for i in range(1, 2**number + 1):
        print(i)

    # Growth is exponential
    # O(2^n)

def main():
    numbers = [8, 2, 3, 4, 6, 99, 100, 101, 12, 3, 5, 6, 1]
    print_last(numbers)
    print()
    print_all(numbers)
    print()
    print_half_each_time(8000)
    print("===============")
    print_double_each_time(5)

main()