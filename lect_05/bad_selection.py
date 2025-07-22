# 3. if - else if ... else
# used for mutually exclusive ranges / situations
marks = 85
if 80 <= marks <= 100:
    grade = "A"
if 60 <= marks < 80:
    grade = "B"
if 40 <= marks < 60:
    grade = "C"
if 0 <= marks < 40:
    grade = "U"

print(f"You got {grade} for {marks} marks")

# 4. nested if