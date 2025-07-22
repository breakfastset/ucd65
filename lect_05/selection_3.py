# 4. nested if
#    testing more than 1 condition that are mutually exclusive
#
age = 65
citizenship = "pr"
voucher_amount = 0

if age >= 65 and citizenship == "sg":
    voucher_amount = 800
elif age >= 65 and citizenship == "pr":
    voucher_amount = 500
elif age >= 40 and citizenship == "sg":
    voucher_amount = 600
elif age >= 40 and citizenship == "pr":
    voucher_amount = 300

print(f"You will get ${voucher_amount} worth of vouchers")
print("----------" * 5)

age = 65
citizenship = "sg"
voucher_amount = 0

if citizenship == "sg":
    if age >= 65:
        voucher_amount = 800
    elif age >= 40:
        voucher_amount = 600
elif citizenship == "pr":
    if age >= 65:
        voucher_amount = 500
    elif age >= 40:
        voucher_amount = 300
else:
    voucher_amount = 0

print(f"You will get ${voucher_amount} worth of vouchers")
print()

print("Hello how are you", end="")
print("Had your dinner?", end="")
print("Want to eat prata?")


