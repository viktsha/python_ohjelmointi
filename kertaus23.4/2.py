oppilaat = {
    "Vikki":["Vikki", 11, "matikka"],
    "Sonja": ["Sonja", 10, "historia"],
    "Alex": ["Alex", 11, "liikunta"]
}

print(oppilaat["Vikki"][2])
print(oppilaat["Sonja"][1])

oppilaat["Vikki"][2]="yhteiskunta"

oppilaat ["Kettu"] = ["Kettu", 10, "yhteiskunta"]

del oppilaat["Vikki"]

print(oppilaat)
