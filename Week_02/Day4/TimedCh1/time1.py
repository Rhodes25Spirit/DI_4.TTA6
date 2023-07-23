string_input = "stringger"
char_input = "g"


def occ_count(string_input, char_input):
    count = 0
    for char in string_input:
        if char == char_input:
            count += 1
    return print(count)


occ_count(string_input, char_input)
