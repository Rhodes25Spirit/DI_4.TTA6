def name_fct():  # def = definition de la fonction
    # auto index
    '''Prints str:hello'''
#     print("Hello")


# name_fct()

# # call the fonction

# print(name_fct.__doc__)  # Ecrit ce quil y a entre les 3 guillemets.

# # ____________________

# def say_hello(name):
#     '''Prints  Hello and name'''
#     print(f"Hello{name}")
# # call the fonction
# say_hello("Mickey")
# say_hello("Donald")

# # call the fonction
# say_hello("Mickey")
# say_hello("Donald")

# def say_hello_lg(name, language):
#     '''Prints  Hello and name in different language'''

#     if language == "EN":
#         print(f"Hello {name}")
#     elif language == "RU":
#         print(f"Hello {name}")
#     elif language == "FR":
#         print(f"Hello {name}")
#     else:
#         print("Sorry, this fonction doesn't support this language")

# say_hello_lg("olga,"RU")
#                     # posotional arguments
# say_hello_lg("Olga,language = "EN")
#                     #keyword


# def say_hello_lg2(name = " ", language):
#     '''Prints  Hello and name in different language'''

#     if language == "EN":
#         print(f"Hello {name}")
#     elif language == "RU":
#         print(f"Privet {name}")
#     elif language == "FR":
#         print(f"Salut {name}")
#     else:
#         print("Sorry, this fonction doesn't support this language")

# say_hello_lg2("olga,"RU")
#                     # posotional arguments
# say_hello_lg2("Olga,language = "EN")
#                     #keyword


### GLOBAL###
# count = 10


# def calculation(a, b) -> None:
#     '''action number_a + number_b'''

#     result = a + b
#     count = 10
#     count += result
#     return result  # OR return print(result)


# res = calculation(40, 10)
# print(res)
# print(count)
# pass


# Returning more than one value with a tuple
my_tuple = ("jimi", "hendrix")
first_name, last_name = my_tuple


def format_name(first_name, last_name) -> str:
    return (first_name.title(), last_name.title())


first, last = format_name("RICk", "mORTY")
print(first)
print(last)
print("First name is: " + first_name.capitalize)
print("Last name is: " + last_name.upper)
