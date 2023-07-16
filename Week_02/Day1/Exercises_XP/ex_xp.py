# EX1
# print("Hello\n"*4)

# _________________________________________

# EX2
# print((99*3)*8)
# print(99*3)
# print(297*8)

# _________________________________________

# EX3
# print(5 < 3)
# # ans: FALSE
# print(3 == 3)
# #ans: TRUE
# print(3 == "3")
# ans: FALSE
# print("3" > 3)
# #ans: ERROR
# print("Hello" == "hello")
# ans: FALSE

# _________________________________________

# # EX4
# computer_brand = "Acer"
# print(f"I have a {computer_brand} computer")

# _________________________________________

# # EX5
# name = "Anna"
# age = 36
# shoe_size = 38
# print(
#     f"My name is {name}, I am {age} years old and my shoe size is {shoe_size}.")

# _________________________________________

# EX6
# A = 98
# B = 54
# if A > B:
#     print("A is greater than B")

# _________________________________________

# EX7
# num = int(input("chosse a whole number \n"))
# if num % 2 == 0:
#     print("It is an odd number")
# else:
#     print("It is an even number")

# _________________________________________

# EX8
# name = input("What is your name? \n")
# if name == "Anna":
#     print("Call me by your name")
# else:
#     print(f"Nice to meet you {name}!!")

# _________________________________________

# EX9
height = float(input("What is your height in inches? \n"))
cm = 2.54
height_cm = round(height * cm, 0)
if height_cm >= 145:
    print("you are tall enough, go RIDE!")
else:
    print("Eat more soup")
