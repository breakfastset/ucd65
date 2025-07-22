name = "Kali"
height = 1.84
weight = 75
bmi = weight / height / height

# Kali weighs 75kg and stands at 1.84m and his bmi is 22.153

# using commas ,
print(name, "weighs", weight, "kg and stands at", height, "m and his bmi is", bmi)

# using plus +
print(name + " weighs " + str(weight) + "kg and stands at " + str(height) +
      "m and his bmi is " + str(bmi))

# using .format()
print("{} weighs {}kg and stands at {}m and his bmi is {:.3f}".format(name, weight, height, bmi))

# using f""
print(f"{name} weighs {weight}kg and stands at {height}m and his bmi is {bmi:.3f}")