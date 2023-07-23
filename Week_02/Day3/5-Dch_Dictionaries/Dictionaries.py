# ___________________Challenge 1_____________________

userword = input("Enter a word: ")

valid = True
for char in userword:
    if char.isalpha() == False:
        valid = False
        break
    else:
        valid = True


def userworddict(userwordlist):
    from collections import defaultdict

    userworddict = defaultdict(list)
   
    for index, char in enumerate(userwordlist):
        userworddict[char].append(index)

    userworddict = dict(userworddict)

    print(userworddict)


if valid == True:
    userwordlist = [*(userword)]
    userworddict(userwordlist)
else:
    print("Invalid input")
    exit()

# ___________________Challenge 2_____________________

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}

wallet = "$300"

def value(currency):
    import re

    value = re.findall(
        "[0-9]+", currency
    )  # removes the $ from the wallet value and returns an int
    value = "".join(value)  # joins the list into a string
    intvalue = int(value)  # converts the string to an int
    return intvalue


# print(value(wallet))

value_of_item = items_purchase.values()

int_value_of_item = []

# print(value_of_item)

for item in value_of_item:
    int_value_of_item.append(value(item))

# print(int_value_of_item)

what_can_i_afford = []

for itemcheck in int_value_of_item:
    if itemcheck <= value(wallet):
        what_can_i_afford.append(itemcheck)

# print(what_can_i_afford)

name_of_whats_affordable = []

for key, item in items_purchase.items():
    name_of_whats_affordable.append(key)

# print(name_of_whats_affordable)

name_of_whats_affordable = sorted(name_of_whats_affordable)

if name_of_whats_affordable == []:
    print("Nothing")

print(name_of_whats_affordable)