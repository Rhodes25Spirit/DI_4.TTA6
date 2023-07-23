#Exercise 1 : Convert lists into dictionaries
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# # for item in zip(keys, values): #here you just printed the tuples. to make it a dictionary you need dict()
# #     print(item)
# dict_result = dict(zip(keys, values))

# # Exercise 2 : Cinemax
# family = {"rick": 43, "beth": 13, "morty": 5, "summer": 8}
# ticket = 0

# for key, value in family.items():
#     if value < 3:
#         ticket += 0
#     elif value < 12:
#         ticket += 10
#     else:
#         ticket += 15

# print(f"The final price is ${ticket}")

# #Bonus

# ticket_count = 0
# family_dict = {}
# while True:
#     # family_inp = input("Next member or if you finish, write: 'quit'\n") # lets take names and ages separetate by spaces
#     family_inp = input("Enter member`s name and age separated by space, or if you finish, write: 'quit'\n")
#     if family_inp=="quit":
#         break
#         # ticket_count = ticket_count + 1 # this should be outside the if because you can't do anything after "break"
#     # ticket_count = ticket_count + 1  # you dont need this line here
#     # family_inp = family_inp.split(" ") #you don't need to specify an argument in split() if you want to split by space.
#     family_inp = family_inp.split()
#     family_dict.update({family_inp[0]:int(family_inp[1])})

# for key, value in family_dict.items():
#     if value < 3:
#         # ticket_count += 0 # you don't need to increase if it is 0. just use "continue"
#         continue
#     elif 3 < value < 12:
#         ticket_count += 10
#     else:
#         ticket_count += 15

# print(family_dict)
# print(f"The final price is ${ticket_count}")


# Exercise 3: Zara
brand = {"name": "Zara",
        "creation_date": 1975, 
        "creator_name": "Amancio Ortega Gaona", 
        "type_of_clothes": ["men", "women", "children", "home"], "international_competitors": ["Gap", "H&M", "Benetton"], "number_stores": 7000, 
        "major_color":{"France": "blue", "Spain": "red", "US": ["pink", "green"]}}
    
# brand["number_stores"] = 2

clients = ", ".join(brand["type_of_clothes"])

print(f"Zara's clients are: {clients}")

# brand["country_creation"]= "Spain"

# brand_keys = brand.keys()
# if "international_competitors" in brand_keys:
#     brand["international_competitors"].append("Desigual")
#     print(brand)
# else:
#     print("international_competitors is not in the dictionary")

# del brand["creation_date"]
# print(brand)

# print(brand["international_competitors"][-1])

# print(brand["major_color"]["US"])

# length_dic = len(brand)
# print(length_dic)

# print(brand.keys())

# more_on_zara = {"creation_date": 1975, "number_stores": 10000}

# brand.update(more_on_zara)

# #Ans: the new value of number of stores is 10000.
# print(brand)


#Exercise 4 : Disney characters

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

users_A = dict(enumerate(users))
users_A = {v: k for k, v in users_A.items()}
print(f"users_A {users_A}")

users_B = {}
for i, v in enumerate(users):
    valuepush = {i: v}
    users_B.update(valuepush)
print(f"user_B {users_B}")

users_sorted = sorted(users)
users_C = dict(enumerate(users_sorted))
users_C = {v: k for k, v in users_C.items()}
print(f"users_C {users_C}")

# you are getting a different output than what the exercise is asking. Look again, remenber to use sort()
for letter_i_users in users:
    if "i" in letter_i_users:
        print(f"letter_i_users: {letter_i_users}")

for letter_mp_users in users:
    if letter_mp_users.lower().startswith("m") or letter_mp_users.lower().startswith("p"):
        print(f"letter_mp_users: {letter_mp_users}")