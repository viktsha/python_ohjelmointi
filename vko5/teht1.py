import random

arpakuutioiden_lkm = int(input("Anna arpakuutioiden luukumäärä:"))

summa = 0
for i in range(arpakuutioiden_lkm):
    luku = random.randint(1, 6)
    summa = summa + luku

print("Silmälukujen summa on", summa)