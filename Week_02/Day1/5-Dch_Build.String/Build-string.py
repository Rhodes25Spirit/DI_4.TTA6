import random
sent_user = input("Please write a sentences at least 10 caracters long \n")

# if len(pou_r)
print(len(sent_user))
if len(sent_user) > 10:
    print('the sentence is too long')
elif len(sent_user) < 10:
    print('the sentence not long enough')
else:
    len(sent_user) == 10
    print('perfect string')

a = sent_user[0]
b = sent_user[-1]
print(a + b)

for i in range(1, len(sent_user)):
    # print(pour_)
    print(sent_user[:i + 1])

Bonus
wordlist = list(sent_user)
print(wordlist)

# #sent_user_List = sent_user.split(",")
# #print(sent_user_List)
suff_list = random.shuffle(wordlist)
# #print(suff_list)

# #for caract in suff_list:
suf_sent = "".join(wordlist)
print(suf_sent)
