kirjasto ={
    "Muumit ja suuri tuhotulva": ["Tove Jansson", 1945, "lastenkirjallisuus"],
    "Kalevala": ["Elias Lönnrot", 1835,"kansalliseepos"],
}

print(kirjasto["Muumit ja suuri tuhotulva"][0])
print(kirjasto["Kalevala"][2])

kirjasto["Muumit ja suuri tuhotulva"][2] ="kaunokirjallisuus"

kirjasto ["Hildur"] = ["Satu Rämö", 2023, "Kaunokirjallisuus"]

del kirjasto["Kalevala"]

print(kirjasto)
