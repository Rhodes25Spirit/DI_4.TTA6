matrix = [
    ["7", "i", "3"],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"],
]

first_column_words = list(map(lambda x: x[0], matrix))
Only_letters_col1 = list(filter(lambda x: x.isalpha(), first_column_words))
second_column_words = list(map(lambda x: x[1], matrix))
Only_letters_col2 = list(filter(lambda x: x.isalpha(), second_column_words))
third_column_words = list(map(lambda x: x[2], matrix))
Only_letters_col3 = list(filter(lambda x: x.isalpha(), third_column_words))

Decoded_text = (
    "".join(Only_letters_col1)
    + " "
    + " ".join(Only_letters_col2)
    + " "
    + " ".join(Only_letters_col3)
)

print(Decoded_text)
