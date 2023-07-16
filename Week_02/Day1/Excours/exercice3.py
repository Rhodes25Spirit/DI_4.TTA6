# Exercise 5 : ask a user for a number of miles, to convert kilometers and display it.
# Exercice 5
miles = float(input("Give me number of miles \n"))
km = 1.60934
miles_to_km = round(miles * km)
print(f"{miles} miles  valent {miles_to_km} en km")
