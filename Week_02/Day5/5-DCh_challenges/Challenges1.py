#  Challenge 1 : Sorting
# Simple way, without using list comprehension. It works however

def sorting_function(message):
    message = message.split(',')
    # return sorted(message)
    message = sorted(message)
    message = ','.join(message)
    return message

user_message = input('Enter a list of words, separated by a comma (dont use spaces). My function will sort them alphabetically ')
print(sorting_function(user_message))

# Challenge 2 : Longest Word
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

def longest_word(sentence):
    return max(sentence.split(' '),key=len)

print(longest_word("Margaret's toy is a pretty doll."))


# + CategoryInfo : ObjectNotFound: (longest_word:String) []  
# , CommandNotFoundException
# + FullyQualifiedErrorId : CommandNotFoundException