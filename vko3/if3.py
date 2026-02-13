sukupuoli = input("Anna biologinen sukupuoli (nainen/mies):").strip()
hemoglobiiniarvo = int(input("Anna hemoglobiiniarvo (g/l):"))

if sukupuoli == "nainen":
    if hemoglobiiniarvo <117:
        print("Hemoglobiiniarvo on alhainen.")
    elif 117 <= hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")

elif sukupuoli == "mies":
    if hemoglobiiniarvo <134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")




