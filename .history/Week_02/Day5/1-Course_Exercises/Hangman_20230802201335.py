import random

# generate a random word

computer_word = random.choice(
    [
        "correction",
        "childish",
        "beach",
        "python",
        "assertive",
        "interference",
        "complete",
        "share",
        "credit",
        "rush",
        "south",
    ]
)

print(computer_word)

list_letter = [*(computer_word)]

# replace the letters with stars

list_stars = ["*" for letter in list_letter]

stars_for_print = " ".join(list_stars)

print(stars_for_print)

# game

for i in range(15):
    guess_letter = input("Guess a letter: ")

    if guess_letter in list_letter:
        for letter in list_letter:
            if letter == guess_letter:
                list_stars[list_letter.index(letter)] = letter
                list_letter[list_letter.index(letter)] = "*"
                stars_for_print = " ".join(list_stars)
                print(stars_for_print)

    else:
        print("You died")
        i += 1

    if "*" not in list_stars:
        print("You win!")
        break