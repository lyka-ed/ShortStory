# ---------** ## String Method ## **--------
# 1- len()
location = "Nigeria"
print(len(location))

# 2- [] Notation
print(location[1] )
print(location[-2])

# 3- [] Notation
print(location[-5:-1])
print(location[0:4])
print(location[0:])
print(location[:6])
print(location[:])

#4- Concatenation ->>>> Formatted Strings
country = "Nigeria"
city = "Lagos"
# fullAddress = country + "," + city + "."
fullAddress = f"{}"
 # print(fullAddress)

#5 - in operator
print("un" in city)
print("ge" in country)

#6 not operator
print("go" not in country)
print("go" not in city)

#7- replace()
print(location.replace("Ni","To"))

#8- upper()
print(location.upper())

#9- lower()
print(location.lower())

#10- strip()
greetings = "         Good morning    "
print(greetings)
print(greetings.strip())
print(greetings.lstrip())
print(greetings.rstrip())

#11- title()
print(greetings.title())

#12 find()
print(country.find("e"))
