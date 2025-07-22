
price = 23.45
product = "Lego"

print(f"|{price:10}|")   # numbers align to the right

print(f"|{product:10}|")  # strings align to the left
print(f"|{product:>10}|")  # align to the right
print(f"|{product:^10}|")  # align to the center  (circum accent, caret)

print(f"|{price:10.1f}|")
print(f"|{price:010.1f}|")  # fill up with 0s for empty spaces

print()
print()

header = "{:=^40}"
row = "| {:10} | {:10} | ${:9.2f} |"
bottom = "=" * 40

print(header.format(" Sales "))
print(row.format("Oranges", 10, 1.71))
print(row.format("Apples", 20, 1.50))
print(row.format("Eggs", 20, 0.80))
print(bottom)







