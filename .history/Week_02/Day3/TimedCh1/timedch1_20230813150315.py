# Write a program to reverse the sentence word wise.

# Input:
# You have entered a wrong domain
# Output:
# domain wrong a entered have You
# You have 30 minutes to finish this challenge : time release 2:51


# sentence = input("Enter a sentence: ")

sentence = "You have entered a wrong domain"
print (sentence)
sentence_word_list = sentence.split(" ")

sentence_word_list.reverse()

print(" ".join(sentence_word_list))