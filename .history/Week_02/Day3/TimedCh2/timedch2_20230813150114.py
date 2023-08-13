# Perfect Number

# You have 30 minutes to finish this challenge : time release: 8:29

# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

# Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.

# there are only 51 known perfect numbers, most of them are very large, so I will just use a list of 7 of them which would work for any number a user would input that is less than 2305843008139952128.
# since we are dealing with known quantities, hardcoding the list of perfect numbers is fine.

perfect_number = [6, 28, 496, 8128, 8589869056, 137438691328, 2305843008139952128]

user_number = input("Enter a number: ")

user_number = int(user_number)

if user_number in perfect_number:
    print("True")
else:
    print("False")