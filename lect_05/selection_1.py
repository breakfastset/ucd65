# 1. if only (apply only if matters)
amount = 499.90
is_member = False
if is_member:
    amount = 0.9 * amount   # 10% discount

print(f"Please pay ${amount:.2f}")

# 2. if - else (2 different pathways)
age = 18
if age >= 21:
    print("You are an adult!")
else:
    print("Hi Kid!")
    print("Bye")
