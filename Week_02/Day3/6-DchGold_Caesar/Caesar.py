# Daily challenge GOLD: Caesar Cypher
uncryptedtext = "this is text to encrypt"

# make the aplphabet into a list
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = [*alphabet]

cryptedtext = ""
for letter in uncryptedtext:
    if letter.isalpha() == False:
        cryptedtext += letter
    else:
        # takes the letter, find its index in the aplphabet list, and then adds 3 to it then add it to the crytedtex string variable
        letterindex = alphabet.index(letter.lower())
        cryptedtext += alphabet[letterindex - 3]
print(cryptedtext)


cryptedtext2 = input("Please write the sentence to decode? \n")

cryptedtext2 = ""
for letter2 in cryptedtext2:
    if letter2.isalpha() == False:
        cryptedtext2 += letter2
    else:
        # takes the letter, find its index in the aplphabet list, and then remove 3 to it then add it to the crytedtex string variable
        letter2index = alphabet.index(letter2.lower())
        uncryptedtext2 += alphabet[letter2index + 3]
print(uncryptedtext2)

# Why the invert of the code doesnot work. Please some help.