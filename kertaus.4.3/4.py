tarina = ""
edellinen = ""

while True:
    sana = input("Anna sana lisättäväksi tarinaan:").strip()

    if sana == "loppu" or sana == edellinen:
        print (tarina.strip())
        break

    tarina = tarina + sana + " "
    edellinen = sana
