#Montserrat Guadalupe Ramírez Esparza   3°J

#A list with 5 items, add a new element and print it using a for loop.
print ("Below I will show a list of my friends from TIDSM:")
friends = ["Sofi", "Max", "Jacob", "Erasmo", "Carlos"]
friends.append("Marco")
for friend in friends:
    print (friend)
print ("******************")

#A tuple with 7 items and print it using a while loop.

print ("Below is a list of the 7 most dangerous animals on the planet")

danguerousAnimals = ("Crocodile", "Scorpions", "Assassin bugs", "Dogs(rabies)", "Snakes", "Elephants", "Mosquitoes")
i = 0
while i < len(danguerousAnimals):
    print (danguerousAnimals[i])
    i += 1
print ("******************")

#dictionary with 3 properAes, modify any of those and print it.

print ("Next I will show some of my personal information")
mont = {"age": 20, "pets": 3, "name": "Montserrat"}
mont["age"] = 19

print ("Name: ", mont["name"])
print ("Age: ", mont["age"])
print ("Pets: ", mont["pets"])

print ("******************")
