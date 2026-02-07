name = input("Enter your name: ")

print ("Hello", name,"!")
print ("Hello " + name + "!")
print (f"Hello, {name}!")



import math
radius = float(input("Enter your radius: "))
circle_area = math.pi * radius ** 2

print(math.pi * radius ** 2)


base = float(input("Enter the base of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

perimeter = 2 * (base + height)
rectangle_area= base * height

print("The perimeter of the rectangle is:", perimeter)
print("The area of the rectangle is:", rectangle_area)


eka = int (input('Enter the first number:'))
toka =  int (input('Enter the second number:'))
kolmas =  int (input('Enter the third number:'))

summ = eka + toka + kolmas
income = eka * toka * kolmas
average = summ / 3

print("The summ of the numbers is:", summ)
print("The income of the numbers is:", income)
print("The average of the numbers is:", average)


lieviska = float(input("Enter the number of lieviska: "))
naula = float(input("Enter the number of naula: "))
luoti = float(input("Enter the number of luoti: "))
total_luoti = lieviska * 20 * 32 + naula * 32 + luoti
total_grams = total_luoti*13.3

kilograms = int(total_grams // 1000)
grams = total_grams % 1000

print(f"Massa on {kilograms} kilograms ja {grams: .2f} grams.")


import random
code3 = (
        str(random.randint(0, 9)) +
         str(random.randint(0,9)) +
         str(random.randint(0,9))
)
code4 = (
    str(random.randint(1, 6)) +
    str(random.randint(1, 6)) +
    str(random.randint(1, 6)) +
    str(random.randint(1, 6))
)

print ("Kolmenumeroinen koodi:", code3)
print ("Nelinumeroinen koodi:", code4)


