import random

## EX1______________________##

# def display_message():
#     print("I'm learning python")


# display_message()

# ## EX2______________________##


# def favorite_book(title):
#     print(f"One of my favorite books is {title.title()}")


# favorite_book("The secret")

# ## EX3______________________##


# def describe_city(city="Carthage", country="Tunisia"):
#     print(f"{city.title()} is in {country.title()} and it's one of Lost Cities Forgotten by Time")


# describe_city("Skara Brae", "main island of Orkney")

# describe_city()

## EX4______________________##


# def secretnum(num):

#     random_number = random.randint(1, 101)

#     if 1 < num < 100:
#         print("ERROR, please choose a number between 1 and 100")

#     if num == random_number:
#         print("You found the right number")
#     else:
#         print(f"You didn't found the number. The number was {random_number}")


# print(secretnum(52))
## EX5______________________##


# def make_shirt(txt="I love Python", size="Large"):
#     print(f"The size of the shirt is: {size}\n and the text is: {txt}")


# make_shirt()

# make_shirt(size="Medium")

# make_shirt(txt="I also like the green tree python")

## EX6______________________##

# magician_names = ["Harry Potter", "Norbert Dragonneau", "Quentin Coldwater"]


# def magiciens(args):
#     for arg in args:
#         print(arg)


# magiciens(magician_names)
# print("______________________")


# def make_great(args):
#     for arg in args:
#         index_of_args1 = args.index(arg)
#         args.pop(index_of_args1)
#         args.insert(index_of_args1, f"{arg}, the Great!")


# make_great(magician_names)
# magiciens(magician_names)

# EX7______________________## First part OK but do not understand to enter a fct into an other one.

def temp():
    temp_r = random.randint(-10, 40)  # temp_r = random.random(-10.0, 40.9)

    print(f"The temperature is {temp_r} degrees Celsius.")

    if temp_r <= 0:
        print("Brrr, it is freezing! Stay at home today with hot chocolate!")
    elif 0 < temp_r < 16:
        print("Quite chilly! Do not forget your coat")
    elif 16 <= temp_r <= 23:
        print("It is a nice day")
    elif 24 <= temp_r <= 30:
        print("It is a hot day")
    else:
        print("It is a very hot day. Don't forget to drink a lot!")


print(temp())
# _________________________________________

# user_season = input("Press enter to season: ")


# def main():
#     rand_temp = temp(user_season)
#     print(f"The temperature is {rand_temp} degrees Celsius.")


# print(main())


# def temp(season):

#     if season == "winter":
#         return random.randint(-10, 10)
#     elif season == "autumn":
#         return random.randint(10, 16)
#     elif season == "spring":
#         return random.randint(16, 25)
#     elif season == "summer":
#         return random.randint(26, 40)
#     else:
#         return 0


#

# print(temp())


## EX8___Star Wars________##
