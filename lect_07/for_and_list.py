fruit_list = ["apple", "orange", "pear", "guava", "papaya"]
# for each loop with list
for fruit in fruit_list:   # fruit is a copy of the element
    fruit = fruit.title()
    print(fruit)

print(fruit_list)
print("---" * 30)

# indexed for loop with list
for i in range(len(fruit_list)):
    fruit_list[i] = fruit_list[i] + "s"  # modify actual element
    print(fruit_list[i])
print(fruit_list)

print("---" * 30)
