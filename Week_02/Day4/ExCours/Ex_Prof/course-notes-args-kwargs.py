

def user_info(*names:tuple, **details: dict)->dict:
    user_info = {}
    for name in names:
        user_info[name] = details
    return user_info

print(user_info('Juliana', 'Lise', 'Avner', work = 'Developers Institute', city = 'Ramat Gan', hobbie = 'coding'))

# output
{'Juliana': {
    'work': 'Developers Institute', 
    'city': 'Ramat Gan', 'hobbie': 'coding'
    }, 
'Lise': {
    'work': 'Developers Institute', 
    'city': 'Ramat Gan', 
    'hobbie': 'coding'
    }, 
'Avner': {
    'work': 'Developers Institute', 
    'city': 'Ramat Gan', 
    'hobbie': 'coding'
    }
}