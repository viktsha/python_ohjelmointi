min_luku = None
max_luku = None

luku = input("Anna luku: ")

while luku != "":
    luku = int(luku)

    if min_luku is None or luku < min_luku:
        min_luku = luku

    if max_luku is None or luku > max_luku:
        max_luku = luku

    print ("Luku:", luku)

    luku = (input("Anna luku:"))

print("Ohjelma lopetettu.")
print("Pinenin luku:", min_luku)
print("Suurin luku:", max_luku)