
# bool(x) returns True or False depending on x
#
# False if x is one of the following:
#       1) an empty string
#       2) an empty list
#       3) 0
#
# True is everything that is not in 1), 2) or 3)
#
print(bool(0))         # False
print(bool(10000))     # True
print("----------")

print(bool(0.0001))    # True
print(bool(-0.0001))   # True
print("----------")

print(bool("Hello World!"))   # True
print(bool("False"))          # True, "False" is a string
print("----------")

print(bool(""))        # False, empty string
print(bool(" "))       # True,  a space



