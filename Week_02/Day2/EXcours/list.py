all_colors = ["red", "blue", "yellow"]

userans = input("Give a number and a colordivided by a dash \n")
# "1-green"
listans = userans.split("-")
# ["1", "green"]
all_colors.insert(int(listans[0]), listans[1])
print(all_colors)
