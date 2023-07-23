## Exercise 1: Concatenate lists##
list1 = [10, 15, 20, 25, 30]
list2 = [1, 2, 3]


res = list1 + list2


print("Concatenated list:\n" + str(res))

## Exercise 2: Range of numbers##

nuum1 = 0
for element in range(1500, 2500):
    if element % 5 == 0:
        num1 = nuum1 + element
print(nuum1)

nuum2 = 0
for element in range(1500, 2500):
    if element % 7 == 0:
        num2 = nuum2 + element
print(num2)

print(num1 + num2)
