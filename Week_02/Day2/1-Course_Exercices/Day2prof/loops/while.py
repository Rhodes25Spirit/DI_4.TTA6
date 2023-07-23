# while condition :
#     do something

# while the condition is True
# enter the while loop
# as soon as the condition is False
# you go out of the while loop

number = 1

while number < 5 :
    number += 1
    print(number)

# 1st 
# number = 1
# the condition is true, I enter the loop
# number = 2

# 2st 
# number = 2
# the condition is true, I enter the loop
# number = 3

# 3st 
# number = 3
# the condition is true, I enter the loop
# number = 4

# 4st 
# number = 4
# the condition is true, I enter the loop
# number = 5

# 5st 
# number = 5
# the condition is false, so I stop

# ---------------- infinite loop
# number = 1

# while number >= 1 :
#     number += 1
#     print(number)


# ----------------------- infinite loop
# while True :
#     print("hello")

#  BREAK

number = 1

while True :
    if number < 5 :
        number += 1
        print(number)
    else :
        print("stop")
        break #break out of the loop

bank_amount = 10200
computer_price = 2000
counter = 0

while bank_amount >= computer_price :
    print("in the while")
    bank_amount -= computer_price
    counter += 1

print(f"I bought {counter} computers, I have {bank_amount} money left")

# NINJA YESTERDAY

word = ""
play_game = input("do you want to play")

while play_game != "quit" :
    user_word = input("give me a word").lower()
    if "a" in user_word :
        continue
    elif len(user_word) > len(word) :
        word = user_word
        print(f"congratulations, new record is {word}")
        play_game = input("do you want to play")
    else :
        continue
    