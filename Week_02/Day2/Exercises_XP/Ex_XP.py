# # EX1:

# set_A = set({13, 9, 555, 666})
# # set_A.add("13")
# # set_A.add("9")
# # set_A.add("555")
# # set_A.add("666")
# print(set_A)
# set_A.add("589")
# set_A.add("991")
# print(set_A)
# # Delete the last number: impossible because it is a set
# friend_fav_numbers = set({78, 96, 5412, 6589, 687})
# print(friend_fav_numbers)
# # Concatenate the last number: impossible because it is a set
# friend_fav_list = list(friend_fav_numbers)
# list_A = list(set_A)
# list_combi = list_A + friend_fav_list
# print(list_combi)

# ______________________
# # EX2:

# tuple_A = (88, 99, 1111)
# #  is it possible to add more integers to the tuple
# # ans: Not Tuple is immuable

# ______________________
# EX3:

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# # print(basket)
# basket.remove("Banana")
# # print(basket)
# basket.remove("Blueberries")
# # print(basket)
# basket.append("Kiwi")
# # print(basket)
# basket.insert(0, "Apples")
# # print(basket)
# appels = basket.count("Apples")
# # print(appels)
# basket.clear()
# print(basket)

# ______________________
# EX4:

# ans: Float decimal number, integer is a whole number or digit
# ans: The Python range() works only with integers. It doesn’t support the float type or with "numpy module"
# stt = float(1)
# seq_1 = stt + 1
# for seq_1 in stt + 0.5:  # TypeError: 'float' object is not iterable
#     print(seq_1)

# ______________________
# EX5:
# nbrs = range(1, 21)
# for num in nbrs:
#     print(num)

# for num, dig in enumerate(nbrs):
#     if num % 2 == 0:
#         print(dig)

# ______________________
# EX6:
# user_proposition = input("What is my name?\n")
# while user_proposition != "spirit":
#     user_proposition = input('Again, what is my name?\n ')
# print("BRAVO!")

# ______________________
# EX7:
# fruits_fav = input("Write 3 fruits, separated by a space\n")
# fruit_list = fruits_fav.split(" ")
# print(fruit_list)
# user_fruit = input("Choose 1 fruit\n")

# if user_fruit in fruit_list:
#     print("Bon Appetit")
# else:
#     print("you choose a new one, try it...")

# ______________________
# EX8:
top_ping = input("Add toppings\n")
topping_count = 0
while top_ping != "quit":
    top_ping = input("Add your toppings or if you have finish, write: 'quit'\n")
    print("we will add to your pizza ")
    topping_count = topping_count + 1

totalprice = 10 + (2.5 * topping_count)
print(f"You add {topping_count} toppings and the total price is {totalprice} ")

# ______________________
# EX9:

# family = input(
#     "Enter the age of each person who needs ticket, separated by a space\n")
# family = family.split(" ")
# list_family = list(family)
# print(list_family)

# price = []
# print(len(family))
# ## convert family_list  into integrer
# for age in family:
#     if age < 3:
#         price.append(0)
#     elif 3 <= age <= 12:
#         price.append(10)
#     elif age > 12:
#         price.append(15)

# print(f"For you cinema entrance you will pay:" (sum(price)))


# ______________________
# EX10:

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich",
                   "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

print("Deli has run out of pastrami.")
print(sandwich_orders)
finished_sandwichs = []

for sand in sandwich_orders:  # 1st loop
    sandwich_orders.pop(1)
    finished_sandwichs.append(sand)

for sandfin in finished_sandwichs:
    print(f"your {sandfin} is ready.")

# Why only 2 sandwiches (Tuna and Egg) move from sandwich_orders to the finished_sandwichs ? I would like to have a loop of the 1st loop.

print(sandwich_orders)
print(finished_sandwichs)
