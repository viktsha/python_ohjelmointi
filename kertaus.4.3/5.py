while True:
    lasku = (input("Valitse laskutoimitus(kertolasku/yhteenlasku/vähennyslasku/jakolasku/loppu): "))

    if lasku == "loppu":
        print ("Laskin suljetaan.")
        break

    luku1 = float(input("Anna eka luku: "))
    luku2 = float(input("Anna toka luku: "))

    if lasku == "kertolasku":
        tulos = luku1 * luku2

    elif lasku == "yhteenlasku":
        tulos = luku1 + luku2

    elif lasku == "vähennyslasku":
        tulos = luku1 - luku2

    elif lasku == "jakolasku":
        tulos = luku1/luku2

    else:
        print ("Virheellinen laskutoimitus.")
        continue

    print ("Tulos:", tulos)



