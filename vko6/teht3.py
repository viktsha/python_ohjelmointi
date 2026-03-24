def gallona_litroiksi(gallonat):
    return gallonat * 3.785

while True:
    nestegallona = float(input("Anna gallonamäärä："))

    if nestegallona < 0:
        break

    litramaara = gallona_litroiksi(nestegallona)
    print ("Bensiinin määrä litroina on:", litramaara)