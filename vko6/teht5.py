def karsi_parittomat(lista):
    uusi_lista = []

    for i in lista:
        if i % 2 == 0:
            uusi_lista.append(i)

    return uusi_lista

numerot = [1, 2, 3, 4, 5, 6]

karsittu = karsi_parittomat(numerot)

print("Alkuperainen lista:", numerot)
print("Karsittu lista:", karsittu)


