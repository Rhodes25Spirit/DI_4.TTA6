# colors = ["blue", "red", "yellow"]

# manipulate them
# add elements to a list, delete, update
# methods

# my_list = ["a", 1, True, [1,2,3]] #nested list

colors = ["blue", "red", "yellow"] #ordered
first_color = colors[0]
print(first_color)

elements = ["blue", "red", "yellow", ["apple", "pear"]]
fruit_element = elements[3][1]
print(fruit_element) #"pear"

# elements = [
#     "blue", 
#     "red", 
#     "yellow", 
#     ["apple", "pear"]
# ]

fav_colors = ["blue", "red", "yellow"]
last_element = fav_colors[-1] #same
# index -1 : always the last element
print(last_element) # yellow

last_element_second= fav_colors[len(fav_colors)-1] #same
                    # fav_colors[3-1]
                    # fav_colors[2]
                    # yellow which is the last element of the list
print(last_element_second) # yellow

names = ["John", "Tom", "Lea", "Lysa"]

# add to the end of the list --> append method

names.append("Sarah")
print(names) #['John', 'Tom', 'Lea', 'Lysa', 'Sarah']

names.insert(1, "Albert") #between "John" amd "Tom"
print(names) #['John', 'Tom', 'Lea', 'Lysa', 'Sarah']
# ['John', 'Albert', 'Tom', 'Lea', 'Lysa', 'Sarah']

names.insert(-1, "Lola") #add before the last element
print(names) #['John', 'Albert', 'Tom', 'Lea', 'Lysa', 'Lola', 'Sarah']

names.insert(len(names), "Jade") #add at the end of the list
print(names) #['John', 'Albert', 'Tom', 'Lea', 'Lysa', 'Lola', 'Sarah', 'Jade']


# ask the user for a position and a color, 
# separated by a dash
# "2-blue"
# use the position to insert the color into the all_colors list

all_colors = ["red", "blue", "yellow"]

user_answer = input("Give me a number and a color divided by a dash \n")
# "1-green"
list_answer = user_answer.split("-")
# ["1", "green"]
print("list_answer", list_answer)

all_colors.insert(int(list_answer[0]), list_answer[1])

# # all_colors.insert(int("1"), "green")
# # all_colors.insert(1, "green")

print(all_colors)


my_colors = ["red", "blue", "yellow"]
my_colors[1] = "pink"
print(my_colors) #['red', 'pink', 'yellow']

# delete elements from a list
animals = ["horse", "cat", "dog"]
animals.pop() #delete the last element
print(animals) # ['horse', 'cat']
animals.pop(0) #delete the element at the specific position
print(animals) # ['cat']


all_animals = ["horse", "cat", "dog", "horse"]
animal_removed = all_animals.remove("horse") #remove the first horse
print(animal_removed) #None
print(all_animals) #['cat', 'dog', 'horse']

my_animals = ["horse", "cat", "dog"]
deleted_animal = my_animals.pop(1)
print(f"the animal deleted was a {deleted_animal}")
#the animal deleted was a cat

# my_animals.pop(10) #error no position 10
# my_animals.remove("hamster") #ValueError: list.remove(x): x not in list


