# Daily Challenge 1

# user_numb = int(input("Choose a number:\n"))
# user_length = int(input("choose a length\n"))

# count_len = 0
# usernumber = 0
# usernumberlist = []

# while count_len < user_length:
#     usernumber = user_numb + usernumber
#     usernumberlist.append(int(usernumber))
#     count_len = count_len + 1

# print(usernumberlist)

# usernumber = usernumber == 0


# _____________________________________________________________
# Daily Challenge 2

stringlist = [*(input("Enter a word:\n"))]
# find something on the Internet but don't understand why: [*(input....?
result = []
last_char = []
for char in stringlist:
    if char != last_char:
        result += char
        last_char = char

fullword = "".join(result)
print(fullword)
