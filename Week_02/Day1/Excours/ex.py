# EX1_____________________________________________________________________

# name = 'John Doe'
# if len(name)>20:
#     print(f'Name "{name}" is more than 20 chars long')
#     length_description = 'long'
# elif ____:
#     print(f'Name "{name}" is more than 15 chars long')
#     length_description = 'semi long'
# elif ____:
#     print(f'Name "{name}" is more than 10 chars long')
#     length_description = 'semi long'
# elif ____:
#     print(f'Name "{name}" is 8, 9 or 10 chars long')
#     length_description = 'semi short'
# else:
#     print(f'Name "{name}" is a short name')
#     length_description = 'short'

# EX2________________________________________________________________


# Here is a table of prices for a wedding catering company:
#             Up to 50 people	      $4,000
#             Up to 100 people        $10,000
#             Up to 200 people	      $15,000
#             More than 200 people	  $20,000
#
# 📝 Instructions:
# Please write an program that prompts the user for the number of people attending their wedding and prints the corresponding price in the console.
# For example, if the user says that 20 people are attending to the wedding, it must cost $4,000 dollars.
number_people = int(input("How many guest at the wedding?\n"))

if number_people > 200:  # [201 et +]
    print("the wedding will coast $20.000")
elif 100 < number_people <= 200:  # [101-200]
    print("the wedding will coast $15.000")
elif 50 < number_people <= 100:  # [51-100]
    print("the wedding will coast $10.000")
elif 0 < number_people <= 50:  # [0-50]
    print("the wedding will coast $4.000")
