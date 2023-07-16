# syntax
# if condition :
#     what we want to do if the condition is true
# elif condition :
#     what we want to do if the first condition is false and the 
#     second one is True
# else :
#     if all of the above is false

bank_amount = 1000
computer_price = 2000
phone_price = 500

if bank_amount >= computer_price :
    print("I buy the computer")
elif bank_amount >= phone_price :
    print("I buy the phone") #here
else :
    print("I buy a pen")

print("end")


bank_amount = 10000

if bank_amount >= computer_price :
    # bank_amount = bank_amount - computer_price
    bank_amount -= computer_price
    print("I buy the computer")
    print(f"I have {bank_amount} left in the bank")

    # print("I have  " + bank_amount + " left in the bank")
elif bank_amount >= phone_price :
    bank_amount -= phone_price
    print("I buy the phone") 
    print(f"I have {bank_amount} left in the bank")
else :
    print("I buy a pen")

print("end")

height = 1.7
age = 15

if height >= 1.6 and age > 13 :
    print("you go to Disneyland") #here
else :
    print("you don't to Disneyland")

# age = 10

# both conditions need to be true
if height >= 1.6 and age > 13 :
    print("you go to Disneyland") 
else :
    print("you don't to Disneyland") #here

# at least one of the condition needs to be true
if height >= 1.6 or age > 13 :
    print("you go to Disneyland") #here
else :
    print("you don't to Disneyland")

height = 1.4

if height <= 1.6 and height >= 1.3 :
    print("you go to Disneyland") #here
else :
    print("you don't to Disneyland")

if 1.3 <= height <= 1.6 :
    print("you go to Disneyland") #here
else :
    print("you don't to Disneyland")


friend_age = 20

if friend_age > 30 :
    print("you are an adult")
else :
    print("you are a child")

if friend_age > 30 :
    print("you are an adult")
elif 25 <= friend_age <= 29 :
    print("you are almost an adult")
elif 20 <= friend_age <= 24 :
    print("you are almohdhdhdst an adult")
elif 20 <= friend_age <= 24 :
    print("you are --- an adult")
else :
    print("you are a child")

my_age = 45

if my_age > 30 :
    print("you are an adult")
elif 25 <= my_age <= 29 :
    print("you are almost an adult")
elif 20 <= my_age <= 24 :
    print("you are not a child")
else :
    print("you are a child")

print("end")

# all if statement ran

if my_age > 30 :
    print("you are an adult")

if my_age > 25 :
    print("you are almost an adult")

print("end")


#  EXERCISES

name = 'John Doe'
if len(name) > 20:
    print(f'Name "{name}" is more than 20 chars long')
    length_description = 'long'
elif 15 < len(name) < 20:
    print(f'Name "{name}" is more than 15 chars long')
    length_description = 'semi long'
elif 10 < len(name) < 15:
    print(f'Name "{name}" is more than 10 chars long')
    length_description = 'semi long'
elif 8 <= len(name) <= 10:
    print(f'Name "{name}" is 8, 9 or 10 chars long')
    length_description = 'semi short'
else:
    print(f'Name "{name}" is a short name')
    length_description = 'short'


name = 'John Doehhhhhyyy'
if len(name) > 20:
    print(f'Name "{name}" is more than 20 chars long')
    length_description = 'long'
elif len(name) > 15:
    print(f'Name "{name}" is more than 15 chars long')
    length_description = 'semi long'
elif len(name) > 10:
    print(f'Name "{name}" is more than 10 chars long')
    length_description = 'semi long'
elif 8 <= len(name) <= 10:
    print(f'Name "{name}" is 8, 9 or 10 chars long')
    length_description = 'semi short'
else:
    print(f'Name "{name}" is a short name')
    length_description = 'short'

# Here is a table of prices for a wedding catering company:

# of guests	price
# Up to 50 people	$4,000
# Up to 100 people	$10,000
# Up to 200 people	$15,000
# More than 200 people	$20,000

# 📝 Instructions:

# Please write an program that prompts the user 
# for the number of people attending their wedding and prints the corresponding price in the console.
# For example, if the user says that 20 people are attending to the wedding, it must cost $4,000 dollars.

# 2nd exercise

number_people = int(input("how many guests"))

if number_people > 200 :
    print("the wedding will cost $20000")
elif 100 < number_people <= 200 : #[101 - 200]
    print("the wedding will cost $15000")
elif 50 < number_people <= 100 :
    print("the wedding will cost $10000")
elif 0 <= number_people <= 50 : #[0 - 50]
    print("the wedding will cost $4000")

if number_people > 200 :
    print("the wedding will cost $20000")
elif number_people <= 200 and number_people > 100 : #[101 - 200]
    print("the wedding will cost $15000")
elif 50 < number_people <= 100 :
    print("the wedding will cost $10000")
elif 0 <= number_people <= 50 : #[0 - 50]
    print("the wedding will cost $4000")

if number_people > 200 :
    print("the wedding will cost $20000")
elif number_people > 100 : #[101 - 200]
    print("the wedding will cost $15000")
elif  number_people > 50 :
    print("the wedding will cost $10000")
elif  number_people > 0 : #[0 - 50]
    print("the wedding will cost $4000")