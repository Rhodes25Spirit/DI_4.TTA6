matrix = [
    [7, ' ', 3], #row1
    ['T','s','i'], 
    ['h','%','x'], 
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['i', 'r', '!']
]

for column in matrix:
    column0 = [column[0] for column in matrix]
    column1 = [column[1] for column in matrix]
    column2 = [column[2] for column in matrix]

message = []

# check if it is a letter and append, skip if not
# decode the message

def check_if_letter(some_list):
    for element in some_list:
        if isinstance(element, str):
            message.append(element)
        elif isinstance(element, int):
            continue

check_if_letter(column0)
check_if_letter(column1)
check_if_letter(column2)
print(message)

def decode_message(message):
    final_message = ''
    for char in message:
        if char.isalpha():
            final_message += char
        elif char == ' ':
            continue
        else:
            final_message += ' '
    return final_message


decoded_matrix = decode_message(message)
final_message = decoded_matrix.replace(' i', 'i')
print(final_message)

    







# print(column0)