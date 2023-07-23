# __________________________
# EX1

# __________________________
# EX2

# __________________________
# EX3

# >>> 3 <= 3 < 9                                  ans:
# >>> 3 == 3 == 3                                 ans:
# >>> bool(0)                                     ans:
# >>> bool(5 == "5")                              ans:
# >>> bool(4 == 4) == bool("4" == "4")            ans:
# >>> bool(bool(None))                            ans:

# x = (1 == True)
#     y = (1 == False)
#     a = True + 4
#     b = False + 10

#     print("x is", x)
#     print("y is", y)
#     print("a:", a)
#     print("b:", b)                              ans:
# __________________________
# EX4

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len(my_text))
#  ans: 445
# __________________________
#  EX5
no_A = input("Write the longest sentence without the character “A”.")
Verif = no_A.find("a")
if Verif == -1:
    print("BRAVO!")
else:
    print("TRY AGAIN!")
