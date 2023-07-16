bank_amount = 10000
computer = 2000
phone = 500


# syntax
# if condition: what we want to do if the first condition is TRUE
# elif condition: what we want to do if the first condition is FALSE and the second is true
if bank_amount >= computer:
    print(f"I will buy computer")
elif bank_amount >= phone:
    print(f"I will buy phone")
else:
    print(f"I will buy a pen")
