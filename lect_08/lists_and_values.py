age = 16
age2 = age
print(f"age  {id(age)} : {age}")
print(f"age2 {id(age2)} : {age2}")

age = 20
print()
print(f"age  {id(age)} : {age}")
print(f"age2 {id(age2)} : {age2}")

print()
items = ["bobo", "chacha"]
items2 = items
print(f"items  {id(items)} : {items}")
print(f"items2 {id(items2)} : {items2}")

print()
items[0] = "Bubu"
print(f"items  {id(items)} : {items}")
print(f"items2 {id(items2)} : {items2}")

print()
items2 = list(items)   # a copy
items3 = items[:]      # a copy
items4 = [item for item in items] # a copy
items2[0] = "Momo"
items3[1] = "Baba"
items4[0] = "Little"
print(f"items  {id(items)} : {items}")
print(f"items2 {id(items2)} : {items2}")
print(f"items3 {id(items3)} : {items3}")
print(f"items4 {id(items4)} : {items4}")
