## list

## retrieve element from a list

colors = ["blue", "red", "yellow"]
print(colors[1])

## update element in a list

colors = ["blue", "red", "yellow"]
colors[1] = "green"

## add element in a list

colors = ["blue", "red", "yellow"]
colors.append("white") #add at the end
colors.insert(0, "black") #add the color at the position 0

## delete element in a list

colors = ["blue", "red", "yellow"]
colors.pop() #delete the last one
colors.pop(1) #delete the element at this index
colors.remove("blue") #delete element with this value

## slice element in a list

colors = ["blue", "red", "yellow"]
other_colors = colors[start:end not included]

other_colors = colors[0:2] #["blue", "red"]
other_colors_second = colors[1:] #["red", "yellow"]
other_colors_third = colors[:] #["blue", "red", "yellow"]

# combine lists

color = ["blue", "red"]
numbers = [1,2,3]
new_list = color + numbers
new_list #['blue', 'red', 1, 2, 3]
