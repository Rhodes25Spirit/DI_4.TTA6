def name_of_function():
    '''Prints str:hello'''
    print(f'hello')

name_of_function()

def say_hello(name):
    '''Prints str:hello'''
    print(f'hello {name}')

# calling the function
# say_hello('Donald')
# say_hello('Anna')

def say_hello(name = 'John Doe', language = 'EN')-> str:
    '''Prints str:hello to a specified name in a specified language'''
    if language == 'EN':
       gretting = f'Hello {name}'
    elif language == 'RU':
        gretting =f'Privet {name}'
    elif language == 'EN':
        gretting =f'Hello {name}'
    else: gretting ='Sorry, this function doesn`t support this language'

    return gretting

say_hello('Olga', 'RU') #positional arguments
say_hello(name = 'Olga', language = 'EN') #keywords arguments
print(type(say_hello()))

# Local And Global Scope

# global scope
count = 10
def calculation(a,b):
    # local scope
    count = 5
    result = a + b
    count += result
    return count

print(calculation(2,5))
print(count)

# global scope
count = 10
def calculation(a,b):
    # local scope
    global count #using the 'global' keyword you can modify the variable inside the function
    result = a + b
    count += result
    return count

print(calculation(2,5))
print(count)

# Returning More Than One Value With A Tuple
country = ('Moscow', 'Russia')
capital, name = country
print(f'{capital} is the capital of {name}')

def country_info(name)->tuple:
    if name == 'Brazil':
        capital = 'Brazilia'
        population = 214000000
    if name == 'Israel':
        capital = 'Jerusalem'
        population = 9000000
    return (capital, population)

capital, population = country_info('Brazil')
print(f'The capital of Brazil is {capital}, and the population is {population}')




        




