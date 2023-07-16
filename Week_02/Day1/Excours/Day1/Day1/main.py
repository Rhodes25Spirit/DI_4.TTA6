print("hello") # display hello

# Variables
username = "John"
my_friend_age = 12
myFriend = 13

user = "Tom"
hobby = "football"
print("user")
print(user)

# print("Tom plays football")

sentence = user + " plays " + hobby
print(sentence)

city = "TLV"
temperature = 39

# todays_weather = "In " + city + " the weather is " + temperature
# print(todays_weather) #error

todays_weather_second = f"In {city} the weather is {temperature}"
print(todays_weather_second)

todays_weather_third = f"In {city} the weather is {temperature+10}"
print(todays_weather_third)

# METHODS

current_city = "tlv"
current_user = "TlV" #TLV tLV

print(current_city == current_user.lower())

city_two = "tlv"
user_answer = input("where do you live ?") #TLV
print(user_answer)

print(city_two == user_answer.lower())

sentence = "hello world how are you"
sentence_list = sentence.split() #by default if you want to split by space 
#  ['hello', 'world', 'how', 'are', 'you']
print("sentence : ", sentence, "\n list :", sentence_list)

sentence_second = "hello,world,how,are,you"
sentence_list_second = sentence_second.split(",")
#  ['hello', 'world', 'how', 'are', 'you']
print(sentence_second, sentence_list_second)



# split method of strings that creates a list out of a string
sentence_test = "Hello World Python"


# >>> "hello world python".split(" ")
# ['hello', 'world', 'python']
# >>> "hello+world+python".split("+")
# ['hello', 'world', 'python']
# >>> "hellowordopythono".split("o")
# ['hell', 'w', 'rd', 'pyth', 'n', '']
# list("hello")
# ['h', 'e', 'l', 'l', 'o'] #list of characters

# Length and positions

user_word = "hello"
# the game is to always find the last letter of the word
last_letter_index = len(user_word) - 1
last_letter = user_word[last_letter_index]
            # user_word[5-1]
            # user_word[4]

user_word_second = input("give me a word \n")
last_letter_index_second = len(user_word) - 1
last_letter_second = user_word[last_letter_index_second]
print(f"the last letter of the word {user_word_second} is {last_letter_second}")


color = "blue"
favorite_color = color
print(color, favorite_color)
print(id(color), id(favorite_color))
print(id(color) == id(favorite_color))
print(color is favorite_color)

# print("------------------")

color = "red"
print(color, favorite_color)
print(id(color), id(favorite_color))
print(id(color) == id(favorite_color))
print(color is favorite_color)

number = 2
# number = 3
number = number + 1
number += 1


# ask a user for a number of miles, 
# to convert kilometers and display it.

miles = float(input("give me a number of miles \n")) #20.5
kilometers = 1.608
miles_to_km = round(miles * kilometers, 2) #rounding 2 numbers after the decimal
print(miles_to_km)