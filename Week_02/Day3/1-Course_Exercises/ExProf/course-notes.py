from collections import namedtuple

# Define a dictionary

user_a = { 'first_name': 'Bob',
          'last_name': 'Smith',
          'email': 'bob@gmail.com',
          'age': 50,
          'hobbies': ['painting', 'tenis', 'quitar', 'coding'],
          'pets':[('Rufus', 'dog'), ('Lola', 'cat')]
}

# Acessing data
print(user_a['email'])
print(user_a['age'])
print(user_a['hobbies'])

# Dictionaries And Lists
print(user_a['pets'][1][0])

# Modify An Entry In A Dictionary
user_a['last_name'] = 'Ross'
print(user_a)

# Adding An Entry To An Existing Dictionary
user_a['hair_color']= 'white'
print(user_a)

# Delete An Entry In A Dictionary
del user_a['hair_color']
print(user_a)

# The "in" keyword
print('Bob' in user_a.values())
print('first_name' in user_a)

if 'pets' in user_a:
    for each_pet in user_a['pets']:
        print(each_pet)
# 1st loop print user_a['pets][0]
# 1st loop print user_a['pets][1]

# Built-In Methods
print(user_a.values())
print(user_a.keys())
print(user_a.items())

new_entry = {'gender': 'M'}
user_a.update(new_entry)
print(user_a)

for key, value in user_a.items():
    print(f'key: {key} --> value {value}')

# ------------------------ Advenced topics -------------------------

# Enumerate Operator
for key, value in enumerate('ABC'):
    print(key, value)

# ZIP
list_users = ['Bob', 'John', 'Carol']
list_ages = [30, 15, 10]
list_cities = ['Tel Aviv', 'Moscow', 'New York']

users = list(zip(list_users, list_ages, list_cities))
print(users)

# USEFULL BONUS: namedtuple
infoUsers = namedtuple('User', ['name', 'age', 'city']) # using the module that we imported in the top of the file

users_info = []
for name, age, city in users:
    users_info.append(infoUsers(name, age, city))

# print(users_info)

# List Comprehension
my_numbers = [1,2,3,4,5,6,7,8,9]
my_list = []

for num in my_numbers:
        my_list.append(num)
print(my_list)

my_list = [num for num in my_numbers if num % 2 == 0]
print(my_list)








