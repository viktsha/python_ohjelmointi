def kuusi(koko):
    print("Tämä on kuusi!")

    for i in range(1, koko+1):
        valilyonnit = " " * (koko - i)
        tahdet = "*" * (2 * i - 1)
        print(valilyonnit + tahdet)

    runko = " " * (koko - 1) + "*"
    print(runko)

kuusi(4)


