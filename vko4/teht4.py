import random

luku = random.randint(1,10)

#print(luku)

arvaus = int(input("Arvaa luku (1-10):"))

while arvaus != luku:
    if arvaus < luku:
        print("Liian pieni luku")
    elif arvaus > luku:
        print("Liian suuri luku")

    arvaus = int(input("Arvaa uudestaan:"))

print ("Oikein!")




