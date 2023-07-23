# list of 15 numbers
# if the numbers is odd --> the number ... is odd
# if the numbers is even --> the number ... is even

for num in range(0, 15):
    if num % 2 == 0:
        print(f"the number {num} is even (pair)")
else:
    print(f"the number{num} is odd (impair)\n\n")

for n2um in range(0, 16):
    if n2um % 2 == 0:
        result = "even (pair)"
    else:
        result = "odd (impair)"

    print(f"The n2umber {n2um} is {result}")

# Exercice:
# Accept a number from the user and print its multiplication table

user_num = int(input("choos a digit\n"))
for i in range(1, 16):
    print(user_num, "x", i, "=", user_num*i)

# Exercice:
# Print the numbers from 1 to 10 using while loop
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1
print("Finished")
