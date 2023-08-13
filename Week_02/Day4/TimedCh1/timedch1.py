# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.

# String: Programming is cool!
# Character: o
# 3

# You have 15 minutes to finish this challenge : time release 3:47

string_input = "Many a tale was told. Many a man has tried but few men have succeeded."
char_input = "a"


def occ_count(string_input, char_input):
    count = 0
    for char in string_input:
        if char == char_input:
            count += 1
    return print(count)


occ_count(string_input, char_input)
