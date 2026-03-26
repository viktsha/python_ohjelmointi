lista = []

while True:
    teksti = input("Anna sana (lopeta tyhjällä): ")

    if teksti == "":
        break

    lista.append(teksti)
    print ("Nyt lista on:", lista)

laskuri = 0

for sana in lista:
    if len(sana) >5:
        laskuri += 1

print(f"Listasta on {laskuri} sanaa, joissa on enemmän kuin 5 kirjainta.")







