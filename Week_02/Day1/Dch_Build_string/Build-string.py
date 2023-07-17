pou_r = input("Please write a sentences at least 10 caracters long \n")

# if len(pou_r)
print(len(pou_r))
if len(pou_r) > 10:
    print('the sentence is too long')
elif len(pou_r) < 10:
    print('the sentence not long enough')
else:
    len(pou_r) == 10
    print('perfect string')

a = pou_r[0]
b = pou_r[-1]
print(a + b)

for pour_ in range(1, len(pou_r) + 1):
    print(pou_r[:pour_])
