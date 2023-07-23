# some_list = ["Olga", "Alex", "Lisa"]
# print(some_list)


# some_dict = {"Olga": "email@gmail.com", "Alex": "alex@gmail.com", "Lisa": "Lisa@gmail.com"}

# user_a = {"firstname":"Bob",
#         "lastname":"Smith",
#         "gender":"undefined", 
#         "Email":"BobS@gmail.com",
#         "age":59,
#         "hobbies":["painting", "tennis", "guitar", "coding"],
#         "pets":[("Rufus","dog"),("Lola","bird"),("Inook","cat")]}

# print(user_a["Email"])
# print(user_a["age"])
# print(user_a["hobbies"])
# print(user_a["pets"][1][0])

# # EX   Access the value of key "history"

# sample_dict = { 
# "class":{ 
# "student": {
# "name": "Mike",
# "marks": {"physics": 70, "history": 80}}}}

# # print("The history note of Mike is:", class['student[Mike]'])


# user_a["lastname"] = "Sanchez"
# print(user_a)

# user_a["haircolor"]= "almost white"
# print(user_a)

# del user_a["gender"]
# print(user_a)


# print("Bob" in user_a.values())
# print("Bob@gmail.com" in user_a.values())
# print ("age" in user_a)

# print(user_a.values)

# if "pets" in user_a:
#     for each_pet in user_a["pets"]:
#         print(each_pet)

# # print(user_a.values)
# # print(user_a.keys)
# # print(user_a.items)

# nw_entry = {"favcolor": "orange"}

# print(user_a)

# # Exercise: Delete set of keys from Python Dictionary

# sample_dict2 = {
# "name": "Kelly",
# "age":25,
# "salary": 8000,
# "city": "New york"}
# print(sample_dict2)

# del sample_dict2["name"] 
# print(sample_dict2)

# del sample_dict2["salary"] 
# print(sample_dict2)

#___________________Advanced List, Dictionaries and Loops____________
#___For Loops and dictionaries____
# my_books = {
# "title": "Harry Potter",
# "author": "JK Rowling",
# }
#___Loops Operator______
# for x, y in my_books.items(): 
#     print("The " + x + " is " + y)

# print(list(range(2, 13, 2))) #range(start, stop , step)

# for item in enumerate('abcdef'): # Syntax : (index , value)
#     print(item)
# for (index_count, letter) in enumerate('abcd'):
#     print('At index {} the letter is {}'.format(index_count, letter.upper()))

# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# list3 = [10.1, 10.2, 10.3, 10.4, 10.5]

# for item2 in zip(list1, list2, list3): # only go as far it is possible
#     print(item2)


# list1a = [9,2,15,19,35]
# list2a = ['Alex','Bob','Carol','Dany','Elly']
# list3a = ["IL,", "US", "FR", "IT", "DK"]

# for item3 in zip(list1a, list2a, list3a): # only go as far it is possible
#     print(item3)

# list1a = ['Alex','Bob','Carol','Dany','Elly']
# list2a = [9,2,15,19, ]
# list3a = ["IL,", "US", "", "", "DK"]

# for item3 in zip(list1a, list2a, list3a): # only go as far it is possible
#     print(item3)

#!!!!NAMETUPLE!!!! module to import

#____FOR ELSE_____


# #____Break, Continue, Pass_____
# for letter in 'Leonardo':
#         if letter == 'a':
#                 break
#         print(letter, end='') # end='' renders each letter next to the other
#         print(letter, end='\n') # end='\n' renders each letter under to the other


#___List Comprehension: quickly way to creating a list____
#__The basic way of appending an element into a list___
my_number = '146523'
my_list = []

# # # How to translate str into int or inverse w/out changing Hardcode?
                # my_number_int = int(my_number)
                # print(my_number_int)
                # my_number_str = str(my_number)
                # print(my_number_str)

#or num in my_number:
# my_list.append(num)    #instead of for num in my_number: print(my-list)
#rint(my_list)