toistot = 0

while toistot < 5:
    kayttajatunnus = input("Anna kayttajatunnus: ")
    salasana = input("Anna salasana:")

    if kayttajatunnus == "python" and salasana == "rules":
        print ("Tervetuloa!")
        break

    else:
        print("Käyttäjätunnus tai salasana on väärin.")
        toistot += 1

if toistot == 5:
    print ("Pääsy evätty")