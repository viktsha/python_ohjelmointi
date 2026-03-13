luku = []

number = input ("Anna eka luku tai lopeta syötämällä tyhä merkkijono:")

while number != "":
    luku.append(int(number))
    number = input ("Anna seuraava luku tai lopeta syöttämällä tyhjä merkkijono:")

luku.sort(reverse=True)

print(luku[0], luku[1], luku[2], luku[3], luku[4])
