# y = 2x + 1
# f(x) = 2x + 1
# f(3) = 2(3) + 1
#      = 7
# f(10) = 2(10) + 1 = 21

def func(x):   # x is a parameter
    return 2 * x + 1

def main():
    print("Start of program")

    y1 = func(3)    # 3 is an argument
    print(y1)    # 7

    y2 = func(10)
    print(y2)    # 21

main()   # call main function to run