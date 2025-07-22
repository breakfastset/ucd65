# for i in something:     <something is an iterable>
#    <statement>
import time

# range() is an iterable
for i in range(5):   # for i in range(start=0, end=5, step=1)
    print(i)

print("===" * 30)
for i in range(1, 11):  # for i in range(start=1, end=11, step=1)
    print(i)   # 1, 2 ... 10

print("===" * 30)
for i in range(3, 20, 4):  # 3, 7, 11, 15, 19
    print(i)

print("===" * 30)
for i in range(10, 0, -1):
    # time.sleep(1)
    print(i)
print("~~ BLAST OFF!!! ~~")

print("===" * 30)
vowels = "aeiou"
for v in vowels:  # a string is an iterable
    print(v)

print("===" * 30)
# other iterables: list, set, tuples
vowels = "aeiou"
sentence = "Seize the day!"
for char in sentence:
    if char in vowels:
        print(char)



