import math

def pizzan_yksikkohinta (halkaisija, hinta):
    sade = halkaisija/2
    sade_metreina = sade / 100
    pinta_ala = math.pi * sade_metreina ** 2
    return hinta / pinta_ala

ekahalkaisija = float(input("Anna ekan pizzan halkaisija:"))
ekahinta = float(input("Anna ekan pizzan hinta:"))

tokahalkaisija = float(input("Anna tokan pizzan halkaisija:"))
tokahinta = float(input("Anna tokan pizzan hinta:"))

eka_yksikkohinta = pizzan_yksikkohinta(ekahalkaisija, ekahinta)
toka_yksikkohinta = pizzan_yksikkohinta(tokahalkaisija, tokahinta)

print (f"Ekan pizzan yksikköhinta:1.{eka_yksikkohinta:.2f}")
print (f"Tokan pizzan yksikköhinta:{toka_yksikkohinta:2f}")

if eka_yksikkohinta < toka_yksikkohinta:
    print ("Eka pizza antaa paremman vastineen rahalle")
else:
    print("Toka pizza antaa paremman vastineen rahalle")