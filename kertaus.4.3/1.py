nimi = input("Kerro nimesi: ")

if nimi.upper() != "MATTI":
    annokset = int(input("Montako keittoannosta?"))
    hinta = annokset * 5.90
    print ("Kokonaishinta on:", hinta)
    print("Seuraava, kiitos!")

else:
    print("Seuraava, kiitos!")

