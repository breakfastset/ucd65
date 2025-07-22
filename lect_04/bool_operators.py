
age = 23
citizenship = "Antarctica"

# and condition -> all must be True to be True
can_vote = (age >= 21 and citizenship == "Singaporean")

print(f"Eligible to vote? {can_vote}")

print()

# or condition -> as long as satisfy one of the criteria -> True
num_points = 70
is_school_team_player = False
eligible_to_admit = (num_points >= 60 or is_school_team_player == True)

print(f"Can admit to school? {eligible_to_admit}")

# not is to negate
age = 20
print("Person is not older than 21: ", (not (age > 21)))

print("Person is not older than 21: ", (age <= 21))

