seatings = [
    ["JJ", "J Chou", "Xin ru", "Momoa"],     # 0
    ["Rock", "Hogan", "Gaga", "Cindy"],      # 1
    ["Vivian", "Bala", "Anan", "Abigail"],   # 2
]   #  0         1        2       3

first_row = seatings[0]
print(first_row)
print(first_row[2])   # Xin ru

print(seatings[2][1])   # Bala

print()
for row in range(len(seatings)):
    for col in range(len(seatings[row])):
        print(seatings[row][col])

print()
print((len(seatings[0]) * 11 + 1) * "-")
for row in range(len(seatings)):
    for col in range(len(seatings[row])):
        print(f"|{seatings[row][col]:^10}", end="")
    print("|")
    print((len(seatings[row]) * 11 + 1) * "-")