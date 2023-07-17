# MEMORY

colors = ["blue", "red", "yellow"]
fav_colors = colors

print("fav_colors : ", fav_colors, "colors : ", colors)
print(id(fav_colors) == id(colors)) #same

fav_colors.append("black")

print("fav_colors : ", fav_colors, "colors : ", colors)
print(id(fav_colors) == id(colors)) # same

# SLICING

fruits = ["apple", "banana", "pear"]
my_fruits = fruits[0:2] #last index not included
print(my_fruits) #['apple', 'banana']
print(fruits) #['apple', 'banana', 'pear']

fruits_second = ["apple", "banana", "pear", "melon", "apple"]
my_fruits_second = fruits_second[2:5] #last index not included
print(my_fruits_second) #['pear', 'melon', 'apple']
my_fruits_third = fruits_second[2:len(fruits_second)] #last index not included
print(my_fruits_third) #['pear', 'melon', 'apple']

my_fruits_fourth = fruits_second[2:] #to the end
print(my_fruits_fourth) #['pear', 'melon', 'apple']

my_fruits_fifth = fruits_second[:] #from the begining to the end
print(my_fruits_fifth) #["apple", "banana", "pear", "melon", "apple"]

colors_two = ["blue", "red", "yellow"]
fav_colors_two = colors_two[:]

print("fav_colors_two : ", fav_colors_two, "colors_two : ", colors_two)
print(id(fav_colors_two) == id(colors_two))

fav_colors_two.append("black")

print("fav_colors_two : ", fav_colors_two, "colors_two : ", colors_two)
print(id(fav_colors_two) == id(colors_two))