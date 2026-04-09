lentoasemat = {}

while True:
    print ("\n1 = Syötä uusi lentoasema")
    print ("2 = Hae lentoaseman tiedot")
    print ("3 = Lopeta")

    toiminto = input ("Valitse toiminto:")

    if toiminto == "1":
        icao = input ("Anna ICAO-koodi:")
        nimi = input ("Anna lentoaseman nimi:")
        lentoasemat[icao] = nimi
        print("Lentoasema lisätty.")

    elif toiminto == "2":
        icao = input ("Anna ICAO-koodi:")
        if icao in lentoasemat:
            print (lentoasemat[icao])
        else:
            print ("Lentoasemaa ei löytynyt.")

    elif toiminto == "3":
        break