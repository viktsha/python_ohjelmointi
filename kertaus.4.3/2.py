tuntipalkka = float(input("Anna tuntipalkka: "))
tehdyt_tunnit = float(input("Anna tehdyt_tunnit: "))
viikonpaiva = input("Anna viikonpaiva: ")

if viikonpaiva != "sunnuntai":
    print ("Tuntipalkka: ", tuntipalkka)
    print ("Tehdyt_tunnit: ", tehdyt_tunnit)
    print ("Viikonpaiva: ", viikonpaiva)
    paivapalkka = tuntipalkka * tehdyt_tunnit
    print ("Paivapalkka: ", paivapalkka, "euroa")

else:
    paivapalkka = tuntipalkka * 2 * tehdyt_tunnit
    print ("Paivapalka: ", paivapalkka, "euroa")
    