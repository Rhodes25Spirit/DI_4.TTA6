# print("hello"*5)
#  for loop
# for varible in list :
#     do something

# list(range(0,5))
# [0, 1, 2, 3, 4] # 5 not included

for number in range(0,3) :
    print("hello : ", number)

# 1st loop
#     hello 0

# 2nd loop
#     hello 1

# 3rd loop
#     hello 2

colors = ["blue", "red", "yellow"]

for color in colors :
    print(color)

# 1st loop
#     color : blue

# 2nd loop
#     color : red

# 3rd loop
#     color : red

# loop through 
# list of 15 numbers
# if the number is odd --> the number -- is odd
# if the number is even --> the number -- is even

for num in range(0,15):
    if num % 2 == 0 :
        print(f"The number {num} is even")
    else :
        print(f"The number {num} is odd")

for num in range(0,16):
    if num % 2 == 0 :
        result = "even"
    else :
        result = "odd"

    print(f"The number {num} is {result}")

# DAILY CHALLENGE

user_answer = input("give me a word")
lenght_word = len(user_answer)

if lenght_word < 10 :
    print("string not long enough")
elif lenght_word > 10 :
    print("string too long")
elif lenght_word == 10 :
    print("string good")

print("first :", user_answer[0])
print("last :", user_answer[-1])

sentence = ""

# loop by letter
for letter in "HelloWorld" : #HelloWorld
    sentence = sentence + letter
    print(sentence)

# 1st loop
#     letter : H
#     sentence = "" + "H"
#     sentence = "H"

# 2nd loop
#     letter : e
#     sentence = "H" + "e" 
#     sentence = "He"

# 3rd loop
#     letter : l
#     sentence = "He" + "l" 
#     sentence = "Hel"

# loop by index
# for x in range(len(user_answer)) :
#     print(user_answer[:x+1])
