# 3. if - else if ... else
# used for mutually exclusive ranges / situations
marks = 85
if 80 <= marks <= 100:
    grade = "A"
elif 60 <= marks < 80:
    grade = "B"
elif 40 <= marks < 60:
    grade = "C"
else:
    grade = "U"

print(f"You got {grade} for {marks} marks")

